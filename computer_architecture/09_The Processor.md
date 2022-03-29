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



### Forwarding Paths

![img](https://blog.kakaocdn.net/dn/cI2ix3/btq53kGNvaP/X2K353J2vN04DdB5J60Gw1/img.png)

저기 가운데 fwd unit이 네 개의 화살표를 받는다 각각이 보면 각 스테이지의 pipeline register가 주는 Rs, Rt / Rd / Rd를 받는 거고 그걸 비교해야 저 위의 네 가지 경우를 알 수 있다. 

만약 넷 중 하나가 만족하면 ALU의 첫 번째 연산에 대해 fwd하는 게 FwdA, 두 번째 연산(종종 target)에 대해 fwd 하는 게 FwdB라고 볼 수 있다. 각각의 MUX는 세 가지를 받아서 선택할 수 있는데 그 세 개가 1. 정상적으로 들어오는 값 2. 저어 멀리 MEM에서 Fwd된 값 3. EX에서 Fwd된값...임 그이까 이게 어떻게 되는 거냐면



### Forwarding Conditions

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



### Double Data Hazard

별게 다있네...







