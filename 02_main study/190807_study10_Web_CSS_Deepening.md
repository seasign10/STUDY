### :page_facing_up:CSS (cascading)

#### :pushpin:position

1. **static**

2. relative -top, bottom, left, right => **부모를 찾지 않음** (=> absolute와의 차이점) 본인의 위치에서 이동
3. **absolute** : **부모 요소나 가장 가까운 조상요소(static 제외) 를 기준**으로 top, bottom, left, right만큼 이동 static이면 body가 최종 요소
4. **fixed** : 브라우저의 viewport를 기준으로 t, b, l, r 스크롤 되어도 화면에서 사라지지 않고 같은 위치 (고정)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="09_positon.css">
</head>
<body>
  <h2>1. static</h2>
  <div>static</div>
  <div>static</div>
  <!-- div는 inline이 아닌 block 속성이므로 떨어진다? -->

  <!-- 
1. absolte
  absolute 는 부모 or 조상 요소를 기준으로 위치하는데,
  static 이 아닌 부모 or 조상 요소를 기준으로 찾아 올라간다.
  absolute-1 박스는 부모가 static 이어서 최종적으로
  body 를 기준으로 위치하게 된다.
   -->

   <h2>2. absolute-1 (모든 부모가 static)</h2>
   <div class="parent">
     static
     <div class="absolute">absolute-1</div>
   </div>
 
   <h2>3. absolute-2 (조상 중에 static이 아닌 가장 가까운 부모가 있을때)</h2>
   <div class="parent relative">
     relative
     <div class="absolute">absolute-2</div>
   </div>
 
   <h2>4. absolute-3 (해당 부모나 조상이 움직이면 따라움직인다)</h2>
   <div class="parent relative-move">
     absolute-3
     <div class="relative-move">absolute-3</div>
   </div>
 
   <!-- 
     2. relative
     자기가 원래 있어야할 위치 (static)
     - 주의사항
     - relative 이동하면 과거 static 이었던 공간도 차지한 상태로 이동
    -->
   <h2>5. relative - 자기가 있어야할 위치를 기준으로 이동</h2>
   <div class="relative-move">relative</div>
 
   <!-- 3. fixed -->
   <div class="fixed">
     <h2>6. fixed - 브라우저 위치에 따라 고정</h2>
   </div>
 
   <!-- 4. z-index -->
   <h2>7. z-index - 큰 숫자 값을 지정할수록 화면 전면에 출력</h2>
   <div class="relative">
     <div class="z-index-1"></div>
     <div class="z-index-2"></div>
     <div class="z-index-3"></div>
   </div>
</body>
</html>
```

```css
div {
  width: 100px;
  height: 100px;
  background-color: red;
  color: white;
  text-align: center;
  line-height: 100px      
  
/* 수직 가운데 정렬: line height를 부모의 height와 동일하게 적용 */
}

.parent {
  background-color: burlywood;
}

.absolute {
  position: absolute;
  top: 50px;
  left: 50px;
}
/* 모든부모가 static 이어서 body를 기준으로 위치를 이동함 (집 나간 자식) */

.relative {
  position: relative;
}

.relative-move {
  position: relative;
  top: 30px;
  left: 30px;
}

.fixed {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
}

.z-index-1 {
  position: absolute;
  background-color: green;
  z-index: 100;
}

.z-index-2 {
  position: absolute;
  background-color: grey;
  top: 30px;
  left: 30px;
  z-index: 99;
}

.z-index-3 {
  position: absolute;
  background-color: yellow;
  top: 60px;
  left: 60px;
}
```



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="10_float.css">
</head>
<body>
<!-- 
  float
  해당 요소를 다음 요소 위에 떠 있게(부유) 한다. 
  여기서 떠 있다 라는 의미는, 요소가 기본 layout 흐름에서 벗어나
  요소의 모서리가 왼쪽이나 오른쪽으로 이동하는 것을 말한다.
  - 주의사항
  - float 를 사용할 때는 요소의 위치를 고정시키는 position: absolute 를 사용하면 안된다.
 -->

  <div>div</div>
  <div class="float-left">float-left</div>
  <div class="back">back</div>

  <div class="float-left">1</div>
  <div class="float-left">2</div>
  <div class="float-right">3</div>
  <div class="float-right">4</div>
  <div class="back clear">back</div>
  <!-- back 은 flat-left 아래에 있어서 안보임 -->

</body>
</html>
```

```css
div {
  width: 100px;
  height: 100px;
  background-color: crimson;
  color: white;
  text-align: center;
  line-height: 100px;
}

.float-left {
  float: left
}

.back {
  background-color: orange;
  width: 300px;
}

.float-right {
  float: right
}

/* float 값을 무시하고 진행: clear */
.clear {
  clear: both;
}
```



```html
<!-- box.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
  <link rel="stylesheet" href="box.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green">
      <div class="small-box" id="purple"></div>
    </div>
    <div class="small-box" id="blue">
      <div class="small-box" id="orange"></div>
    </div>
    <div class="small-box" id="pink"></div>
  </div>
</body>
</html>
```

```css
/* box.css */

.big-box {
  position: relative;
  margin: 100px auto 500px;
  border: 5px solid black;
  width: 500px;
  height: 500px;
}

.small-box {
  width: 100px;
  height: 100px;
}

#red {
  background-color: red;
  
  /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
  position: absolute;
  left: 400px;
  top: 400px;
}

#gold {
  background-color: gold;
  /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */

  position: fixed;
  bottom: 50px;
  right: 50px;
}

#green {
  background-color: green;
  /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
  position: absolute;
  left: 200px;
  top: 200px;
}

#blue {
  background-color: blue;
  /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 // 자기가 과거에 스테틱일때 기준으로 움직임*/
  position: relative; 
  top: 100px;
  left: 100px;
}

#pink {
  background-color: pink;
  /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
  position: absolute;
  /* 부모 기준으로 위의값이 없어야 하고 왼쪽 값이 없어야 함. */
  top: 0;
  left: 0;
}

#purple {
  background-color: purple;
  /* 초록 사각형의 우측 하단 모서리에 보라 사각형 좌측 상단 모서리 맞대기 */
  position: absolute;
  left: 100px;
  top: 100px;
}

#orange {
  background-color: orange;
  /* 파란 사각형 오른쪽 위 모서리에 오렌지 사각형 좌측 하단 모서리 맞대기 // 부모는 블루, 부모가 확실하다면 앱솔루트를 쓰는게 더 편하다. */
  position: absolute;
  left: 100px;
  top: -100px;
}
```







