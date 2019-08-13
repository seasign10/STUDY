# :package:Web



#### :page_facing_up:Web service : client <=>server / requests <=> response

> **flask** 와 **django**를 통한 server 만들기
>
> **browser를 통해** 서버에 요청. 
>
> 서버 컴퓨터에서 **요청과 응답**을 처리할 프로그램을 개발한다.(back-end) = web service
>
> 실제 주소 IP에 편의상 도메인(google)을 씌움  => 실제로 서버에 접근하는 URL
>
> **이미 만들어진 상태**로 업로드만 하는 상태 
>  *(ex) github 은 static web 서버 한 페이지만 무료로 나눠주는것*



**static web** 
*(ex) 포트폴리오 페이지 처럼 정보를 한 방향으로 제공하기만 하고 변화가 없는 site*

**dynamic web** 
*(ex) SNS와 같이 새로운 글이 올라오면 바로 업데이트 되는 동적인 형태의 site*



- URL 보다 넓은 개념으로 URI은 많이 사용안함

- **HTML**(프로그래밍언어가 아니라 단순히, 텍스트를 보여주기 위한 표시언어)

- HYPER TEXT : 페이지 상 링크기능으로 특정 순서없이 자유롭게 이동가능
                           => 이전에는 책 넘기듯 하나하나 이동했어야함 

- **CSS** : html을 꾸미는 기능(표시언어)

- **JavaScript** : 프로그래밍 언어로 html(뼈대), css(꾸밈), javascript(활기)

  

> **http**는 HYPER TEXT 고유의 규칙
>
> **http(s)**  **=>**  http에서 보안이 강화된 버젼 (속도도 차이도 난다.)



**open graph(og)** : 페이스북이 만든 기술로 url 전송시 하단에 그래프가 같이 뜨는 기술

                                -  표준화가 된 기술



------



#### :page_facing_up:IE

사용안하는 이유

1. 웹 표준을 지키지 않음
2. 모바일 대응 하지 않음
3. 성능 개선 X, 느림 X

모든 사용자가 같은 브라우저는 사용하는게 아니기 때문에 IE에도 어느정도 대응을 해야 함.
=> **Cross Browsing** 



### :page_facing_up:HTML

- HTML은 정보와 구조화 

1. 들여쓰기는 공백 2문자를 사용

2. 속상 값에는 반드시 큰 따옴표를 사용 (''도 작동되기는 하지만 가이드라인을 지켜야 더 보기 편함)

3. 태그, 속성, 속성값 등에는 모두 소문자만 사용

4. 최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정

   - 스크린 리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환 하거나 해당 언어에 적합한 발음을 제공한다. (접근성을 위함)
     - 웹 접근성 : 소수의, 특정한 경우의 사람들과 같은 사람들도 web을 사용하기 때문에 무턱대고 개발하면 안된다.

5. IE는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅 되도록 지정해준다.

   ```html
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   ```

6.  =(equal)을 붙여서 사용 (지키지 않으면 코드가 길어지고 보기 불편)

7. **Semantic Tag**는 태그를 지키지 않아도 동작을 제대로 하지만 규격을 제대로 지키기 위해 사용됨.



**! 입력 한 후, Tap** : 기본 틀 자동 완성

