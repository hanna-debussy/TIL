# 00



## '무어의 법칙(Moore's Low)'

모르면 간첩되는 것, 가장 기본이 되는 법칙

: The number of transistors that can be integrated on single chip would double about every two years.
근데 두 배보다 거의 기하급수적으로 늘어남 (보통 그림 자체는 산술급수처럼 보이지만 y축이 Log scale이기 때문에 기하급수 ㅇㅇ)

이제는 무어의 법칙이 유효하지 않다 (한 칩의 집적도를 높이기 힘들어져서 등등의 이유)



이제는 Computers are pervasive

 

## classes of computers

*  Personal computers: 우리가 쓰는 거
* Server computers: 서버 기반… 매우 크다
* Super computers: 최신 과학적 기술적 계산을 위한 (특수한 하나의 목적)
* Embedded computers: Hidden as components of system 컴포넌트 안에 숨어있다 - 저전력 저가 저성능

 

## 단위

- bit는 0 또는 1을 저장

- byte = bit * 8

- kilo > mega > giga > tera > peta > exa
  - 2^10 > ^20 > ^30 …
  - _ > _ > 10^6 > 10^9 > 10^12 … (네트워크를 말할 때는 수가 달라짐)

 

## Language

High-level language: 우리가 치는 코딩

↓

Assembly language: 기계가 읽는 언어. 쓰기 어려워서 하이 레벨이 나온 거

↓

Hardware representation: 2진수binary digits로 표현되는… 010101101000010110 이런 거. 우리는 읽을 수 없다

 

 

 

 

# 01. Performance

 

Processor(CPU)는 세 가지로 구성되어 있다: data path, control, cache memory

- arm core * 2
- processor data path * 2 * 2 

 

## Abstractions

문제를 단순화할 수 있다. hide lower-level detail!
여러 군데에서 사용된다.

- Instruction set architecture(ISA)
  - computer processor에서 쓰인다. software/hardware (cf) SW를 HW로 구현)
  - SW랑 HW를 independent하게 만드는 policy

- Application binary interface(ABI)
  : ISA + system software interface 프로그램이 다른 컴퓨터에서 실행될 수 있는지

- implementation
  - ISA를 실제로 구현할 건가
  - SW랑 HW를 independent하게 만드는 걸 실제로 행할 수 있게 하기 위해 얘가 있음

 

## 기술 발전 트렌드

- volatile(휘발성) main memory: DRAM 

- non-volatile(비휘발성): storage



Dram 용량이 또 무어의 법칙에 맞게 증가한다 (물론 y축은 log scale이라 기하급수긴 하지만)

포포몬쓰는 늘고 가격은 낮춤… 비용 대비 성능이 겁나 빠르게 발전함

 

## Performance

### Defining performance

성능에는 여러가지가 있는데 그 하는 게 중요하다

 

### 우리는 보통 포포몬쓰를 두 가지에 의해 정의된다

1. Response Time: response time: latency: task 처리하는데 얼마나 오래 걸리냐
2. throughput: unit time에 할 수 있는 total work (시간 당 태스크 수 트랜잭션 수 이런)



### 이제 포인트는 둘이서 어떻게 서로 영향을 받느냐…

* response time을 줄이면 throughout은 자동적으로 향상

* 하나의 프로세서를 추가하면 only throughput만이 증가

∴우리는 이제 response time에 집중할 거다 (throughput은 그냥 프로세스 추가하면 늘어나니까)

 

 ### Relative Performance

아하 퍼포먼스 두 개(y는 x보다 얼마나 좋은가)를 비교할 때 식
: [y의 처리시간 / x의 처리 시간 = n]배 더 좋다/나쁘다

 

### Measuring Execution Time

* elapsed time: total response time을 뜻함 system performance를 잴 때 사용. 오직 CPU time을 잰다(I/O time, other job's share를 뺌)

* CPU clocking (하나의 clock(= clock period, clock cycle(CC) 기간) 관련)
  * clock period가 얼마나 짧은가
    ex) 250ps = 0.25ns = 250 * 10^-12s
  * clock frequency(rate): 1초 동안 돌아간 clock cycle
    ex) 40GHz = 4000MHz = 4.0 * 10^9Hz
  * Clock Cycle = 1 / Clock Rate
    1nsec(10^-9) clock cycle = 1GHz(10^9) clock rate

 

 

 

 

 

 