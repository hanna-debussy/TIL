# 01 display: flex;

양심선언 웹퍼플리싱 배웠지만 이건 몰랐다!



https://flexboxfroggy.com/#ko 의 도움을 많이 받았다



## Overview

`display: flex;`는 주축과 크로스축이 전부다. 약간 선형대수 벡터 공간과 비슷한 느낌? 두 직선의 시작점(start)과 어디로 뻗어나가는지(end)를 따지면 된다.



***

여기서부터는 감싸고 있는 `<div>`에 적용하는 전체 속성



## justify-content

`justify-content: ___;`는 가로선에서의 이동을 맡는다.



`flex-start`: 보통의 한글 나열하듯 왼 -> 오 (default)

`flex-end`: 보통의 아랍어 나열하듯 오 -> 왼

`center`: 가운데 정렬

`space-between`: 요소들 '사이'에 동일한 간격

`space-around`: 요소들 '주위'에 동일한 간격 (마치 margin을 동일하게 주는 느낌)





## align-items

`align-items: ____;`는 교차축에서의 정렬을 맡는다.



*주축이 가로라는 전제 하

`flex-start`: 위 -> 아래 (default)

`flex-end`: 아래 -> 위

`center`: 가운데 정렬

`baseline`: start -> end

`stretch`: div에 맞게 늘린다





## flex-direction

`flex-direction: ___;`는 주축의 start와 end 방향을 설정한다.



\* 화면에 보이는 기준

`row`: start -> end

`row-reverse`: end <- start

`column`: start ↓ end

`column-reverse`: start ↑ end



## flex-wrap

flex 개념은 default로  `<div>` 안의 모든 요소를 한 줄에 넣는다. 그걸 여러 줄로 나눌 때 쓴다고 생각하면 된다.



`nowrap`: 모든 요소들을 한 줄에 정렬, 요소 가로가 좁아진다. (default)

`wrap`: 요소들의 가로를 다 살리고 가로가 다 차면 줄바꿈

`wrap-reverse`: wrap에 반대 정렬을 곁들인





## flex-flow

`flex-direction`과 `flex-wrap`이 동시에 쓰일 때가 많아서 이마저도 같이 쓰게 만들었다. 인자는 두 속성과 공유하며 `flex-direction ` - `flex-wrap` 순으로 쓰면 된다.

ex) `flex-flow: column wrap;`





## align-content

여러 '줄'이 있을 때 설정한다. 줄들을 어디서(위? 아래?) 어떤 간격으로 놓을지 결정

`flex-start`: '줄'을 위 -> 아래

`flex-end`: '줄'을 아래 -> 위

`center`: 상하 가운데 정렬

`space-between`: 여러 줄 '사이'에 동일한 간격

`space-around`: 여러 줄 '주위'에 동일한 간격

`stretch`: 여러 줄들을 컨테이너에 맞게 늘리기







***

여기서부터는 개별 요소에 넣는 속성



## order

`order: ___;` 는 나열된 컨테이너들의 순서를 바꾸는 것
양수나 음수를 넣어서 움직인다.



## align-self

`align-self: ___;`는 `align-items`를 개별 속성으로 쓰는 거다. 걔만 똑 움직일 수 있음. `align-items`와 인자를 공유한다.