**Ctrl + /** : 주석

**Ctrl + L** : 한줄을 전체 선택

**Alt + Shift + 위,아래 방향키** : 줄이 복사 됨

**Ctrl + Alt + 위, 아래 방향키** : 동시에 여러줄 작성

**Ctrl + Alt + 오른쪽 키** : 멀티창으로 빼냄

##### <~~>을 전부다 쓸 필요 없이 바로 div, span ..쓰고 바로 Enter 이나 Tab 을 치면 된다.



> **ol**  : order list
>
> `<ol>` `<ul>`  : 부모
>
>  `<li>`  : 자식

- lang 을 en에서 ko로 바꾸어 주어야, 구글에서 번역을 할것인지에 대한 창이 뜨지않음.





------



#### :bookmark_tabs:구글 크롬 확장자 (Web Developer)

##### 해당 페이지의 html 구조를 알 수 있다.

![](https://user-images.githubusercontent.com/52684457/62180787-2a6b9e00-b38c-11e9-9c14-4dd0f24852a5.PNG)



##### 사용법)

![](https://user-images.githubusercontent.com/52684457/62180790-2b043480-b38c-11e9-87c7-6d44619c1e28.png)



------



##### :baby_chick:HTML을 하기 전에 . . . (기본 설정)

![](https://user-images.githubusercontent.com/52684457/62180788-2a6b9e00-b38c-11e9-94e9-2386c7243bd4.png)

![](https://user-images.githubusercontent.com/52684457/62180782-29d30780-b38c-11e9-9ce4-b159058ad456.png)

2 space 설정 (HTML은 2space가 규격)

![](https://user-images.githubusercontent.com/52684457/62180789-2b043480-b38c-11e9-8432-6768bd9b02c3.png)

마저 설정해준다.





#### :bookmark_tabs:open in browser  확장자 

##### (code에서 바로 구글크롬을 열어주는 확장자 - 바로바로 확인가능)

![](https://user-images.githubusercontent.com/52684457/62180792-2b043480-b38c-11e9-8a68-9646d3115ede.png)

###### 만약 ctrl + b 가 작동되지 않는다면 . . . 



1) 기본 웹 브라우저를 확인 한다.

![14](https://user-images.githubusercontent.com/52684457/62180793-2b043480-b38c-11e9-8201-5d55e1765327.png)



2) 키 셋팅을 바꿔준다.

![](https://user-images.githubusercontent.com/52684457/62180795-2b9ccb00-b38c-11e9-9f30-cb057c3b8e8f.png)

![](https://user-images.githubusercontent.com/52684457/62180796-2b9ccb00-b38c-11e9-89c8-4d03da30f437.png)



#### :bookmark_tabs:Beautify 확장자

![](https://user-images.githubusercontent.com/52684457/62180780-293a7100-b38c-11e9-9b8b-637c81185f3b.PNG)

단축키 설정

![](https://user-images.githubusercontent.com/52684457/62180781-29d30780-b38c-11e9-9f84-a2ccd6c90e0b.png)





#### :baby_chick:HTML 의 Semantic Tag를 알아보자!

```html
<body>
  <!-- Heading -->
  <h1>Hi, h1!</h1>
  <h2>Hi, h2!</h2>
  <h3>Hi, h3!</h3>
  <h4>Hi, h4!</h4>
  <h5>Hi, h5!</h5>
  <h6>Hi, h6!</h6>

  <!-- bold -->
  <div>
    <b>This is bold.</b>
    <strong>This is strong.(semantic)</strong>
  </div>

  <!-- italic -->
  <div>
    <i>This is italic.</i>
    <em>This is em.(semantic)</em>
  </div>

  <!-- highlighted -->
  <h2>This is <mark>Mark.</mark></h2>

  <!-- del / ins -->
  <h2>This is <del>del.</del></h2>
  <h2>This is <ins>ins.</ins></h2>

  <!-- sub / sup -->
  <h2>This is <sub>sub.</sub></h2>
  <h2>This is <sup>sup.</sup></h2>

  <!-- p / br -->
  <p>
    This is p tag.<br>
    This is p tag.<br>
    This is p tag.<br>
    This is p tag.<br>
    This is p tag.
  </p>
  <pre>
    from flask import flask
    app = Flask(__name__)

    @app.route('/')
    def hello('/'):
      return 'Hello world'
  </pre>

  <!-- headline -->
  <hr>

  <!-- q / blockquote -->
  <p>
    Haein, said <q>Hi there!</q>
  </p>

  <!-- ol / ul / il -->
  <ol>
    <li>first</li>
    <li>second</li>
    <li>third</li>
  </ol>
  <ul>
    <li>first</li>
    <li>second</li>
    <li>third</li>
  </ul>


</body>
```

![](https://user-images.githubusercontent.com/52684457/62180786-2a6b9e00-b38c-11e9-8bd6-2f65d7e5eb5b.png)

------



```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <header>
    <h1>프로그래밍 교육</h1>
    <a href="#python"><img src="images/python.png" alt="python image" style="width: 50px; height: 50px;"></a>
    <a href="#web"><img src="images/html.png" alt="#" width="50px" height="50px"></a>
    <a href="index.html">참고사이트</a>
  </header>
  <hr>
  <article>
    <a href="https://docs.python.org/ko/3/" target="_blank" id="python">파이썬</a></h2>
    <h3>Number tpye</h3>
    <h4>파이썬에서 숫자형은 아래와 같이 있다.</h4>
    <ol>
      <li style="list-style-type: lower-roman">int</li>
      <li style="list-style-type: lower-latin">float</li>
      <li style="list-style-type: lower-greek">compriex</li>
      <li><del>str</del></li>
    </ol>
    <h3>Sequence</h3>
    <h4>파이썬에서 시퀀스는 아래와 같이 있다.</h4>
    <h3>시퀀스는 for문을 돌릴 수 있다!!</h3>
    <ol>
      <li>str</li>
      <li>list</li>
      <li>tuple</li>
      <li>range</li>
    </ol>
  </article>
  <hr>
  <header>
    <h2><a href="https://developer.mozilla.org/ko/" id="web">웹</a></h2>
    <h3>기초</h3>
    <ul>
      <li style="list-style-type: circle">HTML</li>
      <li style="list-style-type: circle">CSS</li>
    </ul>
    <a href="mailto:seasign10@gamil.com">메일보내기</a>
    영상 소스코드 복사 붙여넣기 하면 영상을 올릴 수 있다.
  </header>
</body>

</html>
```



>```html
><li style="list-style-type: ...">ABCD</li>
>```
>
>위의 ...에 다른 단어를 넣어 바꿀 수 있다.
>
>구글 **=>** `CSS list-style-type`
>
>https://www.w3schools.com/cssref/pr_list-style-type.asp
>W3school
>
>
>
>**뒤에 mdn을 추가적으로 검색 하면** => `CSS list style type mdn`
>
>https://developer.mozilla.org/en-US/docs/Web/CSS/list-style
>
>Mozilla (규격과 표준이 좀 더 정확)
>
>
>
>`<a>` 에 대해 **=>** https://www.w3schools.com/tags/tag_a.asp



```html
<a href="#python"><img src="images/python.png" alt="python image" style="width: 50px; height: 50px;"></a>

<a href="#web"><img src="images/html.png" alt="#" width="50px" height="50px"></a>
```

> 위 아래의 코드 두줄은 서로 같은 코드다.
>
> **이미지를 넣는 방법** 
>
> alt - 이미지가 로딩이 되지 않을 때 뜨는 대체 이미지나 글자, 빈 이미지는 #으로 채워 넣는다.
>
> ```html
> <!-- 상대경로 --> 원래의 위치에서 이미지가 있는 폴더로 이동하는 것.
> <ima src="../Image/my_photo.png" alt="#">
>  뒤로가기 한 후(..), 다른 폴더에 접속하는 루트
> <!-- 절대경로 --> ~부터(사용자) 시작하는 것. 대신 위치를 정확히 알고 있어야 한다.
> <ima src="/SSAFY/Image/my_photo.png" alt="#">
> ```



#### :baby_chick:상호작용 하는 HTML의 기본

![](https://user-images.githubusercontent.com/52684457/62194131-2c495780-b3b4-11e9-9659-a7662e3ec383.PNG)



#### :paperclip:<연습 문제 #1>

![](https://user-images.githubusercontent.com/52684457/62193571-f9529400-b3b2-11e9-8c2c-e470cc9dd58e.png)

![](https://user-images.githubusercontent.com/52684457/62193631-230bbb00-b3b3-11e9-8390-7f04342ed42c.png)

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <header>
    <h1>FORM</h1>
  </header>
  <p>주문서를 작성하여 주십시오</p>

  <form action="#">
    <label for="text">이름:</label>
    <input type="text" id="text" placeholder="이름을 입력해주세요"><br>
    <label for="text">날짜:</label>
    <input type="date" id="text"><br>
  </form>

  <h3>1. 샌드위치 선택</h3>
  <form action="#">
    <input type="radio" name="sandwich" value="1" checked>에그마요<br>
    <input type="radio" name="sandwich" value="2">이탈리언 비엠티<br>
    <input type="radio" name="sandwich" value="3">터키 베이컨 아보카도<br>
  </form>
  <hr>
  <h3>2. 사이즈 선택</h3>
  <form action="#">
    <label for="number"></label>
    <input type="number" max="30" min="15" step="15"><br>
  </form>
  <hr>
  <h3>3. 빵</h3>
  <form action="#">
    <select name="bread">
      <option value="1">허니오트</option>
      <option value="2" disabled="">플랫브레드</option>
      <option value="3">하티 이탈리안</option>
    </select><br>
  </form>
  <hr>
  <h3>4.야채/소스</h3>
  <form action="#">
    </select><br>
    <input type="checkbox" name="option" value="1">토마토<br>
    <input type="checkbox" name="option" value="2">오이<br>
    <input type="checkbox" name="option" value="3">할라피뇨<br>
    <input type="checkbox" name="option" value="4">핫 칠리<br>
    <input type="checkbox" name="option" value="5">바베큐
  </form>
  <input type="submit">
</body>

</html>
```



##### 속성값은 따로 설정 하지 않는다 (boolean)

```html
<input type="radio" checked><br> => 안좋은 예 (가이드라인이 맞지 않음)
<input type="radio" ><br> => 올바른 예
```



### :page_facing_up:CSS (cascading)

- styling의 정의 
  - css또한 프로그래밍이 아니며 각자 문법이 다른 별개의 언어 하지만HTML이 없으면 무의미, 독자적이지 않음
  - 대게 마지막에 온 코드가 적용 순위가 높지만, 종류에 따라 다름. (css는 떨어진다는 의미가 있음. 가장 아래에 있는 코드가 적용됨)

###### CSS 활용하기

1. Inline(인라인)
2. Embedding(내부참조)
3. Link file(외부참조)

- 1, 2, 3번 순으로 적용 순위가 강함
  - 그래서 1번을 잘 사용하지 않는다. 다만 강조하고 싶거나 변경되지않기를 원하거나 특수한 경우일 때에만 사용 한다.
  - 컴포넌트화 - 일반적으로 외부파일로서 css를 활용함으로서 모듈화를 선호하기 때문에 3번이 가장 선호된다.

```html
<!-- intro.html -->

<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="00_intro.css">
  <style>
    h2 {
      color: rgb(255, 195, 138);
    }
  </style>
</head>

<body>
  <h1 style="color: rgb(231, 166, 166);">inline css 적용</h1>
  <h2>내부참조, embedding</h2>
  <h3>외부참조, file link</h3>

</body>

</html>
```

```css
<!-- intro.css -->

h3 {
  color: salmon;
}
```



#### 프로퍼티 값의 단위

1. ##### 키워드

2. ##### 크기단위 

   1. (px / 디바이스별로 픽셀의 크기는 제각각 ) => 절대 단위가 아님
   2. %는 백분율 단위의 상대단위. 상대적인 사이즈를 설정.
   3. em 은 배수 단위로 상대 단위이다.(상속의 영향으로 값이 달라질 수 있음) rem은 최상위 요소(html)의 사이즈를 기준으로 삼는다. rem의 r은 root를 의미
   4. Viewport 단위 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 뷰포트를 기준으로 만들어짐 IE지원이 완전하지 않으므로 주의가 필요.

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Unit</title>
     <link rel="stylesheet" href="01_unit.css">
   </head>
   
   <body>
     <h1>단위를 알아보자</h1>
     <p>Default font</p>
    <!-- rem => 24px : 20 * 1.2 -->
     <ol>
       <li>1.2rem</li>
     </ol>
   <!-- em => 28.8px : 20* 1.2 * 1.2 -->
     <ul>
       <li>1.2em</li>
     </ul>
   
     <!-- vw, vh -->
     <span class="vw">10vw</span>
     <span class="vh">10vh</span>
     <div class="div-vw"></div>
     <div class="div-vh"></div>
   
     <!-- vmin -->
     <div class="div-vmin">10vmin</div>
   </body>
   
   </html>
   ```

   ```css
   html {
     font-size: 20px;
   }
   
   ol,
   ol li {
     font-size: 1.2rem;
   }
   
   ul
   ul, li {
     font-size: 1.2em;
   }
   
   .vw {
     font-size: 10vw;
   }
   
   .vh {
     font-size: 10vh;
   }
   
   .div-vw {
     width: 10vw;
     height: 10vw;
     background-color: crimson;
   }
   
   .div-vh {
     width: 10vh;
     height: 10vh;
     background-color: royalblue;
   }
   
   .div-vmin {
     width: 10vmin;
     height: 10vmin;
     background-color: greenyellow;
   }
   ```

   

3. ##### 색상표현 단위

`!import` **>** 인라인 스타일 **>** 아이디 선택자 **>** 클래스 선택자 **>** 태그 선택자 **>** 전체 선택자

아이디는 중복으로 사용하는게 아닌, 하나만 쓰는 것이 원칙. 클래스 선택자는 가능하다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="02_selector.css">
</head>
<body>
  <p>빨간색</p>
  <h1>태그 선택자</h1>
  <h2 class="pink">클래스 선택자</h2>
  <h3 id="green">아이디 선택자</h3>
  <h3 id="green" class="pink">아이디 > 클래스</h3>
  <h1 class="pink">클래스 > 태그</h1>

  <!-- span 태그와 div 태그는 모두 의미는 없지만 '마크업'을 해야
  css를 적용시킬 수 있기 때문에 활용된다. 특정한 곳을 지정해야하고 따라서 선택자가
  필요하게 되고 선택자를 잡기 위해서는 마크업이 필요한 것이다. -->
  <p><span class="pink">핑크핑크,</span><span id="green"> 초록초록</span></p>

  <!-- 클래스는 공백을 기준으로 각각 클래스가 나뉨 -->
  <!-- 아래처럼 pink 가 마지막에 써졌지만, css 코드상으로 yellow가 마지막에 선언되었기
  때문에 노란색으로 적용된다. -->
  <p class="bold yellow pink">노랑노랑</p>

  <p class="bold yellow pink" id="orange" style="color: purple;">가장 강한 우선수위</p>
</body>
</html>
```

```css
/* 전체 선택자 */
* {
  color: red;
}

