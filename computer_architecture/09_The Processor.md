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



## control Hazard

### Branch Hazard

브랜치의 결과를 MEM에서 알게 되기 때문에 WB을 해 줘야 비로소 알 수 있음 그러므로 세 개의 cycle을 쉬어줘야 한다. 

그래서 우리가 ID stage에서 알 수 있도록 브랜치 결과를 알 수 있도록 target address adder랑 register comparator를 추가했다.
&rarr; 근데? 이렇게 해도 적어도 한 개의 cycle은 쉬어줘야 한다.





















