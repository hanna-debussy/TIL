package hello.projectname;

import hello.projectname.repository.MemberRepository;
import hello.projectname.repository.MemoryMemberRepository;
import hello.projectname.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {
    @Bean // 2 그걸 쓰는 MemberService 있고 이거 두개를 직접 bean에 넣어준 거
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean // 1 얘가 일차적으로 있고
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    // 근데 Controller는 Autowired로 해야 함...
}