/* 태그 선택자 */
h1 {
  color: blue;
}

/* 클래스 선택자 */
.pink {
  color: pink;
}

/* 아이디 선택자 */
#green {
  color: green;
}

.bold {
  font-weight: bold;
}

.yellow {
  color: yellow;
}

#orange {
  color: brown !important;
  color: orange;
}
```

- ###### \<el>:nth-child(n)

  - el 태그의 부모의 자식들 중, n번째 자식이 el 이라면 선택! (잘 사용하지 않음)

    p: => p라면 실행 됨. 아닌 경우 선택하지 않음.

- ###### \<el>:nth-of-type(n)

  - el 태그 부모의 자식들 중 el 인 것들 중에서 n번째를 선택! (조금 더 직관적)

    

#### :baby_chick:CSS 스타일 가이드

1. 들여쓰기 2문자
2. 클래스, 아이디명은 케밥 케이스(kebob-case)를 사용한다.
3. 다중 선택 시 한줄에 선택자를 하나씩 작성

```css
.bold,
.yellow,
.bold {
  font-weight: bold;
}
```

4. 모든 스타일 뒤에는 세미콜론을 붙인다.

5. ##### 스타일 지정 시 아이디, 태그 대신에 클래스를 사용한다. (되도록, 대부분)

6. 숫자 0 이후에는 불필요한 단위를 작성하지 않는다.

7. @import 대신 \<link>  방법을 사용한다.

8. 가능한 한 단축어(축약형)를 사용한다. (단, 불필요하게 과용하는 것을 피한다.)

( https://ui.toast.com/fe-guide/ko/ 기준 )





```html
<body>
  <!-- 그룹 선택자 -->
  <p>그룹 선택자</p>
  <h3>그룹 선택자</h3>
  <p>그룹</p>
  <p>그룹</p>

  <!-- 인접 선택자 -->
  <div class="red"></div>
  <div class="blue"></div>
  <div></div>

  <!-- 자식 선택자 -->
  <ol>
    <li>ol 자식 li</li>
  </ol>
  <ol id="chocolate">
    <li>허쉬</li>
    <li>드림카카오</li>
    <li>쿠엔크</li>
  </ol>

  <!-- 자손(후손) 선택자 -->
  <!-- 박스는 왜 생겨요? - css의 위의 div 때문에, -->
  <ul>
    <div>
      <li>자손</li>
      <li>자손</li>
      <li>자손</li>
    </div>
  </ul>

