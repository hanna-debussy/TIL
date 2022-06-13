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

        assertThat(result.size()).isEqualTo(2);
    }
}
