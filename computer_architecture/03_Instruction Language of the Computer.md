# 02. Instruction: Language of the Computer

## Introduction

### Instruction Set

* 명령어의 집합
* 프로세서마다 서로 다른 Instruction Set를 가지고 있다 - 하지만 많은 부분이 비슷함 
* 예전엔 Simple Instruction Set, 요즘은 Reduced Instruction Set Computer (RISC)



### Instruction Set Architecture

* SW와 HW의 interface...
* OS: system SW interface라고 볼 수 있다. 모든 것들이 IS를 통해 구현되니까
* ABI(Application Binary Interface)
  * ISA와 system SW interface의 combination
  * 어플이 실행이 될지 안 될지(portability) 체크해야 할 게 ABI
  * 아하 인텔의 instruction set... MS, Mac 약간 이런 개념이구나
  * 그 프로그램이 다른 컴퓨터에서 돌아갈 수 있는지 아닌지는 ABI가 동일해야 한다 아하



### MIPS

* Million Instruction Per Second
* 1초에 백만 개 이상의 명령어를 실행시킬 수 있다구
* 임베디드에서 많이 쓰임 (ARM)
* Typical of many modern ISAs 오...



## Operations of the Computer Hardware

### Arithmetic Operations

* add a, b, c == a가 destination 이고 a에 b+c가 저장
  : 요런 form으로 돌아간다

* >  Design Principle 1: Simplicity flavours 'regularity' 정규화

* 오

* f = (g + h) - (i + j) 라는 코드가 있다면
  compiled MIPS code는 괄호 안의 add 두 번과 sub(stract) 하는 세 번의 연산을 거치게 된다
  이게 바로 리얼 컴퓨터가 돌리는 과정

* 저 심플 코드에서 MIPS code로 바꿔주는 게? Compiler!



## Operands of the Computer Hardware

### Register Operands

* Arithmetic instructions은 대표적인 Register 간의 연산

  * RISC 계열 프로세서에서 지원하는 방식
  * MIPS가 대표적인 RISC 계열 프로세서라서 MIPS가 Aris웅앵을 register 연산으로 한다

* MIPS는 32*32 bit register를 사용한다

  * 자주 사용하는 data를 이용하기 위해 사용

  * 0~31이 되고
  * 이 32-bit data를 보통 word(4 bytes)라고 부른다



### Assembler

* * $t0~$t9 이 10개가 Temporary values를 사용하고
  * s0~$s7 까지의 8개가 Saved variables를 사용한다

* > Design Principle 2: Smaller is faster

* 아하

* f = (g + h) - (i + j) 를 다시 가져오면

  * f, g, h, i, j는 saved variables
  * g+h, i+j 는 temporary 안에 들어간다



### Byte Addresses

* byte가 기본 단위잔아
* MIPS는 32bit로 이루어져 있는데
* Alignment restriction: 메모리가 word 단위로 access 하게 되는데 어떤 데이터나 명령어로 word 단위로 access로 align을 하게 된다. 모든 명령어가 32bit으로 align된다는 말임
  * Big Endian: 오름차순으로 저장
    ex) IBM 360/370, MIPS, HP PA
  * Little Endian: 내림차순으로 저장
    ex) Intel 80x86, DEC Vax
  * endian이 뭐냐면 32bit가 있으면 어떻게 저장하냐는 거임



### Memory Operands

* Main memory ⊃ arrays, structures, dynamic data
* Arithmetic operation을 적용하기 위해서는
  * Load/Store Architecture: 메모리를 레지스터에 올리고 연산 다 하고 결과를 레지스터에서 메모리에 저장하게 되거든 근데 이 architecture는 메모리에 접근하는 명령어가 딱 지정되어 있어 Load(memory&rarr;register)에 쓰이는 명령어 Store(register&rarr;memory)에 쓰이는 명령어가 정해져 있음 그래서 arithmetic operation이 메모리에 바로 접근할 수가 없음
* 메모리는 기본 단위가 byte다
* 메모리는 word(4byte)로 align되어있다
* MIPS는 말했다시피 Big Endian
* example 1
  * g = h + A[8]이 있다고 하자. 여기서 A는 int array이다.
  * g, h는 $s1, $s2에 들어가고 base address(A[0]의 주소)도 $s3에 들어간다
  * 그러고 나서 lw라는 개념이 나오는데 load word라고... 뭐라 해야 하지? 일단 설명을 하면
    : $s3에 base address에서 여덟 번째 후라는 거잖아 그러면 1~8까지 가기 위해서 8*4byte(왜냐면 하나하나가 word 단위로 align되어 있으니까)번 가야 함 그래서 $s3에 32를 더한 게 $t0에 들어가게 된다 이 '$s3 + 32'를 offset이라 부름
    결론적으로 lw = base address + offset
  * 그러고 뭐... $s1에 $t0 + offset 넣으면 끝

* example 2
  * A[12] = h + A[8]
  * h를 $s2, A의 base address를 $s3에 놓고 lw랑 h + offset 까지 하는 건 같다
  * 그러고 나서 A[12]에 저걸 store를 또 해야 함: 이게 sw(store word)
    A[12]에 접근하기 위해서 4*12 = 48을 $s3에 더해야 하는 거임 그 메모리 주소에다가 $t0을 넣으면 됨 이게 sw



### Registers vs. Memory

* register가 memory 접근보다 훨씬 빠름
  : memory data를 작업하기 위해선 load랑 store를 해야하는 작업이 추가되기 때문 명령어도 늘어나고
* 그러므로 register를 최대한 활용하는 게 낫다! 이게 main issue
* 그렇다고 memory를 안 쓰는 건 불가능하지 근데 대신 less frequently used variables에 쓰긔



### MIPS Register File

* 그... register는 32bit가 32개 있음 2*2배열에서 N = 32의 형태를 떠올리면 된다
  * 여기에 register는 2개의 read port(5bit... 왜 5개?) 그니까 연산할 두 개
  * 그리고 그 답을 적을 write port 이렇게 세 개가 필요
* 이걸 머릿속에 떠올려보자면
  * read port 두 개가 하나의 연산으로 어떤 답을 내서 그게 destination address에 들어간다
  * 그것들이 모여서 write data가 되는 거임
  * 근데 모든 것이 32*32 배열의 write control 안에서 이루어진다는 것



### Therefore...

* 레지스터는
  * memory보다 빠른 건 맞는데 register를 키우면 느려질 수 있다는 문제점 존재
  * 연산할 때 레지스터 쓰는 게 더 효과적
  * 가능하면 레지스터에 많은 변수값을 가지고 있는 게 성능 향상에 도움이 된다



### Immediate Operands

* addi $s3, $s3, 4 처럼 바로 상수(4)에 접근할 수 있을 때

  * 근데 substract를 지원하지 않아서 4 빼려면 -4를 더하면 됨

* > Design Principle 3: Make the common case fast
  >
  > : 사용할 수 있으면 immediate operands 써라



### The Constant Zero

* $zero 아하
* saved를 temp에 잠시 copy하고 싶을 때 연산자 없이 박을 수는 없어서 0을 더해주는 식으로 넣는 것
* ex) $t2, $s1, $zero