</body>
```

```css
/* 그룹 선택자 */
p,
h3 {
  color: gray;
}

/* div 세팅 */
div {
  width: 100px;
  height: 100px;
  border: 1px solid black;
}

.red {
  background-color: red;
}

.blue {
  background-color: blue;
}

/* 인접 선택자, 바로 붙어있음 */
.red + .blue + div {
  background-color: purple;
}

/* 자식 선택자 인덴트 한칸 차이만 읽을 수 있다.*/
ol > li {
  color: darkgreen;
}

ol#chocolate > li {
  color: chocolate;
}

/* 자손(후손) 선택자 */
ul li {
  color: lime;
}
```



#### :baby_chick:기본 박스모델 활용 

###### top을 10px => top에 10px만큼의 공간을 준다는 의미. (위로 10xp옮겨간다는 뜻이 X)

![](https://user-images.githubusercontent.com/52684457/62263051-cad9c500-b455-11e9-82e5-085125efeb51.png)

> ###### 개수에 따른 적용 순서
>
> 상하좌우 : 1개
>
> 상하 > 좌우 : 2개
>
> 상 > 좌우 > 하 : 3개
>
> 상 > 우 > 하 > 좌 :4개

##### emmet 

- https://docs.emmet.io/abbreviations/syntax/
- https://docs.emmet.io/cheat-sheet/



![](https://user-images.githubusercontent.com/52684457/62263258-771bab80-b456-11e9-8026-1cd33cc1f0bb.png)

개발자 확장자 (F12)를 사용하여 자세한 정보를 보거나 코드를 수정해서 바로바로 확인 할 수 잇다.

- 하지만 새로고침(F5)을 사용하면 원래대로 돌아오는 형식



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="04_box_model.css">
</head>
<body>
  <!-- div>ol>li*3 + Tab -->
  <!-- div#apge>(header>ul.first>li.item$$@3{hi,there}*5>a{link})+footer>p>lorem10 -->
  <!-- lorem10 - 10글자를 생성 -->
  <div>div</div>
  <!-- .margin.padding == div.margin.padding -->
  <div class="margin padding">margin</div>
  <!-- div는 오른쪽 끝공간을 다 잡아먹고 있음, span은 아님. -->
  <div class="padding">padding</div>
  <div class="border">border</div>

  <!-- .margin-shorthand-$@1*4 -->
  <div class="margin-shorthand-1"></div>
  <div class="margin-shorthand-2"></div>
  <div class="margin-shorthand-3"></div>
  <div class="margin-shorthand-4"></div>

  <!-- .ailing-center -->
  <div class="aling-center"></div>
  <div class="aling-right"></div>


</body>
</html>
```

