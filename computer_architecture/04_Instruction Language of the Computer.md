# 02. Instruction: Language of the Computer

## Supporting Procedures in Computer Hardware

### Execution of a Procedure 6단계

함수를 부르는 메인 루틴이 caller, 불려지는 함수가 callee

1. caller가 callee에 접근할 수 있게 parameters(변수... a.k.a. arguments)를 놓는다
   : $a0 - $a3 의 네 개가 argument registers
2. caller가 calle로 컨트롤을 넘긴다(callee가 실행된다는 뜻)
3. callee가 실행되면 callee가 실행되기 위해 필요한 스토리지 공간(=memory)을 할당한다(보통 stack에 할당 받음)
4. callee가 자기 할 일 한다
5. 할 일이 다 끝나면 caller가 접근할 수 있는 공간에 result vale를 갖다놓는다
   : $v0 - $v1 의 두 개가 value registers
6. callee가 caller로 컨트롤을 넘긴다
   : 여기서 $ra (return address)가 쓰이는데 리턴해야 할 값이 있는 주소가 있는 register임 그래서 이게 실행되면 program counter register로 복사돼서 ra에 있는 명령어(도출된...)부터 실행하게 됨



### Procedure Call Instructions

* procedure call: Jump And Link (JAL)
  `jal ProceduresLabel`: 레이블에 있는 명령어로 가게 됨 + 현재 이 명령어의 다음에 있는 명령어의 메모리 주소를 $ra에 넣게 됨
  오! jal 뫄뫄 /n 다른연산 이렇게 있으면 뫄뫄 먼저 해야하니까 뫄뫄로 가는 대신에 다음 줄의 다른 연산으로 돌아오기 위해 $ra에 저장해둔다는 거구나
* procedure return: Jump Register (JR)
  `jr $ra`: ra에 있는 걸 program counter(PC)로 복사
  아니면 computed jumps에도 쓰임(ex. switch/case문(≒ if elif 문! 뭔 말인지 알겠지))



### Leaf Procedure Example

: 하나의 함수에서 다른 함수를 부르지 않는 씩씩한 함수네...

1. addi $sp, $sp, -n
   : stack pointer. n이 변수 갯수라 치면 그만큼 슥삭 해서 가져다가 메모리로 쓰겠다는 말
2. sw $s0, 0($sp)
   : store word 기억나니 $s0를 stack[0]에 복사해서 s0값 보존하려구
3. $a0 - $a4 들과 $t0 - 들로 함수가 하라는 만큼 연산을 해
4. add $v0, $s0, $zero
   :오 zero가 이렇게 복사할 때 쓰이는 거 ㅇㅇ 완성된 $s0를 return할 $v0에 넣어줌
5. lw $s0, 0($sp)
   : load word... 지금 $s0 값에는 우리가 연산을 다 해서 결과값이 들어있는데 그걸 다시 원상복원 해주겠다는 뜻
6. addi $sp, $sp, n
   : 스택 잘 썼습니다 돌려드릴게요
7. jr $ra
   : ra의 값을 pc로 복사해서 caller로 가게 함 그러니 이 다음은 caller가 실행될 것



### Non-Leaf Procedures

: 한 함수 내에서 다른 함수(me 포함)를 부르는 것...(ex. factorial) 이기 때문에 caller는 return address랑 call 다음에 쓰일 변수 등등을 저장하고 있어야 함 + 사용 후에 복원시켜야 함

0. 뭐임 왜케 복잡해

1. addi $sp, $sp, -n
2. $ra랑 $a0이랑 각각 $sp 적당한 자리에 sw (오 C언어에서 무슨 내가 자리 할당해줘야 한다는 게 이런 건가)
   : 왜냐면 재귀만 해도 자꾸 재귀되면서 바뀐 변수가 들어가고 들어가고 들어가니까 바뀌는 변수도 저장하고 그거에 대한 리턴값들도 재귀 때마다 바뀌니까 그거도 저장하구
3. 그러면 안은 똑같아 팩토리얼이라 치면
   1. n이 1보다 작지 않으면 Label1 으로 가고
   2. 아니면 1 반환하고 jr $ra를 적어줘야 함
      저 끝났어요 하면 이제 다시 `jal main_func` 다음 줄로 가게 되는 거지
4. Label1로 들어오면
   1. (변수 -1) 하고 다시 재귀를 돌려
   2. 그럼 다시 메인함수로 가서(여기가 `jal main_func`인데 이 말이 그 해당 함수로 간다는 뜻과 동시에 그 해당함수에 다녀오면 다시 돌아올 곳(이 다음 줄)을 저장하는 역할도 하는 것)
   3. 그 시점의 값들을 저장해뒀다가 또 돌리고 하다보면
   4. n=1이 되는 순간이 오니까 딱 재귀처럼 그 때부터 아까 저장해뒀던 값들 회수하면서 올라가는데 내가 원하는 값으로 변한 리턴값은 가져가고 stack pointer에 복사한 걸 lw로 그 자리에 되돌려놓으면서 가는? 그런느낌인 거 같은데 데이터를 원상복구 시켜준다는 것
5. addi $sp, $sp, n
   : 스택 잘 썼습니다
6. jr $ra
   : 마지막 쨘



### Local Data on the Stack

* Local data는 stack에 저장된다!!!!!!!!!!!!!!!!!!!!
* 아하 sp는 stack의 top을 저장하고 있음
* procedure frame(a.k.a. activation record)은 함수를 위한 프레임 
  그리구 frame pointer는 현재 실행하는 함수frame의 시작 
* ?????????????
* 뭔 말임



### Memory Layout

* stack: 가장 위, stack은 아래로 쌓이고(넣으면 아래로 내려간다고)
* dynamic data: heap... 위로 쌓인다 ex) C에서 malloc, Java에서 new
* Static data: global variables 전역변수와 global pointer($gp)... static data를 저장할 수 있는 중간값을 가지고 있는 거래
* Text: 명령어들
* Reserved: 가장 아래



## Communicating with people

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