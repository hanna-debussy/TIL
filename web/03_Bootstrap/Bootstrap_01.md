# Bootstrap_01



## Grid

### 1. Container

grid를 설정할 때에는 가장 최상위 div에 `.container`를 넣어야 한다.



### 2. row / column

`div.container>div.row>(div.col)*n`

***

row는 그냥 row로 끝나는데 col은 옵션이 아주 많다.
보통 `.col-(gridTier)-(columnWidth)`의 형태로 설정한다



#### 1) col

그냥 `.col`, `.col-6` 등으로 지정하면 width 상관없이 지정을 하겠다는 뜻
특히 `.col` = `.col-12`: 당연하지만 div는 block이므로 모든 폭을 다 가져간다



#### 2) grid tier

window-width에 따라

`.col-`: < 576px

`.col-sm-`: >= 576px

`.col-md-`: >= 768px

`.col-lg-`: >= 992px

`.col-xl-`: >= 1200px

`.col-xxl-`: >= 1400px



#### 3) column width

1~12까지의 숫자가 들어갈 수 있으며, 하나의 row 안에 들어가있는 모든 col width의 합이 12여야 한다.
12의 약수가 많아 다양하고 깔끔하게 쪼갤 수 있어서 12가 되었대

```html
<div class="container">
    <!-- 한 row 안에 -->
    <div class="row">
        <div class="col-2">
            col-2
        </div>
        <div class="col-8">
            col-8
        </div>
        <div class="col-2">
            col-2
        </div>
        <!-- 2+8+2 = 12 이렇게 계산 -->
    </div>
</div>
```

