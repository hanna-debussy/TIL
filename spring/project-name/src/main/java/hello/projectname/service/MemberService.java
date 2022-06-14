package hello.projectname.service;

import hello.projectname.domain.Member;
import hello.projectname.repository.MemberRepository;
import hello.projectname.repository.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {

    // 이렇게 repository를 만들어줘도 되지만
    // private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 외부에서 만들어진 repository를 넣겠다 이말이야: Dependency Injection (DI)
    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    // 회원가입
    public Long join(Member member) {
        // 중복 이름 안 되게 하기
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    // 전체 회원 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    // 해당 사람 조회
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
