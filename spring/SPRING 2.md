# SPRING 2

## 회원관리 예제: 백엔드 개발

> alt+insert: generate
>
> alt+enter: optional



### 시작

`domain`이라는 이름의 controller를 하나 만들고, 그 밑에 `Member`라는 class를 하나 만든다.

```java
package hello.projectname.domain;

public class Member {
    // 우리는 일단 id와 name만 수집할 것
    private Long id;
    private String name;

    // 각각의 getter & setter
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

```



이걸 저장할 곳을 만들 건데 db가 확정되지 않았다는 가정 하에 만들어보자.

`repository`라는 controller 밑에 `MemberRepository`라는 interface와 `MemoryMemberRepository`라는 class를 하나 만들자

```java
// MemberRepository

package hello.projectname.repository;

import hello.projectname.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    // optional로 감싸줘야 null 관련 오류 피하기 가능
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
```

```java
// MemoryMemberRepository

package hello.projectname.repository;

import hello.projectname.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository{
	// 까지 치면 빨간 줄이 그이면서 option이 생기는데 여기서 implement methods하면 다 가져온다
    
    private static Map<Long, Member> store = new HashMap<>();
    // sequence는 pk 만들어주는... 그런...
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence); // 만들 때 +=pk 해주기
        store.put(member.getId(), member); // 저장 ㄴㄱ
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // store.get(id) 값이 없을 수 있으니 Optional.ofNullable로 감싸준다
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
            	// member의 name이 여기 param으로 넘어온 name인지 filtering
                .filter(member -> member.getName().equals(name))
            	// 하나라도 찾았다면 바로 그걸 반환
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        // list로 반환
        return new ArrayList<>(store.values());
    }
}

```



### 테스트 케이스 만들기

근데 이게 동작을 할까? 그때 하는 게 테스트 케이스를 만들어보는 것이다.

`test/java/group.projectname`에 controller를 하나 만든다. 이때 테스트할 controller와 이름을 같게 해주는 게 통상적이다.

그리고 그 밑에 class 하나 만들면 된다. 이름은 test하고자 할 class 이름에 Test 붙이는 게 또 통상적.

```java
package hello.projectname.repository;

import hello.projectname.domain.Member;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

public class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    // 아래의 세 테스트들은 적힌 순서에 상관없이 실행되므로 데이터가 중복되거나 하면 오류가 난다.
    // 그래서 해주는 게 AfterEach 에서 clear를 해주는 것
    // clear는 지금 테스트하는 곳에서 적어줘야 함
    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        Member result = repository.findById(member.getId()).get();
        // System.out.println("result = " + (result == member));
        // result가 우리가 기대하는 member와 일치하는지?
        // Assertions.assertEquals(member, result);
        // 라고 해도 되고

        // 이걸 쓰려면 import static org.assertj.core.api.Assertions.*;를 가져와야 하는데
        // 왜 난... 자동으로 import가 안 되지?
        assertThat(member).isEqualTo(result);

        // Assertions.assertEquals(member, null); 처럼 다르게 하면 에러뜸
    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring1");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();

        assertThat(result).isEqualTo(member1); // good
        // assertThat(result).isEqualTo(member2); // error
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2); // good
    }
}

```

```java
// test하고자 하는 해당 repository

public class MemoryMemberRepository implements MemberRepository{

    // ...

    // 이게 AfterEach에 쓰이는 clear
    public void clearStore() {
        store.clear();
    }
}

```



### 회원가입

일단 또 컨트롤러를 만들자. 이번엔 음... `service`란 이름의 controller 안에 `MemberService`라는 class를 생성한다.

```java
package hello.projectname.service;

import hello.projectname.domain.Member;
import hello.projectname.repository.MemberRepository;
import hello.projectname.repository.MemoryMemberRepository;

import java.util.Optional;

public class MemberService {

    private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 회원가입
    public Long join(Member member) {
        // 중복 이름 안 되게 하기
        // ctrl+alt+v: optional로 반환

        // 1번 방법
        Optional<Member> result = memberRepository.findByName(member.getName());
        result.ifPresent(m -> {
            throw new IllegalStateException("이미 존재하는 회원입니다.")
        });

        memberRepository.save(member);
        return member.getId();
    }
}

```

```java
public class MemberService {

    private final MemberRepository memberRepository = new MemoryMemberRepository();

    public Long join(Member member) {

        // 2번 방법: 바로 하기
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.")
                });

        memberRepository.save(member);
        return member.getId();
    }
}

```

```java
public class MemberService {

    private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 회원가입
    public Long join(Member member) {
        // 3번 방법: method로 extract해서 넣어버리기
        // 만들어둔 걸 method로 바꾸는 법: 해당 코드들 블럭 -> ctrl+alt+m
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.")
                });
    }
}

```



### 조회

```java
public class MemberService {

	// ...
    
    // 전체 회원 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }
    
    // 해당 사람 조회
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}

```

