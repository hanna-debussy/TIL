# 02. Instruction: Language of the Computer

## Supporting Procedures in Computer Hardware

### Execution of a Procedure 6단계

함수를 부르는 메인 루틴이 caller, 불려지는 함수가 callee

1. caller가 callee에 접근할 수 있게 parameters(변수... a.k.a. arguments)를 놓는다
   : $a0 - $a3 의 네 개가 argument registers
2. caller가 callee로 컨트롤을 넘긴다(callee가 실행된다는 뜻)
3. callee가 실행되면 callee가 실행되기 위해 필요한 스토리지 공간(=memory)을 할당한다(보통 stack에 할당 받음)
4. callee가 자기 할 일 한다
5. 할 일이 다 끝나면 caller가 접근할 수 있는 공간에 result vale를 갖다놓는다
   : $v0 - $v1 의 두 개가 value registers
6. callee가 caller로 컨트롤을 넘긴다
   : 여기서 $ra (return address)가 쓰이는데 리턴해야 할 값이 있는 주소가 있는 register임 그래서 이게 실행되면 program counter register로 복사돼서 ra에 있는 명령어(도출된...)부터 실행하게 됨



### Procedure Call Instructions

* procedure call: Jump And Link (JAL)
  `jal ProceduresLabel`: 레이블에 있는 명령어로 가게 됨 + 현재 이 명령어의 다음에 있는 명령어의 메모리 주소를 $ra에 넣게 됨
  오! `jal 뫄뫄 (엔터하고) 다른연산` 이렇게 있으면 뫄뫄 하고 오면 다음 줄의 다른 연산으로 가야 하니까 거기를 $ra에 저장해둔다는 거구나
* procedure return: Jump Register (JR)
  `jr $ra`: ra에 있는 걸 program counter(PC)로 복사
  아니면 computed jumps에도 쓰임(ex. switch/case문(≒ if elif 문! 뭔 말인지 알겠지))



### Leaf Procedure Example

: 하나의 함수에서 다른 함수를 부르지 않는 씩씩한 함수네...

1. addi $sp, $sp, -n
   : stack pointer. n이 변수 갯수라 치면 그만큼 슥삭 해서 가져다가 메모리로 쓰겠다는 말
2. sw $s0, 0($sp)
   : store word 기억나니(register=>memory) $s0를 stack[0]에 복사해서 s0값 보존하려구
3. $a0 - $a4 들과 $t0 - 들로 함수가 하라는 만큼 연산을 해
4. add $v0, $s0, $zero
   :오 zero가 이렇게 복사할 때 쓰이는 거 기억나지 완성된 $s0를 return할 $v0에 넣어줌
5. lw $s0, 0($sp)
   : load word... 지금 $s0 값에는 우리가 연산을 다 해서 결과값이 들어있는데 그걸 메모리에서 레지스터로 가져와서 다시 원상복원 해주겠다는 뜻
6. addi $sp, $sp, n
   : 스택 잘 썼습니다 돌려드릴게요
7. jr $ra
   : jr(jump register)... ra의 값을 pc로 복사해서 caller로 가게 함 그러니 이 다음은 caller가 실행될 것



### Non-Leaf Procedures

: 한 함수 내에서 다른 함수(me 포함)를 부르는 것...(ex. factorial) 이기 때문에 caller는 return address랑 call 다음에 쓰일 변수 등등을 저장하고 있어야 함 + 사용 후에 복원시켜야 함

0. 뭐임 왜케 복잡해

1. addi $sp, $sp, -n
2. $ra랑 $a0 값들 각각 $sp 적당한 자리에 sw (오 C언어에서 무슨 내가 자리 할당해줘야 한다는 게 이런 건가)
   : 왜냐면 재귀만 해도 자꾸 재귀되면서 바뀐 변수가 들어가고 들어가고 들어가니까 바뀌는 변수도 저장하고 그거에 대한 리턴값들도 재귀 때마다 바뀌니까 그거도 저장하구
3. 그러면 안은 똑같아 팩토리얼이라 치면
   1. n이 1보다 작지 않으면 Label1 으로 가고
   2. 아니면 1 반환하고 jr $ra를 적어줘야 함
      저 끝났어요 하면 이제 다시 `jal fact` 다음 줄로 가게 되는 거지
