# 03. Arithmetic for Computers

## Introduction

* 사칙연산에 해당
* overflow와 싸워야 한다
* floating-point와 관련된 연산 / 표현 문제



## Addition and Subtraction

### overflow

* 양수 두 개를 더할 때 음수가 나오면, 음수 두 개를 더할 때 양수가 나오면 overflow가 생긴다
* 아니면 음수 - 양수 / 양수 - 음수 에서 overflow가 생긴다
* 이게 생기면 C언어에서는 무시한다...
  * 그래서 프로그램에게 이 문제를 해결하라고 떠넘김
  * ex) MIPS에서는 addu, addui, subu 처럼 overflow의 exception을 만들지 않게 하는 걸 따로 만들어둠



### arithmetic for multimedia

* 아하 그래픽이나 미디어 실행은 보통 8비트나 16비트 데이터라서 64비트 adder를 조각partitioned내서 쓸 수 있게 한다 8비트 8개 / 16비트 4개 / 32비트 2개 이런 식으로 해서 동시에 8/4/2개를 처리할 수 있는 셈

  &rarr; 이걸 SIMD(single-instruction, multiple-data) 라고 하네

* 아니면 멀티미디어에서 saturating operations라고 overflow가 났을 때 값을 줄 수 있는 가장 최댓값으로 주는 거임 #FFF + #FFF 하면 걍 에러 안 나고 걍 #FFF가 되게



## Multiplication

### How to

* a(multiplicand, 64bit(인데 이제 하위 32비트를 쓰고 있는))를 b(multiplier, 32bit)번 곱한다 했을 때 우리는 지금 2진수를 논하고 있는 거니까 b가 0과 1, 즉 그 자릿수에 a가 있냐없냐를 더해줘서 값을 product(64bit)에 구할 거임
* b의 가장 오른쪽이 0이냐 1이냐에 따라 연산이 달라지고 그건 b가 오른쪽으로 움직이면서 2의 자리, 4의 자리, 8의 자리를 탐색 / 반면 a는 왼쪽으로 움직이면서 내가 더해질 자리로 움직인다
* 아 근데 b가 32비트라서 32번 해야 됨



### optimized multiplier

* 어차피 product가 64비트라서 b를 넣어도 자리 남는다면 애초에 하위 32비트에 multiplier를 넣어서 제일 하위에서 하나씩 뽑아내서 상위에 연산하고 버리고 다시 오른쪽으로 밀어내면서 계산을 하자 이말이야
  : add and right shift
* 왜냐면 자리수마다 더하는 그 위치가 왼쪽으로 옮겨지잖아 근데 그 더하는 애는 고정시켜두고 컨베이어벨트를 오른쪽으로 당겨주자 이 말



### fast multiplier

* 걍 adder 여러 개 붙여 쓰는 거
* 그러면? 성능은 좋은데 이제 가격도 높아지는
* 파이프라인 방식? 이래 병렬적으로 여러 개 처리 가능한



### MIPS multiplication

* ?? 일단 명령어에 hi가 들어가면 상위 32비트, lo가 들어가면 하위 32비트를 가져온다는 건 알겠어



## Division

분자: dividend / 분모: divisor / 몫: quotient / 나머지: remainder

* 나누기는 뭔가 고려해야 할 게 많다
* 가장 먼저 분모divisor가 0인지 체크할 것
* 음... 또 수기로 나누는 걸 생각해보면 b*3으로 빼면 나머지 남고 b\*4로 빼면 음수라서 결국 *3이 맞다면 걔가 그걸 어케 알아 4까지 가보고 빽하는 거잖아 그래서 4까지 갔을 때 아 아니네 하고 돌아가기 + 다음 자릿수로 가기 위해 a를 돌려놓는... 그런 연산까지 필요한



### Division Hardware

오 곱하기 HW랑 같네 근데 이제 여기서는 몫이 왼쪽으로 움직이고 분모는 오른쪽으로 움직인다는 거임

결국 다 2진수라서 이 자릿수에서 뺄 만큼이 남아있나? 이걸 보는 거임 뺄 만하다 하면 1 아니면 0



### Optimized Divider

: left shift and subtract

여전히 곱하기와 같다 분자가 하위에 들어가있는 64짜리 한 칸만 쓰자는 거임 근데? 이번엔 이 루프가 시계 반대 방향, 그니까 왼쪽으로 돌아가게 된다

