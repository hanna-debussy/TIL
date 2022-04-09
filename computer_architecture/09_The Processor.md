# 4. The Processor

## Data Hazards: Forwarding vs. Stalling

언제 hazard가 나타나고 어떻게 forwarding을 해야 하는가?



R읽기와 W쓰기는 경우의 수가 네 가지가 나오는데 R after R나 WaR는 전에 했던 R이 뒤의 연산에영향을 주지 않고, WaW도 처음에 write 했지만 그 다음 write이 그 전의 write을 덮어쓰는 경우이기 때문에 처음의 write는 의미가 없어져서 상관이 없다. 하지만? RAW... **Read After Write** 일 때 비로소 hazards가 발생한다. read 하려면 그 앞의 연산인 write가 끝까지 다 끝나야 하기 때문뿡



### Detecting the Need to Forward

음 일단 들어가기 전 register...의 넘버? 그게 뭐지 예를 들어 ID/EX RegisterRs 의 뜻은 ID/EX 사이의 pipeline register의 source Register에 있는 레지스터 넘버라고 한다.

그러면 EX stage에서는 source하고 target이 두 개가 있으니까 ID/EX RegisterRt 얘도 있음ㅇㅇRd는 destination Register를 칭하고



**Data hazards when ★**

1. EX/MEM RegisterRd = ID/EX RegisterRs
2. EX/MEM RegisterRd = ID/EX RegisterRt
3. MEM/WB RegisterRd = ID/EX RegisterRs
4. MEM/WB RegisterRd = ID/EX RegisterRt

인데 1, 2는 EX/MEM pipeline register에서 일어나는 fwd고 3, 4는 MEM/WB pipeline register에서 일어나는 fwd

그러면 fwd은 hazard가 일어나서 각각의 경우에 EX/MEM RegWrite 또는 MEM/WB RegWrite가 1이 되면 fwd instruction이 on이 된 상태

\+ EX/MEM RegisterRd != 0 and MEM/WB RegisterRd != 0인 상태여야 함 당연함 `$zero`는 읽기용임 WAR이든 RAR이든 R이 선행되면 쿨스루됨

이런 조건들이 있어야 fwd가 필요하다는 것을 우리가 알 수 있음



#### Forwarding Paths