4. Label1로 들어오면
   1. (변수 -1) 하고 다시 재귀를 돌려
   2. 그럼 다시 메인함수로 가서(여기가 `jal fact`(정확히는 이 다음 줄)인데 이 말이 그 해당 함수로 간다는 뜻과 동시에 그 해당함수에 다녀오면 다시 돌아올 곳(다음 줄)을 저장하는 역할도 하는 것)
   3. 그 시점의 값들을 저장해뒀다가 또 돌리고 하다보면
   4. n=1이 되는 순간이 오니까 딱 재귀처럼 그 때부터 아까 저장해뒀던 값들 회수하면서 올라가는데 내가 원하는 값으로 변한 리턴값은 가져가고 stack pointer에 복사한 걸 lw로 그 자리에 되돌려놓으면서 가는? 그런느낌인 거 같은데 레지스터의 데이터를 원상복구 시켜준다는 것
5. addi $sp, $sp, n
   : 스택 잘 썼습니다
6. jr $ra
   : 마지막 쨘



### Local Data on the Stack

* Local data는 stack에 저장된다!!!!!!!!!!!!!!!!!!!!
* 아하 sp는 stack의 top을 저장하고 있음
* procedure frame(a.k.a. activation record)은 함수를 위한 프레임 말 그대로 함수의 테두리라 보면 된다 함수 크기가 얼마나 되묘?
  그래서 frame pointer는 이 함수의 첫(?) 테두리 그니까 시작점을 가지고 있다
* 이게 왜 쓰이냐면 non-leaf에서 내가 예를 들어 func1을 주소값 4에서 시작하고 안의 연산 하다가 그 안에 func2가 들어있는 거야 그러면 func1이 완성되려면 func2를 수행해서 같이 담아야 하니까 일단 func2에 가서 막 연산을 해 근데 연산 중의 값들이 전부 stack에 쌓이잖아 그래서 신나게 func2 연산하고 나서 돌아가야 할 func1이 어딘지 모름... 그래서 그 func1의 시작점인 4를 fp에 저장해두고 func2가 거슬러 올라올 시점에 이 func2의 값이 어디로 반환되어야 하는지를 알려주는 거임... 근데 이거를 sp가 다음 stack 올 자리라 했잖아 여기에 func2를 바로 시작하는 게 아니라 func2가 시작되는 시점에 아예 func1 주소(4)를 박아버림 너 돌아갈 곳 여기야 해놓고 시작하는 거 그리고 다시 fp는 이 func2가 시작되는 시점을 다시 가져감
* 이게 원래 이렇게 문과식으로 구구절절하게 적혀도 되는 거임?



### Memory Layout

아래에서부터 위로 보면 된다 스택에 쌓이는 구조대로 필기해뒀엉

* stack: 가장 위, stack은 아래로 쌓이고(넣으면 아래로 내려간다고???? 이게 뭐지)
* dynamic data: heap... 아 stack과는 달리 메모리 공간이 동적으로 쌓이는 거구나 아래->위로 쌓인다 ex) C에서 malloc, Java에서 new 아 stack은 메모리 할당 해제가 함수 시작되면/끝나면 자동적으로 되는데 이거는 내가 관리를 해줘야 한대 그 메모리 할당하는 함수가 C에서 malloc()이라 하는구나 참고로 해제는 free()
* Static data: global variables 전역변수와 global pointer($gp)... static data를 저장할 수 있는 중간값을 가지고 있는 거래
* Text: 명령어들
* Reserved: 가장 아래



## Communicating with people

닝겐노 언어 관련

### Character Data

* byte-encoded char sets: 8-bit 
  ex) ASCII
* Unicode: 32-bit 
  ex) UTF-8



### Byte/Halfword Operations

수의 비트 범위를 확장시키는 거(8-bit => 16-bit 등등) 그니까 같은 값을 더 많은 비트를 이용해서 표현하겠다고
약간 바이트를 저장하는 방법인 거구나

