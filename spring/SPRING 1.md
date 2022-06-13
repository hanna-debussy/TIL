# SPRING 1

## 정적 페이지와 동적 페이지

정적 페이지는 쉽다. 그냥 적어서 화면에 보여주면 된다.

하지만 동적 페이지는 controller에서부터 시작된다.



`src/main/java/group.projectname/controller`에 java class 생성

```java
package hello.projectname.controller;
// 아래의 것들은 우리가 자동완성 시킬 때마다 자동으로 적힘
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {

    @GetMapping("hello-mvc") // 주소에 넣을 이름... 예를 들면 8080/hello 를 쳐야 들어간다
    // request param이니까 param이 있어야 한다 여기서는 8080/hello-mvc?name=넣고픈param 해야 나옴
    // param이 없어도 되게 하고 싶으면 @RequestParam("name", required=false) 해주면 됨
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }
}

```

해놓고 `src/resources/templates`에 `return`뒤에 적은 이름의 html을 만들자(보통 정적 페이지는 `src/resources/static`에 html을 만든다). 

```java
<!doctype html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<p th:text="'hello ' + ${name}">hello! empty</p>
<!--서버로 타고 들어갈 때 th가 나오는 거-->
<!--attribute 이름을 name으로 했기 때문에 name-->
</body>
</html>
```



```java
@Controller
public class HelloController {

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

```

이러고 결과 보면

1. `http://localhost:8080/hello-string?name=idkyet`

   ```
   hello idkyet
   ```

   소스를 확인해도 html어쩌구... 가 아니라 이거만 날아온다

2. `http://localhost:8080/hello-api?name=tada`

   ```ㅗ싀
   {"name":"tada"}
   ```

   json 형식!