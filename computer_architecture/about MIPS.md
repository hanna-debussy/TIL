# MIPS 명령어들

https://programming119.tistory.com/41

직관적인 거 빼고

`addi $s1 $s2 10` add immediate: 상수를 더할 때 주로 쓴다

`sll $s1, $s2, 10` shift left logical: $s1 = $s2 << 10 s1은 s2를 10만큼 왼쪽으로 비트 이동한 것이다

`srl $s1, $s2, 10` shift right logical: $s1 = $s2 >> 10 s1은 s2를 10만큼 오른쪽으로 비트 이동한 것이다



`beq $s1, $s2, 25` branch on equal: s1=s2 면 25로 이동

`bne $s1, $s2, 25` branch on not equal: s1!=s2 면 25로 이동

`slt $s1, $s2, $s3` set on less than: s1<s2 라면 1 아니면 0



  