```css
div {
  color: white;
  width: 100px;
  height: 100px;
  background-color: gray;
}

.margin {
  margin-top: 30px;
  margin-bottom: 30px;
  margin-left: 10px;
  margin-right: 10px;
}

.padding {
  padding-top: 30px;
  padding-bottom: 30px;
}

.border {
  border-width: 5px;
  border-style: dotted;
  border-color: red;
  border-top-color: blue;
  border-radius: 10px;
  /* border: 5px dotted red; */
}

.margin-shorthand-1 {
  /* 상하좌우 */
  margin: 10px;
}

.margin-shorthand-2 {
  /* 상하 > 좌우 */
  margin: 10px 20px;
}

.margin-shorthand-3 {
  /* 상 > 좌우 > 하 */
  margin: 10px 20px 30px;
}

.margin-shorthand-4 {
  /* 상 > 우 > 하 > 좌 */
  margin: 10px 20px 30px 40;
}

/* 마진 상쇄 => 위 아래 마진px이 겹치면서 10px + 10px = 20px이 아니라,
위아래 마진이 겹치면서 10px 그대로 나타나는 것. */




/* 가운데 정렬 */
.aling-center {
  /* 오른쪽, 왼쪽에 반반 나눠준다. 0인 경우에는 단위를 안 써주는 것이 좋다.*/
  margin: 0 auto;
}

/* 오른쪽 정렬 */
.aling-right {
  /* 오른쪽으로 남은 너비를 왼쪽으로 보낸다. (붙인다.) */
  /* 왼쪽에 남은 너비를 붙인다. 오른쪽에있던 공간을 왼쪽으로 넘겨버리는 것. */
  margin-left: auto;
}

```