어렵네... 일단 한 칸 왼쪽으로 가서(left shift) 오른쪽에 몫을 넣을 자리를 하나 비워주고 왼쪽으로 뺴꼼 밀려난 애들에서 분모를 빼봐(subtract) 그러고 나서 음수 나오면 그 자릿수에 분모가 못 들어간다는 거고 양수나 0이면 들어간다는 거니까 젤 오른쪽에 전자는 0, 후자는 1을 넣게 된다 그리고 음수 나오면 빼준 거도 다시 더해서 복원시켜줘야 됨 이걸 반복반복

이렇게 하고 나면 상위는 나머지, 하위는 몫이 나오게 된답니다



### Faster Division

이거는? 불가
나누기는 병렬이 불가하다 왜냐면 한 번 빼 봤을때 음수니 양수니에 따라 다음 연산이 달라지기 때문 (conditional)



## Floating Point

컴퓨터에서 어떻게 플로팅 포인트 넘버를 인식하고 처리하냐?

* Floating point: 정수가 아닌 숫자덜 including very small and very large numbers
* normalized scientific notation
  : 그... 3.24 * 10*\*3 이런 표기 있잖아 이런 거 말하는데 뒤의 10의 n승(n을 exponent라고 함) 말고 앞의 숫자를 significand라고 하는데 얘가 소수점 위 1의 자리만 있어야 normalized라고 할 수 있다
  한편 2진수에서는 significand의 소수점 위가 0이 아니어야 하는데 0과 1 뿐이므로 앞의 숫자가 항상 쁠마 1.xxxxx가 된다 1.xxxx \* 2**n 의 모습



### IEEE Floating-point Format

원래 회사마다 실수를 표현하는 방법이 다 달랐는데IEEE에서 754-1985라는 표준을 만들었다 거기에 따르면 single(float)은 32비트, double은 64비트로 표현된다

그리고 그 비트는 세 영역으로 나뉘는데

1. S
   : sign bit, 0이면 0과 양수, 1이면 음수
   &rarr; 왜냐면 (-1)에 이 S를 지수로 올려주게 돼서 -1**0 은 1, -1\*\*1은 -1 이렇게 가는 거
2. Exponent
   : single은 8비트, double은 11비트 / bias는 single이 127, double이 1023
   지수... 2의 지수인데 다만 여기서 저장하는 건 실제 지수에다가 bias라는 걸 더한 값을 저장한다 아 아아 왜냐면 0과 1 뿐이니까 음수인 지수를 저장할 수 없잖아!!! 그래서 그거 표현하려고 하는 거
   single로 예를 들면 00000000부터 11111111을 저장할 수 있는데 가장 작은 value는 00000001이겠고 얘는 1-127 해서 -126승을 표현 가능하게 됨 반면 가장 큰 value는 11111110이고 254-127 = 127승을 표현하게 되는 것두와리
3. Fraction
   : single은 23비트, double은 52비트
   얘가 뭐냐면 significand의 소수점을 말한다 그러니까 significand - 1이라고 할 수 있지 (2진수니까)
   오 얘만 저장하는 이유는 2진수에서는 항상 1의 자리가 1이기 때문에 굳이 저장하지 않겠다는 것 오

그래서 저렇게 표현을 하면 single은 대략 10진수 기준 소수점 여섯 자리까지 표현할 수 있고(정확하고) double은 소수점 16자리까지 표현이 가능



### Example

-0.75를 표현해보자

1. 일단 음수니까 S는 1
2. fraction은 0.75 = 0.5 + 0.25 = 2**\-1 + 2\*\*-2 = 0.11(2진수) 가 된다
   끈데? significand는 1의 자리가 무조건 1이어야 하니까 1.1 \* 2\*\*-1이 되겠고 fraction은 0.1
3. exponent는 -1승이 찐이고 우리가 저장할 거는 127 더해야 하니까 -1 + 127 = 126이 저장된다



### Addition

더해보자고

#### decimal

원래 10진수로 표현하자면

1. 일단 exponent를 맞춰주고
2. 그 다음 바뀐 significand를 더해주고
3. 만약 10의 자리 이상을 넘어갈 만큼 커졌으면 다시 fraction 조정해서 normalized 해줌
4. 거기에 마지막으로 만약에 원래 더하던 두 개 숫자가 소수점 이하 세 자리, 그니까 4-digit 이었다면 얘도 fraction이 막... 소수점 네 자리라 해도 그거 반올림해서 세 자리로 같이 맞춰줘야 한다 아 물론 여기서도 예를 들어 9.99를 반올림하면 10.00이 되니까 renormalized해주는 절차가 필요방스



