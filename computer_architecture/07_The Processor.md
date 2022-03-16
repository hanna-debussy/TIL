# 04. The Processor

## Introduction

두 가지 MIPS implementations에 대해 배울 겁니다
: a simplified version, a more realistic pipelined version



실행 순서

1. 프로그램 카운터가 주소값에 해당하는 메모리에 가서 명령어를 읽어온다
2. 레지스터에 access
3. 그 명령어에 따라 일을 한다



### CPU overview

PC가 자동으로 4를 더하고 instruction memory에서 불러온 값을 가져와 그 두개를 더하면 그게 branch target address가 된다

그 다음 register에서 일을 하고 두 개의 output을 내면 ALU(Arithmetic/Logic Unit)에 들어가고 그 output이 data memory에 쇽 들어감



## Logic Design Conventions

우리는 0과 1밖에 없는데... 1bit에 하나의 와이어가 들어간다 그래서 multi bit을 처리하려면 여러 개의 와이어가 필요하대

회로는 크게 두 가지로 나뉘는데

1. **combinational logic**
   * 데이터의 값을 좌우한다. function of input... input에 의해 output이 결정되므로 input이 같으면 output도 같다
     ex. AND-gate, multiplexer, adder, arithmetic/logic unit
   * 하나의 clock cycle에 하나의 연산이 다 끝나야 한대 그래서 combination logic이 복잡하면 clock이 길어지게 되는 거임 그래서 긴 cycle이 하나가 되면 간단한 연산이라도 그 cycle에 맞춰줘야 하니까 별 거 아닌 것도 느려질 수 있음
2. **state(sequential) logic**
   : 어떤 정보를 저장하고 있어서 다음 state가 달라진다. 
   edge-triggered: clock에 동기화되어있어서 clock이 rising인지 falling인지에 따라 바뀐대 보통은 rising edge 때 값이 업뎃되는데 거기다가 write라는 명령? flag? signal이 있으면 clock이 rising이어도 write가 1이어야 업뎃됨 



## Building a Datapath 

말 그대로 data들이 components들을 거쳐가는 그 path... data나 addresses를 CPU에서 처리해주는 element들을 어떻게 연결할 건가?



1. **Instruction Fetch**
   : 프로그램 카운터에 32(64)bit register가 들어가면 두 가지 과정이 일어나는데

   1. pc+4(8) (다음 칸)이 다시 pc에 들어가게 된다(그니까 다음 칸에 있는 값을 다시 처리하기 위해... 약간 재귀 느낌? 뭔 말인지 알겠니
   2. pc가 instruction memory에 들어가 해당 pc에 있는 address에 있는 명령어를 읽어와서  다음 단계로 넘어감

2. **R-Format Instruction**
   : register 간의 연산... 두 register(source, target register)를 통해 읽은 걸 ALU로 연산하고 그 결과를 destination register를 통해 저장 ㄴㄱ

   1. register에는 저장하는 창구가 네 갠데
      1 2번이 read register(5bit)라고 하나가 source 하나가 target
      3번이 destination register(결과 적으라고, 5bit)
      4번이 결과가 저장될 곳(32bit)
   2. 그러면 두 개의 read register로 읽은 두 개의 data(32bit)는 ALU에 들어가게 된다
      \+ target register는 다음다음 단계인 data memory에도 들어감
   3. ALU control은 4 bit고 여기서 연산 삐릭삐릭
      그 결과가 4번 창구로 들어가고 또 다음 단계로 넘어가게 된다

3. **Load/Store Instruction**
   : read register operands... data memory에 들어온 ALU의 값(얘는 address가 됨)과 target register(32bit) 이렇게 두 개가 들어오면 결과값이 하나 나오게 되는데 address가 만약 load 명령어면 address에 해당되는 32bit 값이 그대로 나오고 store 명령어면 address data에다가 target register의 값을 씌워버림
   data memory에는 flag가 두 갠데(MemRead, MemWrite) load 명령어면 MemRead가, store 명령어면 MemWrite가 1이 된다
   그리고 offset이 16bit였는데 그 16bit를 32bit로 바꿔준다(sign-extend, 상위에 복사)

4. **Branch Instructions**

   1. register 값 읽어오고 ALU를 한다

   2. substract을 해서 값이 0인지 아닌지(값이 같은지 아닌지)를 output으로 낸다

   3. calculate target address하기

      1. sign-extend해주고
      2. 왼쪽으로 2bit 움직인다 즉 *4를 하는 셈 for 명령어 넣기 32bit니까...
      3. pc에 +4 까지 해준다면? (1단계 fetch에서 +4 해줬으니까 target도 +4 해줘야지)

      이러면 branch target 이 output으로 나옴



## A Simple Implement Scheme

### ALU Control

Load/Store, Branch, R-type에서 쓰인다
4bit라서 0000, 0001, 뭐 이렇게 있넴...

#### combinational logic derives ALU control

![img](https://www.cs.fsu.edu/~hawkes/cda3101lects/chap5/F5.14.gif)

cf) ALUOp: ALU Operand
사진의 ALU control input의 앞에 0을 하나 더 붙여야 됨 4bit니까

ALU control을 입력하면 action이 실행



#### control signals defived from instruction

* R-type: opcode, source register, target register, destination register, shiftamount, function로 나뉨
* Load/Store: opcode(35 or 43), rs, rt, address(offset)
* Branch: opcode(4), rs, rt, address(offset)

cf) opcode는 6bit



### Datapath with Control

datapath에 control을 끼워보자

#### R-type Instruction

