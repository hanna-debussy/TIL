# 라우팅 프로토콜과 NAT

## 라우팅 프로토콜

일전의 포스트(*OSI model and 2nd, 3rd layer*)에서 네트워크 계층(3계층)을 설명할 때, 라우팅을 이렇게 설명하였다.

>라우팅
>:현재 네트워크에서 다른 네트워크로의 최적의 경로를 찾고 데이터를 전송하는 기술을 말한다.

한 마디로 최적의 경로를 찾고(제어 영역), 데이터를 전송(포워딩)하는(데이터 영역)을 맡는 게 라우팅, 더 크게는 네트워크 계층이다. 여기서는 제어 영역인 최적의 경로를 찾는 다양한 방식, 즉 **라우팅 프로토콜**에 대해서 알아보고자 한다.



### 라우팅 프로토콜의 종류

또한 일전의 포스트에서 *라우팅 테이블을 구성하는 방식은 크게 두 가지로 나뉘어진다.* 라고 설명한 적 있다. 바로 **정적 라우팅**과 **동적 라우팅**이다. 전자는 사람이 수동으로 경로를 입력한다고 했고, 후자는 라우터가 스스로 라우터 경로를 동적으로 결정한다고 했다. 전자는 누가 봐도 많은 한계가 있기 때문에 현재 우리가 쓰는 라우팅 프로토콜은 대부분 동적 라우팅에 속한다고 보면 된다.

