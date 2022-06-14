package hello.projectname.service;

import hello.projectname.domain.Member;
import hello.projectname.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

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

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}