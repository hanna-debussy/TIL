package hello.projectname.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @GetMapping("hello") // 주소에 넣을 이름... 예를 들면 8080/hello 를 쳐야 들어간다
    public String hello(Model model) {
        model.addAttribute("data", "controller에서 정한 hello!");
        return "hello"; // hello.html로 넘겨주삼
    }

    @GetMapping("hello-mvc")
    // request param이니까 param이 있어야 한다 여기서는 8080/hello-mvc?name=넣고픈param 해야 나옴
    // param이 없어도 되게 하고 싶으면 @RequestParam("name", required=false) 해주면 됨
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }

    // 바로 데이터 내리기
    @GetMapping("hello-string")
    @ResponseBody // http에서 header와 body 중 body부에 이 데이터를 직접 넣어주겠다는 뜻
    public String helloSTring(@RequestParam("name") String name) {
        // 이거 그대로 내려감... source 보기 하면 html 어쩌구 나오는 거 아니고 hello 어쩌구 만 나옴
        return "hello " + name;
    }

    // json 형식으로 뽑기
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
