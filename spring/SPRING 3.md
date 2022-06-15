# SPRING 3

## 웹 MVC 개발

### 홈 화면 추가

```java
// src/main/java/group.projectname/controller에 HomeController 생성

package hello.projectname.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
    // static에 index.html이 있어도 여기 먼저 뒤지기 때문에 home.html로 간다
    // static보다 이 컨트롤러 뒤지는 게 먼저다
}

```



### 회원 등록