#### binary

방법 당연히 같음 지수 맞춰서 significand끼리 더해주고 normalized 해주고 round랑 renormalized 필요하면 해주고



#### Floating-Point Adder Hardware

걍 정수 계산보다 훨씬 복잡하기 때문에 한 클럭사이클에서 해내려면 너무 오래 걸린다
그래서 보통 여러 사이클에 걸쳐서 하게 됨 &rarr; 그래서 pipeline 형식을 취하게 된다 (4장에 나온대)



### Multiplication

1. 지수를 더해야겠지 곱하기니까
2. 그다음 significand끼리 곱하고
3. 10의 자리(2의 자리) 이상 넘어가면 normalize하고
4. 만약 또 조정해야하면 round랑 renormalized하고
5. 그리고 Sign도 필요하면 고려해야 한다



### FP Arithmetic Hardware

multiplier의 복잡도는 adder보다 더하다 significand를 곱해야하기 때문
보통 사칙연산, 역수, 제곱근을 구해주는 걸 제공해주고 fp랑 integer 변환도 지원한다
마찬가지로 여러 사이클이 걸리지만 다 파이프라인화 시킨다



### FP Instruction in MIPS

* 보통 FP HW는 보충... 보조적인 프로세서(coprocessor)로 나옴 ISA extension 격
* 아하 그래서 FP를 위한 레지스터가 따로 존재하게 됨: 32개의 32비트 레지스터 $f0 ~ $f31 (아하 double은 두개 붙여서 64비트를 만드네 $f0과 $f1이 한 쌍, 그 다음 2와 3이 한 쌍 이런 식, 대표는 앞에 오는 거)
  아 근데? MIPS 2 버전에서는 그냥 64비트짜리 레지스터가 걍 따로 또 32개 지원하게 됨
* 그리고 이 레지스터들은 정수에서는 안 먹힘 호환되는 게 아니고 오로지 플로팅에서만 동작
  왜냐하면 명령어 길이 굳이굳이 늘일 필요가 없기 때문
* load: single - `lwcl`, double - `ldcl`
  store: single - `swcl`, double - `sdcl`



### Accurate Arithmetic

* 아 그 반올림 방식을 우리가 정할 수 있어서 그걸로 정확도를 더 정밀하게 올릴 수 있다
* 그리고 모든 프로그램들이 이... Std 754-1985 이거를 따르는 게 아니라서 중요한 부분은 대부분 따르지만 모든 implement나 options들이 탑재되어 있는 건 아니다 왜냐면 다 탑재하면 복잡도는 올라가고 비싸지니까 대신 안 탑재된 거면 안 돌아갈 수 있겠지 그래서 잘 실어야 한다는 말씀



## Parallelism and Computer Arithmetic: Subword Parallelism

그... 보통 그래픽이나 오디오가 8비트나 16비트 쓰잖아 근데 예를 들어 내가 128비트짜리 adder를 써 그러면 8비트\*16개 나 16비트\*8개 써서 동시 연산 되게 내가... 그렇게 성능 향상을 하겠지? 

이런 걸 data-level paralleism, 혹은 vector parallelism, 제일 자주 쓰는 말은 Single Instruction, Multiple Data 해서 SIMD라고 한다



## Fallacies and Pitfalls

### Right Shift and Division

우리가... 곱하기 할 때 a를 b번 곱한다고 하면 그 a가 한 자리수씩 올라가면서 더해지잖아 그러니까 2\*\*n승씩 올라가는 거고 그거는 n번 left shift해서 더하게 된다

&rarr; 그렇다면... right shift하면 나눠져? 라는 의문이 생긴다는 것

근데 그거는 unsigned integer에 한해서만 가넝한



### Associativity

parallel program들은 더하기 순서에 따라 결과가 달라질 수 있음 아 좟나 큰 수랑 있으면 좟나 작은 수가 무시될 수 있군 그래서 큰 수끼리 먼저 더하고 작은 수를 나중에 더해주삼요



### Who Care About FP Accuracy?

ㅋㅋㅋㅋㅋㅋㅋ 사실 일반 사람들은 크게... 신경쓰지 않음 내 계좌에 0.00003원씩 나간다 해서 쉬익쉬익 이러진 않을 거 아님 근데? 이게 한 나라 국민들에게 모두 적용된다면? 전 세계는? 뭔가... scientific code에서는 중요해진다는 뜻

그리고 Intel Pentium Floting point DIVision(FDIV) bug가 있었음...
