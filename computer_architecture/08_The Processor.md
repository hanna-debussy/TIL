# 4. The Processor

## An Overview of Pipelining

### Hazards

: 다음 사이클의 다음 명령어를 실행하지 못 하는 상황

1. Structure hazards
   : 리소스를 다른 게 쓰고 있어서 대기 중
2. Data hazards
   : 앞에서 실행한 명령어의 아웃풋이 아직 안 나와서 대기 중
3. Control hazards
   : 이전 명령어에 따라서 해야할 게 달라질 때 앞 결과 받으려 대기 중

즉 resource use의 충돌 때문...



#### Structure Hazards

ex) MIPS pipeline에서 원래라면 instruction memory와 data memory가 따로 있는데 하나의 메모리에 같이 있다고 가정한다면 load/store도 데이터에 접근해야 하고 instruction fetch도 접근해야 한다. 근데 load도 안 됐는데 instruction이 깔짝되면 안 되니까 stall(멈춤)이 발생 그니까 이거는 구조적... 여기가 single memory를 쓰는 구조라서 생긴 것

&rarr; resource를 하나 더 추가해서 메모리를 하나 더 두면 두 개가 데이터 하나 놓고 싸우는 일은 없겠지



#### Data Hazards

다음 명령어가 이전 명령의 결과값을 필요로 할 때

c = a + b
e = c + d 라면 e를 연산하기 위해서는 c값을 불러와야 하기 때문에 대기하게 됨

&rarr; Forwarding(a.k.a. Bypassing)
: 결과값이 나오자마자 슥삭 바로 사용하자는 거임

