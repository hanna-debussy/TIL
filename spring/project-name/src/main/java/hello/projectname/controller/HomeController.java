package hello.projectname.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
    // index.html이 있어도 여기 먼저 뒤지기 때문에 home.html로 간다
    // static보다 이 컨트롤러 뒤지는 게 먼저다
}
