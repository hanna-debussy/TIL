# The Processor

## Parallelism via Instructions

### Instruction-Level Parallelism (ILP)

: 명령어 여러 개를 동시에 실행시키는 것 ex) pipelining



ILP를 증가시키기 위해서는 

* 파이프라인 스테이지를 더 많이(deeper) 만든다
  : 그러면 스테이지마다 할 일이 줄고 시간이 짧아져서 사이클도 덩달아 짧아진다
* 한 사이클에 한 명령어가 아닌 여러 명령어를 실행시킨다
  : 그러려면 파이프라인 자체를 여러 개 만들어야 한다
  한 사이클에 몇 명령어? == Instructions Per Cycle IPC



### Multiple Issue

* Static multiple issue
  어떤 명령어를 어떤 사이클에 실행할지 컴파일러가 결정한다. 함께 실행될 명령어들을 그룹화 하는 것 그래서 컴파일러가 컨파일러 타임에 hazards를 탐지/피하는 일을 함
* Dynamic multiple issue
  : 컴파일러가 아닌 CPU가 함 물론 컴파일러가 도와주긴 하는데 프로세서가 주도적으로 한다 at runtime

#### Speculation

multiple issue에 쓰인다.
브랜치 예측이 제일 주요 예시고 또 LW에서 같은 값을 계속 로드하는 경우가 많기 때문에 그걸 예측하는 일도 많다. 성능과 관련됨(예측이 잘 되면 성능이 좋아지고 아니면 저하되고)

#### Compiler/Hardware Speculation

* 컴파일러
  : 예측이 틀리면 브랜치 전에 로드를 갖다놓는 것처럼 컴파일러는 명령어 순서를 바꿀 수 있(는 명령어를 가지고 있)다.
* 하드웨어
  : 실제로 쓰이기 전에 결과를 버퍼링해뒀다가 잘못 쓰였다면 버퍼링해둔 걸 flush하는 거

#### Speculation and Exceptions

만약 미리 우리가 예측한 결과에서 예외가 생긴다면?
ex) null-pointer check하기전에 예측한 로드를 쓴다면?

* Static speculation
  : ISA에서 예외 발생을 실제 값이 확정될 때까지 늦춘다
* Dynamic speculation
  : 명령어가 끝날 때까지 예외를 버퍼링해서 명령어가 끝나면 예외를 발생시킨다



#### Static Multiple Issue

컴파일러가 명령어들을 issue packet라는 그룹으로 만들어두고 하나의 사이클에 이걸 동시에 돌린다. issue packet를 하나로 묶어 생각하기 때문에 Very Long Instruction Word VLIW 구조를 따라간다

그리고 static은 컴파일러가 모든 일을 하니까 컴파일러에서 hazards를 다 없애줘야 하는데

1. 명령어를 reorder해주거나
2. 패킷 안에서 dependencies가 있으면 안 됨(대신 패킷들 사이에는 가능)
3. hazards를 해결하지 못하면 nop을 띄워야



#### Dynamic Multiple Issue

CPU가 어떤 여러 개의 명령어를 실행시킬지 결정한다... 근데 이게 컴파일러의 scheduling이 필요없다는 말이지만 동시에 그렇다고 컴파일러가 아주 손 떼는 건 아니고 도와주기는 한다.

명령어 실행은 out of order로 뒤죽박죽 할 수 있지만 그 결과를 실제 레지스터에 쓸 때에는 순서를 따라야 한다.



#### 왜 Dynamic multiple issue를 쓰나요?

* 컴파일러가 모든 stall을 다 예측할 수 없음 (ex. cache miss는 런타임에서만 알 수 있음)
* 브랜치 결과값이 늘 바뀌는데 그걸 다 커버하면서 스케쥴링이 불가
* 명령 실행이 다르면 latencies나 hazards가 다르게 되어 그걸 커버하려면 dynamic

하지만 우리가 예상하는 만큼 효과가 나지 않는데 그 이유는 아무래도 dependencies + 병렬화는 구현하기가 힘듦