![컴퓨터구조 #6(Pipelining & Hazard)](https://media.vlpt.us/images/leejaehyuck9/post/ce3d27c7-20a7-428e-b4d4-f8bda4ea10df/image.png)

결과값음 EX stage에서 나오는데 그 register에 결과값을 보여주는 단계는 WB(write back) stage이기 때문에 EX에서 나온 값은 두 stage를 기다려야 하는 거임 근데 걔를 바로 다음 명령어로 넘겨버리자는 거지 슉. 슈슉.

그러려면 datapath의 추가적인 연결(하드웨어)이 필요함



#### cf) Load-Use Data Hazard

forwarding을 쓴다 해도 이 stall을 완벽히 피할 수는 없음

![img](https://image-hosting.zhangjc.tech/ghost/content/images/2019/06/2894104957.png)

load의 경우에는 EX가 아니라 memory에 접근해서 가져와야 하기 때문에 MEM 단계 이후에 값이 나옴 그래서 위의 data hazard의 경우보다 한 사이클이 더 밀려나서 대기를 타게 된다는 말



#### Code Scheduling to Avoid Stalls

헐 그래서 stall을 어떻게 피하냐면 정말 곧이곧대로 그 순서대로 계산을 하는 게 아님

a = b + e, c = b + f 두 개를 연산해야 한다고 치면

b랑 e를 불러와서 a 하고 b랑 f 불러와서 c 하면 b로드-e로드-연산1-a스토어-f로드-연산2-c스토어 이렇게 차례대로 되잖아 이때 e로드-연산 사이에서 한 사이클 stall, f로드-연산 사이에서 한 사이클 stall 되는데

이걸   b로드-e로드-f로드-연산1-a스토어-연산2-c스토어 이렇게 f로드 자리를 바꿔주면 f로드되는 동안 e가 로드되고 연산1이 가능해짐 그리고 그 연산1할 동안 f 로드해서 바로 연산2가 가능해지는 거임 두 사이클이 절약되는 것



#### Control Hazards

브랜치 명령어는 그 명령어를 실행해야 그 결과에 따라 다음 명령어가 결정되기 때문에 pipeline에서는 순차적으로 fetch하는데 줄 세워놔봐야 항상 그게 정확한 instruction이 아닐 수도 있다는 말

그래서 나온게 **Branch Prediction**
: 긴 파이프라인에서 중간에 branch 결과값을 알 수 있다면 그걸로 예측을 하고 돌리는 거임 그러면 stall이 그 예측이 틀렸을 때에만 발생하는 거지 MIPS의 경우에는 branch가 발생하지 않는 걸로 예측하고 fetch를 진행함

조금더 실질적인 branch prdiction에는 두 가지가 있는데

1. Static branch prediction
   : 어떤 브랜치는 항상 taken으로, 어떤 브랜치는 항상 not taken으로 예측
2. Dynamic branch prediction
   : 최근 branch 값을 알아뒀다가 branch taken이 많은 branch면 taken으로 예측, branch not taken이 많으면 not taken으로 예측하는 것. 이 경우에는 최근 히스토리를 저장해둘 여분의 메모리가 필요하다



## Pipelined Datapath and Control

stages 사이사이에 pipeline register가 필요하다 곧 네 개가 필요하다는 말씀
그리고 그 register에는 다음에 필요한 데이터들을 저장해둔다



### Pipeline Operations

cycle-by-cycle flow... 그림을 그릴 때 보통 두 가지로 그리는데 특정한 한 사이클의 파이프라인 상태를 보여주는 single-clock-cycle diagram이랑 여러 사이클에 걸쳐서 어떻게 실행되고 있는지를 보여주는 multi-clock-cycle diagram 특히 load/store를 볼 때 ㅇㅇ

그 중 후자를 보자

#### Load

1. IF 단계: pc + 4랑 fetch된 instruction이 pipeline register에 저장
2. ID 단계: 명령어를 통해 register에 access하고 하위 16비트가 32비트로 바뀜 그리고 pc+4 그대로 가져가고
3. EX 단계: 메모리 계산한 거 pipeline register에 들어가고
4. MEM 단계: 실제 데이터 메모리에 aceess하고 거기서 읽은 것들을 pipeline register에 들어가고 
5. WB: 그 MEM pipeline register에 있던 걸 register에 들어가게 됨

근데... 원래 target register는 ID 단계에서 정해지는데 실제 데이터가 쓰여지는 건 WB단계이기 때문에 실행된 load 명령어가 WB에 가 있다는 말은 ID에는 엉뚱한 게 있다는 말... 그 엉뚱한 명령어에 의해 target register가 결정되고 쓰여져야 할 값이 엉뚱한 곳에 저장된다는 말
&rarr; 그래서 ID 단계의 target register를 pipeline register에 저장해서 게속 보내줘야 함



#### Store

1. EX 단계: Load 와 같다
2. MEM 단계: ID단계에서의 데이터를 데이터 메모리에 쓴다
3. WB 단계: store는 아무 일도 하지 않음



#### 그래서 multi-clock-cycle diagram은...

![img](https://i.stack.imgur.com/XnKKi.png)

이렇게 그리게 된다. 아니면 그냥 stage 단계를 적어두기도 한다.



#### Single-clock-cycle pipeline diagram

![img](https://media.vlpt.us/images/slchoi/post/906162a7-fead-4ca1-ba80-b7e9e4943c8d/image.png)

좀 흐릿하긴 한데 여튼 저 위에 각 단계에서 지금 어떤 게 실행되고 있는지 보여주는 거 한 마디로 이거 여러개 붙여둔 게 multi라고 보면 된다
보면 하나의 cycle에서 다섯 개의 명령어가 동시에 돌아가는 중이다.  pipeline의 단적인 모습... 이런 방법으로 성능을 향상시킨다. 



### Pipelined Control

![img](https://www.cise.ufl.edu/~mssz/CompOrg/Figure5.5-PipelineControl.

control은 ID 단계에서 OPcode에 의해서 만들어지는데 이 control이 WB에 쓰일 거 MEM에 쓰일 거 EX에 쓰일 거 pipeline register를 통해 저장/전달 해주는 거

이제 이걸 붙이면

![img](https://blog.kakaocdn.net/dn/w8cLV/btq5uHoyvBh/nCeNYdG9eMM23k09QjLFWk/img.png)

...으