![](https://user-images.githubusercontent.com/52684457/62263045-c7463e00-b455-11e9-8ce0-21bba5eb3ada.png)

```html
 <div class="box-sizing content-box">
    <p>content-box</p>
  </div>
  <div class="box-sizing border-box">
    <p>border-box</p>
  </div>
```

```css
/* box-sizing */

.box-sizing {
  margin: 20px;
  padding: 20px;
  border: 10px solid red;
  width: 300px;
}

.content-box {
  box-sizing: content-box;

}

.border-box {
  box-sizing: border-box;
}
```

###### 대게 보더박스로 설정을 한 후 개발을 하는 경우가 많음.



> ###### block
>
> 항상 새로운 라인에서 시작한다.
>
> 화면 크기 전체의 가로폭을 차지한다.  *width : 100%*
>
> 너비가 정해지면 나머지를 margin으로 처리한다.
>
> 
>
> ###### inline
>
> 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.
>
> content의 너비만큼 가로폭을 차지한다.
>
> 프로퍼티를 지정할 수 없는 치명적인 부분이 있지만 상, 하 여백은 line-height로 설정할 수 있다.
>
> 
>
> ###### inline-block
>
> 인라인의 너비를 조정할 수 없는 단점을 보안하여 블락과 인라인 레벨 요소의 특징을 모두 갖는다.
>
> 한줄에 표시 되면서 블럭의 속사을 모두 사용할 수 있다.
>
> 
>
> ###### None
>
> 해당 요솔르 화면에 표시하지 않는다. ( <u>공간조차 사라진다.</u> ) => 공간을 가린다는 개념이 X

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="05_display.css">
</head>

<body>

  <!-- block -->
  <h1>display</h1>
  <h2>block</h2>
  <p>display: block은
    기본적으로 가질 수 있는 영역의
    100%를 갖는다!</p>
  <p>h1~6, p, div, form, table, ol, ul, li...</p>
  <div>block</div>
  <form action="">폼을 작성해 주세요.</form>

  <!-- block 가로정렬 -->
  <div class="ml-auto">ml-auto</div>
  <div class="mr-auto">mr-auto</div>
  <div class="mx-auto">mx-auto</div>

  <!-- inline -->
  <h2>inline</h2>
  <span class="red">inline은 content 영역만큼</span>
  <span>너비를 가진다.</span>
  <input type="text">
  <input type="date" name="" id="">
  <a href="#">링크</a>
  <img src="#" alt="img">

</body>

</html>
```

```css
div {
  width: 100px;
  height: 100px;
  background-color: crimson;
  color: white;
  line-height: 100px;
  text-align: center;
}

/* 오른쪽 정렬 */
.ml-auto {
  /* 왼쪽에 남은 너비를 붙인다. */
  margin-left: auto;
}

/* 왼쪽 정렬 */
.mr-auto {
  margin-right: auto;
}

/* 가운데 정렬 */
.mx-auto {
  margin: 0 auto;
}

.red {
  color: red;
}
```

- visible
  - hidden - 해당 요소를 안 보이게 할뿐 사라지는 것은 아니다. (영향을 주지 않음.)

###### 숫자 0 이후에는 불필요한 단위를 작성하지 않는다.

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="06_display.css">
</head>

<body>
  <div>block</div>
  <div>block</div>

  <!-- inline -->
  <!-- 내용없이 존재 할 수 없음.
  (width, height 적용불가) -->
  <div class="inline">안녕하세요??</div>
  <div class="inline">저는 내용영역이 필요해요!</div>


  <!-- inline-block -->
  <!-- block 속성(width, height)
  + inline 속성 (우측 margin이 사라짐) -->
  <div class="inline-block">i-b</div>
  <div class="inline-block">i-b</div>

  <!-- display: none; 공간조차 사라짐
  visibility: hidden 공간은 유지 -->
<div>div</div>
<div class="none">none</div>
<div class="hidden">hidden</div>
<div>div</div>

<!-- opacity 요소의 투명도를 정한다. -->
<div class="opacity">div</div>




</body>

</html>
```

```css
div {
  width: 100px;
  height: 100px;
  color: white;
  background-color: crimson;
  text-align: center;
  line-height: 100px;
}

.inline {
  display: inline;
}

.inline-block {
  display: inline-block;
}

.none {
  display: none;
}

.hidden {
  visibility: hidden;
}

.opacity {
  opacity: 0.5;
}
```





#### Background

고화질 사진 참고 사이트 : https://unsplash.com/

- 이 외 :

  https://www.pexels.com/
  https://pixabay.com/
  https://web.500px.com/
  http://gratisography.com/
  https://www.splitshire.com/
  https://littlevisuals.co/
  https://nos.twnsnd.co/
  https://magdeleine.co/browse/ 

구글에서 **css reset** 검색 => 완전 백지상태에서 css를 만지는 방법의 코드 (기본값들을 완전히 초기화)



> ######  cover 
>
> - 배경이미지의 크기 비율을 유지한 상태에서 부모 요소의 sidth, height중 큰 값에 배경 이미지는 맞춘다. 따라서 이미지의 일부가 보이지 않을 수 있다.
>
> ###### contain
>
> - 배경이미지의 크기 비율을 유지한 상태에서 부모 요소의 영역에 배경이미지가 보이지 않는 부분까지 전체가 들어갈 수 있도록 이미지 크기를 조절한다.
>
> ###### attachment: fixed
>
> - 화면이 스크롤 되더라도 배경 이미지는 스크롤 되지 않고 고정시킨다.

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="07_background.css">
</head>

<body>
 
  <div class="bg-box"></div>
  
</body>

</html>
```

```css
*,
*:after,
*:before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  width: 100%;
  height: 100%;
}