![소스 이미지 보기](https://d2vlcm61l7u1fs.cloudfront.net/media%2Fa46%2Fa46c6383-ecb8-407a-8234-c53a12c6b40c%2FphpIWmbrj.png)

와!
그... 회색 부분은 하드웨어적으로는 돌아가지만 우리는 거기서 나오는 정보는 쓰지 않는다는 뜻이고

r-type은

1. pc에서 instruction memory에서 명령어를 읽어서 register로 간 정보가 ALU에서 처리되고 그 결과가 그대로 data memory를 거치지 않고 mux에 의해(mux는 두 개의 와이어가 들어오면 그때그때 선택해서 픽할 수 있음) 다시 register 4번 창구에 들어옴
2. 한편 pc는 걍 add로 4bit 간 다음에 다시 돌아온다



#### Load Instruction

![소스 이미지 보기](https://image3.slideserve.com/5802330/datapath-for-load-instruction-l.jpg)

개짱인둡

여기는 data memory에 주목하면 될 거 같다 ALU를 통해 들어온 address의 명령어를 보니까? load네... 그러면 rt 필요 없이 address의 data만 다시 mux를 통해 register에 보내주면 되는 것 



#### Branch-on-Equal Instruction

![소스 이미지 보기](https://i.stack.imgur.com/odCHi.png)

ㅇㅇb

data memory는 아예 쓰지 않고 ALU가 보내는 substract연산 값(같냐 다르냐)에 따라 pc의 값이 0 or 1로 갈릴 수 있다



### Implementing Jump

jump 명령어를 만들어보자 (이게 지원을 하는 게 있고 아닌 게 있나봄...?)

jump는 6bit의 opcode(2)와 나머지 26bit의 offset을 가지고 있는데 현재 최상위 4bit를 가져오고 offset 26bit를 왼쪽으로 두 칸 옮기고 00 넣어서 28bit로 늘려준 걸 가져와 붙임... 그러면 이게 짬푸

jump를 opcode가 읽을 수 있도록 하게 위해서는 extra control signal이 필요하다

![소스 이미지 보기](https://www.cs.drexel.edu/~jjohnson/2012-13/fall/cs281_fa12/assignments/Figure4_24.png)

다른 거 바뀐 건 없고(안 쓰고) 저 위에 브랜치 쪽 보면... 최하위 26bit가 오면 왼쪽으로 2 옮겨서 28로 만들고 adder 밑에 있는 4비트 저거랑 붙여버림 ㅇㅇ 그 32비트를 MUX...가 만약에 야 점프! 하면 밑에 브랜치 대신 이걸 보내주는 거



### Performance Issues

* 가장 긴... 수행시간이 한 clock이 되는데 보통 가장 길게 걸리는 게 load instruction이다. 거치는 게 제일 많구나 pc instruction memory register ALU data memory register file... 다 거치기 때문
* 그러면 각자 다 다른 clock으로 하면 안 돼? &rarr; ㅇㅇ 기술적으로 힘들어 왜냐면 보통 프로세스들이 다 clock에 동기화되어있기 때문에... 통일이 되어야
* 그래서 Make the common case fast 하라 이말이야



## An Overview of Pipelining

가보자고

pipeline이 뭐냐?

![소스 이미지 보기](https://th.bing.com/th/id/R.4bf60a01f5b5686d2032c38ad09342a2?rik=nrA4GQPgkTXg1w&riu=http%3a%2f%2fcs.stanford.edu%2fpeople%2feroberts%2fcourses%2fsoco%2fprojects%2frisc%2fpipelining%2flaundry2.gif&ehk=3OXTr8WR1Wm5a3duKUDuslitgtU%2bcT61Y16RUsvIe7Q%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1)

병렬화가 매우 중요하고만 A가 모든 일 전부 다 하고 B가 세 가지 일 전부 다 하고 C가 또 하고... 하다보면(이게 single-cycle) 너무 오래 걸리니까 병렬화를 해서 사진처럼 남이 하는 동안 세탁기가 비었다면 나도 시작하는 거임... 각각의 operation들을 중첩시켜서 존나 논스탑으로 하는 거임
그렇게 하면 시간이 약 number of stages가 된다능



### MIPS Pipeline

#### 5 Stages

MIPS는 5단계stage로 이루어져있다 암긔리기 

1. IF: Instruction fetch from memory
2. ID: Instruction decode & register read
3. EX: Execute operation or calculate address
4. MEM: Access memory operand
5. WB: Write result back to register



각 스테이지마다 걸리는 시간이 다르다

* register를 읽고 쓰는 데에는 100ps
* 나머지 수행은 200ps



#### 성능 향상하기

1. If all stages are balanced
   : pp한 instructions = (not pp한 instructions) / (number of stages)
2. 근데? balanced가 아니라면? 몇 개는 200ps이고 몇 개는 100ps라면?
   : 저만큼 빨라지지는 않고... 이 pp을 통한 성능 향상은 response time을 줄이는 게 아니라 throughput을 증가시켜서 높이는 거 ㅇㅇ response time은 오히려 늘어날 수도 있음



#### ISA

MIPS의 ISA랑 pp는 꽤나 잘 어울린다... 왜냐하면

1. 모든 명령어가 32bit라서 한 사이클에 맞추기가 아주 좋음
2. 명령어의 format도 작음 한 stage에 decode & read 가 가능
3. 3번째 스테이지에서 주소 계산해서 4단계에 그 메모리에 접근한다는 방식도 같음
4. memory access가 한 사이클 안에서 일어난다는 것도 같대 (200ps)