* `lb(load byte) rt, offset(rs)`: offset 메모리에서 특정 한 바이트를 타겟 레지스터(rt)에 넣는 거... 라는데 찾아보니까 레지스터의 하위 8비트(0-7)를 32-bit에 저장하려고 7번 비트를 나머지 8-31에 다 넣는 거임 그래서 32비트인데 이제 연장된 버전으로 로드하는 거 물론 값에는 변화가 없음
  `lh rt, offset(rs)` load halfword
* `lbu(load byte unsigned) rt, offset(rs)`: offset에서 한 바이트를 32bit으로 확대해서 rt에 넣음 음 이거보다는 저기는 7번째를 쭉 77777... 했다면 여기는 8-31을 0으로 채워넣는 거
  `lhu rt, offset(rs) ` 얘는 halfword를
* `sb(store byte) rt, offset(rs)`: 바이트 값을 스토어
  `sh rt, offset(rs) ` ㅇㅇ...



## MIPS Addressing for 32-bit Immediates and Addresses

### 32-bit Constants 상수

대부분의 상수 값은 작아서 16비트면 충분히 표현이 가능함 하지만... 역시 가끔은 32비트가 필요하다

`lui rt, 61(contstant)` load upper immediates 변수를 타겟 레지스터의 상위 16비트(왼쪽)에 일단 61을 넣음 그리고 하위 16비트(오른쪽) 16비트에 0으로 채워

그러고 나서 `ori $s0, $s0, 2304` 하면 하위에 2034가 들어감

32비트 값이 들어가있는 메모리에서 상수 값을 읽어와야 하는데 혹시 명령어가 2개면 더 느리지 않을까? 라고 생각할 수 있지만 이게 레지스터에서만 작동하는 거라 메모리에 엑세스하지 않는대 그래서 메모리에서 하나의 명령어로 가져오는 것보다 더 빠르대



### Branch Addressing

상위부터 차례대로
operation code(6비트)
rs(5비트) register operand피연산자 1번
rt(5비트) 피연산자 2번
그리고 나머지 하위 16비트에 상수(or address) 넣음

label에 있는 명령어가 있는 곳인 branch target은 보통 branch(if문 같은 거) 근처에 있음 (forward or backward)
이런 걸 PC-relative addressing이라 한대

* target address = PC + (offset(=하위 16비트)*4) 거리!
* 현재 A를 실행하고 있으면 PC는 A 다음의 B를 가지고 있음 내가 다음에 할 일을 메모하고 있다는 거니까 PC는 미리 4만큼 증가되어있다는 것!



### Branching Far Away

물론 branch target이 너무 멀리 떨어져 있을 수도 있다... 그럴 때는 아하

`beq $s0, $s1, L1` s0 == s1이면 L1으로 가라 할 게 아니라
`bne $s0, $s1, L2
j L1`  != 일 때 L2로 가고 같다면 밑으로 계속 가니까 밑에다가 jump를 써서 L1으로 보내버림 그러면 jump는 16이 아닌 26bit를 쓰고 있기 때문에 더 멀리 갈 수 있다구 한다



### Jump Addressing

상위 op(6비트) 나머지 26비트가 address 이런 걸 J-type이라 하는구나

`j`나 `jal` 명령어들은 모두 어디에나 가능함 모든 address를 전부 인코딩 가능: Pseudo direct jump addressing

target address = address의 26개 가져오고 끝에 00 두개 붙여서 28비트로 만듦 그리고 나머지 4비트는 PC의 하위(가장 끝) 4비트를 가져와서 씀



### Addressing Mode Summery ★

1. Immediate addressing: i로 끝나는 명령어들
2. Register addressing: r-format addressing
3. Base addressing: Load/Store 명령어
4. PC-relative addressing: Branch에 해당
5. Pseudo direct addressing: jump 명령어들



## Translating and Starting a Program

### Translation and Startup

1. 우리가 C program(high level lang)을 짜면
2. compiler를 통해 compile을 하고
3. Assembly language program으로 만들게 된다
4. 이걸 assembler를 통해
5.  object code, 즉 머신 랭귀지죠 binary code로 바꾸는 겁니다
6. 근데 이 object code와 프로그램에서 사용한 라이브러리에 대한 object code를 연결하는 linker를 통해
7. 실행 파일을 만든다
8. 이 실행 파일을 메모리에 올려서 로드해주는 게 loader
9. 메모리까지 닿게 되는 것



