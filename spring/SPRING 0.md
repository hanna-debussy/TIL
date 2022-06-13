# SPRING 0

## 프로젝트 생성하기

1. https://start.spring.io 에 들어가기

2. Project: Gradle Project

   Spring Boot: SNAPSHOT이나 M1이 아닌 것 선택

   Language: Java

   Packaging: Jar

   Java: 자기 java ver.

3. Project Metadata

   Group: group id 느낌

   Artifact: project name 느낌... build된 결과물 이름

4. Dependencies: 어떤 라이브러리를 쓸 것인가?

   Spring Web, Thymeleaf 추가

5. GENERATE

6. 압축을 푼다

7. IntelliJ에서 다운 받은 폴더의 build.gradle을 오쁜

8. 처음엔 외부에서 다운로드를 하기 때문에 조금 시간이 걸린다

9. 쨘



## 실행하기

`src/main/java` 들어가면 `Group/Artifact` 안에 어쩌구Application이라고 뜬다. 거길 보면 이미 `public static void main...` java에서의 실행 함수가 있는데, 거기 왼쪽에 초록색 실행 버튼을 누르면 무언가 또 설치를 시작한다. 그 중 보면 `Tomcat started on port(s): 8080 (http) with context path ''`라고 나오는데, `http://localhost:8080/` 들어가서 error 어쩌구 페이지 뜨면 프로젝트를 실행할 준비가 되었다는 뜻이다.



참고로 File > settings 들어가서 gradle 치면 무언가 Gradle로 설정된 거 두 개가 있는데, 그거 전부 IntelliJ IDEA로 바꿔주자. 실행이 더 빨라진다.



## view 환경설정

아까 8080 페이지에서 error 났던 그곳을 꾸며보자.

1. `src/main/resources/static`에다가 `index.html`을 생성한다.
2. 말 그대로 html... 근데 spring은 welcome page를 제공하긴 하지만 그건 정적 페이지인 거고 우리가 땡겨온 thymeleaf가 바로 템플릿 엔진이기 때문에 그걸 쓸 거다.



### Thymeleaf

공식 문서: https://www.thymeleaf.org/



## build하고 실행하기

```bash
cd project-name
./gradlew build
cd build/libs
java -jar project-name-0.0.1-SNAPSHOT.jar
```

저 `project-name-0.0.1-SNAPSHOT.jar`는 `./gradlew build`하면서 생기는 build/libs에 들어가면 있는 거... 약간 python manage run server랑 비슷하군



만약 버벅인다면

```bash
./gradlew clean build
```

하면 build 폴더가 사라지니까 다시 깔면 됩니다



