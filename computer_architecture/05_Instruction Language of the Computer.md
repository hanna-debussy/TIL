# 02. Instruction: Language of the Computer

## A C Sort Example to Put It All Together

### C Sort Example

#### leaf

```c
void swap(int v[], int k)
{
    int temp;
    temp = v[k];
    v[k+1] = temp;
}
```

음 두 개 자리 바꾸는 거구나 이런 C 코드가 있다고 치면 v 는 $a0에, k는 $a1에, temp는 $t0에 매핑되어있다고 가정할 거임 
이걸 어셈블리어로 바꾸면

`sll $t1, $a1, 2` 아 v의 idx가 k 구나 근데 array 칸 하나가 4바이트니까 k*4만큼 t1에 저장

`add $t1, $a0, $t1` v[k]의 시작주소를 t1에 저장하는 거

`lw $t0, 0($t1)` v[k]를 t0에,

`lw $t2, 4($t1)` v[k+1]을 t2에 넣고

`lw $t2, 0($t1)` t2에 있는 v[k+1]을 0번에 넣고

`lw $t0, 4($t1)` t0에 있는 v[k]를 4(1)번에 넣구

`jr $ra`



#### non-leaf

...? 개복잡한데? 에바킹스텀 이제 보니 C언어가 선녀 같네 뭐... 이거까지는 할 필요가



### Effect of Compiler Optimization

최적화 none, o1(medium), o2(full), o3(proc mig) 이케 비교하면...

* performance와 instruction count, performance와 clock cycle은 대충 반비례 관계
* ic는 o3가 더 높지만 퍼포먼스가 o3가 더 좋은 건 cpi가 o1보다 o3가 적어서 그렇다



## Arrays versus Pointers

array로 프로그래밍할 수도 있고 pointer로 할 수도 있다

* 전자는 index를 사용해야 하니까 idx*element size 해주고 base address에 더해줘야 하는 일을 해야 해서
* 후자는 indexing해야 하는 복잡함을 피할 수 있음



어셈블리어로 보면

* 전자는 항상 idx에 4 곱하고 base에 더해주는 걸 항상 해줘야 하는데
* 후자는 바로 사이즈를 더한 끝 idx를 바로 구하는 것 같은데? 그래서 loop 안에 idx 곱하고 더하고 하는 게 없음



ㅋㅋㅋ근데 최신 컴파일러들은 array로 해도 전문적인 프로그래머가 포인터를 사용해서 프로그램을 작성한 것만큼 성능을 보여주고 있음 한마디로 크게 상관없어졌다는 말
왜냐면 array를 사용하면 프로그램이 더 오류 나기 적고 이해하기 쉽거든... pointer는 버그 많고 어렵대;



## Real Stuff: ARM Instructions

* 오 임베디드 시스템에서 가장 보편적으로 사용되고 있음 
* ARM과 MIPS는 유사하다 
* conditional execution이 ARMS의 가장 큰 특징(MIPS는 없음)인데 뭐냐면
  * 어떤 연산을 한 후에 그 결과가 음수냐 0이냐 overflow냐 등등의 조건에 따라 뒤에 나오는 명령들을 실행시키거나 안 시키거나 할 수 있음
    한 마디로 그냥 결과가 조건이 되어서 그거에 따른 명령들을 나눠서 실행 가능하다는 거네
  * 각 명령어들이 이걸 지원함 상위 4비트에 conditional value가 들어있어서 사용 가능
  * 이렇게 하는 이유는 branch 명령어 안 쓰고도 그 효과를 낼 수 있게 해서 명령어 수를 줄이기 위함



## Real Stuff: x86 Instructions

### 인텔

* ...과 MIPS의 가장 큰 차이점은 MIPS는 모든 register들이 32비트인 반면 인텔은 몇몇은 16비트라는 것

* 일반적인 명령어에서 메모리 어드레싱이 가능함 아 그니까 operand가 register + memory / memory + register / memory + immediate 이렇게도 가능하다는 것 (MIPS는 register register / register immediate까지만 가능했음)

* 명령어 길이도 난리났네 variable length encoding... 복잡하다

* 그래서 인텔 프로세서는 구현하기 아주 어렵다: Complex Instruction Set Computer (CISC)시스크...구나
  -> 그러면 고성능을 만들기 어려움

* 그래서 microoperation, microengine을 쓰기로 했다
  : 솦트웨어가 복잡하니까 하드웨어가 명령어를 내부적으로 간단한 여러 개의 명령어로 쪼갬 와우 이게 microoperation이고 이걸 microengine이 실행하는 것 아 하드웨어가 RISC(register 웅앵)처럼 하게 했다는 거네 그래서 RISC와 비슷한 성능을 갖게 했다

* 시장 점유율market share로 들이박았다고? 이게 뭐임

> 아 근데 요즘은 RISC 계열로 바꾸자는 움직임도 있다 걍 translation 필요 없이 할 수 있어서 더 효율적이니까



## Fallacies and Pitfalls

### Fallacies

#### Powerful instruction

여러 개의 일을 한꺼번에 할 수 있는 명령어를 뜻한다. 이걸 쓴다면? high performance가 되지 않을까?
-> 실제로 그렇게 될 확률은 적다! 명령어 수는 줄겠지만 복잡한 명령은 구현하기 어렵고 로직 수가 많아져서 clock이 느려지게 된다... 아하 모든 명령어가 그 클락에 맞춰 다같이 느려지게 됨 간단한 것들마저도
그렇다면? 간단한 명령어 여러 개 조합해서 어려운 거 하는 게 훨 낫다! < 가 RISC의 철학



#### Use assembly code for high performance

어셈블리어를 사용하면 고성능 구현 가능함 근데?? 최신 컴파일러들은 이 어셈블리 코드 수준으로 최적화가 가능해져서 이제는 머 딱히... 어셈블리 코드보다 C코드 등의 하이레벨 랭귀지 사용하라 이 말이야
또 어셈블리 코드는 라인이 훨씬 길어서 오류가 많아짐 생산성이 낮아짐



## Concluding Remarks

### Addressing Mode

1. register addressing
2. base addressing은 load store 관련
3. immediate addressing은 i type
4. PC-relative addressing은 branch 관련
5. Pseudo-direct addressing은 jump



### design principles

1. simplicity favors regularity
2. smaller is faster
3. make the common case fast
4. good design demands good compromises



### hmm...

common case가 어떤 프로그램을 실행시키느냐에 따라 달라지기 때문에 compromise가 중요하다