#### :pushpin:Bootstrap

##### CDN? (content delivery(distribution) network)

- 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능 (지리적 이점)
- 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐





구글 크롬 확장자 프로그램 추천 : **Wappalyzer**

![](https://user-images.githubusercontent.com/52684457/62593886-792cb100-b913-11e9-9d37-4c015572735c.PNG)

해당 페이지의 사용된 프로그램 등을 알 수 있다.



> ##### :clipboard: bootstrap Library
>
> ![](https://user-images.githubusercontent.com/52684457/62593887-792cb100-b913-11e9-9f95-821c8c417906.PNG)
>
> installation 과 bootstrapCDN 두가지의 다운로드 경로가 있으나 후자가 좀 더 사용하기 좋다.
>
> Documentation 클릭 후 
>
> ![](https://user-images.githubusercontent.com/52684457/62594139-6070cb00-b914-11e9-887a-343f9d453026.png)
>
> 위와 같이 적용 시켜주면 된다. JS는 \<body>가 닫히기 직전에 넣어주도록 하자.
>
> 
>
> ![ìº¡ì²3](https://user-images.githubusercontent.com/52684457/62593889-792cb100-b913-11e9-9cab-bf4d6da6ce1b.PNG)
>
> mix.css 는 css를 완전 압축시켜 공백을 최대한 줄인 파일. 둘 중 하나만 가지고 있어도 된다.
>
> - 극단적으로 로딩속도를 줄이기 위한 것
>
> 
>
> **여러 가이드라인이나 사용법을 보기 위해서 아래 링크를 통해 components 카테고리를 이용하거나 검색을 이용하도록 하자.**
>
> https://getbootstrap.com/docs/4.3/content/typography/#headings



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <h1 class="h1">Bootstrap heading</h1>
  <h2>Bootstrap heading</h2>
  <h3>Bootstrap heading</h3>
  <hr>

  <p>
    Lorem ipsum <mark>dolor sit</mark> amet consectetur adipisicing elit. Nisi, non distinctio. Suscipit quasi voluptates quisquam iusto rerum eos minus voluptatibus, reiciendis unde qui dicta aut sunt asperiores iste vitae modi.
  </p>
  <p>
    Lorem ipsum dolor <del>sit amet, consectetur</del> adipisicing elit. Ab ipsam est possimus, facilis itaque voluptatum maiores magnam minima non officia. Repellat molestiae vitae sint sunt corporis! Praesentium tenetur recusandae commodi.
  </p>
  <p>
    Lorem ipsum, <strong>dolor sit amet consectetur</strong> adipisicing elit. Cupiditate illum, aspernatur, adipisci aperiam dolore vel sed explicabo hic quos assumenda placeat nesciunt, officia accusantium veniam accusamus aliquam ullam eum in!
  </p>

  <blockquote class="blockquote text-center">
    <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
    <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
  </blockquote>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

여러가지 기능을 적용시켜보자



1. ##### Utilities - 클래스로 적용시켜보자!

   - **Spacing** - 편안하게 공간 확보 하자!
     - .m-0 / margin 0
     
     - .mr-0 / margin right 0
     
     - .mx-o / margine 좌우 0 
     
     - .py-0 / padding 상하 0
     
     - .mt-1 / 0.25rem == margin top: 4px;
     
     - .mx-auto / 가운데 정렬 (좌우 auto)
     
     - 음수는 n *(ex) n1, n2 ...*
     
     - 
     
       |  mt  | rem  |  px  |
       | :--: | :--: | :--: |
       | mt 2 | 0.5  |  8   |
       | mt 3 |  1   |  16  |
       | mt 4 | 1.5  |  32  |
       | mt 5 |  3   |  64  |
     
       
     
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <style>
         div {
           width: 100px;
           height: 100px;
           background-color: crimson;
           color: white;
         }
           </style>
       </head>
       <body>
         <div class="mt-3">margin top 3</div>
         <div class="mt-2">margin top 2</div>
         <div class="mt-1">margin top 1</div>
         <div class="mb-2">margin bottom 2</div>
         <div class="ml-2">margin left 2</div>
         <div class="mr-2">margin right 2</div>
         <div class="m-3">margin 3</div>
       
         <div class="pt-2">padding top 2</div>
         <div class="pr-2">padding right 2</div>
         <div class="pb-2">padding bottom 2</div>
         <div class="pl-2">padding left 2</div>
         <div class="p-5">padding 5</div>
       
         <div class="mx-auto">가운데 정렬</div>
         <div class="ml-auto">오른쪽 정렬</div>
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       </body>
       </html>
       ```
     
     
   
   - **color** - 좀 더 보기 편한 색으로 변한다.
   
     - .bg-색이름 / background color
   
     - .text-색이름 / color 글자 색을 바꾸는 것
   
     - .alert-warning-색이름 / 경고문
   
     - .btn-색이름 / 버튼
   
     - .navbar-색이름.bg-색이름
   
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <!-- <style>
             div {
               width: 100px;
               height: 100px;
             }
         </style> -->
       </head>
       <body>
         <div class="bg-primary"></div>
         <div class="bg-secondary"></div>
         <div class="bg-warning"></div>
         <div class="bg-info"></div>
       
         <button type="button" class="btn btn-outline-warning">Warning</button>
         <button type="button" class="btn btn-info">Info</button>
         <button type="button" class="btn btn-light">Light</button>
         <button type="button" class="btn btn-dark">Dark</button>
       
         <p class="text-primary">텍스트 색깔은 어떻게??</p>
         <p class="text-danger">이건 빨간색??</p>
         
         <div class="alert alert-primary" role="alert">
             A simple primary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
         </div>
         
         <div class="alert alert-info" role="alert">
             <h4 class="alert-heading">Well done!</h4>
             <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
             <hr>
             <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
         </div>
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       </body>
       </html>
       ```
   
     
   
   - **border** - 테두리
   
     - .border.border-색 이름 / border-color:
   
     - rounded-circle, rounded pill
   
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <style>
             div {
               width: 100px;
               height: 100px;
             }
         </style>
       </head>
       <body>
         <div class="border border-primary">경계가 파란색</div>
         <div class="border border-warning">경계가 노란색</div>
         <div class="border border-danger">경계가 빨간색</div>
         <div class="border border-info">경계가 민트색</div>
         
         <span class="border">4방향</span>
         <span class="border-top">top</span>
         <span class="border-right">right</span>
         <span class="border-bottom">bottom</span>
         <span class="border-left">left</span>
         <br>
         <img src="images/image.png" alt="#" class="rounded-circle">
         <img src="images/image.png" alt="#" class="rounded-pill">
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       </body>
       </html>
       ```
   
   
   
   - **display**
     
   - .d-none
     
   - **position**
   
     - .position-static / position-static (그대로 사용)
   
     - .fixed-top, bottom => fixed같은 경우에는 위아래 고정 시킬 때에는 position을 생략
   
     - ```html
       <!-- displaty, position -->
       <!DOCTYPE html>
    <html lang="ko">
   <       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <style>
           div {
             width: 100px;
             height: 100px;
           }
       
           .sticky {
             width: 100%;
             height: 30px;
           }
         </style>
       </head>
       <body>
         <!-- div는 원래 block이지만 inline 으로 만들 수 있다. -->
         <!-- .d-inline.bg-primary.text-white -->
         <div class="d-inline bg-primary text-white">div to inline</div>
         <div class="d-inline bg-primary text-white">div to inline</div>
         <div class="d-inline bg-primary text-white">div to inline</div>
         <br>
         <hr>
       
         <!-- span은 원래 inline이지만 block으로 만들 수 있다. -->
         <!-- span.d-block.bg-dark.text-white -->
         <span class="d-block bg-dark text-white">span to block</span>
         <span class="d-block bg-dark text-white">span to block</span>
       
         <hr>
       
         <!-- 반응형 맛보기 - 왜 bootstrap을 사용하는가? -->
         <!-- .bg-danger.d-sm-none.d-m-block -->
         <!-- 백그라운드는 빨간색, sm사이즈(576px 이상)에서는 보이지 않고 m사이즈(768px)에서는 block(다시 나타남) -->
         <div class="bg-danger d-sm-none d-m-block">보이나? 안보이나?</div>
         <div class="bg-warning d-md-none d-xl-block">보이나? 안보이나?</div>
       
         <!-- position fixed -->
         <!--   .fixed-top.bg-dark -->
         <div class="sticky fixed-top bg-dark"></div>
         <div class="sticky fixed-bottom bg-dark"></div>
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       </body>
       </html>
       ```
   
     
   
   
   
   - **text**
   
     - .text-center
   
     - .font-weight-bold / font-weight: bold
   
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       
       </head>
       <body>
         <p class="text-left">Left aligned text on all viewport sizes.</p>
         <p class="text-center">Center aligned text on all viewport sizes.</p>
         <p class="text-right">Right aligned text on all viewport sizes.</p>
         
         <!-- text 정렬 + 반응형 / 기본 값은 좌측 정렬 -->
         <p class="text-sm-left">Left aligned text on viewports sized SM (small) or wider.</p>
         <p class="text-md-center">Left aligned text on viewports sized MD (medium) or wider.</p>
         <p class="text-lg-right">Left aligned text on viewports sized LG (large) or wider.</p>
         <p class="text-xl-right">Left aligned text on viewports sized XL (extra-large) or wider.</p>
       
         <!-- 텍스트 변형 -->
         <p class="text-lowercase">Lowercased text.</p>
         <p class="text-uppercase">Uppercased text.</p>
         <p class="text-capitalize">CapiTaliZed text.</p>
       
         <!-- 폰트 굵기 및 이텔릭 / 부모에 따라 bolder와 lighter이 상대값이기 때문에 굵기 둥이 달라진다. -->
         <p class="font-weight-bold">Bold text.</p>
         <p class="font-weight-bolder">Bolder weight text (relative to the parent element).</p>
         <p class="font-weight-normal">Normal weight text.</p>
         <p class="font-weight-light">Light weight text.</p>
         <p class="font-weight-lighter">Lighter weight text (relative to the parent element).</p>
         <p class="font-italic">Italic text.</p>
       
         <!-- monospace -->
         <p class="text-monospace">This is in monospace</p>
       
         <!-- text decoration / 링크를 걸었을 때, 밑줄이 나타나지 않음 -->
         <a href="#" class="text-decoration-none">Non-underlined link</a>
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" 
         integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" 
         integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" 
         integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
       </body>
       </html>
       ```
   
   - **component**
   
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
           integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       
       </head>
       
       <body>
       
         <div class="alert alert-success" role="alert">
           A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
         </div>
         <div class="alert alert-danger" role="alert">
           A simple danger alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
         </div>
         <div class="alert alert-warning" role="alert">
           A simple warning alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
         </div>
         <div class="alert alert-info" role="alert">
           A simple info alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
         </div>
       
         <span class="badge badge-warning">Warning</span>
         <span class="badge badge-info">Info</span>
         <span class="badge badge-light">Light</span>
         <span class="badge badge-dark">Dark</span>
       
         <span class="badge badge-pill badge-warning">Warning</span>
         <span class="badge badge-pill badge-info">Info</span>
         <span class="badge badge-pill badge-light">Light</span>
         <span class="badge badge-pill badge-dark">Dark</span>
       
         <button type="button" class="btn btn-primary">
           Profile <span class="badge badge-light">9</span>
           <span class="sr-only">unread messages</span>
         </button>
       
         <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
           <button type="button" class="btn btn-secondary">1</button>
           <button type="button" class="btn btn-secondary">2</button>
       
           <div class="btn-group" role="group">
             <button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown"
               aria-haspopup="true" aria-expanded="false">
               Dropdown
             </button>
             <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
               <a class="dropdown-item" href="#">Dropdown link</a>
               <a class="dropdown-item" href="#">Dropdown link</a>
             </div>
           </div>
         </div>
       
         <div class="card" style="width: 18rem;">
           <img src="images/image.png" class="card-img-top" alt="#">
           <div class="card-body">
             <h5 class="card-title">Card title</h5>
             <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
               content.</p>
             <a href="#" class="btn btn-primary">Go somewhere</a>
           </div>
         </div>
         <button type="button" class="btn btn-primary btn-lg btn-block">Block level button</button>
         <button type="button" class="btn btn-secondary btn-lg btn-block" disabled>Block level button</button>
       
         <div class="card text-center">
           <div class="card-header">
             <ul class="nav nav-tabs card-header-tabs">
               <li class="nav-item">
                 <a class="nav-link active" href="#">Active</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link" href="#">Link</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
               </li>
             </ul>
           </div>
           <div class="card-body">
             <h5 class="card-title">Special title treatment</h5>
             <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
             <a href="#" class="btn btn-primary">Go somewhere</a>
           </div>
         </div>
       
         </div>
         <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
           <div class="card-header">Header</div>
           <div class="card-body">
             <h5 class="card-title">Dark card title</h5>
             <p class="card-text">이것은 깜장색 카드당
             </p>
           </div>
         </div>
       
       
         <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
           <ol class="carousel-indicators">
             <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
             <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
             <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
           </ol>
           <div class="carousel-inner">
             <div class="carousel-item active">
               <img src="images/image.png" class="d-block w-100" alt="#">
             </div>
             <div class="carousel-item">
               <img src="images/image.png" class="d-block w-100" alt="#">
             </div>
             <div class="carousel-item">
               <img src="images/image.png" class="d-block w-100" alt="#">
             </div>
           </div>
           <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
             <span class="sr-only">Previous</span>
           </a>
           <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
             <span class="carousel-control-next-icon" aria-hidden="true"></span>
             <span class="sr-only">Next</span>
           </a>
         </div>
       
         <p>
           <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false"
             aria-controls="collapseExample">
             Link with href
           </a>
           <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample"
             aria-expanded="false" aria-controls="collapseExample">
             Button with data-target
           </button>
         </p>
         <div class="collapse" id="collapseExample">
           <div class="card card-body">
             우히힝 깜짝 놀랐지!
           </div>
         </div>
       
         <div class="dropdown">
           <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown"
             aria-haspopup="true" aria-expanded="false">
             Dropdown button
           </button>
           <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
             <a class="dropdown-item" href="#">Action</a>
             <a class="dropdown-item" href="#">Another action</a>
             <a class="dropdown-item" href="#">날 제발 눌러죠!</a>
           </div>
         </div>
       
         <form>
           <div class="form-group">
             <label for="exampleInputEmail1">Email address</label>
             <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
               placeholder="Enter email">
             <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
           </div>
           <div class="form-group">
             <label for="exampleInputPassword1">Password</label>
             <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
           </div>
           <div class="form-group form-check">
             <input type="checkbox" class="form-check-input" id="exampleCheck1">
             <label class="form-check-label" for="exampleCheck1">Check me out</label>
           </div>
           <button type="submit" class="btn btn-primary">Submit</button>
         </form>
       
         <div class="jumbotron bg-info text-white">
           <h1 class="display-4">안녕, 세상아!</h1>
           <p class="lead">이것은 세상이 우리에게 주는 경고입니다. 귀담아 들으세요~ listen carefully~</p>
           <hr class="my-4">
           <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
           <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
         </div>
       
         <div class="media">
           <img src="#" class="mr-3" alt="#">
           <div class="media-body">
             <h5 class="mt-0">Media heading</h5>
             Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio,
             vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec
             lacinia congue felis in faucibus.
       
             <div class="media mt-3">
               <a class="mr-3" href="#">
                 <img src="#" class="mr-3" alt="#">
               </a>
               <div class="media-body">
                 <h5 class="mt-0">Media heading</h5>
                 Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio,
                 vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec
                 lacinia congue felis in faucibus.
               </div>
             </div>
           </div>
         </div>
       
         <!-- Button trigger modal -->
         <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
           Launch demo modal
         </button>
       
         <!-- Modal -->
         <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
           aria-hidden="true">
           <div class="modal-dialog" role="document">
             <div class="modal-content">
               <div class="modal-header">
                 <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                   <span aria-hidden="true">&times;</span>
                 </button>
               </div>
               <div class="modal-body">
                 이것은 자바스크립트로 대부분 짠 것이지요...
               </div>
               <div class="modal-footer">
                 <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                 <button type="button" class="btn btn-primary">Save changes</button>
               </div>
             </div>
           </div>
         </div>
       
         <nav aria-label="Page navigation example">
           <ul class="pagination justify-content-center">
             <li class="page-item disabled">
               <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
             </li>
             <li class="page-item"><a class="page-link" href="#">1</a></li>
             <li class="page-item"><a class="page-link" href="#">2</a></li>
             <li class="page-item"><a class="page-link" href="#">3</a></li>
             <li class="page-item">
               <a class="page-link" href="#">Next</a>
             </li>
           </ul>
         </nav>
       
         <div class="progress">
           <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
         </div>
         <div class="progress">
           <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0"
             aria-valuemax="100"></div>
         </div>
         <div class="progress">
           <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0"
             aria-valuemax="100"></div>
         </div>
         <div class="progress">
           <div class="progress-bar" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0"
             aria-valuemax="100"></div>
         </div>
         <div class="progress">
           <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0"
             aria-valuemax="100"></div>
         </div>
       
         <div class="progress">
           <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75"
             aria-valuemin="0" aria-valuemax="100" style="width: 75%"></div>
         </div>
         <br>
         <div class="progress" style="height: 1px;">
           <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0"
             aria-valuemax="100"></div>
         </div>
       
         <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
           <span class="sr-only">Loading...</span>
         </div>
         <div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status">
           <span class="sr-only">Loading...</span>
         </div>
       
       
         <button class="btn btn-primary" type="button" disabled>
           <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
           <span class="sr-only">Loading...</span>
         </button>
         <button class="btn btn-primary" type="button" disabled>
           <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
           <span class="sr-only">Loading...</span>
         </button>
       
       
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
           integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
         </script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
           integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
         </script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
           integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
         </script>
       </body>
       
       </html>
       ```
   
     
   
   - **grid**
   
     - *CSS layout history*
       레이아웃이 없던 시절 => 테이블 레이아웃 => 프레임 레이아웃(html로 분할) => CSS(float / position) => flex box (요소들을 1차원적으로 정렬) => grid 시스템 (규칙적인 격자무늬.2차원. x축과 y축을 동시에 조절가능)
   
       - grid는 flex box에서 부터 파생되었기 때문에 flex box에 대한 개념이해가 필요하다.
   
     - 12는 작은 수지만 약수가 많다. => 그만큼 그리드 배열을 다양하게 할 수 있다.
   
     - ```html
       <!DOCTYPE html>
       <html lang="ko">
       
       <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
           integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <style>
           .square {
             width: 200px;
             height: 200px;
             background-color: lightcoral;
             border: 1px solid black;
             text-align: center;
             line-height: 200px;
           }
         </style>
       </head>
       
       <body>
         <!-- 1. gird 기본 골격 -->
         <div class="container">
           <!-- row는 flex의 속성을 가지고 있다. -->
           <div class="row">
             <div class="square col-4">1</div>
             <div class="square col-4">2</div>
             <div class="square col-4">3</div>
           </div>
         </div>
       
         <!-- 2. container - fluid -->
         <div class="container-fluid">
           <div class="row">
             <div class="square col-4">1</div>
             <div class="square col-4">2</div>
             <div class="square col-4">3</div>
           </div>
         </div>
       
         <!-- 3. grid - col-1 -->
         <!--   .container>.row>.square.col-1*12 -->
         <!-- 컨테이너 안에 로우 안에 스퀘어 col-1을 12개 -->
         <div class="container">
           <div class="row">
             <div class="square col-1">1</div>
             <div class="square col-1">2</div>
             <div class="square col-1">3</div>
             <div class="square col-1">4</div>
             <div class="square col-1">5</div>
             <div class="square col-1">6</div>
             <div class="square col-1">7</div>
             <div class="square col-1">8</div>
             <div class="square col-1">9</div>
             <div class="square col-1">10</div>
             <div class="square col-1">11</div>
             <div class="square col-1">12</div>
             <!-- grid 값(12칸)을 초과하는 순간 아래로 떨어진다. -->
             <div class="square col-1">13</div>
           </div>
         </div>
       
         <!-- 4. grid col합이 12를 초과하는 경우 -->
         <div class="container">
           <div class="row">
             <div class="square col-9">col-9</div>
             <div class="square col-4">col-4</div>
             <div class="square col-3">col-3</div>
           </div>
         </div>
       
         <!-- 5. gird 정리 -->
         <div class="container">
           <h1 class="text-center">정리</h1>
           <div class="row">
             <div class="square col-1">col-1</div>
             <div class="square col-1">col-1</div>
             <div class="square col-1">col-1</div>
           </div>
       
           <div class="row">
             <div class="square col-3">col-3</div>
             <div class="square col-3">col-3</div>
             <div class="square col-3">col-3</div>
             <div class="square col-3">col-3</div>
           </div>
       
       
           <div class="row">
             <div class="square col-4">col-4</div>
             <div class="square col-8">col-8</div>
           </div>
       
           <div class="row">
             <div class="square col-2 offset-5">col-2 offset-5</div>
           </div>
         </div>
       
         <div class="row">
           <div class="square col-md-3 col-6">col-</div>
           <div class="square col-md-3 col-6">col-</div>
           <div class="square col-md-3 col-6">col-</div>
           <div class="square col-md-3 col-6">col-</div>
         </div>
       
       
       
         <h2 class="text-center">퀴즈</h2>
         <!-- 
           해당 조건에 맞게 grid 를 통해 작성해보시오.
           576px 미만 : 1등분
           576px 이상 : 2등분
           768px 이상 : 3등분
           992px 이상 : 4등분
           1200px 이상 : 6등분
          -->
       
          <div class="row">
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
            <div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
          </div>
       
       
       
       
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
           integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
         </script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
           integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
         </script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
           integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
         </script>
       
       </body>
       
       </html>
       ```



------



### :point_up: CSS하기에 유용한 사이트



#### **Lorempixel** - http://lorempixel.com/

- 사진을 무작위로 끌어다 쓸수있는 링크 (html에 바로 넣어주면 된다.)
- ![](https://user-images.githubusercontent.com/52684457/62667255-cff0c400-b9c1-11e9-8484-9f7d8aa57dac.PNG)
  - 뒤의 400/200은 px 사이즈. 이미지가 필요한 코드에 복사 붙여넣기 하면 된다.



#### **fontawesome** - https://fontawesome.com/

- 아이콘 등을 제공해주는 사이트 Doc 카테고리를 이용하면 사용 방법을 알 수 있다.
- https://l-lin.github.io/font-awesome-animation/ - fontawsome 애니메이팅을 도와줌
- ![](https://user-images.githubusercontent.com/52684457/62667256-cff0c400-b9c1-11e9-8dbf-0f31b190d8b8.png)



#### **animate.css** - https://daneden.github.io/animate.css/

- fontawesome만으로는 애니메이팅에 한계가 있다. animate.css를 사용해보자.
- ![](https://user-images.githubusercontent.com/52684457/62667257-cff0c400-b9c1-11e9-870a-a7b8eb32e183.PNG)
  - 동작을 선택 후 animate it을 클릭하면 동작예시를 볼 수 있다.
  - 직접 사용하기 위해서 View on GitHub에 들어가보자.
  - ![](https://user-images.githubusercontent.com/52684457/62667252-cf582d80-b9c1-11e9-9343-558400a18389.PNG)
    - readme를 읽어보면 CDN링크가 나와있다. 복사해서 \<head>안에 넣어준다.
    - CDN을 좀 더 권장하고 있으니  CDN을 사용하자.
  - ![](https://user-images.githubusercontent.com/52684457/62667254-cf582d80-b9c1-11e9-8641-75ff7804b17f.PNG)
    - 예제를 보며 여러가지 애니메이팅 클래스들을 사용해보자.

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="00_font_awsome.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css">
    <script src="https://kit.fontawesome.com/e7c9242ec2.js"></script>
  <style>
  .square {
    width: 100px;
    height: 100px;
  }

  /* 부트 스트랩은 컬러가 디폴트 되어있어서 !important 해주어야 덮어 씌울 수 있다. */
  /* hover은 마우스 커서를 가져다 대었을때 작용하는 코드 */
  .square-animate:hover {
    background-color: crimson !important;
    opacity: 0.7;
    animation: tada 2s infinite;
  }

  </style>
</head>

<body>
  <i style="color: tomato;" class="fas fa-angry fa-10x faa-bounce animated"></i>
  <div class="square bg-primary d-inline-block animated infinite bounce delay-2s"></div>
  <div class="square square-animate bg-primary d-inline-block"></div>




  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```



### flex box

- container : 부모 (상위 요소)
- flex items : 자식
- 정해진 이름은 아님



```css
<!-- 기본 베이스 css -->
body {
  margin: 0;
  color: white;
}

.item {
  text-align: center;
  font-size: 100px;
}

.item1 {
  background-color: pink;
}

.item2 {
  background-color: red;
}

.item3 {
  background-color: darkorange;
}

.item4 {
  background-color: yellow;
}

.item5 {
  background-color: darkgreen;
}

.item6 {
  background-color: skyblue;
}

.item7 {
  background-color: blue;
}

.item8 {
  background-color: navy;
}

.item9 {
  background-color: purple;
}

.item10 {
  background-color: brown;
}

.item11 {
  background-color: darkgrey;
}

.item12 {
  background-color: black;
}
```

```html
/* 1 */
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="01_flex.css">
  <style>
    .container {
      height: 100vh;
      border: 10px solid royalblue;
      display: flex;
      /* flex-direction: row-reverse; */
      /* flex-direction: column;
      flex-direction: column-reverse; */
      flex-wrap: wrap; /* 부모의 총 길이보다 넘치면 다음 줄로 넘김 */
      flex-wrap: nowrap; /* 기본 값, 한줄에 나타내려고 함. */
      flex-wrap: wrap-reverse; /* wrap과는 반대로 넘치면 위로 넘김 */
      /* direction과 wrap을 한줄로 작성 */
      /* flex-flow: row nowrap; 이것도 기본값 */
      /* flex-flow: column wrap */
    }

    /* flex속성을 주는 순간 block속성이 없어져서 자유로워 짐 */
    /* column이 돌아가는 순간 축이 바뀌므로 잘 생각해야 한다. x, y축 */
  
    .item {
      /* 브라우저는 5000px보다 작지만 총 5000px을 준것을 자동으로 가로폭에 맞춰준다.  */
      width: 500px;
    }

  </style>
</head>

<body>
  <div class="container p-0">
    <div class="item item1">1</div>
    <div class="item item2">2</div>
    <div class="item item3">3</div>
    <div class="item item4">4</div>
    <div class="item item5">5</div>
    <div class="item item6">6</div>
    <div class="item item7">7</div>
    <div class="item item8">8</div>
    <div class="item item9">9</div>
    <div class="item item10">10</div>
  </div>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

```html
/* 2 */
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="02_flex.css">
  <style>
    .container {
      height: 100vh;
      border: 10px solid royalblue;
      display: flex;
    }

    .item {
      width: 300px;
      height: 200px;
    }

    .item2 {
      flex-grow: 2;
    }

    .item3 {
      flex-grow: 3;
    }
/* 남는 여백을 기준으로 나누는 것이지 2:3이 되거나 일정하게 자리를 차지하는 것이 아님 */
/* flex grow 는 남는 좌우 여백을 5등분해서 지정한 클래스에 지정한 값만큼 각각 나눠준다 */
/* 
3개 박스 비율이 정확히 1:2:3 이 되지는 않는다.
남는 여백 부분에서 비율을 정해서 각 박스에 촉을 추가하기 때문.
전체적으로 부모에 맞춰 꽉차게 만들오주긴 하는데, 각 박스의 비율은
원래 남는 비율을 지정된 grow 만큼 계산에서 추가해주기 때문. */
/* point : 남은 여백을 꽉차게 해주기 위함 */
  </style>
</head>

<body>
  <div class="container p-0">
    <div class="item item1">1</div>
    <div class="item item2">2</div>
    <div class="item item3">3</div>
  </div>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

```html
/* 3 */
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="03_flex.css">
  <style>
    .container {
      height: 100vh;
      border: 10px solid royalblue;
      display: flex;

      /* x축 정렬 */
      /* 왼쪽 정렬 (기본값) */
      /* justify-content: flex-start;
      /* 오른쪽 정렬 */
      /* justify-content: flex-end;
      /* 가운데 정렬 */
      /* justify-content: center; */
      /* 좌우 정렬 */
      /* justify-content: space-between; */
      /* 균등 좌우 정렬 : 외곽의 너비의 두배가 내곽의 너비 / 요소 여백은 외곽 여백의 2배 */
      /* justify-content: space-around; */
      /* 균등 정렬 : 완전히 모든 여백이 동일 / 요소 여백 == 외곽 여백 */
      /* justify-content: space-evenly;  */

      /* y축 정렬 */
      /* 상하단 꽉차게 (기본) */
      align-items: stretch;
      /* 상단 정렬 */
      align-items: flex-start;
      /* 하단 정렬 */
      align-items: flex-end;
      /* 가운데 정렬 */
      align-items: center;
      /* baseline 정렬 : item 내부의 text 라인 맞추기 */
      align-items: baseline;
        
      /* align-content: flex-start : justify의 값을 받아서  여러줄 사이의 간격을 지정할 수 있다. */
    }

    .item {
      border: 10px solid olive;
    }

    .item1 {
      font-size: 2rem;
    }
    
    .item2 {
      font-size: 10rem;
    }

    .item3 {
      font-size: 5rem;
    }


  </style>
</head>

<body>
  <div class="container p-0">
    <div class="item item1">1</div>
    <div class="item item2">2</div>
    <div class="item item3">3</div>

  </div>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

```html
/* 4 */
<!DOCTYPE html>
<html lang="ko">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="stylesheet" href="04_flex.css">
	<style>
		.container {
			height: 100vh;
      border: 10px solid royalblue;
      display: flex;
    }
    
    .item {
      width: 200px;
      height: 300px;
      border: 10px solid olive;
      line-height: 300px
    }

    .item8 {
      align-self: flex-end;
    }

    .item5 {
      align-self: center;
    }
	</style>
</head>

<body>
	<div class="container p-0">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
		<div class="item item4">4</div>
		<div class="item item5">5</div>
		<div class="item item6">6</div>
		<div class="item item7">7</div>
		<div class="item item8">8</div>
		<div class="item item9">9</div>
		<div class="item item10">10</div>
		<div class="item item11">11</div>
		<div class="item item12">12</div>
	</div>

	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>
</body>

</html>
```

```html
/* 5 */
<!DOCTYPE html>
<html lang="ko">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="stylesheet" href="05_flex.css">
	<style>
		.container {
			height: 100vh;
      border: 10px solid royalblue;
      display: flex;
    }
    
    .item {
      width: 200px;
      height: 300px;
      border: 10px solid olive;
      line-height: 300px;
    }

    .item1 {
      order: 0;
    }

    /* order값이 없는 요소들은 기본적으로 0을 가지고 있다.
    그래서 1의 입장에서는 가장 마지막일 수 밖에 없다. */
    .item2 {
      order: 1;
    }

    .item8 {
      order: 2;
    }

    .item4 {
      order: -1;
    }

    .item5 {
      order: -2;
    }

	</style>
</head>

<body>
	<div class="container p-0">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
		<div class="item item4">4</div>
		<div class="item item5">5</div>
		<div class="item item6">6</div>
		<div class="item item7">7</div>
		<div class="item item8">8</div>
		<div class="item item9">9</div>
		<div class="item item10">10</div>
		<div class="item item11">11</div>
		<div class="item item12">12</div>
	</div>

	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>
</body>

</html>
```

> x축 **justify** (거의 content만 사용 하기 때문에 content를 잘 기억해두면 된다.)
>
> y축 **align**
>
> direction을 column으로 바뀌는 순간 축이 바뀌는 것을 생각해야 한다. (90도씩 돌려짐)
>
> 
>
> 한줄 **items**
>
> 여러줄 **content**
>
> 개별 요소 **self**

#### css.trick - https://css-tricks.com/snippets/css/a-guide-to-flexbox/

- A Complete Guide to Flexbox
- 이 외 여러 snippets(팁 같은)가 있음



> ###### 직접 코드를 짜면서 구조를 알아보자
>
> ```html
> <!DOCTYPE html>
> <html lang="ko">
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <meta http-equiv="X-UA-Compatible" content="ie=edge">
>   <title>Document</title>
>   <link rel="stylesheet" href="06_flex_layout.css">
> </head>
> <body>
>   <div class="container">
>     <nav>
>       <div class="logo">LOGO</div>
>       <ul class="items">
>         <li>Home</li>
>         <li>About</li>
>         <li>Content</li>
>         <li>Contact</li>
>       </ul>
>     </nav>
>     <div class="main">
>       <aside>왼쪽</aside>
>       <section>
>         <div class="article">
>           Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum distinctio placeat alias temporibus quidem adipisci, consectetur perferendis enim? Placeat hic molestias fugiat quibusdam doloremque et ut sunt libero enim dicta?
>         </div>
>         <div class="article">
>           Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione dignissimos tempore blanditiis unde cupiditate animi consequatur voluptas error, at nostrum et tenetur voluptates aperiam, voluptatibus reiciendis fugiat ipsam. Voluptas, exercitationem.
>         </div>
>         <div class="article">
>           Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laudantium unde consectetur dicta id, totam doloribus quam voluptate reiciendis rerum nulla vitae maxime maiores. Odit, atque deleniti temporibus accusantium sint voluptates?
>         </div>
>       </section>
>     </div>
>     <footer>
>       이곳은 푸터입니다.
>     </footer>
>   </div>
> </body>
> </html>
> ```
>
> ```css
> .container {
>   display: flex;
>   height: 100vh;
>   /* 축을 바꾸기 위해서 column */
>   flex-direction: column;
> }
> 
> nav {
>   display: flex;
>   height: 100vh;
>   height: 100px;
>   background-color: rgb(53, 50, 52);
>   justify-content: space-between;
>   align-items: center;
> }
> 
> .items {
>   display: flex;
> }
> 
> .items > li {
>   list-style-type: none;
>   /* 상하0 좌우20 */
>   margin: 0 20px;
> }
> 
> .main {
>   display: flex;
>   height: 100%;
> }
> 
> aside {
>   width: 300px;
>   height: 100%;
>   background-color: greenyellow
> }
> 
> section {
>   display: flex;
>   background-color: green;
>   height: 100%;
>   flex-grow: 1;
>   flex-direction: column;
>   /* direction:  */
> }
> 
> .article {
>   background-color: crimson;
>   border: 1px solid yellow;
>   padding: 30px 15px;
>   flex-grow: 1;
> }
> 
> footer {
>   background-color: rgb(184, 235, 227);
>   /* 꽉차게 해주고 싶을 때 100% */
>   width: 100%;
>   height: 100px;
>   /* block일때는 margin-top: auto;가 불가능하다. (값이 없기 때문) flex기때문에 가능 */
>   margin-top: auto;
> }
> ```



###### 직접 짠 코드를 보면서 bootstrap을 사용해보자.

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <style>
    nav {
      height: 100px;
    }

    footer {
      height: 100px;
    }

    .items>li {
      list-style-type: none;
    }

    aside {
      width: 200px;
    }
  </style>
</head>

<body>
  <div class="vh-100 container d-flex flex-column p-2 ">
    <nav class="d-flex align-items-center justify-content-between bg-dark">
      <div class="p-2 font-weight-bold text-white">LOGO</div>
      <ul class="items d-flex my-0">
        <li class="p-2 text-white">Home</li>
        <li class="p-2 text-white">About</li>
        <li class="p-2 text-white">Content</li>
        <li class="p-2 text-white">Contact</li>
      </ul>
    </nav>
    <div class="main d-flex h-100 p-1">
      <aside class="w-100 bg-info py-5 px-5 font-weight-bold text-white" style="height: ">left</aside>
      <section class="d-flex flex-grow-1 flex-column">
        <div class="p-2 border border-white bg-light flex-grow-1">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum distinctio placeat alias temporibus quidem
          adipisci, consectetur perferendis enim? Placeat hic molestias fugiat quibusdam doloremque et ut sunt libero
          enim dicta?
        </div>
        <div class="p-2 border border-white bg-light flex-grow-1">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione dignissimos tempore blanditiis unde
          cupiditate animi consequatur voluptas error, at nostrum et tenetur voluptates aperiam, voluptatibus reiciendis
          fugiat ipsam. Voluptas, exercitationem.
        </div>
        <div class="p-2 border border-white bg-light flex-grow-1">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laudantium unde consectetur dicta id, totam
          doloribus quam voluptate reiciendis rerum nulla vitae maxime maiores. Odit, atque deleniti temporibus
          accusantium sint voluptates?
        </div>
      </section>
    </div>
    <footer class="d-f w-100 bg-dark mt-auto text-center font-weight-light text-light text-uppercase">
      This is footer
    </footer>
  </div>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

![](https://user-images.githubusercontent.com/52684457/62680211-aa7bae80-b9f1-11e9-9d2f-5191bea8c706.png)







## :triangular_flag_on_post: flex 총정리

```html
<!-- boot_flex.temp.html -->

<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="boot_align_temp.css">
  <title>Grid: Column_Finish</title>
</head>

<body>
  <!-- JUSTIFY-CONTENT
    ============================================ -->
  <div class="container">
    <h1 class="display-1 text-center">JUSTIFY-CONTENT</h1>
    <br>
    <!-- justify-content-center -->
    <h3 class="display-1 text-center">center</h3>
    <div class="row justify-content-center">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-start -->
    <h3 class="display-1 text-center">start</h3>
    <div class="row justify-content-start">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-end -->
    <h3 class="display-1 text-center">end</h3>
    <div class="row justify-content-end">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-between -->
    <h3 class="display-1 text-center">between</h3>
    <div class="row justify-content-between">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
    <br>
    <!-- justify-content-around -->
    <h3 class="display-1 text-center">around</h3>
    <div class="row justify-content-around">
      <div class="col-2">1</div>
      <div class="col-2">2</div>
      <div class="col-2">3</div>
    </div>
  </div>

  <br><br>

  <!-- ALIGN ITEMS
    ============================================ -->
  <div class="container">
    <h1 class="display-1 text-center">ALIGN ITEMS</h1>
    <br>
    <!-- align-items-center -->
    <h3 class="display-1 text-center">center</h3>
    <div class="row row-vh align-items-center">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
    <br>
    <!-- align-items-start -->
    <h3 class="display-1 text-center">start</h3>
    <div class="row row-vh align-items-start">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
    <br>
    <!-- align-items-end -->
    <h3 class="display-1 text-center">end</h3>
    <div class="row row-vh align-items-end">
      <div class="col">1</div>
      <div class="col">2</div>
      <div class="col">3</div>
    </div>
  </div>

  <br><br>

  <!-- ALIGN SELF
    ============================================ -->
  <div class="container">
    <h1 class="display-1 text-center">ALIGN SELF</h1>
    <br>
    <div class="row row-vh align-items-center">
      <div class="col align-self-start">start</div>
      <div class="col">center</div>
      <div class="col align-self-end">end</div>
    </div>
  </div>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```

```css
body {
  margin: 5rem auto;
  background-color: darkslategray;
  color: white;
}

.container {
  margin: 10px auto;
  padding: 20px auto;
  border: 10px solid yellow;
}

.container h1 {
  text-transform: uppercase;
}

.row {
  border: 10px solid lightblue;
}

.container>.row>div {
  padding: 20px 10px;
  border: 10px solid white;
  font-size: 50px;
  text-align: center;
}

.container>.row>div:nth-child(odd) {
  background: orange;
}

.container>.row>div:nth-child(even) {
  background: green;
}

.row-vh {
  height: 500px;
}
```

#### FlexBox Froggy - https://flexboxfroggy.com/#ko

- flex에 대한 개념 이해를 도울수 있는 미니게임 사이트
- 개발자 모드(F12)에 들어가면 정답을 알 수 있다.





------

### media query

------

- 개발자 모드에서 빨간 표시된 아이콘을 누르면 모바일 버전을 볼 수있다.
- 파란 표시를 누르면 가로모드로 전환이 된다.

![](https://user-images.githubusercontent.com/52684457/62678572-d3e60b80-b9ec-11e9-9b53-5f5397588aed.PNG)



```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="09_media_query.css">
</head>

<body>
  <h1>안녕하슈~</h1>
  <p class="orientation">지금 방향은~</p>
  <h2>작으면 반짝!</h2>
  <h1 class="rainbow">무지개를 찾아라!</h1>
  <h3>너비와 높이를 함께 적용!</h3>
  <p class="print">나는 프린트할때만 빨강색이야!!!</p>
</body>

</html>
```

```css
@media not|only mediatype and (조건문) {
  실행문
}

/* 우리는 이렇게만 사용할 것이다 */
@media (조건문) {
  실행문
}

@media only all and (max-width: 1200px) {
  * {
    margin: 0;
  }
}

/* 
 1. only | not : 즉정 미디어 타입에서만, 또는 특정 미디어 타입을 제외하고 스타일 적용
    ( only screem / only print / not print )

 2. all : 모든 미디어 타입 (기본값)
    ( screen / print / tty / tv ... )

 3. 논리 연산자를 사용하여 조건을 설정 할 수 있다.
    ( not / and / ,(or) )
*/


/* 뷰포트 너비가 600px 이상 (최소 너비 600px) */
@media (min-width:600px) {
  h1 {
    color: crimson;
  }
}

@media (max-width:500px) {
  h2 {
    color: blue;
  }
}

@media (width: 500px) {
  h1 {
    color: orange;
  }
}

/* 가로 모드 */
@media (orientation: landscape) {
  .orientation::after {
    content: '가롱이~'   
  }
}

/* 세로 모드 */
@media (orientation: portrait) {
  .orientation::after {
    content: '세롱이~'   
  }
}

/* 무지개 만들기 */
@media (min-width: 500px) {
  .rainbow {
    color: red
  }
}
@media (min-width: 600px) {
  .rainbow {
    color: orange;
  }
}
@media (min-width: 700px) {
  .rainbow {
    color: yellow;
  }
}
@media (min-width: 800px) {
  .rainbow {
    color: green;
  }
}
@media (min-width: 900px) {
  .rainbow {
    color: blue;
  }
}
@media (min-width: 1000px) {
  .rainbow {
    color: navy;
  }
}
@media (min-width: 1100px) {
  .rainbow {
    color: purple;
  }
}

/* 뷰포트 너비가 500px 이하 그리고 높이가 500px 이하 이면 실행 */
@media (max-width: 500px) and (max-height: 500px) {
  h3 {
    color: rosybrown;
  }
}

/* print */
@media only print {
  .print {
    color: red
  }
}
```