![img](https://t1.daumcdn.net/cfile/tistory/242FEE3D58161E7923)

라우팅 프로토콜의 종류를 크게 나누자면 이런 관계를 가진다. 이 프로토콜들을 오늘 알아보고자 한다.



### IGP vs. EGP

전체 큰 네트워크 집합을 '하나의 관리 정책 하에 운영되는 라우팅 범위'라는 기준으로 몇 개의 그룹으로 나눠본다면, 보통 기업, 또는 KT, SKT, LG U+ 같은 ISP(Internet Service Provider)의 개별 네트워크를 하나의 그룹이라고 볼 수 있다. 우리는 이 하나의 그룹(네트워크)을 **Autonomous System(자율 시스템, AS)**라고 한다. 

AS '내'에서 사용하는 라우팅 프로토콜이 **IGP(Internal Gateway Protocol)**이고, AS '간' 사용되는 라우팅 프로토콜이 바로 **EGP(Exterior Gateway Protocol)**이다. 쉽게 말하면 IGP는 내부 경로 설정, EGP는 외부 경로 설정이라 보면 된다.



### IGP에 속하는 라우팅 프로토콜

IGP 안에는 다시 사용하는 알고리즘 종류에 따라 두 가지로 분류되는데, 그 종류가 바로 거리 벡터 알고리즘(Distance Vector, DV)과 링크 상태 알고리즘(Link State, LS)이다. 



#### DV와 LS

##### Distance Vector, DV

DV는 분산 제어 방식이다. 간단하게 말하자면 각각의 라우터들이 경로를 설정하고, 연결된 이웃들끼리 반복적으로 정보를 교환하면서 최소 비용경로를 계산하게 된다. 말 그대로 거리와 방향으로 길을 찾아가는 알고리즘이다. 그 어떤 라우터도 전체 네트워크 환경은 볼 수 없다. DV의 가장 대표적인 알고리즘이 바로 벨만-포드 알고리즘이다.



##### Link State, LS

반면 LS는 중앙 집중 제어 방식이다. DV와 달리 네트워크 전체에 대한 정보를 획득한 후, 이를 기반으로 경로를 계산한다. 네트워크 간의 비용을 전부 알아야 하기 때문에 DV보다 메시지 복잡성이 크다. 대표적인 알고리즘으로 다익스트라 알고리즘이 있다.



이하는 DV를 채택한 두 가지, LS를 채택한 두 가지 라우팅 프로토콜을 소개한다. 



#### RIP(Routing Information Protocol)

DV에 속하는 프로토콜. 다음 라우터로 한 칸 가는 단위를 '홉'이라고 하는데, RIP는 라우팅되는 홉 카운트가 가장 적은 경로를 택하는 프로토콜이다. 

*  쉽고 간편하게 구성이 가능하다.
* 라우터의 메모리를 적게 사용한다.
* 최대로 셀 수 있는 홉 카운트가 15로 제한되어 있기 때문에 보통 소규모 네트워크에서 채택한다.
* 단순히 홉 카운팅만 하기 때문에 경로의 네트워크 속도는 판단하지 않는다. 때문에 비효율적인 경로로 패킷을 전달할 가능성이 있다.
*  30초마다 라우팅 정보를 업데이트한다.



#### IGRP (Interior Gateway Routing Protocol)

역시 DV에 속하는 프로토콜. RIP의 한계를 넘기 위해 시스코(Cisco)라는 회사에서 만든 사유 프로토콜이라 시스코 라우터에서만 사용이 가능하다. RIP와 비교하자면 다음 특징이 있다.

* 15개였던 최대 홉 카운트를 255개로 확장해서 중대형 네트워크에서도 쓸 수 있게 되었다.
* 홉 카운트만 고려하던 RIP와 달리 대역폭, 지연, 신뢰성, 로드, MTU(Maximum Transmission Unit)  다섯 가지를 고려해 경로를 선택하므로 좀 더 정교해졌다.
* 다중 경로를 지원하기 때문에 여러 개의 경로를 사용함으로써 로드(부하)를 분산시키는 효과가 있다.
* 하지만 라우팅 루프 문제가 생길 수 있다.
* 90초마다 라우팅 정보를 업데이트한다.



#### EIGRP (Enhanced Interior Gateway Routing Protocol)

그림에서는 LS에 속한다고 나오지만, 사실 EIGRP는 엄연히 따지면 DV와 LS가 합쳐진 DUAL 방식의 프로토콜이라 볼 수 있다. 또한 IGRP의 한계를 넘기 위해 만든 거라 또 시스코가 만든 시스코 전용 라우팅 프로토콜이다. 

* 메트릭 방식은 IGRP를 그대로 사용한다.

  > 하지만 신뢰성과 로드를 5분마다 평균을 낸 값을 사용하기 때문에 네트워크 안전성에 문제가 발생할 수 있어서, 오늘날에는 대역폭과 지연만 메트릭에 사용된다고 한다.

* 이 DUAL 알고리즘 방식에 따라 최적 경로(Successor)와 후속 경로(Feasible Successor)를 모두 정한다.

  * 최적 경로와 후속 경로를 알려면 FD와 AD를 알아야 하는데, FD는 출발지 라우터 &rarr; 목적지 라우터까지의 전체 메트릭을 말하고, AD는 출발지 '다음' 라우터 &rarr; 목적지 라우터까지의 메트릭을 말한다.
  * 그러므로 FD가 가장 낮은 경로가 최적 경로가 되고, 최적 경로의 FD보다 AD가 작으면 그 경로는 후속 경로가 된다.
  * 이게 왜 나왔냐면 IRGP의 라우팅 루프 문제를 해결하기 위함이다. 더 알고 싶다면 https://peemangit.tistory.com/35 참고.

* 네트워크 변화에 즉시 반응해서, 최적 경로에 문제가 생기면 후속 경로로 바로 변경이 가능하므로 convergence time이 적다는 장점이 있다.

  > convergence time: 네트워크의 변화가 반영된 새로운 라우팅 테이블을 만드는 데 걸리는 시간

* 중소 규모 네트워크는 문제 없지만 대규모 네트워크에서 SIA 현상이 발생할 수 있어 관리가 힘들다.

  >SIA(Stuck in Active): 대체 경로가 없을 때, 이웃 라우터에게 이에 대한 정보를 물어보는 쿼리에 대한 응답이 3분 안에 안 오면 그 라우터와 연결이 끊어진다. 문제가 생긴 곳과 연결(neighbor)이 끊어졌기 때문에 문제가 생긴 곳(원인)이 어딘지 찾기가 힘들어진다. 보통 네트워크가 혼잡할 때 일어나서 대규모 네트워크에서 SIA 현상이 발생하기 쉽다는 것이다.



#### OSPF (Open Shortest Path First)

![img](https://mblogthumb-phinf.pstatic.net/20110816_55/twers_1313452279780NL29U_PNG/area_%B0%B3%B3%E4.png?type=w2)

LS 알고리즘 중에서도 다익스트라 알고리즘과 SPF(Shortest Path First) 알고리즘을 사용하는 라우팅 프로토콜. 'Open'이라는 이름에 걸맞게 프로토콜이 공용으로 사용 가능해서 표준 라우팅 프로토콜로 채택되었고, 상위 계층 ISP들이 주로 사용한다.

OSPF는 라우터가 전체 AS에 대한 토폴로지(Topology, 네트워크 물리 연결 방식)를 정기적으로 주고 받아 링크 가중치에 대한 최저 비용 경로를 최적 라우팅 경로로 결정한다. 



##### Area

OSPF에는 'Area'라는 개념이 있다. 규모가 큰 네트워크를 더 작은 영역으로 나누고 그 영역을 area라고 하는데, 이 area들은 각각 독립적이다. 대신 area 0으로 표현되는 Backbone Area에 모든 area들이 물리적으로 연결되어 있어야 한다.

이렇게 area를 나누면, 해당 area 내에서만 동작하는 내부 라우터는 굳이 다른 area의 라우터의 라우팅 갱신 정보를 받을 필요가 없어져서 라우터의 메모리와 CPU 등의 자원 절약이 가능하다. 또 stub area라는 개념도 사용해서(그림에서 area 3), 외부 대상에 관계 없이 Backbone area에 도달할 수 있는 area를 stub area로 지정해서 외부 경로에 대한 정보를 차단해서 라우팅 테이블의 크기를 감소시킬 수 있다. 이렇게 되면 안정성, 성능이 모두 올라간다.



##### 장점

* Area 개념을 사용해서 안정적이고 효율적인 관리가 가능하다.
* RIP나 IGRP 등과 달리 OSPF는 링크 상태에 변화가 있으면 즉각적으로 flooding을 해서 알려주기 때문에 convergence time이 매우 적어진다.
* 모든 메시지들의 교환은 인증을 받는다. 또한 특정 area 전체를 인증할 수도 있기 때문에 보안 면에서 뛰어나다.
* 홉 카운트의 제한이 없다.



### EGP에 속하는 라우팅 프로토콜

EGP는 다른 도메인 간 일어나는 라우팅이기 때문에 딱히 정리된 관리자가 없고, 대부분 신용도가 낮기 때문에 빠른 수행보다는 보안과 제어가 EGP의 목적이라고 할 수 있다.



#### BGP (Border Gateway Protocol)

![bgp multihoming](https://www.noction.com/wp-content/uploads/2012/03/xbgp.jpg.pagespeed.ic.GTRWCfME1Q.jpg)

EGP에 해당하는 게 현재 BGP밖에 없어서 국제 표준으로 사용된다. 대규모 네트워크 통신을 위해 다양하고 강력한 라우팅 기능을 가지고 있다. 

* DV와 LS를 섞은 Path Vector 방식을 사용한다.
  * DV를 사용해서 convergence time은 조금 느리지만, 분산형이므로 대용량의 라우팅 정보를 교환할 수 있고, 루프 문제를 방지한다.
  * LS를 사용해서 이웃 라우터와의 neighbor를 맺고 서로 상태를 즉각 업데이트(advertising)가 가능하다.
* 메트릭이 다양하고 메트릭 간에도 우선 순위가 있다.
* 정책 기반이므로 다른 AS의 정책을 침범하지 않는 한에서 필요한 라우팅 정책을 또 구현할 수 있다. 예를 들면 경쟁 상대인 SKT와 KT 사이에만 정보 공유를 최소화하거나 특정 경로를 무시할 수 있다.
* 호스트의 변경이 감지되었을 때에만 라우팅 테이블 정보를 갱신해서 보내는데, 이때 오직 연관된 정보만이 보내진다.
* TCP 179번 포트를 이용해서 인접하지 않은 라우터와도 neighbor를 맺을 수 있고(대신 수동으로 해줘야 함) 신뢰성 있는 통신이 가능하다.
* BGP에는 두 가지 연결이 존재한다. AS 내에서 통신하는 iBGP(internal)와 eBGP(external)이 그것이다. iBGP는 같은 AS 내 라우터 간에 BGP 라우팅 정보를 교환하기 위해 사용되고, eBGP는 서로 다른 AS 간에 연결된 BGP 구간이다.



BGP에 대해 검색하면 '광고'라는 단어가 많이 쓰인다. BGP의 존재 이유가 주변의 여러 라우터들에게 '어떤 라우터가 어느 AS에 속해있는지'에 대한 정보를 광고하기 위함이라서 그렇다. 이렇게 도달 가능성 정보를 교환함으로써 많은 IP들은 연결이 가능해진다. 이때 광고되는 것은 IP주소의 prefix다.



## NAT

![NAT은 무엇이며, 왜 필요한 것인가?](https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/JqQ/image/-CHZhKIMxmFM48sgQ2jjC1cAShE)

NAT(Network Address Translation)은 직역하면 네트워크 주소 변환자라는 뜻인데, 말 그대로 공인 IP를 사설 IP로, 혹은 사설 IP를 공인 IP로 변환해준다. 기업이나 기관 등에서 내부 망을 사용하는 PC들은 보통 사설 IP를 쓰는데, 외부 인터넷과 연결 시에는 공인 IP 하나를 같이 사용하기 위해 NAT가 필요하다.

비유를 하자면, 회사 대표 번호로 전화를 하면 그 안에 또 내선 번호가 지정되어 있어 각 부서의 각 사원들과 연락이 가능한 것과 같다. 그러므로 우리는 회사 대표 번호만 알면 되고, 사원들은 개인 전화번호를 외부에 알릴 필요가 없어 더 안전하다.



NAT 테이블이 가지고 있는 정보는 아래와 같다.

* 내부 네트워크 내 호스트들의 사설 IP와 각각의 포트 번호
* 외부로 나갈 때 IP와 포트 번호: 공인 IP는 같지만 각기 다른 포트 번호
* 목적지 포트 번호: 상대 네트워크도 공인 IP만 공개해뒀으므로 해당 공인 IP만 적혀있다



### 왜 변환하지?

1. 공인 IP 주소는 한정되어 있기 때문이다. 
   IPv4에서 IPv6으로 오면서 만들어진 것이 바로 NAT다. 공인 IP를 절약하기 위해 사설 IP가 필요하고, 그 사이에서 일을 해주는 게 바로 NAT가 필요한 이유이다.
2. 보안성을 높일 수 있다.
   공개망(공인 IP)만 알려서 내부망(사설 IP)을 보호할 수 있고, 또 공개망과 내부망 사이에 방화벽도 운영해서 외부 공격으로부터 내부망을 지킬 수 있다. 





## 면접 예상 질문

?



## 참조

IGP, EGP

https://min-310.tistory.com/162

https://as-backup.tistory.com/21?category=1156499

RIP

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hmin011&logNo=150150130677

IGRP

https://www.datanet.co.kr/news/articleView.html?idxno=9114

https://m.blog.naver.com/hmin011/150150130677

EIGRP

https://peemangit.tistory.com/35

https://choraengyi.tistory.com/59

https://blog.1nfra.kr/209

https://bignet.tistory.com/30

https://bignet.tistory.com/67

https://m.blog.naver.com/cafca23/90072402455

OSPF

https://www.cisco.com/c/ko_kr/support/docs/ip/open-shortest-path-first-ospf/13703-8.html#anc3

https://www.stevenjlee.net/2020/06/25/%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EB%9D%BC%EC%9A%B0%ED%8C%85-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C-ospf-open-shortest-path-first/

http://www.ktword.co.kr/test/view/view.php?m_temp1=1930

https://net-study.club/entry/Routing-Protocol-OSPF-Open-Shortest-Path-First

https://m.blog.naver.com/seungj1031/221012340470

https://m.blog.naver.com/three_letter/220540146298

BGP

https://www.stevenjlee.net/2020/06/27/%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EB%9D%BC%EC%9A%B0%ED%8C%85-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C-bgp/

https://blog.naver.com/taeheon714/222384978033

https://ddongwon.tistory.com/97

NAT

https://brunch.co.kr/@sangjinkang/61

https://jwprogramming.tistory.com/30