/* 위는 기본 셋팅 무시 */
.bg-box {
  height: 100%;

  /* background-image */
  background-image: url("images/image.jpg");

  /* background-size */
  /* background-size: 700px 500px; */
  background-size: cover;
  /* background-size: contain; */

  /* background-repeat */
  background-repeat: no-repeat;
  
  background-position: 0, 0;
  background-position: center;

  /* background-attachment */
  background-attachment: fixed;
}
```

>   background-size: cover;
>
>   background-position: center;
>
> - 배경을 넣을 때 기본적으로 입력하면 깔끔하게 나오는 코드.



폰트 공유 : https://fonts.google.com/?subset=korean

###### @import 대신 \<link>  방법을 사용한다. 그리고 영어 font를 제공하는것이 더 많다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="08_font_text.css">
  <link href="https://fonts.googleapis.com/css?family=Song+Myung&display=swap" rel="stylesheet">
</head>

<body>
  <p>default font size: 16px</p>
  <!-- p.font-$@1{This is font $@1}*5 -->
  <p class="font-1">This is font 1</p>
  <p class="font-2">This is font 2</p>
  <p class="font-3">This is font 3</p>
  <p class="font-4">This is font 4</p>
  <p class="font-5">This is font 5</p>

  <div class="box">
    <p>PYTHON</p>
  </div>
  
  <p class="web-font">가나다라마바사</p>



  
</body>
</html>
```

```css
.font-1 {
  font-size: 30px;
  font-family: 'Courier New', Courier, monospace;
  font-style: italic;
}

.font-2 {
  font-size: 2rem;
  font-family: 'Times New Roman', Times, serif;
  font-weight: lighter;
}

.font-3 {
  font-size: 130%;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
}

.font-4 {
  font-size: small;
  font-weight: 700;
}

.font-5 {
  /* font shorthand */
  /* font: font-style font-weight line-height font-size(필수) font-family(필수) */
  font: italic 2rem "Hack";

}

.box {
  width: 100px;
  height: 100px;
  background-color: crimson;
  color: white;
}

.box > p {
  text-align: center;
  /* line-height를 부모의 height 만큼 주면
  텍스트를 수직 중앙 정렬 하기에 용이하다. (단, 텍스트가 한 줄인 경우에) */
  line-height: 100px
}

.web-font {
  font-family: 'Song Myung', serif;
}
```



![](https://user-images.githubusercontent.com/52684457/62271905-c07af380-b474-11e9-9699-a23222c5334b.PNG)

Korean을 설정해주어야 제대로 작동하는 경우가 많다.