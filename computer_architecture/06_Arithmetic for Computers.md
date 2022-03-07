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

