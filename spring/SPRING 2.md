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

근데 이 틀을 더 쉽게 만드는 방법이 있다. 그건 좀 더 밑에.



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



### 다시 테스트케이스

이번엔 그 클래스 이름(혹은 내부)에 커서를 두고 alt+enter를 하면 거기에 create test라고 있을 것이다. 그걸 하면 위에 했던 동작 그대로 한다. test 안에 package 만들어지고, 그 안에 ~Test 라는 이름으로 class가 생성된다. 안에 틀도 다 짜여져서 만들어진다. 그래서 우리는 그 안을 채워넣기만 하면 된다.

```java
// 이게 최초 틀... 다 줄게

package hello.projectname.service;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {

    @Test
    void join() {
    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}
```



#### 회원가입 테케 + Dependency Injection (DI)

```java
class MemberServiceTest {

    MemberService memberService;

    // for DB clearing
    // MemoryMemberRepository memberRepository = new MemoryMemberRepository();
    MemoryMemberRepository memberRepository;
    // 처럼 새로 또 생성을 해줘도 되지만 하나의 repository에 다 넣기 위해서 아래처럼 해준다

    @BeforeEach
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository(); // 생성해주고
        memberService = new MemberService(memberRepository); // 그걸 이용하게
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }


    @Test
    void 회원가입이라고한국어로적어도된다test는실제빌드되는코드가아니라서() {
        // given 이러한 게 주어졌을 때
        Member member = new Member();
        member.setName("Hello");

        // when 이 상황에는
        Long savedId = memberService.join(member);

        // then 이렇게 되어야 해
        Member findMember = memberService.findOne(savedId).get();
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복회원예외() {
        // given
        Member mem1 = new Member();
        mem1.setName("spring");

        Member mem2 = new Member();
        mem2.setName("spring");

        //when
        memberService.join(mem1);
        //try-catch도 좋지만
        assertThrows(IllegalStateException.class, () -> memberService.join(mem2));
        // assertThrows(예외종류, () -> 내가 실행시킬 것) 아 람다함수네
        // 그래서 실제 join에서 지정한 예외(illegalstate)가 터진 게 맞는지 확인

        //then
    }

}
```

```java
// 테케 돌리는 원 class에도 DI 관련 처리

public class MemberService {
    // 이렇게 repository를 만들기보다
    // private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 외부에서 만들어진 repository를 넣겠다 이말이야
    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
    
}
```



### Spring Bean

spring bean을 등록하는 두 가지 방법

1. Annotation 사용: 컴포넌트 스캔과 자동 의존관계 설정 (ex.`@Controller` `@Service` `@Repository` `@Autowired`...)

   ```java
   // example
   
   // MemoryMemberRepository
   @Repository // repository라고 spring container에 알려주고 등록
   public class MemoryMemberRepository implements MemberRepository{
   }
   
   // HelloController
   @Controller
   public class HelloController {
   }
   
   // MemberService
   @Service
   public class MemberService {
   }
   
   
   // 공유된 걸 부를 때
   @Controller
   public class MemberController {
       // 여러 개 생성할 필요가 없으니까 new MemberService()로 할 필요 x
       private final MemberService memberService;
   
       @Autowired // spring container에서 관리되고 있는 걸 넣어주는(연결해주는)
       public MemberController(MemberService memberService) {
           this.memberService = memberService;
       }
   }
   
   ```

   

2. 자바 코드로 직접 스프링 빈 등록

   ```java
   // src/main/java/group.projectname 에 SpringConfig class 생성
   
   package hello.projectname;
   
   import hello.projectname.repository.MemberRepository;
   import hello.projectname.repository.MemoryMemberRepository;
   import hello.projectname.service.MemberService;
   import org.springframework.context.annotation.Bean;
   import org.springframework.context.annotation.Configuration;
   
   @Configuration // 1 내가 직접 지정해보겠다 이말이야
   public class SpringConfig {
       @Bean // 3 그걸 쓰는 MemberService 있고 이거 두개를 직접 bean에 넣어준 거
       public MemberService memberService() {
           return new MemberService(memberRepository());
       }
       
       @Bean // 2 얘가 일차적으로 있고
       public MemberRepository memberRepository() {
           return new MemoryMemberRepository();
       }
   
       // 근데 Controller는 Autowired로 해야 함...
   }
   
   ```

   

spring bean을 감지하는 범위는 `src/main/java/group.projectname/`안에 있는 애들만 스캔



> 스프링 빈을 등록할 때, 기본적으로 싱글톤으로 등록한다(=유일하게 하나만 등록해서 전부 그걸 공유한다).
