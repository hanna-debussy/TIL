# REACT 1

## 시작하기

### 설치하기

일단 yarn이 필요하다. 깔아주시고



```bash
$ npx install -g create-react-app pjt-name
```

> npx가 없다면 npm으로 하면 된다
>
> ...but!
> -g로 설정해서 global에 저장하게 되면 컴퓨터에 라이브러리가 남게 된다. 무거운 것들을 컴퓨터에 남겨서 용량을 절약하는 대신 버전이 업데이트 되면 걔를 재설치해야 한다. 이런 문제점을 해결할 수 있는 게 npx이기 때문에 npx가 더 좋다.
>
> ```bash
> npm install npx -g pjt-name
> ```
>
> 를 통해 npx 설치 가능



이제 실행해보자.

```bash
$ npm start
```

...이때 `'react-scripts'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.` 라고 뜰 수 있는데, 그럴 땐 `react-scripts`를 설치하면 된다.

```bash
$ npm install -g react-scripts
$ yarn add react-scripts
$ npm start
```

이렇게 나타나는 이유는 원래 yarn에는 start라는 명령어가 없다. 그래서 `package.json` 파일에 scripts를 보면 start라는 명령어로 재명명해둔 원래 명령어가 적혀있는데, 이 scripts를 이용하기 위해서 react-scripts를 설치해야 하는 것이다.



### 시작하기

불필요한 건 지우자. src에는

```
src
├── App.js
└── index.js
```

만 남아야 하고, index.js에는 `ReactDOM.render(<App />, document.getElementById('root'));` 밑을 지우면 된다. 

App.js에는 `import React from 'react';`만 남기고,  `<div className="App">` 안의 모든 내용을 전부 지운다.

