### Assembler Pseudoinstructions

어셈블리 프로그램을 쉽게 해주려고 (원래는 지원 안 해주지만) 가상으로 지원해주는 명령어들 어셈블러가 실제 명령어로 바꿔준대

어셈블러 프로그램 왈 `move $t0, $t1` => 어셈블러가 듣기를 `add $t0, $zero, $t1`

cf) $at ? assembler temporary 명령 내 임시값



### Producing an Object Module

어셈블러는 프로그램을 머신 언어로 바꾸는데 이 머신 랭귀지, 오브젝트 코드로 프로그램을 짜게 된다 

* Header: 오브젝트 모듈에 대한 내용
* Text segment: 명령어들
* Static data segment: 전역 변수
* Relocation info: 어떤 것들은 시작 주소에 의해서 주소가 결정되는데 그런 정보들을 말함
* Symbol table: 전역 변수에 대한 정보들
* Debug info: 디버깅 관련 소스 코드들

이런 걸 가지고 하나로 묶어서 실행 파일을 만들게 되는 거임

1. 코드들을 합치고
2. 각각의 레이블들의 주소값을 결정(resolve labels)
3. location dependent와 external reference들을 patch 즉 맞춰준다

근데 그... location에 의존적인 얘네들은 사실 우리가 virtual memory를 쓰기 때문에 절대 주소를 통해 쓰면 되므로 내버려둬도 됨 원래는 relocating loader에 의해서 값을 바꿔줘야 하는데 그걸 덜어주는 거



### Loading a Program

메모리 올려보자고

1. 헤더 읽고 세그먼트들 뭐 있고 크기 어떤지 본다
2. virtual memory address space 만들고
3. text와 memory를 복사해서 올림
4. arguments들을 stack에 할당
5. register 초기화
6. 처음 시작하는 루틴으로 jump



### dynamic Linking

static linking 이랑 반대인데 장점이 많아서 요즘 이거 많이 쓴대 특히 library procedure

* 실행할 때 링킹이 된다!
* 그러려면 relocatable한 실행 코드 필요
* 개짱조은 장점
  1. static에 비해 실제 이미지의 크기가 커지지 않음
  2. 새로운 라이브러리가 나오면 static은 실행 파일을 새로 만들어야 하는데 얘는 그럴 필요 없음 자동으로 새로운 라이브러리가 적용되게 할 수 있음



### Lazy(dynamic) Linkage

라이브러리 100개를 썼다 치면 실제로는 10개만 자주 사용하고 나머지는 특수한 경우에만 사용을 하는 거 그럴 때 사용하는 건데... 어렵네

내가 명령어(text) 1번을 실행시켰어 근데 그 lw하려는 데이터 1이 어딘가에 있겠지? 근데 그 데이터가 까보니 또 다른 text야... 그리고 거기 안에 j가 있어서 또 어떤 text로 갔고 그 안에 j가 data나 text라서 결국 이 안에 있는 데이터가 원래 찐 명령어 1번이 원하는 리얼 데이터였던 거임... 그니까 걍 거기까지 가는데 존나 복잡했다는 거임 근데 이거를 헷갈리니까 한 번 이렇게 해두고 나면 답습하지 말고 걍 data1에 리얼 데이터가 있던 주소를 저장해두고(이게 루틴이 되는 거) 슉슉 뛰어넘자는 거

단점은 느림... static linking은 점프나 브랜치 하나면 끝나는데 얘는 처음 실행이 엄청 복잡하고 느리고... 리얼 데이터까지 가는 데에 data1이라는 게 필요해서 indirect라는 점이 좀... 별로임

근데? 디버그할 때 버전을 업그레이드 시키면 static은 업글 할 때마다 적용하기 위해 실행파일을 새로 만들어야 함 그게 좀... 어려운 일이지 근데 dynamic은 이런 과정을 통해 리얼 데이터만 동적으로 바꾸면 된다는 거임 실행파일을 더 만들 필요가 없음 그래서 보편적으로 사용되고 있다