![img](https://blog.kakaocdn.net/dn/cI2ix3/btq53kGNvaP/X2K353J2vN04DdB5J60Gw1/img.png)

저기 가운데 fwd unit이 네 개의 화살표를 받는다 각각이 보면 각 스테이지의 pipeline register가 주는 Rs, Rt / Rd / Rd를 받는 거고 그걸 비교해야 저 위의 네 가지 경우를 알 수 있다. 

만약 넷 중 하나가 만족하면 ALU의 첫 번째 연산에 대해 fwd하는 게 FwdA, 두 번째 연산(종종 target)에 대해 fwd 하는 게 FwdB라고 볼 수 있다. 각각의 MUX는 세 가지를 받아서 선택할 수 있는데 그 세 개가 1. 정상적으로 들어오는 값 2. 저어 멀리 MEM에서 Fwd된 값 3. EX에서 Fwd된값...임 그이까 이게 어떻게 되는 거냐면



#### Forwarding Conditions

우리는 일전에 네 가지를 경우의 수를 보고 왔었다. 그걸 저 도식도에서 보자는 건데

1. **EX/MEM RegisterRd = ID/EX RegisterRs**
   그러니까 EX/MEM RegWrite가 1이고 EX/MEM RegisterRd != 0일 때...가 전제조건이고 / 거기에다가 EX/MEM RegisterRd = ID/EX RegisterRs일 때 FwdA = 10이 된다.
   그러면 전자의 MUX가 두 번째 값을, 그러니까 EX/MEM에서 온 값을 호출하게 됨

2. **EX/MEM RegisterRd = ID/EX RegisterRt**

   마찬가지다. 위의 전제조건이 맞고 해당 조건이 맞으면 FwdA = 10임
   
3. **MEM/WB RegisterRd = ID/EX RegisterRs**

   이번엔 MEM/WB RegWrite가 1이고 MEM/WB RegisterRd != 0일 때 + 해당조건일 때...! 이번엔 뭐냐면 FwdA = 01이 된다. MUX가 3번, 그러니까 MEM/WB에서 온 값을

4. **MEM/WB RegisterRd = ID/EX RegisterRt**

   ㅇㅇ



#### Double Data Hazard

별 경우가 다있네... 그니까

a = a + b
a = a + c
a = a + d

이렇게 있으면 세 번째 식의 오른쪽 a는 첫 번째 a가 될 수도, 두 번째 a가 될 수도 있는데 우리는 가장 최신 a를 선택해야 한다.
아 이런 경우, 그니까 '가장 최신 데이터를 써야 한다' 이게 MEM hazard 조건에도 걸리고 EX hazard 조건에도 걸리거든 근데 이거 처리는 EX 단계에서 해줘야 한단 말이야 그래서 MEM hazard 조건에 뭘 넣어야 하냐면 EX hazard 조건이 True가 아닐 때만 MEM hazard라고 조건을 고쳐줘야 함 

그러므로 최종! 최종\_최종\_최종.condition

3. **MEM/WB RegisterRd = ID/EX RegisterRs**

   이번엔 MEM/WB RegWrite가 1이고 MEM/WB RegisterRd != 0일 때 + 해당조건일 때...! 이번엔 뭐냐면 FwdA = 01이 된다. MUX가 3번, 그러니까 MEM/WB에서 온 값을
   **+** not EX 조건(EX/MEM RegisterRd != 0 그리고 EX/MEM RegisterRd = ID/EX RegisterRs)

4. **MEM/WB RegisterRd = ID/EX RegisterRt**

   ㅇㅇ **+** not EX 조건(EX/MEM RegisterRd != 0 그리고 EX/MEM RegisterRd = ID/EX RegisterRt)



리얼 최종

![Fig. 2. Pipelined datapath with forwarding unit and Hazard detection unit.](https://d3i71xaburhd42.cloudfront.net/c35e083d3b884c57340843c7e66b39055720b037/3-Figure2-1.png)





### Load-Use Data Hazard Detection

#### 언제 일어나느냐... 하니
ID/EX MemRead 
**+** (ID/EX RegisterRt == IF/ID RegisterRs 거나 ID/EX RegisterRt == IF/ID RegisterRt)

그이까 내가 로드를 해서 그 다음 바로 써야 하는데(== ID/EX에서 써야 할 타겟이 그 직전의 값들) 로드를 해서 그 값을 쓰려면 데이터 메모리까지 가야 가능하단 말임 WB까지 가야 한다고... 그래서 다음 연산은 한 사이클 기다리게 됨

만약 발생이 되면 stall을 하고 한 사이클 쉬어줘야(= 버블을 끼워줘야) 함



#### 그럼 How to Stall the Pipeline?

ID/EX register의 모든 control value를 0으로 만들어주면 된다. 0이 되면 EX, MEM, WB 모두가 할 게 사라져서 no-operation이 됨

근데? 그러려면 PC값이랑 IF/ID register가 갱신되는 걸 막아줘야 한다

* 같은 명령어를 한 번 더 디코딩 해주고
* 다음 명령어를 fetch 한 번 더 해줘야 함
* 글구 한 사이클만큼 stall이 걸린다 해도 MEM이 데이터 읽는 건 가능하게 해야 함 왜냐면 lw는 진행되어야 하기 때문 lw에 대한 fwd은 해조야 한다는 말

![Chapter 4 The Processor n CPU performance factors](https://slidetodoc.com/presentation_image/3d23e45a120983e3f268af1d13d84424/image-82.jpg)

여기 보면 lw랑 and 사이에 버블이 생겼는데 lw에서 메모리를 and로 넘기려면 그 버블에서 Data Memory는 가동 중이어야 한다는 말씀



그리고 실제로는 이렇게 움직인다

![PPT - Chapter 4 PowerPoint Presentation, free download - ID:1986074](https://image1.slideserve.com/1986074/stall-bubble-in-the-pipeline1-l.jpg)

ID/EX register의 값을 0으로 만든댔잖아 그래서 그 버블 칸 보면 그 이후 세 개가 버블이 되는데 대신 EX/MEM은 돌아가는 중임
그리고 and 단계에서 register에서 다시 decoding 하는 것부터 시작을 하게 되고 or에서는 원래 cycle3에서 fetch를 했어야 했잖아 근데 버블 때문에 cycle4에서 fetch를 또 해야 한다.
cycle5에서는 lw가 WB를 하고 and는 EX로, or는 ID로, add는 IF에서 잘 돌아가게 된다.



![Solved Th is exercise is intended to help you understand the | Chegg.com](https://d2vlcm61l7u1fs.cloudfront.net/media%2Fd78%2Fd782f7aa-1932-48b2-b65a-8575636f8749%2FphpAWJIrf.png)

이제 hazard detection unit까지 넣어서 보면 이렇다. 략간 어지럽네요,,, 만약 hazard가 일어났으면 저 위의 MUX에 0을 넣어서 그 뒤의 세 단계를 no operation 시킨다. 



## Control Hazard

### Branch Hazard

브랜치의 결과를 MEM에서 알게 되기 때문에 WB을 해 줘야 비로소 알 수 있음 그러므로 세 개의 cycle을 쉬어줘야 한다. fwd을 해서 MEM에서 바로 슥삭한다 해도 두 cycle을 쉬어줘야 한다.

그래서 우리가 ID stage에서 알게 해서 브랜치 결과를 알 수 있도록 target address adder랑 register comparator를 추가했다.
&rarr; 근데? 이렇게 해도 적어도 한 개의 cycle은 쉬어줘야 한다.



### Dynamic Branch Prediction

deeper and superscalar(나중에 배울 것) pipeline일수록 branch penalty가 더 중요해진다.
이를 막기 위해 우리는 dynamic prediction을 사용하는 것

추가하는 건 branch predictions buffer(a.k.a. branch history table)
: 최근 사용한 결과값(taken or not taken)을 가지고 있는 버퍼/테이블

이 테이블을 보고 값을 예측하고 실행한다
만약 틀리면? 여태 한 거 무효화 시키고 올바르게 다시 실행하고, 더해서 branch prediction을 수정한다



#### 1-bit predictor

가장 최근 결과값 한 개만 들고 있는 거.
아 근데 이중 loop일 때 곤란해진다. 비유를 하자면 for문이 하나 안에 또 하나를 가진 상태고 inner for문 안에 if가 있다고 치자 그러면 if문에서 taken이 나와도 outer for의 'inner for의 결과값이 taken이면 not taken이다...' 이렇게 해버리면 항상 앞의 결과값은 taken인데 not taken이 나와주니 에바고 또 outer for문이 또 돌면 not taken을 가지고 inner for문에 들어가니 not taken 뒤에 taken이 나와줘서 곤란하게 됨



#### 2-bit predictor

![enter image description here](https://i.stack.imgur.com/BfCk8.png)

결과값이 두 개 저장되는 건데 잘 보면 두 번 이상 misprediction이 발생하면 예측값이 바뀌게 되어잇음

이렇게 하면 위의 for문 두 개도 잘 예측할 수 있다. outer for문에서 한 번 not taken이 나온다 해도 아직까지 taken이라고 예측하는 거니까

그리고 2bit이라서 뭐 메모리 늘어난다 해도 크게 영향을 미치지 않음



### calculating the branch target

predictor가 있다 하더라도 branch를 만날 때마다 target address를 계산해야 하는데 이것도! 미리 저장해두고 예측을 하자 이말이야

**branch target buffer**
target address를 캐시해두는 것... 그래서 명령어가 fetch될 대 branch의 명령어가 있을 program counter로 인덱싱이 되어서 같은 값이 예측되면 바로 target address를 아까 걸로 가져오는 거임



## Exceptions

음 예외는 언제 발생하느냐? 컨트롤의 흐름을 바꾸는 'unexpected events'가 발생할 때겠지?

1. Exception
   : CPU 내부에서 발생한다. 
   ex) undefined opcode, overflow, syscall

2. Interrupt
   : 외부 장치에 의해 발생
3. Software Interrupt(a.k.a Trap)
   : 명령어에 의해 interrupt가 발생

이런 예외들은 성능을 떨어뜨리지 않고 처리하기가 매우 힘들다...

### 그럼 어케 처리하니?

MIPS에서는 System Control Coprocessor라는 곳에서 예외를 처리한다. 

1. 일단 예외를 발생시킨 명령어(PC)를 Exception Program Counter(EPC)에 저장함
2. 이 문제를 Cause Register라는 곳에 저장한다. (ex) 뫄뫄 문제면 0 솨솨 문제면 1 등등)
3. handler가 있는 8000 00180으로 간다

#### handler?

##### Vectored Interrupt

: 예외를 발생한 원인에 따라서 handler를 여러 개 등록하는 거다. 하나만 있으면 핸들러로 가서 그제야 어떤 문제인지 찾아야 한다. 하나일 때 처리 시간이 길어지고, vectored면 하드웨어가 받쳐줘야 하지만 그래도 바로 어떤 문제가 생겼는지 알 수 있다.

그래서 vectored를 쓰면 각각 예외마다 주소가 있고 거기 가면 바로바로 예외를 처리하기도 하지만 실제 핸들러가 있는 곳으로 보내는 브랜치 명령어로 이어지기도 한다.



##### handler 작동 방법

1. 원인을 찾고 관련된 handler로 짬푸
2. 필요한 액션 취하기
3. 다시 일하기 / 아님 EPC로 돌아가서 다시 실행하기
4. 회복이 되지 않으면 프로그램 종료 + EPC 가서 이 에러 났다고 repost 해주기



### 근데? 이제 파이프라인이라면?

파이프라인이라면 더 복잡해진다. 파이프라인에서의 예외는 대표적인 control hazard의 일종이다. 약간 mispredicted 한 상태와 같다.

* 예외가 restartable하다면
  파이프라인은 해당 명령어를 flush(무효화)하고 핸들러에서 처리한 다음 다시 명령어로 돌아와서 다시 refetch해준다.
* PC가 EPC register에 저장되어 있잖아 근데 파이프라인에서는 PC가 처리된 순간 다음 명령어 받으려고 +4가 된다. 그러니 EPC에는 PC+4가 저장되는 거...  그래서 핸들러가 어떤 명령어를 실행해야하는지 그 값을 조정해줘야 한다.



#### 여러 개의 명령어를 돌리는 그...

##### multi exceptions가 발생할 수 있다!

파이프라인에서 가장 빨리 실행된 예외 먼저 실행한다. 그 다음 모든 명령어를 flush 시키는 거지 이런 간단하고 예외가 딱 뭔지 알 수 있는 걸 precise exception이라고 한다.

하지만? 복잡한 파이프라인이라면? 실제 실행이 순차적이 아니라 막... 뒤죽박죽으로 실행되는 것도 있는데 그런 걸 out-of-order completion이라고 한대 이런 복잡한 파이프라인이라면 precise exception이 어렵겠지 이런 걸 imprecise exceptions라고 한다.



##### Imprecise Exceptions

1. 일단 파이프라인을 멈추고 전체 상태를 저장한다.
2. 핸들러가 동작 시작
   * 어떤 명령어들이 예외를 가지고 있고
   * 어떤 명령어들을 실행하거나 flush시킬지 결정

하드웨어는 간단하지만 핸들러는 복잡해진다... 그래서 모든 예외를 imprecise로 돌리지는 않음
