package hello.projectname.controller;

import hello.projectname.domain.Member;
import hello.projectname.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
// spring bean이 관리된다?
public class MemberController {
    // 여러 개 생성할 필요가 없으니까 new MemberService()를 할 필요 x
    private final MemberService memberService;

    @Autowired // spring container에서 관리되고 있는 걸 넣어주는(연결해주는)
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }


    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/"; // home으로 redirect
    }
}
