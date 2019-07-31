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



#### :page_facing_up:HTML

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

