

# :yellow_heart: JS : Vue(axios)

- JS의 비동기적 시스템을 적용

![image](https://user-images.githubusercontent.com/52684457/68275637-95292580-00af-11ea-8644-d1406610764a.png)

- 들어가기 앞서 이 설정을해두면 저장할때마다 (ctrl+s) 자동으로 코드를 정리해준다.

### XMLHttpRequest (XHR)

- 브라우저는 XMLHttpRequest 객체를 이용하여 Ajax 요청을 생성하고 전송
- 서버가 브라우저의 요청에 대해 응답을 반환하면 같은 XHR 객체가 그 결과를 처리
- 단, IE5, 6에서는 ActiveXobject를 사용해야 한다.



`return JsonResponse(context)`

- 기존 redirext 로 인해 index.html로 페이지가 로딩되는 것이 아닌 JSON 상태로 응답결과를 반환 받기로 변경 (*boolean 값이 필요하기 때문에 True와 Flase값을 변수에 담아 할당*)
- JSON 데이터에 liked 변수를 만들어서 template 에서 좋아요를 취소할지 추가할지를 판단 할 수 있도록 한다.
- True False 값을 통해 좋아요 버튼의 style 값을 변경한다.

###### _article.html

```django
<p class="card-text">
      {% if user in article.like_users.all %}
        <i class="fas fa-heart like-button" style="color: crimson;" data-id="{{ article.pk }}"></i>
      {% else %}
        <i class="fas fa-heart like-button" style="color: black;" data-id="{{ article.pk }}"></i>
      {% endif %}
      <span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span>명이 이 글을 좋아합니다.
    </p>
```

- `data-id` 는 js에서 지정해준 값이므로 바꾸어 사용할 수 없다.

![image](https://user-images.githubusercontent.com/52684457/68096266-fc4dab00-fef2-11e9-988d-b9728d2cf3df.png)

- 색상을 변경하기 위해서 event를 console 찍어본다.

- `event.target.style.color` 경로에 색상을 변경해주면 색상 값을 설정할 수 있다.

![image](https://user-images.githubusercontent.com/52684457/68096476-58fd9580-fef4-11e9-9fc8-5387e95edf81.png)

- redirect 가 아닌 like 값만 비동기식으로 받는 것을 확인 할 수 있다.
  *redirect는 페이지를 전체적으로 다시 불러오기 때문에 비효율 적*
- 하지만 count를 처리하지 않았기 때문에 count를 따로 설정해주어야 한다.

###### views.py

```python
@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        liked = False
        else:
            article.like_users.add(request.user)
            liked = True
            context = {'liked': liked, 'count': article.like_users.count(),}
            return JsonResponse(context)
```

- `'count': article.like_users.count(),` context에 추가
- _article.html 에서`{{ article.like_users.all|length }}` 구문을 `<span id="like-count-{{ article.pk }}">`  span태그로 담아 id값을 준다.



[`headers: {'X-Requested-With': 'XMLHttpRequest'},`](https://github.com/axios/axios#request-config)

[Global axios defaults](https://github.com/axios/axios#global-axios-defaults)

```python
@login_required
def like(request, article_pk):
    if request.is_ajax(): # 일반요청? ajax 요청? 구분 구문
        article = get_object_or_404(Article, pk=article_pk)
        # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속유저가 있다면 좋아요를 취소
        if article.like_users.filter(pk=request.user.pk).exists():
            # .get()은 없을 때 오류가 발생하므로 키가 없어도 오류(DoesNotExistError) 발생을 막기 위해 .filter()를 사용한다.
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True
        # if request.user in article.like_users.all():
        #     article.like_users.remove(request.user) # 좋아요 취소
        # else:
        #     article.like_users.add(request.user) # 좋아요 선택
        # return redirect('articles:index')
        context = {'liked': liked, 'count': article.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()
```

- 위의 공식문서 링크를 통하여 django가 ajax 값을 제대로 인식 할 수 있도록 설정 해줄 것



###### index.html

```python
axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
```

- 이 구문을 좋아요 요청 전에 삽입

```django
...
{% for article in articles %}
    {% include 'articles/_article.html' %}
  {% endfor %}
  <script>
    // 1. 각 게시글별로 좋아요 버튼이 있으니 모두 선택해야 한다.
    const likebuttons = document.querySelectorAll('.like-button')

    // 2. forEach를 사용해서 각각의 좋아요 버튼을 클릭
    likebuttons.forEach(button => {
      button.addEventListener('click', function (event) {
        // 항상 처음에는 console로 function의 인자를 찍어보고 어디로 들어가야 하는지 반드시 파악하자
        // console.log(event)

        // event.target.dataset.id 의 value는 data-id 값이 들어 있다.
        const articleId = event.target.dataset.id // 이와 같이 사용하기 위해 console로 찍어서 경로를 확인해야 한다!
        // headers: {'X-Requested-With': 'XMLHttpRequest'},
        axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(`/articles/${articleId}/like/`) // 해당 상세 게시글의 좋아요 요청을 보낸다.(url주소는 urls.py 참고)
          .then(response => {
            // console.log(response) // 반드시 console로 먼저 확인
            document.querySelector(`#like-count-${articleId}`).innerText = response.data.count
            if (response.data.liked) {
              // 좋아요 색깔을 빨갛게
              event.target.style.color = 'crimson'
            } else {
              // 좋아요 색깔을 까맣게
              event.target.style.color = 'black'
            }
          })
          .catch(error => console.log(error)) // error catch 구문, 반드시 console로 먼저 확인)
      })
    })
  </script>
{% endblock  %}
```





## :large_blue_circle: VUE [공식 홈페이지](https://kr.vuejs.org/v2/guide/index.html)

![image](https://user-images.githubusercontent.com/52684457/68097501-b1d02c80-fefa-11e9-90cd-d91b43019ca4.png)

##### extention(확장자 설치)

![image](https://user-images.githubusercontent.com/52684457/68097333-db3c8880-fef9-11e9-83b0-f81dfc19caf0.png)

![image](https://user-images.githubusercontent.com/52684457/68097349-f3140c80-fef9-11e9-95e8-a5b37acc2384.png)

- Vetur가 선행설치되어있어야한다.

###### CDN 추가

공식홈페이지 참조

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```



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
  <div id="app">
    {{ message }} <!-- interpolation: 보간법 -->
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app', // element 지정, Vue 인스턴스와 binding
      data: {// vue 인스턴스의 속성: data / 속성, 정보를 나타냄
        message: 'Hello Vue!'
      }
    })
  </script>
</body>
</html>
```



![image](https://user-images.githubusercontent.com/52684457/68099979-daf7b980-ff08-11e9-991b-8874dd95816b.png)

- console 창 에서 값을 바로 바꿀 수 있다.
- html은 껍데기 역할, script가 알맹이 역할을 할 것



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
  <input type="text" id="js-input">
  <p id="js-p"></p>

  <script>
    const input = document.querySelector('#js-input')
    input.addEventListener('keydown', function (e){
      const value = e.target.value
      document.querySelector('#js-p').innerText =value
    })
  </script>
</body>
</html>
```

![image](https://user-images.githubusercontent.com/52684457/68100106-7a1cb100-ff09-11e9-9738-274aa4377a9c.png)

- 하나가 밀려 쓰여지는 동작이 확인된다. (바로 동기화가 안되기 때문)



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
  <h3>JS</h3>
  <input type="text" id="js-input">
  <p id="js-p"></p>

  <h3>Vue</h3>
  <div id="app">
    <input type="text" id="vue-input" v-model="message">
    <p id="vue-p">{{ message }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const input = document.querySelector('#js-input')
    input.addEventListener('keydown', function (e) {
      const value = e.target.value
      document.querySelector('#js-p').innerText = value
    })

    // Vue
    const app = new Vue({
      el: '#app', // div선택
      data: {
        message: ''
      }
    })
  </script>
</body>

</html>
```



![image](https://user-images.githubusercontent.com/52684457/68100227-3a09fe00-ff0a-11e9-8923-c13391768b6a.png)

- Vue는 바로바로 검색되어 입력되는 것을 확인 할 수 있다.
  (*JS와 Vue의 차이*)



#### :large_blue_diamond: [Vue Chrome Extention](https://github.com/vuejs/vue-devtools#installation)

![image](https://user-images.githubusercontent.com/52684457/68100317-cae0d980-ff0a-11e9-9c7b-477d0e7ca150.png)

- `12F` **=>** Vue

![image](https://user-images.githubusercontent.com/52684457/68100342-ec41c580-ff0a-11e9-94c5-0f8364656861.png)

- 제대로 실행 된 모습



## :large_blue_circle: Vue 인스턴스 옵션

###### el

- Vue 인스턴스와 DOM을 연결(마운트, mount) 하는 옵션
- View - View Model 을 연결 시킨다.
- HTML 의 id나 class 와 마운트 가능



###### data

- Vue 인스턴스의 데이터 객체, 인스턴스의 `속성` 이라고도 부름
- 데이터 객체는 반드시 기본 객체 `{}` 여야 한다.
- 객체 내부의 아이템들은 value 로써 모든 타입의 객체를 가질 수 있다. (object, string, interger, array...)
- 정의된 속성은 인터폴레이션 `({{ }})` 통해서 View 에서 렌더링 가능

- data 에서도 이벤트리스터와 비슷한 이유로 화살표 함수를 작성해서는 안된다.



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
  {{ message }} <!-- 속성을 받지 못하는 구간 -->
  <div id="app">
    {{ message }} - {{ count }}
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app', 
      data: { 
        message: 'Hello Vue!',
        count: 0,
      }
    })

    app.message === app.$data.message // 오른쪽이 좀더 명확히 명시할 수 있기 때문에 선호되는 편, 다른 name과 겹치거나 사용하면 안되는 name을 사용되는것을 방지하기 위함
  </script>
</body>
</html>
```



###### methods

- Vue 인스턴스에 추가할 메서드들을 정의하는 곳

:warning: **메소드를 정의하는데에 화살표 함수를 사용해서는 안 된다.**



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
  <div id="app">
    {{ message }} - {{ count }} <!-- interpolation: 보간법 -->
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app', // element 지정, Vue 인스턴스와 binding
      data: { // vue 인스턴스의 속성: data / 속성, 정보를 나타냄
        message: 'Hello Vue!',
        count: 0,
      },
      methods: {
        // 표현식
        plus: function() {
          this.count++ // Vue instance 내에서는 data 내의 값들에 this 로 접근 가능
        },
        // 선언식
        minus() {
          this.count--
        }
      }
    })

    
  </script>
</body>
</html>
```

- `app.message === app.$data.message` 
  오른쪽이 좀더 명확히 명시할 수 있기 때문에 선호되는 편, 다른 name과 겹치거나 사용하면 안되는 name을 사용되는것을 방지하기 위함



```javascript
plus: () => {
    this.count++
},
```

- arrow function 으로 접근하게 되면...

![image](https://user-images.githubusercontent.com/52684457/68100790-55c2d380-ff0d-11e9-80f8-eb91321c4f6d.png)

- 값이 적용되지 않는다.



****

###### `arrow function` VS `function`

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
  <button id="function">function</button>
  <button id="arrow">arrow function</button>
  <script>
    const functionButton = document.querySelector('#function')
    const arrowButton = document.querySelector('#arrow')

    functionButton.addEventListener('click', function(event) {
      console.log('=====function=====')
      console.log(this)
    })

    arrowButton.addEventListener('click', event => {
      console.log('=====arrow function=====')
      console.log(this)
    })
  </script>
</body>
</html>
```

![image](https://user-images.githubusercontent.com/52684457/68100926-2e203b00-ff0e-11e9-83d5-8c5186f7a514.png)

****



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
  <div id="app">
    {{ message }} - {{ count }} <!-- {{}} : interpolation(보간법) -->
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app', // element 지정, Vue 인스턴스와 binding
      data: { // vue 인스턴스의 속성: data / 속성, 정보를 나타냄
        message: 'Hello Vue!',
        count: 0,
      },
      methods: {
        // 표현식
        plus: function() {
          this.count++ // Vue instance 내에서는 data 내의 값들에 this 로 접근 가능
        },
        // 선언식
        minus() {
          this.count--
        }
      }
    })

    // 1. window : 함수 호출(전역), 함수 내 함수 => winodw
    const greeting = function() {
      console.log(this)
    }

    greeting()

    // 2. 메서드 호출 => 해당 객체
    const you = {
      name: 'lee',
      greeting
    }

    you.greeting() // {name: "lee", greeting: f} : this 는 해당 오브젝트(객체)

    // 3. arrow : 함수 내 함수 => 해당 객체
    // arrow 에서의 this 는 호출 위치와 상관없이 상위 스코프 this를 가리킨다.
    // 따라서, 메소드 선언을 arrow 함수로 하게 되면, 해당 오브젝트의 상위 스코프인 전역객체 winodw 가 바인딩 된다.

    const arrowGreeting = () => console.log(this)
    const me = {
      name: 'tak',
      arrowGreeting
    }
    arrowGreeting()    // window
    me.arrowGreeting() // window

    // 그렇다면 arrow 를 언제 활용하는 것이 좋은가? - 함수 내의 함수! 
    const num = {
      numbers: [1],
      print: function() {
        console.log(this) // num 객체 (첫번째 객체가 window)
        console.log(this.numbers) // [1]
        this.numbers.forEach(function(num) {
          console.log(num) // 1
          console.log(this) // window
          // 이 상황에서는 window가 호출되기 때문에 지정 값을 부르기가 힘들어진다.
        })
      }
    }

    num.print()

    const num2 = {
      numbers: [1],
      print: function() {
        console.log(this) // num2 객체
        console.log(this.numbers) // [1]
        this.numbers.forEach(num => { // method를 호출 할때에는 arrow function
          console.log(num) // 1
          console.log(this) // num2 (이것 때문에 arrow 사용!)
        })
      }
    }

    num2.print()

    // 이벤트 리스너로 돌아와서
    // 이벤트 리스너에서의 콜백 함수는 특별하게 function 키워드의 경우에는 이벤트 리스너를 호출한 대상(즉, event.target)을 뜻한다.
    // 따라서, 호출한 대상을 원하면 this 를 사용할 수 있다.
    // 다만 arrow function에 경우 상위 스코프를 지칭하기 때문에 window 객체가 출력된다.

  </script>
</body>
</html>
```



## :large_blue_circle: Vue derective (지시문)

- 디렉티브는 `v-` 접두사가 있는 특수 속성(attr) 이며, 디렉티브 속성의 값은 단일 JS표현식

###### `v-for`

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

  <div id="app">
    <li v-for="todo in todos"> <!-- element 반복문 -->
      {{ todo }}
    </li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({ // instance 생성
      el: '#app', // mount, vue와 vue모델 연결
      data: {
        todos: [ // array 형식으로 만들어 보자
          '점심 메뉴 고민',
          '사다리 타기',
          '낮잠 자기',
          '야자 하기',
        ]
      }
    })
  </script>
</body>

</html>
```

![image](https://user-images.githubusercontent.com/52684457/68101988-f5836000-ff13-11e9-9f8f-c7c43ca9815c.png)

###### `v-if`

- 특정 조건을 만족할 때만 보여지도록(랜더링 되도록)할 수 있다.
- `v-else`는 반드시 v-if 엘리먼트 바로 뒤에 와야 인식 가능
- `v-else-if` 도 존재

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

  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed"> <!-- 특정조건일 때만 랜더링 되도록, flase 인 것만 나타내기 ! 를 붙이면 조건구문이 반대가 된다. -->
      {{ todo.content }}
      <!-- {{ todo.completed }} -->
    </li>
    <li v-else><s>{{ todo.content }}</s>[완료!]</li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({ // instance 생성
      el: '#app', // mount, vue와 vue모델 연결
      data: {
        todos: [
          { // 각각 객체화를 시켜보자.
            content: '점심 메뉴 고민',
            completed: true,
          },
          {
            content: '사다리 타기',
            completed: false,
          },
          {
            content: '낮잠 자기',
            completed: false,
          },
          {
            content: '야자 하기',
            completed: false,
          },
        ]
      }
    })
  </script>
</body>

</html>
```

![image](https://user-images.githubusercontent.com/52684457/68102493-56ac3300-ff16-11e9-8d0c-e098ce72d962.png)



#### 우선 순위

- 동일한 노드에서는 v-for가 v-if 보다 높은 우선순위를 가짐
- 즉, v-if는 루프가 반복 될 때마다 실행! (*일부 항목만 렌더링 할 때 유용하다.*)



###### `v-on`

- JS 에서 이벤트리스터랑 비슷한 역할
- 이벤트 리스터는 HTML element 를 querySelector 로 가져와 이벤트를 붙여줬다면, Vue 는 HTML element 자체에 이벤트를 붙여준다.
- `v-on:` 뒤에 오는 친구를 `전달 인자` 라고 한다.
- `:` 을 붙여 사용하는, 디렉티브 바로뒤에 붙는 친구들을 지칭



![image](https://user-images.githubusercontent.com/52684457/68102376-b950ff00-ff15-11e9-92bf-764a87a9a99b.png)

1. ##### inline 방식

```html
<!DOCTYPE html>
...
<body>

  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="todo.completed = true"> 
      {{ todo.content }}
    </li>
    <li v-else><s>{{ todo.content }}</s>[완료!]</li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
	...
```

2. ##### method 정의

```html
<body>

  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)"> 
      {{ todo.content }}
    </li>
    <li v-else><s>{{ todo.content }}</s>[완료!]</li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({ // instance 생성
      el: '#app', // mount, vue와 vue모델 연결
      data: {
        todos: [
          {
            content: '점심 메뉴 고민',
            completed: true,
          },
          {
            content: '사다리 타기',
            completed: false,
          },
          {
            content: '낮잠 자기',
            completed: false,
          },
          {
            content: '야자 하기',
            completed: false,
          },
        ]
      },
      methods: {
        check: function(todo) {
          todo.completed = true
        }
      }
    })
  </script>
</body>
```



- false를 true 값으로 바꾸었다면 거꾸로 true를 false로 바꾸기 위해서는?

```html
  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)"> 
      {{ todo.content }}
    </li>
    <li v-else v-on:click="check2(todo)"><s>{{ todo.content }}</s>[완료!]</li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        todos: [
		...
        ]
      },
      methods: {
        check: function(todo) {
          todo.completed = true
        },
        check2: function(todo) {
          todo.completed = false
        },
      }
    })
  </script>
```

- v-else 에도 method를 넣어준다.

```html
  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)"> 
      {{ todo.content }}
    </li>
    <li v-else v-on:click="check(todo)"><s>{{ todo.content }}</s>[완료!]</li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
	...
      methods: {
        check: function(todo) {
          todo.completed = !todo.completed
        },
        // check2: function(todo) {
        //   todo.completed = false
        // },
      }
    })
  </script>
```

- `todo.completed = !todo.completed` 서로 반대의 속성을 가지게 해주면 조금더 간략하게 할 수 있다.



###### `v-bind`

- HTML element의 속성 값을 변경할 때 사용

```html
<body>

  <div id="app">
    <img v-bind:src="vueImage" alt="todo-list" width="400px">
	...
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app', 
      data: {
        todos: [
			...
        ],
        vueImage: 'https://user-images.githubusercontent.com/52684457/68103171-0c788100-ff19-11e9-890b-07f2bbadb9da.png'
      },
      methods: {
        check: function(todo) {
          todo.completed = !todo.completed
        },
      }
    })
  </script>
</body>

</html>
```

**shortcut =>** ``<img v-bind:src="vueImage"`
 **=>**`<img :src="vueImage"`
`v-bind` 생략 가능



****

#### :dog::cat: dogs & cats

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    img {
      width: 300px;
      height: 300px;
    }
  </style>
</head>

<body>
  <div id="app">
  <button v-on:click="getDogImage">멈머</button>
  
  <!-- <button id="cat">냐냐</button> -->
  <button v-on:click="getCatImage">냐냐</button>
  <hr>
  <!-- <div class="animals"></div> -->
  <!-- <img v-bind:src="image" alt="img"> -->
  <span v-for="image in images"> <!-- 사진이 아래로 정렬 : div(block 속성) / 사진이 옆으로 정렬 : span(inline 속성) -->
    <img v-bind:src="image" alt="img" v-if="image">
  </span>
</div>

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

  <script>
    const app = new Vue({
      el: '#app',
      data: {
        // image: '', // 데이터를 요청 받을 때 마다 새로운 사진을 받으려면 구문이 돌 때마다 빈 스트링
        images: [],
      },
      methods: {
        getDogImage: function() { // 객체로 들어가는 것이기 때문에 :(콜론)
        const URL = 'https://dog.ceo/api/breeds/image/random'
        axios.get(URL)
          .then(response => { // function을 사용하면 this가 window가 선택되기 때문에(함수안의 함수) arrow function 사용
          // 같은 인스턴스 안에 data 내의 속성 값은 this 키워드를 통해서 접근
            // this.image = response.data.message
            this.images.push(response.data.message)
          })
        },
        
        getCatImage: function() { 
        const URL = 'https://api.thecatapi.com/v1/images/search'
        axios.get(URL)
          .then(response => {
            // this.image = response.data[0].url
            this.images.push(response.data[0].url)
          })
        }
      }
    })

    // // 이전의 코드 (getCatImage)
    // const getCatImage = function() {
    //   axios.get('https://api.thecatapi.com/v1/images/search')
    //     .then(response => { 
    //       const imgUrl = response.data[0].url
    //       const imgTag = document.createElement('img')
    //       imgTag.src = imgUrl
    //       document.querySelector('.animals').append(imgTag)
    //     })
    //     .catch(error => console.log(error))
    // }

    // // 사진이 나오는 버튼 만들기
    // const catButton = document.querySelector('#cat')
    // catButton.addEventListener('click', getCatImage)

  </script>
</body>

</html>
```

****





```html
  <script>
    // 함수를 바깥에 빼낼 수도 있다.
    const dog = function() { 
        const URL = 'https://dog.ceo/api/breeds/image/random'
        axios.get(URL)
          .then(response => { 
            this.images.push(response.data.message)
          })
        }

    const app = new Vue({
      el: '#app',
      data: {
        images: [],
      },
      methods: {
        getDogImage: dog,
        getCatImage:
          ...
          })
        }
      }
    })
```



###### `v-model`

- input tag의 value - **View** <==> v-model <==> data(**VM**)



```html
    <footer>
      <button v-on:click="clearCompleted">Clear</button>
    </footer>
  </div>
```

- 삭제 버튼은 div안에 만들어 주어야 div에 바인딩된 모델을 인식할 수 있다.



```vue
vue.js:634 [Vue warn]: Error compiling template:

style="{{ activeColor }}": Interpolation inside attributes has been removed. Use v-bind or the colon shorthand instead. For example, instead of <div style="{{ val }}">, use <div :style="val">.

1  |  <div id="app">
2  |      <div style="{{ activeColor }}"></div>
   |           ^^^^^^^^^^^^^^^^^^^^^^^^^
```

- vue에서 수정사항 오류를 알려준다.

```html
  <title>Document</title>
  <style>
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>
	...
	<div v-for="todo in todos" v-bind:class="{ completed: todo.completed }"> 
```

- `{{}}` 가 아닌 `{}` 사용
- `v-bind`를 class 앞에 추가



```html
<div id="app">
    <select v-model="status">
      <option value="all" selected>all</option>
      <option value="active">active</option>
      <option value="completed">completed</option>
    </select>
	...
        <div v-for="todo in todosByStatus()" v-bind:class="{ completed: todo.completed }"> 
	...
```

- `todosByStatus()` 를 사용해주어야 상태값이 적용된 값을 가져올 수 있다.



```js
>app.status
"all"

>app.todosByStatus()
(4) [{…}, {…}, {…}, {…}, __ob__: Observer]
0: {__ob__: Observer}
1: {__ob__: Observer}
2: {__ob__: Observer}
3: {__ob__: Observer}
length: 4
__ob__: Observer {value: Array(4), dep: Dep, vmCount: 0}
__proto__: Array

>app.status = "completed"
"completed"

>app.todosByStatus()
[{…}]
0: {__ob__: Observer}
length: 1
__proto__: Array(0)
```

- 해당 객체만 출력되는 것을 확인 가능



```js
addTodo: function() {
          if (this.newTodo.length !==0)
...
```

- 빈 값일때에도 값이 추가 되는 것을 방지



###### `computed`

- 미리 계산된 값을 반환
- 종속 대상을 따라 저장(캐싱)되는 특성이 있다.
- 연산이 많이 필요한 경우 템플릿 안에서 연산 표현식을 사용하는 것 보다 computed를 사용하는 것을 권장
- `{{ newTodo.split('').reverse().join('') }}`

```vue
computed: {
    reversedNewTodo: function() {
		return this.newTodo
	}
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
</head>
<body>
  
  <div id="app">
    <button v-on:click="visible = !visible">TOGGLE</button>
    <ul v-if="visible"> <!-- true일 때에만 보이도록 -->
      <li>Method : {{ dateMethod() }}</li>
      <li>Computed : {{ dateComputed }}</li>
    </ul>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        visible: true,
      },
      methods: { // 호출 할때마다 계산
        dateMethod: function() {
          return new Date()
        }
      },
      computed: { // 새로고침을 하지않으면 캐싱되어있기 때문에 호출이 되어도 값이 변하지 않는다.
        dateComputed: function() {
          return new Date()
        }
      },
    })
  </script>
</body>
</html>
```



> ###### View - VM - M(localstorage)
>
> `localStorage.getItem(key)` : 가져오기
>
> `localStorage.setItem(key, value)` : 저장
>
> `localStorage.removeItem(key)` : 삭제



###### `Watch`

- Vue 인스턴스의 data 변경을 관찰하고 이에 반응
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합

- 특정 데이터가 변경되었을 때 정의한 함수를 실행



```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>

<body>

  <div id="app">
    <select v-model="status">
      <option value="all" selected>all</option>
      <option value="active">active</option>
      <option value="completed">completed</option>
    </select>

    <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">
      <!-- v-bind -->
      Style Test
    </div>

    <img v-bind:src="vueImage" alt="todo-list" width="400px">
    <!-- <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">  -->
    <!-- <div v-for="todo in todos" v-on:click="check(todo)">  -->
    <div v-for="todo in computedTodosByStatus" v-bind:class="{ completed: todo.completed }" v-bind:key="todo.id">
      <!-- <div v-for="todo in todos" v-bind:class="{ completed: todo.completed }">  -->
      <!-- <div v-for="todo in todos" v-bind:class="todo.completed ? 'completed' : ''">  -->
      <input type="checkbox" v-model="todo.completed">
      <span>{{ todo.content }}</span>
    </div>
    <!-- <li v-else v-on:click="check(todo)"><s>{{ todo.content }}</s>[완료!]</li> -->
    <div>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button v-on:click="addTodo">submit</button>
    </div>
    <footer>
      <button v-on:click="clearCompleted">Clear</button>
    </footer>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const STORAGE_KEY = 'vue-todos'
    const todoStorage = {
      fetch: function() {
        // parse: String => JSON
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
      },
      save: function(todos) { // save 할 때에는 인자가 필요
        // stringify: JSON => String
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
      }
    }



    const app = new Vue({ // instance 생성
      el: '#app', // mount, vue와 vue모델 연결
      data: {
        status: 'all',
        activeColor: 'red',
        fontSize: 30,
        todos: [{ // 각각 객체화를 시켜보자.
            id: 1,
            content: '점심 메뉴 고민',
            completed: true,
          },
          {
            id: 2,
            content: '사다리 타기',
            completed: false,
          },
          {
            id: 3,
            content: '낮잠 자기',
            completed: false,
          },
          {
            id: 4,
            content: '야자 하기',
            completed: false,
          },
        ],
        newTodo: '',
        vueImage: 'https://user-images.githubusercontent.com/52684457/68103171-0c788100-ff19-11e9-890b-07f2bbadb9da.png'
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed // ! => 반대 구문
        },
        addTodo: function () {
          if (this.newTodo.length !== 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = '' // 입력 후 빈문자열로 만들어주는 구문
          }
        },
        clearCompleted: function () {
          // completed 가 false 인 객체만 모아서 배열로 return
          const notCompletedTodos = this.todos.filter(todo => {
            return !todo.completed
          })
          this.todos = notCompletedTodos
        },

      },
      computed: { // 값을 캐싱하고 있기때문에 호출이 되어도 값이 변하지 않는다.
        computedTodosByStatus: function () {
          // 진행중인 일(완료되지 않은 일)
          if (this.status === 'active') {
            return this.todos.filter(todo => {
              return !todo.completed
            })
          }
          // 완료된 일
          if (this.status === 'completed') {
            return this.todos.filter(todo => {
              return todo.completed
            })
          }
          // all (active, completed 가 아닌, 완료 혹은 미완료가 모두 포함된 배열)
          return this.todos
        }
      },
      watch: {
        todos: {
          // hendler 특정 데이터가 변경 되었을 때 실행할 함수
          handler: function(todos) {
            todoStorage.save(todos)
          },
          // 객체의 nested item 들도 관찰할지 유무를 설정, true인 경우 내부 요소들도 감시하도록 함
          deep: true,
        }
      },
      // 새로고침 될 때(DOM과 Vue instance 가 연견되는 시점) 실행되는 것, 새로 고침을 해도 기존에 추가한 값이 사라지지 않는다.
      mounted: function() {
        this.todos = todoStorage.fetch()
      },
    })
  </script>
</body>

</html>
```



##### `computed` VS `watch`

> `computed` : 계산해야하는 목표 데이터를 정의하는 방식 (선언형 프로그래밍)
>
> `watch` : 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하라는 방식 (명령형 프로그래밍)



##### `v-if` / `v-show`

> `v-if` : 조건에 맞지 않으면 렌더링 자체를 하지 않음
>
> `v-show` : 조건과 관계 없이 일단 렌더링 후에, 조건에 맞지 않으면 CSS display 속성을 토글해서 숨겨버린다.



#### :mushroom: shortcut

> `v-bind:` => `:`
>
> `v-on:` => `@`

- 아래는 약어로 바꿔준 상태 

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>

<body>
  <div id="app">
    <select v-model="status">
      <option value="all" selected>all</option>
      <option value="active">active</option>
      <option value="completed">completed</option>
    </select>

    <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">
      Style Test
    </div>

    <img :src="vueImage" alt="todo-list" width="400px">
    <div v-for="todo in computedTodosByStatus" :class="{ completed: todo.completed }" v-bind:key="todo.id">
      <input type="checkbox" v-model="todo.completed">
      <span>{{ todo.content }}</span>
    </div>
    <div>
      <input type="text" v-model="newTodo" @keyup.enter="addTodo">
      <button @click="addTodo">submit</button>
    </div>
    <footer>
      <button @click="clearCompleted">Clear</button>
    </footer>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const STORAGE_KEY = 'vue-todos'
    const todoStorage = {
      fetch: function() {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
      },
      save: function(todos) { 
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
      }
    }



    const app = new Vue({ 
      el: '#app', 
      data: {
        status: 'all',
        activeColor: 'red',
        fontSize: 30,
        todos: [{ 
            id: 1,
            content: '점심 메뉴 고민',
            completed: true,
          },
          {
            id: 2,
            content: '사다리 타기',
            completed: false,
          },
          {
            id: 3,
            content: '낮잠 자기',
            completed: false,
          },
          {
            id: 4,
            content: '야자 하기',
            completed: false,
          },
        ],
        newTodo: '',
        vueImage: 'https://user-images.githubusercontent.com/52684457/68103171-0c788100-ff19-11e9-890b-07f2bbadb9da.png'
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed
        },
        addTodo: function () {
          if (this.newTodo.length !== 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = ''
          }
        },
        clearCompleted: function () {
          const notCompletedTodos = this.todos.filter(todo => {
            return !todo.completed
          })
          this.todos = notCompletedTodos
        },

      },
      computed: { 
        computedTodosByStatus: function () {
          if (this.status === 'active') {
            return this.todos.filter(todo => {
              return !todo.completed
            })
          }
          if (this.status === 'completed') {
            return this.todos.filter(todo => {
              return todo.completed
            })
          }
          return this.todos
        }
      },
      watch: {
        todos: {
          handler: function(todos) {
            todoStorage.save(todos)
          },
          deep: true,
        }
      },
      mounted: function() {
        this.todos = todoStorage.fetch()
      },
    })
  </script>
</body>

</html>
```



> 삭제, 생성
>
> ```html
> <!DOCTYPE html>
> <html lang="ko">
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <meta http-equiv="X-UA-Compatible" content="ie=edge">
>   <title>Document</title>
> </head>
> <body>
>   <div id="app">
>     <input type="text" v-model="newTodo"> <!-- 입력 완료 -->
>     <button v-on:click="addTodo">+</button> <!-- 버튼을 누를 때 입력 -->
>     <li v-for="todo in todos" v-bind:key="todo.id">
>       <span>{{ todo.content }}</span>
>       <button v-on:click="removeTodo(todo.id)">x</button> <!-- 삭제 버튼 -->
>     </li>
>   </div>
> 
>   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
>   <script>
>     const app = new Vue({
>       el: '#app',
>       data: {
>         todos: [],
>         newTodo: '',
>       },
>       methods: {
>         addTodo: function () {
>           if (this.newTodo.length != 0) {
>             this.todos.push({
>               id: Date.now(),
>               content: this.newTodo,
>               completed: false,
>             })
>             this.newTodo = '' // 삽입을 하고 나면 다시 빈문자열로
>           }
>         },
>         removeTodo: function (todoId) {
>           this.todos = this.todos.filter( todo => { // 필터로 걸러낸 것들을 인자로 받기
>             // 완료한 todo
>             // 완료된 todo를 제외한 나머지 todo만 filter를 통해서
>             // 새로운 배열로 return
>             return todo.id !== todoId
>           })
>         }
>       }
>     })
>   </script>
> </body>
> </html>
> ```



##### 카테고리

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .todo-list {
      display: inline-block;
      width: 33%;
    }
  </style>
</head>

<body>
  <div id="app">
    <div class="todo-list">
      <h2>취업준비</h2>
      <input type="text" v-model="newTodo1">
      <button v-on:click="addTodo1">+</button>
      <li v-for="todo in todos1" v-bind:key="todo.id">
        <span>{{ todo.content }}</span>
        <button v-on:click="removeTodo1(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>SSAFY</h2>
      <input type="text" v-model="newTodo2">
      <button v-on:click="addTodo2">+</button>
      <li v-for="todo in todos2" v-bind:key="todo.id">
        <span>{{ todo.content }}</span>
        <button v-on:click="removeTodo2(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>ETC</h2>
      <input type="text" v-model="newTodo3">
      <button v-on:click="addTodo3">+</button>
      <li v-for="todo in todos3" v-bind:key="todo.id">
        <span>{{ todo.content }}</span>
        <button v-on:click="removeTodo3(todo.id)">x</button>
      </li>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        todos1: [],
        newTodo1: '',
        todos2: [],
        newTodo2: '',
        todos3: [],
        newTodo3: '',
      },
      methods: {
        addTodo1: function () {
          if (this.newTodo1.length != 0) {
            this.todos1.push({
              id: Date.now(),
              content: this.newTodo1,
              completed: false,
            })
            this.newTodo1 = ''
          }
        },
        removeTodo1: function (todoId) {
          this.todos1 = this.todos1.filter(todo => {
            return todo.id !== todoId
          })
        },
        addTodo2: function () {
          if (this.newTodo2.length != 0) {
            this.todos2.push({
              id: Date.now(),
              content: this.newTodo2,
              completed: false,
            })
            this.newTodo2 = ''
          }
        },
        removeTodo2: function (todoId) {
          this.todos2 = this.todos2.filter(todo => {
            return todo.id !== todoId
          })
        },
        addTodo3: function () {
          if (this.newTodo3.length != 0) {
            this.todos3.push({
              id: Date.now(),
              content: this.newTodo3,
              completed: false,
            })
            this.newTodo3 = ''
          }
        },
        removeTodo3: function (todoId) {
          this.todos3 = this.todos3.filter(todo => {
            return todo.id !== todoId
          })
        }
      }
    })
  </script>
</body>

</html>
```

- 복사 붙여넣기 형식으로 코드를 짜게되면 코드가 길어지게 된다. 조금 더 효율적으로 코드를 짜는 방법은 없을까?



## :large_blue_circle: Component

"소프트웨어 개발에서 독립적인 단위 모듈"

- 대체로 컴포넌트는 특정 기능이나 관련된 기능의 조합으로 구성되는데, 프로그래밍 설계에서 시스템은 모듈로 구성된 컴포넌트로 나뉜다.
- VUE - "기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드로 캡슐화 하는 것"

> #### 컴포넌트 naming convention
>
> - 컴포넌트의 첫번째 인자는 태그 이름, 두번째 인자는 속성들을 넣어준다.
>
> 1. kebab-case - `todo-list`
>    - 호출 할 때: `<todo-list></todo-list>` 
>        <u>케밥케이스</u>로만 호출 가능
> 2. pskalCase - `TodoList`
>    - 호출 할 때 : `<todo-list></todo-list>` / `<todo-list>` 
>    - 단, DOM 에 직접 작성할 때는 케밥케이스만 가능
>
> - 그래서 vue 는 모두 소문자여야 하고 하이픈을 포함하는 규칙을 따르는 것을 권장



###### `props`

- 컴포넌트를 재생산 할 때 컴포넌트에서 사용할 변수를 부모에서 내려주게 되는데 이를 `props` 라고 한다.
- 반복되는 컴포넌트에 서로 다른 정보가 들어가야 할 때 사용
- 하위(자식)에서 상위(부모)로 직접 참조해선 안되고 실제로도 안된다.
- `prob`  옵션을 통해 부모 **=>** 자식으로 데이터를 전달

- 전달하려고 하는 **데이터의 이름을 태그 내의 속성**으로, 내용을 속성 값으로 넣어준다.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .todo-list {
      display: inline-block;
      width: 33%;
    }
  </style>
</head>

<body>
  <div id="app">
    <h1>My Todo App</h1>
    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="ETC"></todo-list>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    var data = {
      counter: 0
    }
    // 컴포넌트 등록
    Vue.component('todo-list', {
      template: `
      <div class="todo-list">
      <h2>{{ category }}</h2>
      <input type="text" v-model="newTodo">
      <button v-on:click="addTodo">+</button>
      <li v-for="todo in todos" v-bind:key="todo.id">
        <span>{{ todo.content }}</span>
        <button v-on:click="removeTodo(todo.id)">x</button>
      </li>
    </div>`,
      props: ['category'],
      // 컴포넌드에서 data 는 함수여야 한다.
      // 이제 모든 todos와 newTodos 는 각각 고유한 내부 상태가 있다.
      data: function () {
        return {
          todos: [],
          newTodo: '',
        }
      },
      methods: {
        addTodo1: function () {
          if (this.newTodo.length != 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = ''
          }
        },
        removeTodo1: function (todoId) {
          this.todos = this.todos.filter(todo => {
            return todo.id !== todoId
          })
        },
      },
    })

    const app = new Vue({
      el: '#app',
    })
  </script>
</body>

</html>
```



![image](https://user-images.githubusercontent.com/52684457/68186328-3d26ec00-ffe7-11e9-882a-94c9ea9d4017.png)



#### 최종본

- shortcut까지 적용 시킨 모습

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .todo-list {
      display: inline-block;
      width: 33%;
    }
  </style>
</head>

<body>
  <div id="app">
    <h1>My Todo App</h1>
    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // 컴포넌트 등록
    Vue.component('todo-list', {
      template: `
            <div class="todo-list">
                <h2>{{ category }}</h2>
                <input type="text" v-model="newTodo" @keyup.enter="addTodo">
                <button @click="addTodo">+</button>
                <li v-for="todo in todos" v-bind:key="todo.id">
                    <span>{{ todo.content }}</span>
                    <button @click="removeTodo(todo.id)">x</button>
                    <!--todo.id 에 해당하는 것만 삭제-->
                </li>
            </div>
            `,
      props: {
        category: {
          type: String,
          required: true,
          validator: function (value) { // value에는 category가 들어감.
            if (value.length < 5) {
              return true
            } else {
              return false
            }
          },
        }

      },
      // 컴포넌트에서 data는 함수여야 한다.
      // 이제 모든 todos 와 newTodo 는 각각 고유한 내부 상태가 있다.
      data: function () {
        return {
          todos: [],
          newTodo: '',
        }
      },
      methods: {
        addTodo: function () {
          if (this.newTodo.length !== 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = '' // 함수 실행된 후 빈문자열로 두어야 입력 후 글 안남음.
          }
        },
        removeTodo: function (todoId) {
          // false 인 애들만 뽑아오기
          this.todos = this.todos.filter(todo => {
            // 완료한 todo
            // 완료된 todo를 제외한 나머지 todo만 filter를 통해서
            // 새로운 배열로 return
            return todo.id !== todoId // 누른애랑 다른애들만 출력...
          })
        }, // 특정 id 삭제
      },
    })
    const app = new Vue({
      el: '#app',

    })
  </script>
</body>

</html>
```



## :large_blue_circle: Module

###### `webpack`

![image](https://user-images.githubusercontent.com/52684457/68270118-ad914400-009f-11ea-944b-417237029b8d.png)

- 웹팩은 현재 가장 널리 쓰이는 번들러
- JS뿐만 아니라, CS, IMAGE 파일 리소스의 의존성들도 관리한다.

> #### 모듈
>
> - 어플리케이션을 구성하는 개별적 요소
> - 재사용 가능한 코드 조각
> - 모듈은 세부사항을 캡슐화
> - 특정 기능을 갖는 작은 코드 단위
>
> #### 모듈번들러
>
> - 웹 어플리케이션을 구성하는 자원(HTML, CSS, IMG 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구

> 개발을 편하게 모듈 단위 개발 
> **=>** 모듈끼리 연결(의존성)을 신경쓰기가 어려워짐 
> **=>** 웹팩으로 하나로 만듦

```bash
$ npm init
```

- 전부 스킵(enter)하면 기본 값 파일이 생성 된다.

```json
{
  "name": "02_view_webpack",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "vue": "^2.6.10"
  },
  "devDependencies": {
    "webpack": "^4.41.2",
    "webpack-cli": "^3.3.10"
  }
}
```



```bash
$ npm install vue
```

- vue 설치



```bash
$ npm i webpack webpack-cli -D
```

- webpack 설치
- `-D` : 개발모드



> ###### 생성 된 파일 목록
>
> :file_folder: node_modules(folder)
> ㄴ .bin
> ㄴ ...
> :open_file_folder: package-lock.json
> :open_file_folder: package.json
> :open_file_folder: webpack.config.json **=>** 직접 생성



> ###### webpack.config.json 작성하기
>
> ```js
> // webpack 설정 파일
> 
> module.exports = {
>   entry: {
>     // __dirname : 최상의 위치(entry point) - Django 에서 BASE_DIR
>     app: path.join(__dirname, 'src', 'main.js')
>   },
>   module: {},
>   plugins: [],
>   output: {
>     filename: 'app.js',
>     path: path.join(__dirname, 'dist'),
>   },
> }
> ```
>
> 최상위 폴더 위치에서 **src** 폴더 생성
>
> :file_folder: src
> ㄴApp.vue
> ㄴmain.js



###### webpack.config.json

```js
// webpack 설정 파일
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  entry: {
    // __dirname : 최상의 위치(entry point) - Django 에서 BASE_DIR
    app: path.join(__dirname, 'src', 'main.js')
  },
  module: {
    rulse: [{ // .은 전역이기 때문에 /\을 앞에 사용해주어야 한다. 
      test: /\.vue$/, // 정규 표현식 : '.vue' 확장자를 가진 모든 파일
      use: 'vue-loader',
    }]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist'),
  },
}
```



###### `entry`

- 여러 js 파일들의 시작점 **=>** 웹팩이 파일을 읽어 들이기 시작하는 부



###### `module`

- 웹팩은 JS만 변환 가능하기 때문에 html, css 등은 모듈을 통해서 웹팩이 이해할수 있도록 변환이 필요
- 변환 내용을 담는 곳



###### `plugins`

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분



###### `output`

- 여러 js 파일을 **하나로 만들어 낸 결과물**



> **webpack은 js 코드만 이해 가능**하기 때문에 vue파일(vue-loader) 및 html, css 파일(vue-template-compiler) 등을 변환하기 위하여 **모듈을 설치**
>
> ```bash
> $ npm install vue-loader vue-template-compiler -D
> ```



###### main.js

```js
// Vue 인스턴스를 최종으로 만드는 파일

// 1. 설치된 vue 를 추가
// (내가 만든 파일이 아닌 경우) 현재 위치에서 vue 이름을 가진 폴더가 없음 => 자동으로 node_modules 에서
import Vue from 'vue'

// 2. 최상위 컴포넌트 추가
// (내가 만든 파일) 상대 경로 표시
import App from './App.vue'

// new Vue({
//   render: function (createElement) {
//     return createElement()
//   }
// })
new Vue({
  render: h => h(App)
}).$mount('#app') // el: '#app'와 기능적으로 같으나 지금 방법이 더 유연하여 선호됨
```



###### App.vue

- vbase

```js
<template> 
  <h1>여기는 최상위 컴포넌트 입니다.</h1>
</template>

<script>

</script>

<style>

</style>
```

- 우리가 필요한 것은 이 세가지 항목



> **package.json** 에서
>
>  `"test": "echo \"Error: no test specified\" && exit 1"`
>
> 대신
>
> `"build": "webpack"` 추가
>
> ```json
> {
>   "name": "02_view_webpack",
>   "version": "1.0.0",
>   "description": "",
>   "main": "index.js",
>   "scripts": {
>     "build": "webpack" // 추가(혹시나 json파일에서 주석은 사용안하는 것을 권장)
>   },
>   "author": "",
>   "license": "ISC",
>   "dependencies": {
>     "vue": "^2.6.10"
>   },
>   "devDependencies": {
>     "vue-loader": "^15.7.2",
>     "vue-template-compiler": "^2.6.10",
>     "webpack": "^4.41.2",
>     "webpack-cli": "^3.3.10"
>   }
> }
> ```



```bash
$ npm run build
```

- 설정이 다 끝났다면 webpack을 작성해준다.



> ###### 생성 된 파일 목록
>
> :file_folder: dist **=>** 자동 생성!​ (`run build` 시에 생성 됨)
> :file_folder: node_modules(folder)
> ㄴ .bin
> ㄴ ...
> :file_folder: src
> ㄴApp.vue
> ㄴmain.js
> :open_file_folder: package-lock.json
> :open_file_folder: package.json
> :open_file_folder: webpack.config.json
> :file_folder: public **=>** 직접 생성
> ㄴindex.html



###### index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <div id="app">


  </div>

  <script src="../dist/app.js"></script> <!-- 경로 설정 -->
</body>

</html>
```

```js
// webpack.config.js
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')
module.exports = {
  mode: 'development', // => mode 추가!
    ...
```

- 설정 후 다시 `npm run build`

![image](https://user-images.githubusercontent.com/52684457/68274152-ac661400-00ab-11ea-9a09-600a5ccf8c2c.png)

- 다시 창을 켜보면 view를 사용할 수 있게 된다.



> 최상 컴포넌트 (App.vue)
>
> 하위 컴포넌트 (TodoList.vue)

**=>** src(source) 폴더에 component 폴더 안에 하위폴더인 TodoList.vue 생성



######  TodoList.vue

- vbase순으로
  template => script => style 순으로 작성

```vue
<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" @keyup.enter="addTodo" />
    <button @click="addTodo">+</button>
    <li v-for="todo in todos" v-bind:key="todo.id">
      <span>{{ todo.content }}</span>
      <button @click="removeTodo(todo.id)">x</button>
    </li>
  </div>
</template>

<script>
export default {
  props: {
    category: {
      type: String,
      required: true,
      validator: function(value) {
        if (value.length < 5) {
          return true;
        } else {
          return false;
        }
      }
    }
  },
  data: function() {
    return {
      todos: [],
      newTodo: ""
    };
  },
  methods: {
    addTodo: function() {
      if (this.newTodo.length !== 0) {
        this.todos.push({
          id: Date.now(),
          content: this.newTodo,
          completed: false
        });
        this.newTodo = "";
      }
    },
    removeTodo: function(todoId) {
      this.todos = this.todos.filter(todo => {
        return todo.id !== todoId;
      });
    }
  }
};
</script>

<style>
.todo-list {
  display: inline-block;
  width: 33%;
}
</style>
```

- 위의 코드는 해당 문서의 **최종본 목록**으로 가서 그대로 가져온 값이다.
- 어떤 코드를 긁어왔는지 잘 비교해보자



### :walking_man: 컴포넌트 등록 3 steps (App.vue)

1. `<script>` 에 등록할 컴포넌트 불러오기 (import)
2. `export default` 에 `components` 항목에 추가
3. `<template>` 에서 컴포넌트 사용할 수 있도록 등록

###### App.vue

```vue
<template>
  <div>
    <!-- 컴포넌트 사용 시 덩어리를 구분하는 div가 필요 -->
    <!-- 3. 컴포넌트 등록 -->
    <h1>여기는 최상위 컴포넌트 입니다.</h1>

    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>
  </div>
</template>

<script>
// 1. 하위 컴포넌트 불러오기
import TodoList from "./components/TodoList.vue";

// 2. 불러온 컴포넌트를 최상위(부모) 컴포넌트에 등록
export default {
  components: {
    TodoList // 자식(하위) 컴포넌트들이 이 뒤로 계속 작성 됨
  }
};
</script>

<style>
</style>
```



```bash
$ npm install vue-style-loader css-loader -D
```

- 두가지의 모듈 설치 후

###### package.json

```json
...
  "devDependencies": {
    "css-loader": "^3.2.0", // 추가된 모듈 두가지를 확인 할 수 있다.
    "vue-loader": "^15.7.2",
    "vue-style-loader": "^4.1.2",
    "vue-template-compiler": "^2.6.10",
    "webpack": "^4.41.2",
    "webpack-cli": "^3.3.10"
  }
}

```

###### webpack.config.js

```js
module.exports = {
  mode: 'development',
  entry: {
    ...
  module: {
    rules: [ 
      {
        test: /\.vue$/, 
        use: 'vue-loader',
      },
      {
        test: /\.css/,
        use: ['vue-style-loader', 'css-loader'] // 여러개는 배열로 작성
      }
    ]
  ...
}
```

- `'vue-style-loader'`, `'css-loader'` 모듈을 사용하겠다는 코드를 작성

- `npm run build`  빌드를 다시 재설정 해준다.



**[vue cli](https://cli.vuejs.org/guide/installation.html#installation)**

- **새로운 폴더에 설치**를 해보자

```bash
$ npm i -g @vue/cli
```

- `i` : install
- `g` : global

```bash
$ vue --version
@vue/cli 4.0.5
```



```bash
$ vue create todo-vue-cli


Vue CLI v4.0.5
? Please pick a preset: default (babel, eslint) 


Vue CLI v4.0.5
✨  Creating project in C:\Users\student\Desktop\수업\TIL\...
⚙  Installing CLI plugins. This might take a while...


> yorkie@2.0.0 install C:\Users\student\Desktop\수업\TIL\...
> node bin/install.js

setting up Git hooks
can't find .git directory, skipping Git hooks installation

> core-js@3.3.6 postinstall C:\Users\student\Desktop\수업\TIL\...
> node postinstall || echo "ignore"


> core-js-pure@3.3.6 postinstall C:\Users\student\Desktop\수업\TIL\...
> node postinstall || echo "ignore"

added 1128 packages from 822 contributors and audited 24120 packages in 34.096s
found 0 vulnerabilities

🚀  Invoking generators...
📦  Installing additional dependencies...

added 56 packages from 44 contributors and audited 24407 packages in 8.518s
found 0 vulnerabilities

⚓  Running completion hooks...

📄  Generating README.md...

🎉  Successfully created project todo-vue-cli.
👉  Get started with the following commands:

 $ cd todo-vue-cli
 $ npm run serve
```

-  `cd todo-vue-cli` 후
   `npm run serve` 서버를 켜보면

```bash
student@DESKTOP ~/Desktop/수업/TIL/... (master)
$ cd todo-vue-cli

student@DESKTOP ~/Desktop/수업/TIL/.../todo-vue-cli (master)
$ npm run serve

> todo-vue-cli@0.1.0 serve C:\Users\student\Desktop\수업\TIL\...\todo-vue-cli
> vue-cli-service serve

 INFO  Starting development server...

  App running at:
  - Local:   http://localhost:8080/
  - Network: http://...:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

- vue 서버가 열린 것을 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/52684457/68277180-04a01480-00b2-11ea-8047-3de1066fb971.png)

- 자동생성된 파일 목록들

- 직접 웹팩 작업을 할 때 있던 webpack.comfig.js 가 보이지 않는데 선택적 숨김파일 설정이 되어있다.(내장으로 들어가있음) 건드리기 위해서는 최상위에 직접 사용자가 만들어야 한다.
- `vue.config.js` 는 vue-cli 에 의해 자동으로 로드되는 선택적 구성 파일로 변경되었다.
- vue-cli 3 버전부터 노출되지 않으며, 설정을 추가하기 위해서는 루트 디렉토리에 직접 파일을 만들고 작성해야 한다.

![image](https://user-images.githubusercontent.com/52684457/68278227-3c0fc080-00b4-11ea-8c61-cf69f4e03ee0.png)

- 이 경로에 설정 파일이 있다.
- 정확히는 package.json 의 `"@vue/cli-service": "^4.0.0",` 구문



- 이곳에서 이전에 작성한 파일내용을 옮겨주자.

###### App.vue

```vue
<template>
  <div id="app">
    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>
  </div>
</template>

<script>
import TodoList from "./components/TodoList.vue";

export default {
  name: "app",
  components: {
    TodoList
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```



###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" @keyup.enter="addTodo" />
    <button @click="addTodo">+</button>
    <li v-for="todo in todos" v-bind:key="todo.id">
      <span>{{ todo.content }}</span>
      <button @click="removeTodo(todo.id)">x</button>
    </li>
  </div>
</template>

<script>
export default {
  props: {
    category: {
      type: String,
      required: true,
      validator: function(value) {
        if (value.length < 5) {
          return true;
        } else {
          return false;
        }
      }
    }
  },
  data: function() {
    return {
      todos: [],
      newTodo: ""
    };
  },
  methods: {
    addTodo: function() {
      if (this.newTodo.length !== 0) {
        this.todos.push({
          id: Date.now(),
          content: this.newTodo,
          completed: false
        });
        this.newTodo = "";
      }
    },
    removeTodo: function(todoId) {
      this.todos = this.todos.filter(todo => {
        return todo.id !== todoId;
      });
    }
  }
};
</script>

<style>
.todo-list {
  display: inline-block;
  width: 33%;
}
</style>
```

- component에 새로 vue파일을 이렇게 만들어 주자. 
  (내용은 그대로 가져온 것)

- `npm run build` 후 `npm run serve` 로 서버를 켜주면 링크가 뜬다. 로컬 링크로 들어가면 적용된 페이지가 잘 뜨는 것을 확인 할 수 있다. (이전에는 index.html에서 open browser 함)

 :star: **(tip)** 서버를 끈 후 터미널에 `vue ui` 코드를 입력하면 프로젝트를 조금더 쉽게 관리할 수 있는 페이지를 제공한다.



![image](https://user-images.githubusercontent.com/52684457/68278988-d8869280-00b5-11ea-8a81-fffdd8abcbb8.png)

- 현재는 하나의 tamplate구간만 짠 상태






## :small_red_triangle_down: Search 

```bash
$ vue create youtube-browser
```

```bash
$ cd youtube-browser/
```

- 설치 후 생성된 `youtube-browser` 폴더로 이동



###### App.vue

```vue
<template>
  <div id="app">
    <search-bar></search-bar>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar'
export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  components: {
    SearchBar,
  }
}
</script>

<style>
</style>
```

- 컴포넌트의 추가할 vue를 import, tag 가져오기 (`search-bar`)



****

### :red_circle: SearchBar

1. 사용자가 input 에 값을 입력하면 oninput 함수가 실행
2. inputChange 이벤트와 사용자가 입력한 value 가 함께 상위 컴포넌트인 App.vue로 emit 된다.

### :red_circle: App



3. SearchBar 에서 넘어온 이벤트 inputChange 로 인해 oninputChange 함수가 실행된다
4. oninputChange 함수는 유튜브 api에 요청을 보내고 비디오 리스트를 응답 받는다.

****



###### component/SearchBar.vue

```vue
<template>
  <div>
    <input @input="onInput" type="text">
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
        console.log(e)
      }
    }
  }
</script>

<style>

</style>
```

- input값을 부여 v-on(`@`), 사용 할 methods 추가



```bash
error: Unexpected console statement (no-console) at src\components\SearchBar.vue:12:9:
  10 |     methods: {
  11 |       onInput(e) {
> 12 |         console.log(e)
     |         ^
  13 |       }
  14 |     }
  15 |   }
```

- 개발모드에서는 유출이되면 안되기 때문에 evevt의 console이 막혀있다.

```json
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {},
    "parserOptions": {
      "parser": "babel-eslint"
    }
  },
```

- package.json 에서 `rules` 설정값을 `"no-console": "off"` 로 준다.



- 서버를 재 시작한 후 콘솔에서 새로고침을 하면

  **=>** `target.value` 에 입력값을 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/52684457/68555216-e6e6fc80-046f-11ea-91c7-6abd1623e330.png)



#### 사용자가 검색어 입력(SearhcBar)

**=>** 검색 결과를 App.vue로 올려줌



###### SearchBar.vue

```vue
<script>
  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
        this.$emit('inputChange', e.target.value)
      }
    }
  }
</script>
```

- `'inputChange'` : 이벤트 이름
- `e.target.value` : 데이터 (arguments)



![image](https://user-images.githubusercontent.com/52684457/68555216-e6e6fc80-046f-11ea-91c7-6abd1623e330.png)

- 값을 하나하나 받는 것을 알 수 있다. (아직 부모로 값을 보내진 않은 상태)



![image](https://user-images.githubusercontent.com/52684457/68555336-a176ff00-0470-11ea-926f-2bda8b01d0c4.png)

- vue로 확인한 이벤트 발생



###### App.vue

```vue
<template>
  <div id="app">
    <!-- inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar'
export default {
  name: 'App', 
  components: {
    SearchBar,
  },
  methods: {
    onInputChange(inputValue) {
      console.log(inputValue)
    }
  }
}
</script>
```

- `@inputChange="onInputChange"` 추가
- `onInputChange` method 추가 후 console로 확인

![image](https://user-images.githubusercontent.com/52684457/68555444-2530eb80-0471-11ea-8365-0bc3c2171e40.png)

- 부모도 값을 하나씩 받는 것을 확인 할 수 있다.



### 단방향 데이터 흐름의 이점

1. vue.app의 데이터 흐름을 쉽게 파악할 수 있음
2. 부모 컴포넌트에서 업데이트가 일어나면 자식컴포넌트는 자동 업데이트 (즉, 자식 컴포넌트의 상태를 관리하지 않아도 된다.)
3. 하위 컴포넌트가 실수로 부모의 상태를 변경하려 app 데이터의 흐름을 추론하기 어렵게 만드는 것을 방지할 수 있다.

- 하위에서 상위로 데이터를 올려 보낼 때는 Event 를 발생 시키는 방법을 사용 (`emit`)
- `props` 는 배열, 객체, 함수 등 무엇이든 내려보내는 **속성(properties)**이고, `emit event` 는 자식에서 부모로 **이벤트를 발생** 시키는 것



- #### SearchBar => App

1. 트리거 : input 값 변경(@input)
   - 인자 : event
   - 실행 함수 : oninput
2. 트리거 : input 내 #emit (inputChange)
   - 인자 : 변경된 값
   - 실행 함수 : outputChange



#### :rocket: [구글 개발자 콘솔](https://console.developers.google.com/) 

- 새 프로젝트를 만든 후, API 및 서비스 사용설정에서 `YouTube Data API v3` 을 사용 할 것
- 사용자 인증 정보에서 웹브라우저, 공용으로 설정 후 키를 발급 (유출 조심)
- 최대 만번 정도의 요청을 보낼 수 있는데, 만약 초과를 했다면 새 프로젝트를 만들어 서비스 사용설정을 다시 한 후, 새로운 프로젝트로 다시 설정을 바꿔주면 된다. (서버를 다시 껐다 켜야 함)
- API 및 서비스 항복 아래에서 사용하고 있는  API를 클릭해서 들어가면 할당량 목록에서 얼마나 요청을 보냈는지 값을 알 수 있다.

```bash
$ npm i axios
```

- axios 확장자 설치



###### App.vue

```vue
<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
const API_KEY = '발급 받은 키'
const API_URL = ''
...
```

- axios 를 `import`, 발급 받은 키를 `API_KEY` 로 입력

- URL 은 [https://www.googleapis.com/youtube/v3/search(문서)](https://developers.google.com/youtube/v3/docs/search/list) 로 요청하면 된다.



![image](https://user-images.githubusercontent.com/52684457/68556667-87401f80-0476-11ea-8b80-696b2d9cac4d.png)

- 위의 문서링크에서 필수 매개변수를 확인하면 part 가 있는 것을 확인 가능

- ![image](https://user-images.githubusercontent.com/52684457/68556875-4b598a00-0477-11ea-9b53-99e4c1136d10.png)

  `q` : `string` 매개변수는 검색할 검색어를 지정합니다.



###### App.vue

```vue
<script>
    ...
export default {
  name: 'App',다.
  components: {
    SearchBar,
  },
  methods: {
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        }) // 함수 vs 함수기 때문에 arrow function 사용
    }
  }
}
</script>
```

- `.env.local` 파일 생성 (최상단)

- 자동으로 gitignore 에 evv.local 이 있기 때문에 값만 넣어주면 된다.

- 내용은 무조건 `VUE_APP_` (접두사) 로 시작해야 한다.

  **=>** `const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY`

  이로서 키 값의 직접적인 노출을 막을 수 있게 되었다.



****

### :red_circle: VideoList​ 

5. 넘겨 받은 비디오 리스트를 videos 라는 배열에 저장
6. `data` object 가 (videos 배열이 있는 곳) 업데이트 되면, 해당 컴포넌트 (App.vue) 가 템플릿을 다시 렌더링 한다.
7. 그리고 바로 자식 컴포넌트들도 모두 다시 렌더링 된다.
8. `VideoList`컴포넌트가 비디오 배열을 받아 화면에 보여주게 된다.

****

- component에서 VideoList.vue 추가

###### component/VideoList.vue

```vue
<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul>
    VideoList
  </ul>
</template>

<script>
  export default {
    name: 'VideoList',
  }
</script>

<style>
</style>
```



###### App.vue

```vue
<template>
  <div id="app">
    <search-bar @inputChange="onInputChange"></search-bar>
      
    <!-- 추가 -->
    <video-list></video-list>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
    
// component import
import VideoList from './components/VideoList'
    
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  components: {
    SearchBar,
    VideoList, // component 등록
  },
  data() {
    return { // return 값을 할 때에는 모든 객체가 return되기 때문에 객체를 한번 더 감싸서 구분을 주어야 한다. (component 의 data만)
      videos: [],
    }
  },
  methods: {
```

- vue component 에서는 반드시 Object 를 return 하는 함수로 작성



###### App.vue

```vue
<template>
  <div id="app">
    <search-bar @inputChange="onInputChange"></search-bar>

    <!--오른쪽에서 왼쪽으로 할당, 왼쪽의 videos는 다르게 써도 상관 없지만 오른쪽의 "videos"는 이미 우리가 지정한 name이기 때문에 이름 그대로 써야 한다. -->
    <video-list :videos="videos"></video-list>
  </div>
</template>

<script>
    ...
methods: {
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          // console.log(response)로 확인한 데이터 경로를 videos에 담아준다.
          this.videos = response.data.items
        })
        .catch(error => {
          ...
```



###### VideoList

```vue
<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul>
    VideoList
    {{ videos.length }}
  </ul>
</template>

<script>
  export default {
    name: 'VideoList',
  props: {
    videos: {
      type: Array,
      required: true,
      },
    },
  }
</script>

<style>
</style>
```

![image](https://user-images.githubusercontent.com/52684457/68561759-4b16ba00-048a-11ea-9dfc-617fc2170343.png)



****

### :red_circle: VideoListItem.vue





###### component/VideoListItem.vue

```vue
<template>
  <li>
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
  }
</script>

<style>
</style>
```



###### VideoList.vue

```vue
<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul>
    <video-list-item v-for="video in videos" :key="video.etag" :video="video"></video-list-item>
  </ul>
</template>

<script>
  import VideoListItem from './VideoListItem'

  export default {
    name: 'VideoList',
    components: {
      VideoListItem,
    },
  props: {
    videos: {
      type: Array,
      required: true,
      },
    },
  }
</script>

<style>
</style>
```



![image](https://user-images.githubusercontent.com/52684457/68561996-2c64f300-048b-11ea-9d81-f096a2907fde.png)

- public **=>** index.html 의 head 위에 bootstrap CSS 적용

  ```html
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  ```



###### SearchBar.vue

```vue
<style scoped>
  /* scoped => 이 vue에만 bootstrap css 적용 */
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>
```

- 적용할 때 scoped를 적용해야 해당 vue만 bootstrap의 CSS를 적용할 수 있다.

- VideoList 의 ul 태그를 `<ul class="list-group">` 
- VideoListItem 의 li 태그를 `<li class="list-group-item">`
  로 class를 준다.



CSS가 적용된 화면

![image](https://user-images.githubusercontent.com/52684457/68562398-ca0cf200-048c-11ea-8749-973128af9cea.png)



###### VideoListItem.vue

```vue
<template>
  <li class="list-group-item">
    <img :src="video.snippet.thumbnails.default.url" alt="img">
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
  }
</script>

<style>
</style>
```



![image](https://user-images.githubusercontent.com/52684457/68562526-7353e800-048d-11ea-91d1-f723a28cb086.png)

- 미리 캐싱을 하게되면 쿼리를 보내는 횟수를 줄일 수 있다.
  **=>** `computed`



###### VideoListItem.vue

```vue
<template>
  <li class="list-group-item">
    <img :src="thumbnailUrl" alt="img">
    <div class="media-body"></div>
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
    computed: {
      thumbnailUrl(){
        return this.video.snippet.thumbnails.default.url
      }
    }
  }
</script>

<style scoped>
  li {
    display: flex; /* 유동적으로 (사이즈를 비율에 맞게) */
    cursor: pointer; /* 가져다 대면 커서를 손가락 모양으로 */
  }

  li:hover {
    background-color: #eee; /* 마우스를 올렸을때 색상이 바뀌도록 hover */
  }
</style>
```

- computed 에서 만든 `thumbnailUrl` 를 :src 에 넣어준다.

![image](https://user-images.githubusercontent.com/52684457/68562794-874c1980-048e-11ea-86db-8b03cf66230a.png)



###### VideoListItem.vue

```vue
<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="img">
    <div class="media-body"></div>
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onVideoSelect() {
        // 인자가 없이 때문에 this.video
        this.$emit('videoSelect', this.video)
      }
    },
    computed: {
      thumbnailUrl(){
        return this.video.snippet.thumbnails.default.url
      }
    }
  }
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: #eee;
  }
</style>
```



###### VideoList

```vue
<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul class="list-group">
    <!-- 태그 안의 내용이 길 경우에는 enter로 줄바꿈을 함으로서 깔끔하게 정리해준다. -->
    <video-list-item 
    v-for="video in videos" 
    :key="video.etag" 
    :video="video"
    @videoSelect="onVideoSelect">
    </video-list-item>
  </ul>
</template>

<script>
  import VideoListItem from './VideoListItem'

  export default {
    name: 'VideoList',
    components: {
      VideoListItem,
    },
  methods: {
    onVideoSelect(video) {
      // 받을 인자가 있기 때문에 this.video가 아닌 video
      this.$emit('videoSelect', video)
    }
  },
  props: {
    videos: {
      type: Array,
      required: true,
      },
    },
  }
</script>

<style>
</style>
```



###### App.vue

```vue
<template>
  <div id="app">
    <!-- inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>

    <!--오른쪽에서 왼쪽으로 할당, 왼쪽의 videos는 다르게 써도 상관 없지만 오른쪽의 "videos"는 이미 우리가 지정한 name이기 때문에 이름 그대로 써야 한다. -->
    <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  components: {
    SearchBar,
    VideoList,
  },
  data() {
    return { // return 값을 할 때에는 모든 객체가 return되기 때문에 객체를 한번 더 감싸서 구분을 주어야 한다. (component 의 data만)
      videos: [],
    }
  },
  methods: {
    onVideoSelect(video) {
      // data가 최종적으로 app.vue까지 올라왔는지 확인 해보기 위해 
      console.log(video)
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          this.videos = response.data.items
        })
        .catch(error => {
          console.log(error)
        }) // 함수 vs 함수기 때문에 arrow function 사용
    }
  }
}
</script>

<style>
</style>

```







![image](https://user-images.githubusercontent.com/52684457/68563841-41915000-0492-11ea-97ef-2605e8786316.png)

- 데이터가 타고타고 올라오는 것을 볼 수 있다.



****

### :red_circle: VideoDetail



###### VideoDetail.vue

```vue
<template>
  <div"video">
    {{ video.snippet.title }}
  </div>
</template>

<script>
  export default {
    name: 'VideoDetail',
    props: {
      video: {
        type: Object,
        // video 선택이 안될수도 있기 때문에 required는 생략 (null이 나올수도 있음)
      }
    }
  }
</script>
```



###### App.vue

```vue
<template>
  <div id="app">
    <!-- inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>

    <!-- 값을 넘겨받은 selectedVideo를 바인드 -->
    <video-detail :video="selectedVideo"></video-detail>

    <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
  </div>
</template>

<script>
...
import VideoDetail from './components/VideoDetail'
...
export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return { 
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onVideoSelect(video) {
      // 최종적으로 video를 받은 다음에 selectedVideo로 넘긴다.
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          this.videos = response.data.items
        })
        .catch(error => {
          console.log(error)
        }) // 함수 vs 함수기 때문에 arrow function 사용
    }
  }
}
</script>

<style>
</style>

```





![image](https://user-images.githubusercontent.com/52684457/68564484-1871bf00-0494-11ea-8372-525ac9d82891.png)

- 새로 고침(아무런 값이 들어가지 않았을 때) null값이 들어가게 되면서 에러가 뜬다. error를 지워보자.



###### VideoDetail.vue

```vue
<template>
  <!-- video 값이 true 일 때만 돌도록 -->
  <div v-if="video">
    <div class="details">
      <h4>{{ video.snippet.title }}</h4>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'VideoDetail',
    props: {
      video: {
        type: Object,
      }
    }
  }
</script>

<style scoped>
    /* 페이지를 좀더 둥글둥글하게 만들기 위해 */
  .details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>
```



- 영상을 띄워 보자 **=>** `iframe` 사용

[embed 문서](https://developers.google.com/youtube/iframe_api_reference)

![image](https://user-images.githubusercontent.com/52684457/68564820-faf12500-0494-11ea-8e87-731f0927f918.png)



###### VideoDetail.vue

```vue
<template>
  <!-- video 값이 true 일 때만 돌도록 -->
  <div v-if="video">
      <iframe :src="videoUrl" frameborder="0"></iframe>
  </div>
</template>

<script>
  export default {
	...
    computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        // return this.data
        return `http://www.youtube.com/embed/${videoId}`
      }
    }
  }
</script>
```



![image](https://user-images.githubusercontent.com/52684457/68564980-7d79e480-0495-11ea-8a5d-09ddab9d236b.png)

- VideoDetail에 있는 id값을 이용



****

### :heavy_check_mark: BootStrap을 사용하여 template 정리

###### VideoDetail.vue

```vue
<template>
  <div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
  </div>
</template>
```



###### VideoList.vue

```vue
<template>
  <ul class="col-lg-4 list-group">
    <video-list-item 
    v-for="video in videos" 
    :key="video.etag" 
    :video="video"
    @videoSelect="onVideoSelect">
    </video-list-item>
  </ul>
</template>
```



###### App.vue

```vue
<template>
  <div id="app">
    <search-bar @inputChange="onInputChange"></search-bar>
     
    <!-- col을 사용한 태그들을 row div로 감싼다. -->
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>
```





- #### browser > lg

![image](https://user-images.githubusercontent.com/52684457/68566513-eb280f80-0499-11ea-873c-ea87e3406535.png)



- #### browser < lg

![image](https://user-images.githubusercontent.com/52684457/68566542-03982a00-049a-11ea-9439-825230fbd673.png)



****



#### :page_facing_up: 최종본

###### VideoDetail.vue

- col값을 주기위해 div 로 한번 감싼다.
- 그 위에 row 값을 준 div도 필요하기 때문에 app.vue에서 태그를 row값으로 감싸주자.

```vue
<template>
  <!-- video 값이 true 일 때만 돌도록 -->
  <div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
      <!-- html형식으로 title을 넣어주어야 글씨 깨짐이 없다. -->
      <h4 v-html="video.snippet.title"></h4>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'VideoDetail',
    props: {
      video: {
        type: Object,
        // video 선택이 안될수도 있기 때문에 required는 생략 (null이 나올수도 있음)
      }
    },
    computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        // return this.data
        return `http://www.youtube.com/embed/${videoId}`
      }
    }
  }
</script>

<style scoped>
  .details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>
```



###### VideoListItem.vue

```vue
<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="img">
    <div class="media-body" v-html="video.snippet.title"></div>
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onVideoSelect() {
        // 인자가 없이 때문에 this.video
        this.$emit('videoSelect', this.video)
      }
    },
    computed: {
      thumbnailUrl(){
        return this.video.snippet.thumbnails.default.url
      }
    }
  }
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: #eee;
  }
</style>
```



###### VideoList.vue

```vue
<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul class="col-lg-4 list-group">
    <!-- 태그 안의 내용이 길 경우에는 enter로 줄바꿈을 함으로서 깔끔하게 정리해준다. -->
    <video-list-item 
    v-for="video in videos" 
    :key="video.etag" 
    :video="video"
    @videoSelect="onVideoSelect">
    </video-list-item>
  </ul>
</template>

<script>
  import VideoListItem from './VideoListItem'

  export default {
    name: 'VideoList',
    components: {
      VideoListItem,
    },
  methods: {
    onVideoSelect(video) {
      // 받을 인자가 있기 때문에 this.video가 아닌 video
      this.$emit('videoSelect', video)
    }
  },
  props: {
    videos: {
      type: Array,
      required: true,
      },
    },
  }
</script>

<style>
</style>
```



###### SearchBar

```vue
<template>
  <div>
    <!-- input => change 로 바꾸면 하나하나 쿼리값이 날라가지 않고 enter 를 쳐야 쿼리 값이 나간다. -->
    <input @change="onInput" type="text">
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
        this.$emit('inputChange', e.target.value)
      }
    }
  }
</script>


<style scoped>
  /* scoped => 이 vue에만 bootstrap css 적용 */
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>
```



###### App.vue

```vue
<template>
  <div id="app">
    <!-- inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>

    <!-- col값을 주려는 태그들을 row div로 감싼다. -->
    <div class="row">
      <!-- 값을 넘겨받은 selectedVideo를 바인드 -->
      <video-detail :video="selectedVideo"></video-detail>

      <!--오른쪽에서 왼쪽으로 할당, 왼쪽의 videos는 다르게 써도 상관 없지만 오른쪽의 "videos"는 이미 우리가 지정한 name이기 때문에 이름 그대로 써야 한다. -->
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return { // return 값을 할 때에는 모든 객체가 return되기 때문에 객체를 한번 더 감싸서 구분을 주어야 한다. (component 의 data만)
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onVideoSelect(video) {
      // 최종적으로 video를 받은 다음에 selectedVideo로 넘긴다.
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          this.videos = response.data.items
        })
        .catch(error => {
          console.log(error)
        }) // 함수 vs 함수기 때문에 arrow function 사용
    }
  }
}
</script>

<style>
</style>

```



## :purple_heart: JWT

- 정보를 안전하게 JSON 객체로 전송하기 위한 간결하고 독립적인 방법
- 세션 / 쿠키와 함께 모바일과 웹의 인증을 책임지는 대표 기술 중 하나. 세션 / 쿠키의 정보 전달 방식과 유사하게 사용자는 Access Token (JWT token) 을 HTTP header에 실어서 서버로 요청을 보냄
- 세션 / 쿠키 방식과 가장 큰 차이점은 세션 / 쿠키는 세션 저장소에 유저의 정보를 넣지만, JWT 는 토큰안에 유저의 정보를 넣는다.
- Client의 입장에서는 HTTP header에 세션 ID / 토큰을 실어서 보낸다는 점은 동일하지만, server 입장에서는 인증을 위해 암호화(JWT 방식) 를 하냐 혹은 별도의 저장소(세션 / 쿠키 방식)를 이용하느냐의 차이 
- HS256이 보통 기본값



#### 사용 상황

1. ##### 회원 인증

   - 서버가 유저 정보에 기반한 토큰(JWT)을 발급해 유저에게 전달하고 유저는 서버에 요청을 보낼때마다 JWT를 포함하여 전달
   - 서버는 세션을 유지할 필요 없이 유저의 요청정보 안에 있는 JWT만 확인하면 되다. (서버 자원 아낄 수 있음)

2. ##### 정보 교환

   - 정보가 서명이 되어 있기 때문에 정보를 보낸 사람의 정보 혹은 정보가 조작여부 확인 등이 가능



#### 요약

- 두 개체에서 JSON 객체를 사용하여 가볍고 자가 수용적인(self-contained, 필요한 모든 정보를 자체적으로 지님) 방식으로 정보를 안정성 있게 전달
- 세션 상태를 저장하는 것이 아니라 필요한 정보를 JWT에 저장해서 사용자가 가지고 있게 하고, 해당 JWT를 증명서처럼 사용하는 방식

> ##### 장점
>
> 1. 세션/쿠키 처럼 별도의 저장소 관리가 필요 없고 발급한 이후에 검증만 하면 된다.
> 2. 토큰을 기반으로 한 다른 인증시스템에 접근이 용이하기 때문에 확장성이 뛰어나다.
> 3. 모바일 환경에 적합 (쿠키와 같은 데이터로 인증할 필요가 없기 때문, 모바일 측은 쿠키를 관리하기 어려운 환경)
> 4. Python, JS, Ruby, Go 등 주류 프로그래밍 언어에서 대부분 지원된다. (웹 표준을 지키고 있기 때문)
>
> 
>
> ##### 단점
>
> 1. 이미 발급 된 JWT는 유효기간이 완료될 때까지 계속 사용하기 때문에 악용(노출)될 가능성이 있음 (한번 발급된 토큰은 값을 수정하거나 폐기할 수 없다.) 그래서 이 문제는 Access Token 의 유효기간(expire time)을 딻게 하고 Refresh Token 등을 이요해서 중간 중간 새로운 토큰을 재발행 해준다.
> 2. 세션/쿠키 방식에 비해 claim 데이터(payload)가 많아진다면 JWT 토큰의 길이가 길어지기 때문에 인증 요청이 많아 질 수록 네트워크의 대역폭이 낭비될 수 있다. (길이 자체가 길어진다면 요청량이 많아짐, 서버쪽에서 들고있는게 아닌 API 호출 시 매 호출마다 헤더에 붙여서 전달하기 때문)



> xxxx(header).yyyy(Payload).zzzz(signature)
>
> - **header** : 토큰과 타입과 사용 알고리즘 정보가 들어감
>
> - **Payload** : 토큰에 담길 정보가 들어있는 곳 (claim - key:value)
>
> - **signature** : 헤더와 페이로드의 값에 비밀키로 해싱(hashing)



#### 정보(payload)

1. ##### registerd claim (등록된 클레임)

   - 토큰에 대한 정보들을 담기 위해 이름이 이미 정해진 클레임들. 클레임의 사용은 모두 선택적이다.

2. ##### public claim

   - 공개 클레임은 충돌이 되지 않는 이름을 가지고 있어야 한다. (이름이 겹치면 안된다. 기존의 키값들도 동일) 보통 충돌을 방지하기 위해 key 값을 URI 형태로 만든다.

     > 'apple' **(X)**
     >
     > 'https://test.co.kr/jwt_token':true **(O)**

3. ##### private claim

   - 등록된 클레임도, 공개 클레임도 아님. 클라이언트와 서버간에 협의하에 사용되는 클레임들
   - key 값이 중복되어 충돌이 될 수 있으니 유의해서 사용.
     충돌을 완전히 막을 수 있다기 보다는 유의하여 신중히 사용할 것
   - ex) `{ "username": "admin" }`



#### 서명 (signature)

- HEADER 의 인코딩 값과, PAYLOAD의 인코딩 값을 합친 후 주어진 비밀키로 해쉬를 생성한 값
- [공식 site](https://jwt.io/) **=>** [Debugger](https://jwt.io/#debugger-io) 되는 과정 **=>** [Libraries](https://jwt.io/#libraries-io) 사용하기위해 설치해야하는 라이브러리
  - 라이브러리를 사용하면 알아서 JWT를 생성해주기 때문에 직접 알고리즘을 적용할 필요는 없다. 



****



1. [Download Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)(Add into Python Path 체크) - **3.7.3**
   bash에서 `python -V` 로 버전 체크, 설치한 버전이 아니라면 환경변수에 들어가 path에서 확인

2. [vue cli install](https://cli.vuejs.org/guide/prototyping.html#instant-prototyping)

3. `vue create todo-front` (bash에서 todo-front라는 프로젝트 create) - defalt

4. ```bash
   $ mkdir todo-back
   $ cd todo-back
   $ python -m venv venv
   $ source venv/Script/activate
   $ pip list
   $ pip install django
   $ django-admin startproject todoback .
   $ python manage.py startapp todos
   $ cd ..
   $ cd todo-front
   $ vue ls
   $ vue ui
   ```

   - **pip list** :  환경 변수가 제대로 source 되었는지 확인

   - 참고로 python 3.5 버전이면 제대로 환경변수가 설치되지 않는다.

   - 환경변수 수정사항이 있다면 vscode를 껐다 실행하자

   - **ls** : 현재 폴더의 파일 목록을 불러온다. 현재 폴더를 확인 할때 사용.

   - 추가된 app을 setting에 추가 

     ```python
     INSTALLED_APPS = [
         'todos',
         ...
     ```

5. vue ui 를 실행하면 페이지가 하나 뜬다. 거기서 가져오기를 통해 `todo-front` 폴더를 가져온다. 

6. install plugin(플러그인 추가) 에서 router를 검색하여 최상단 공식 router( `vue/cli-plugin-router` )를 다운로드 (비활성화 되어있는 체크를 활성화)

   > node_modules / vue-router 폴더가 생성 되어 있음
   >
   > src / views 와 router 가 생성되었는지 확인
   >
   > 하단의 자식들은 component, router로 매핑되는 파일들은 src/views에 작성

   

   ###### 파일 구성

   > :file_folder: todo-back *(django)*
   > ​ㄴtodoback
   >    -`settings.py`
   >    ...
   >
   > ㄴtodos
   > ㄴvenv
   >
   > -`db.spqlite3`
   > -`manage.py`
   >
   > :file_folder: todo-front*​ (vue)*
   > ㄴnode-modules
   > ㄴpublic
   > ㄴsrc
   >
   > -`.gitignore`
   > -`babel.config.js`
   > -`package-lock.json`
   > -`package.json`
   > -`README.md`

   

###### todo-front/src/views/Ligin.vue

- `vbase` 단축키를 사용하면 vue 페이지 작성이 빠르다.

```vue
<template>
  <div>
    <h1>로그인 페이지 입니다.</h1>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style>

</style>
```



###### rodo-front/src/router/index.js

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```



###### todo-list/src/App.vue

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
      <!-- router 속성 안의 to로 인해 연결 -->
    </div>
    <div class="row justify-content-center">
      <router-view class="col-6"/>
    </div>
  </div>
</template>
...
```



###### todo-front/public/index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <link rel="icon" href="<%= BASE_URL %>favicon.ico">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <title>todo-front</title>
</head>

<body>
  ...
```





###### todo-front/src/component/LoginForm.vue

- **CDN only** : `<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">`

- [bootstrap forms](https://getbootstrap.com/docs/4.3/components/forms/)

```vue
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input type="text" class="form-control" id="id" placeholder="아이디를 입력해주세요">
    </div>
    <div class="form-group">
      <label for="password">PASSWORD</label>
      <input type="text" class="form-control" id="password" placeholder="비밀번호를 입력해주세요">
    </div>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style>

</style>
```





##### `router-link`

- router 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트
- 목표 위치는 `to` prop 으로 지정된다.
- 라우팅은 URI 에 따라 해당하는 정적 파일을 내려주는 방식인데 이를 브라우저에서 구현하는 것이 SPA 개발의 핵심
- `router-link` 는 `a` 태그보다 선호되는데 이유는 HTML5 히스토리 모드에서 클릭 이벤트 자체를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 한다.



##### `router-view`

- 라우팅이 경로에 맞는 컴포넌트를 제공하는데 해당 경로에 맞는 컴포넌트를 렌더링 해주는 부분



###### todo-front/src/views/Home.vue

- Home.vue가 Hello 뷰를 가지고있는 것을 지워줌

```vue
<template>
  <div>
    
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  
}
</script>

```



###### Login.vue

```vue
<template>
  <div>
    <!-- 아래를 케밥으로 쓰면 위도 케밥으로 써야하는데, 파스칼로 하면 둘다 사용 가능하다. 파스칼을 권장 -->
    <LoginForm/>
  </div>
</template>

<script>
  // 3step => import => 등록 => 파스칼 or 케밥
  // @ 는 `/src` 의 alias
  // import LoginForm from '../components/LoginForm' // 상대경로 - 눈으로 추적해야하기 때문에 비효율 적
  import LoginForm from '@/components/LoginForm' // 절대경로 /src => @
  export default {
    name: 'login',
    components: {
      LoginForm,
    }
  }
</script>

<style>

</style>
```



###### LoginForm.vue

```vue
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input 
      type="text" 
      class="form-control" 
      id="id" 
      placeholder="아이디를 입력해주세요"
      v-model="credentials.username"
      @keyup.enter="login"
      >
    </div>
    <div class="form-group">
      <label for="password">PASSWORD</label>
      <input 
      type="text" 
      class="form-control" 
      id="password" 
      placeholder="비밀번호를 입력해주세요"
      v-model="credentials.password"
      @keyup.enter="login"
      >
    </div>
    <button class="btn btn-primary" @click="login">로그인</button>
  </div>
</template>

<script>
  export default {
    name: 'LoginForm',
    data() {
      return {
        // 객체로 해야 네임스페이스, 즉 충돌이 되지않고 공간이 나눠진다.
        credentials: {},
        loading: false,
      }
    },
    methods: {
      login() {
        // console.log 자체가 배포단계때에는 사용하면 오류가 난다. 사용하면 안되어서 막혀있음.
        console.log('Login button Clicked!!')
      }
    },
  }
</script>

<style>

</style>
```

- ```json
  "rules": {
        "no-console": "off"
      },
  ```

  - package.json 에서 `rules` 에서 ` "no-console": "off"` 추가해야 console.log 오류가 나지 않는다.

- 여태까지는 false일때, 이젠 true에서 실행되는 것을 해줄 것 : `v-if` `v-else`
  [spinner](https://getbootstrap.com/docs/4.3/components/spinners/#border-spinner) : `class="spinner-border"`

  ```vue
  <template>
    <div class="login-div">
      <div v-if="loading" class="spinner-border">
        <span class="sr-only">Loading...</span>
        <!-- screen reader only 시각 장애인에게 로딩중인 것을 알려주는 것, 우리들 눈에는 none screen으로 보임 -->
      </div>
  
      <div v-else class="login-form">
        <div class="form-group">
          <label for="id">ID</label>
            ...
            ...
        <button class="btn btn-primary" @click="login">로그인</button>
      </div>
    </div>
  </template>
  ```



###### LoginForm.vue

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border">
      <span class="sr-only">Loading...</span>
      <!-- screen reader only 시각 장애인에게 로딩중인 것을 알려주는 것, 우리들 눈에는 none screen으로 보임 -->
    </div>

    <div v-else class="login-form">
      <div v-if="errors.length" class="error-list alert alert-danger" role="alert">
        <!-- errors 값이 true값 이라면 -->
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <!-- 키값이 필요하기 때문에 enumerate 형식으로 써주어야 함 -->
        <div v-for="(error, idx) in errors" :key="idx">"{{ error }}"</div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요"
        v-model="credentials.username"
        @keyup.enter="login"
        >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요"
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
      <button class="btn btn-primary" @click="login">로그인</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'LoginForm',
    data() {
      return {
        // 객체로 해야 네임스페이스, 즉 충돌이 되지않고 공간이 나눠진다.
        credentials: {
          username: '',
          password: '',
        },
        loading: false,
        errors: [],
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          console.log('로그인 성공')
        } else {
          console.log('로그인 실패')
        }
      },
      checkForm() {
        // error 에 누적되어있는 값을 초기화
        this.errors = []

        // 검증 form
        // id를 입력하지 않는 경우 (비어있는 경우)
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        // 길이가 너무 짧은 경우 (8자 이하)
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        // 정상인 것을 판단 => error 배열이 0 일 때 push된 error 가 하나도 없을 때
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>

<style>

</style>
```



#### :black_circle: axios

```bash
$ npm i axios
```

- axios로 login 요청을 보낼 것



###### LoginForm.vue

```vue
<script>
  import axios from 'axios'
  export default {
    name: 'LoginForm',
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        loading: false,
        errors: [],
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          this.loading = true // 스피너가 돌게 될 것
          // axios.get('django url')
          axios.get('http://127.0.0.1:8000', this.credentials) // credentials 통째로 아이디와 패스워드를 넘김
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        console.log('로그인 검증 실패')
        }
      },
      ...
</script>
```

- `import axios from 'axios'`



###### LoginForm.vue : 다듬기

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border">
      <span class="sr-only">Loading...</span>
    </div>
      
    <!-- div => form태그로 바꿔준 후 form태그에 이벤트 속성을 줄 것
 => @submit="login" 하지만 로그인 실패시 페이지가 redirect 되어 오류창이 떴다가 사라진다. 주소 가장뒤에 ?이 붙은 것을 확인 가능 -->
    <form v-else class="login-form" @submit.prevent="login">
      <!-- prevent => 기본적인 활동으로 redirect하게 하지 않은 것 -->
      <div v-if="errors.length" class="error-list alert alert-danger" role="alert">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">"{{ error }}"</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요"
        v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요"
        v-model="credentials.password"
        >
      </div>
      <!-- type을submit으로 -->
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>
```





### :purple_heart: CORS 

- Cross-Origin Resource Sharing

[HTTP 접근 제어 (CORS)](https://developer.mozilla.org/ko/docs/Web/HTTP/Access_control_CORS)

- 연결시키려는 도메인의 주소가 각기 다르기 때문에, sharing을 도와주는 기술
- django와 vue는 도메인은 같지만 포트가 다르기때문에 충돌이 일어난다. **=>** django에서 denine 요청을 보낸다.



#### 정의

- 한 도메인에서 로드되어 다른 도메인에 있는 리소스와 상호작용 하는 것
- 즉, 도메인이나 포트가 다른 서버의 자원을 요청하는 메커니즘



#### 문제 상황

1. 요청을 할 때 cross-origin HTTP 에 의해 요청을 한다.
2. 하지만 CORS 와 같은 상황이 발생하면 외부 서버에 의한 요청 데이터를 브라우저에서 차단하기 때문에 (보안 목적) 정상적으로 데이터를 받을 수 없다.
3. 예를 들어, http://localhost:8080/ 에서 vue를 실행하고,  http://localhost:8000/ 에서 django를 실행할 경우 포트가 달라 다른 도메인으로 인지하고 브라우저가 요청을 차단한다. 



#### 해결 방법

1. 서버(django)와 클라이언트(vue)가 같은 도메인과 포트를 사용하도록 한다.
2. 서버에서 cross-origin HTTP 요청을 허가한다. (우리가 해결할 방법)
   - 실제 API 서버들은 이러한 CORS 제한과 관련된 처리를 모두 해두어야 한다.





- 최상단 폴더인 것을 확인
  **ls** : todo-front / todo-back

> ##### 설치 순서
>
> DRF
>
> DRF-JWT
>
> CORS

[django-rest-framework-jwt](https://jpadilla.github.io/django-rest-framework-jwt/)

[django-cors-headers](https://github.com/adamchainz/django-cors-headers#setup)

```bash
$ pip install djangorestframework
$ pip install djangorestframework-jwt
$ pip install django-cors-headers
```

```python
import os
import datetime

INSTALLED_APPS = [
    'todos',
    'rest_framework',
    'corsheaders',
    ...
]

# DRF jwt 설정 cors보다 먼저 설치 되었으니 미들웨어보다 위쪽에
REST_FRAMEWORK = {
    # 로그인 여부를 확인하는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 인증 여부를 확인하는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # JWT를 encrypt(암호화) 함. 절대 외부 노출 금지
    'JWT_SECRET_KEY': SECRET_KEY,
    # 토큰 해싱 알고리즘 (defalt: HS256)
    'JWT_ALGORITHM': 'HS256',
    # 7일간 유효한 토큰
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 토큰 갱신 허용 여부
    'JWT_ALLOW_REFRESH': True, # 갱신 사용
    # 유효기간 연장시 28일 마다 토큰 갱신
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28), # ~일마다 토큰갱신
}

MIDDLEWARE = [ 
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

# 원래대로라면 아래와 같이 허용할 도메인 리스트를 작성해야 하지만
# 개발 테스트 단계이므로 모든 요청을 허용하기 위해 주석처리 한다.
# CORS_ORIGIN_WHITELIST = [
# ]

# 모든 요청을 허용하도록 설정
CORS_ORIGIN_ALLOW_ALL = True

# 눈에는 보이진 않지만 기본 설정 값 : AUTH_USER_MODEL = 'auth.user'
AUTH_USER_MODEL = 'todos.User'
```

- setting.py 에 등록

- `'django.middleware.common.CommonMiddleware',` 중복되는 이 코드를 삭제 후 위의 코드 두 줄 추가
- [CORS_ORIGIN_ALLOW_ALL](https://github.com/adamchainz/django-cors-headers#cors_origin_allow_all)



###### todo-back/todos/models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```



- todo-back 에서

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

- migrate 후 서버 접속, http://127.0.0.1:8000/api-token-auth/ 로 들어가면 GET방식으로 들어가서 키를 줄수 없다고  뜬다.

![image](https://user-images.githubusercontent.com/52684457/69106512-f7235b00-0ab1-11ea-97f8-154ff5a0c641.png)

- createsuperuser 로 만든 관리자로 POST 접속을 해주면 해당token이 발급 된다.

- **[JWT](https://jwt.io/#libraries-io)** 해당 사이트에 접속 후 Encoded에 토큰을 입력하면 Decoded에 코드 해석이 나온다. (`secret base64 encoded`를 체크해주어야 해당 사이트의 번역코드로 나온다. )



- **터미널을 두개를 켜서** 하나는 django, 하나는 vue 서버를 열어준다. (django 서버는 이미 켜져있을 경우 켜진 상태로 그대로 유지)

```bash
$ python manage.py runserver
```

```bash
$ npm run serve
```



###### LoginForm.vue

```vue

<script>
  import axios from 'axios'
  export default {
    name: 'LoginForm',
    data() {
      return {
        ...
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // 1. django jwt 를 생성하는 주소로 요청을 보냄
          // 이때 post 요청으로 보내야 하며 사용자가 입력한 로그인 정보(credentials)를 같이 넘겨야 함
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials) // credentials 통째로 아이디와 패스워드를 넘김
          .then(res => {
            // 2. 로그인 이후에 loading 의 상태를 다시 false 로 변경 
            // 그래야 spinner 가 계속 돌지 않고 로그인 form을 받아 볼 수 있음
            this.loading = false
            console.log(res)
          })
          .catch(err => {
            // 2. 로그인 실패 시 loading 의 상태를 다시 false 로 변경 
            this.loading = false
            console.log(err)
          })
      } else {
        console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        // error 에 누적되어있는 값을 초기화
        this.errors = []

        // 검증 form
        // id를 입력하지 않는 경우 (비어있는 경우)
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        // 길이가 너무 짧은 경우 (3자 이하)
        if (this.credentials.password.length < 3) {
          this.errors.push("비밀번호는 3자 이상 입력해주세요.")
        }
        // 정상인 것을 판단 => error 배열이 0 일 때 push된 error 가 하나도 없을 때
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>
```

- admin의 비밀번호가 8자 이하라서 길이 오류코드를 3자 이하로 조정 해주었다. (그렇지 않으면 오류 발생) 로그인 실패 시, 주석처리까지 해주는게 좋을 것 같음.



- 인증 된 유저로 로그인을 하면 콘솔에 토큰 확인이 가능
- res **=>** data **=>** token

![image](https://user-images.githubusercontent.com/52684457/69107549-18d21180-0ab5-11ea-8d3a-1ed4ccef359e.png)



- vue 서버를 꺼준 후,

```bash
$ npm i vue-session
```

- [vue-session](https://www.npmjs.com/package/vue-session) 의 To install the plugin, do the following: 을 따른다.



###### todo-front/src/views/main.js

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueSession)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

- `import VueSession from 'vue-session'`
- `Vue.use(VueSession)`





![image](https://user-images.githubusercontent.com/52684457/69108510-35bc1400-0ab8-11ea-966f-778b0542cfbb.png)

> #### [Reference](https://www.npmjs.com/package/vue-session#reference)
>
> ##### this.$session.start()
>
> - session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작
>
> ##### this.$session.set(key,value)
>
> - session 에 해당 key에 맞는 값을 저장
>
> ##### this.$session.has(key)
>
> - key(JWT) 가 존재하는지 여부를 확인
>
> ##### this.$session.destroy()
>
> - 세션을 삭제



0. ##### django

- 회원가입

1. ##### Veu **=>** django

- 로그인 정보(credentials) 를 django 서버로 보냄

2. ##### Django

- Vue 에서 받은 유저정보에 해당하는 고유한 Web Token 발급

3. ##### Django => Vue

- 해당 유저에 대한 토큰을 Vue로 보냄

4. ##### Vue 

- Django 에서 받은 토큰을 vue-session 을 통해 저장(이 시점부터 vue 에서는 로그인 성공 상태)

5. ##### Vue => Django

- vue-session 에 저장된 토큰을 가지고 django에 로그인 요청

6. ##### Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인(세션*(django)* 에 저장된 토큰 == 요청자의 토큰)
- 결국 마지막에 로그인 처리해주는 것은 django



```vue
<script>
  import axios from 'axios'
  import router from '../router'
    ...
  export default {
    ...
    methods: {
      login() {
        if (this.checkForm()) {
          this.loading = true
          // 1. django jwt 를 생성하는 주소로 요청을 보냄
          // 이때 post 요청으로 보내야 하며 사용자가 입력한 로그인 정보(credentials)를 같이 넘겨야 함
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials) // credentials 통째로 아이디와 패스워드를 넘김
          .then(res => {
            this.$session.start()
            this.$session.set('jwt', res.data.token)
            router.push('/') // 로그인 후 메인 페이지로 이동하게 되는 것 
            // 2. 로그인 이후에 loading 의 상태를 다시 false 로 변경 
            // 그래야 spinner 가 계속 돌지 않고 로그인 form을 받아 볼 수 있음
            // this.loading = false // 실패시에만 false 하면 되기 때문에 필요 없어 짐
          })
          .catch(err => {
    }
```

- router 를 import
- `.start()` 를 통해 `session-id` : `sess` + `Date.now()` 가 만들어짐
- `.set()` 을 통해 `jwt: jwt값` 이 만들어짐

![image](https://user-images.githubusercontent.com/52684457/69109369-e4f9ea80-0aba-11ea-93f3-299f6e30d3b8.png)

- 성공적인 로그인 시도 시, 콘솔에 로그인 검증 실패가 뜨지 않고 Home으로 돌아간다. 



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'

export default {
  name: 'home',
  component: {

  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) { // 인증된 사용자가 아니라면
        router.push('/login') // 로그인 폼으로 보낼 것
      }
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted () {
    this.checkLoggedIn()
  },
}
</script>

```

- 서버를 다시 껐다 켜보자.

![image](https://user-images.githubusercontent.com/52684457/69110479-41aad480-0abe-11ea-9779-1e9960f61a32.png)

- 로그인 시 자동으로 Home으로 가는 것을 확인 가능



##### Vue의 라이프 사이클 

> [라이프사이클 다이어그램](https://kr.vuejs.org/v2/guide/instance.html#%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8)
>
> 1. Vue instance 생성 (create)
> 2. DOM 에 부착(mounted)
> 3. Update
> 4. Destroy (삭제)



이어서

### :dog: Djaogn : CRUD



###### todo-back/todoback(project)/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/v1/', include('todos.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
```

- 저장 하기 전에



###### todo-back/todos(app)/urls.pt

- app의 urls.py가 없기 때문에 작성

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
]
```



###### todo-back/todos(app)/serializers.py

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)
```



###### todo-back/todos(app)/views.py

```python
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permissions_classes, authentication_classes
# from rest_framework.permission import IsAuthenticated
# from rest_framework.authentication import JSONWebTokenAuthentication
from .serializers import TodoSerializer

# Create your views here.


@api_view(['POST'])
# 아래의 두가지는 생략이 가능, settings.py에서 DEFAULT 로 REST_FRAMEWORK 설정을 했기 때문
# 1. 인증 받은 사용자만 허가(로그인 여부만 체크)
# @permission_classes((IsAuthenticated, ))
# 2. jwt 인증
# @authentication_classes((JSONWebTokenAuthentication))
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)
```

- [Function Based Views](https://www.django-rest-framework.org/api-guide/views/#function-based-views) : `from rest_framework.decorators import api_view`

- http://127.0.0.1:8000/api/v1/todos/ 접속하게 되면

  ![image](https://user-images.githubusercontent.com/52684457/69111752-d6fb9800-0ac1-11ea-86dd-fab244b8101c.png)

  - 터미널에서 401 error가 뜨는 것을 확인 가능하다.

  - [HTTP 상태 코드](https://developer.mozilla.org/ko/docs/Web/HTTP/Status) / [`401 Unauthorized`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/401)



#### :orange: Postman 으로 확인

##### :large_orange_diamond: token

![image](https://user-images.githubusercontent.com/52684457/69112403-7bcaa500-0ac3-11ea-9afc-38d37d7bec2d.png)

- 토큰 값 확인 가능

![image](https://user-images.githubusercontent.com/52684457/69112497-b9c7c900-0ac3-11ea-804b-c9c5bf37cdae.png)

- 이 상태 그대로 넣으려면 401 error가 뜬다.



##### :large_orange_diamond: CREATE​

![image](https://user-images.githubusercontent.com/52684457/69112670-26db5e80-0ac4-11ea-92a5-89deacb46681.png)

- headers에서 토큰값을 Authorization 로 넣어주면 제대로 글이 작성하는 것을 확인 가능



###### views.py

```python
from .models import Todo

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id): # django안에서만 사용하는 것이 아닌, 범용적이기 때문에 api사용시에는 id 사용
    todo = get_object_or_404(Todo, pk=id) # djago에서 가리키는 id => pk, 기존의 todo
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data) # 현재 데이터 정보, data => 새로 작성할 todo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 : 해당하는 컨텐츠가 없는 경우 (삭제를 했기 때문에 해당 데이터가 이제 존재하지 않음을 알려줌)
        return Response(status=204)
```



###### urls.py(app)

```python
urlpatterns = [
    ...
    path('todos/<int:id>/', views.todo_update_delete),
]
```



##### :large_orange_diamond: UPDATE & DELETE​

![image](https://user-images.githubusercontent.com/52684457/69117431-fb13a500-0ad2-11ea-8dd9-3569866ba659.png)

- Headers에서 토큰값을 담고 PUT으로 요청을 보내면 수정 사항을 확인 가능

- DELETE 요청을 보낼때는 token 값만 입력해주면 삭제가 된다. (삭제되었기 때문에 아무것도 뜨지 않는다.)



###### serializers.py

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model # 추가
from .models import Todo

User = get_user_model() # 표현식을 위해 따로 담아서 사용(권장)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
```



[`from django.contrib.auth.models import AbstractUser`](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L315) 이 기반

- 외부 라이브러리(rest_framework)때문에 암호화가 제대로 되지 않는다. (django만 사용 할 때에는 자동 암호화가 된다.)



###### views.py

```python
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny # AllowAny 전체 허용
# from rest_framework.authentication import JSONWebTokenAuthentication
from .serializers import TodoSerializer, UserCreationSerializer
from .models import Todo

User = get_user_model()
...

@api_view(['POST'])
# 모두에게 접근 허용(로그인 여부 판단 안함)
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
```



###### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    ...
    path('users/', views.user_signup),
]
```



##### :large_orange_diamond: SIGN UP​

![image](https://user-images.githubusercontent.com/52684457/69118124-91e16100-0ad5-11ea-9e20-1db1bb7104e6.png)

- 회원가입이 되는 것을 확인가능

  ```python
  if serializer.is_valid(raise_exception=True):
      user = serializer.save()
      user.set_password(request.data.get('password'))
      user.save()
      print(serializer.data)
      return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
  ```

  - 이러한 과정 없이

  ```python
  if serializer.is_valid(raise_exception=True):
      serializer.save()
      print(serializer.data)
      return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
  ```

  - 바로 `.save()` 세이브하게 된다면, 

   ![image](https://user-images.githubusercontent.com/52684457/69119204-2ef1c900-0ad9-11ea-84b6-af2ef7b5ed98.png)

  - 패스워드가 암호화 되는 것을 확인 할 수 있다.
  - 또한 토큰값이 받아지지 않는 것이 받아진다.





###### serializers.py

```python
class UserSerializer(serializers.ModelSerializer):
    todo_set = TodoSerializer(many=True) # 여러개의 값이 들어갈 수 있기 때문에
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set',)
```



###### views.py

```python
from rest_framework.response import Response
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny # AllowAny 전체 허용
# from rest_framework.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from .models import Todo

User = get_user_model()

...

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        # return Response(status=403) 
        # 클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않음. 
        # 401과 다르게 403은 클라이언트가 누구인지 알고 있다. 
        # (인증은 맞지만 권한이 없는 유저)
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)
```



###### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('todos/<int:id>/', views.todo_update_delete),
    path('users/', views.user_signup),
    path('users/<int:id>/', views.user_detail),
]
```



##### :large_orange_diamond: USER DETAIL​

![image](https://user-images.githubusercontent.com/52684457/69119538-51d0ad00-0ada-11ea-821e-4061d2990b20.png)

- 해당 id의 게시글 조회 

- 만약 다른 id의 글을 조회하고 싶다면, 그 id의 토큰을 가져오면 된다.

  (*이 문서 내의 Postman 가장 초반 부분를을 확인* )



#### :page_with_curl: 최종본(Django)

> #### PROJECT
>
> ###### urls.py
>
> ```python
> from django.contrib import admin
> from django.urls import path, include
> from rest_framework_jwt.views import obtain_jwt_token
> 
> urlpatterns = [
>     path('api/v1/', include('todos.urls')),
>     path('api-token-auth/', obtain_jwt_token),
>     path('admin/', admin.site.urls),
> ]
> ```
>
> 
>
> #### APP
>
> ##### models.py
>
> ```python
> from django.db import models
> from django.conf import settings
> from django.contrib.auth.models import AbstractUser
> 
> # Create your models here.
> class User(AbstractUser):
>     pass
> 
> class Todo(models.Model):
>     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     title = models.CharField(max_length=50)
>     completed = models.BooleanField(default=False)
> 
>     def __str__(self):
>         return self.title
> ```
>
> 
>
> ###### serializers.py
>
> ```python
> from rest_framework import serializers
> from django.contrib.auth import get_user_model
> from .models import Todo
> 
> User = get_user_model()
> 
> class TodoSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Todo
>         fields = ('id', 'user', 'title', 'completed',)
> 
> class UserCreationSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = User
>         fields = ('id', 'username', 'password',)
> 
> class UserSerializer(serializers.ModelSerializer):
>     todo_set = TodoSerializer(many=True) # 여러개의 값이 들어갈 수 있기 때문에
>     class Meta:
>         model = User
>         fields = ('id', 'username', 'todo_set',)
> ```
>
> 
>
> ##### urls.py
>
> ```python
> from rest_framework import serializers
> from django.contrib.auth import get_user_model
> from .models import Todo
> 
> User = get_user_model()
> 
> class TodoSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Todo
>         fields = ('id', 'user', 'title', 'completed',)
> 
> class UserCreationSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = User
>         fields = ('id', 'username', 'password',)
> 
> class UserSerializer(serializers.ModelSerializer):
>     todo_set = TodoSerializer(many=True) # 여러개의 값이 들어갈 수 있기 때문에
>     class Meta:
>         model = User
>         fields = ('id', 'username', 'todo_set',)
> ```
>
> 
>
> ##### views.py
>
> ```python
> from rest_framework.response import Response
> from django.http import HttpResponseForbidden
> from django.shortcuts import render, get_object_or_404
> from rest_framework.decorators import api_view, permission_classes, authentication_classes
> from rest_framework.permissions import IsAuthenticated, AllowAny # AllowAny 전체 허용
> # from rest_framework.authentication import JSONWebTokenAuthentication
> from django.contrib.auth import get_user_model
> from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
> from .models import Todo
> 
> User = get_user_model()
> 
> # Create your views here.
> 
> 
> @api_view(['POST'])
> # 아래의 두가지는 생략이 가능, settings.py에서 DEFAULT 로 REST_FRAMEWORK 설정을 했기 때문
> # 1. 인증 받은 사용자만 허가(로그인 여부만 체크)
> # @permission_classes((IsAuthenticated, ))
> # 2. jwt 인증
> # @authentication_classes((JSONWebTokenAuthentication))
> def todo_create(request):
>     serializer = TodoSerializer(data=request.POST)
>     if serializer.is_valid():
>         serializer.save()
>         return Response(serializer.data)
>     return Response(status=400) # bad request => 400
> 
> @api_view(['PUT', 'DELETE'])
> def todo_update_delete(request, id): # django안에서만 사용하는 것이 아닌, 범용적이기 때문에 api사용시에는 id 사용
>     todo = get_object_or_404(Todo, pk=id) # djago에서 가리키는 id => pk, 기존의 todo
>     if request.method == 'PUT':
>         serializer = TodoSerializer(todo, data=request.data) # 현재 데이터 정보, data => 새로 작성할 todo
>         if serializer.is_valid():
>             serializer.save()
>             return Response(serializer.data)
>         return Response(serializer.errors, status=400)
>     elif request.method == 'DELETE':
>         todo.delete()
>         # 204 : 해당하는 컨텐츠가 없는 경우 (삭제를 했기 때문에 해당 데이터가 이제 존재하지 않음을 알려줌)
>         return Response(status=204)
> 
> @api_view(['POST'])
> # 모두에게 접근 허용(로그인 여부 판단 안함)
> @permission_classes((AllowAny, ))
> def user_signup(request):
>     serializer = UserCreationSerializer(data=request.data)
>     if serializer.is_valid(raise_exception=True):
>         user = serializer.save()
>         user.set_password(request.data.get('password'))
>         user.save()
>         # print(serializer.data)
>         return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
> 
> @api_view(['GET'])
> def user_detail(request, id):
>     user = get_object_or_404(User, pk=id)
>     if request.user != user:
>         # return Response(status=403) 
>         # 클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않음. 
>         # 401과 다르게 403은 클라이언트가 누구인지 알고 있다. 
>         # (인증은 맞지만 권한이 없는 유저)
>         return HttpResponseForbidden()
>     serializer = UserSerializer(user)
>     return Response(serializer.data)
> 
> ```





## :large_blue_circle: Vue <=> Django

- 직접적으로 통신하는 것은 Hoem.vue 여기서 TodoList.vue로 올려줄 것



##### :large_blue_diamond: READ

###### todo-front/src/components/TodoList.vue

```vue
<template>
  <div class="todo-list">

  </div>
</template>

<script>
  export default {
    name: 'TodoList',
  }
</script>

<style>

</style>
```

- todolist를 보여줄 새로운 component를 기본 틀 작성



```bash
$ npm i jwt-decode
```

- 디코드 라이브러리 설치
- 유저정보만 decode해서 가져와야 함



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoList/>
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'
import TodoList from '@/components/TodoList'
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: [], // 여기에 todolist 가 올 것
    }
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) { // 인증된 사용자가 아니라면
        router.push('/login') // 로그인 폼으로 보낼 것
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token //JMT(공백)
        }
      }
      // axios를 하기 전에
      const user_id = jwtDecode(token).user_id
      console.log(jwtDecode(token))
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted () {
    this.checkLoggedIn()
    this.getTodos()
  },
}
</script>

```

![image](https://user-images.githubusercontent.com/52684457/69121041-96f6de00-0ade-11ea-8a0e-ce891dec052b.png)



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <!-- 왼쪽, 자식리스트(props) 오른쪽, 받는 todos -->
    <TodoList :todos="todos" /> 
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'
import TodoList from '@/components/TodoList'
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: [], // 여기에 todolist 가 올 것
    }
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) { // 인증된 사용자가 아니라면
        router.push('/login') // 로그인 폼으로 보낼 것
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token //JMT(공백)
        }
      }
      // axios를 하기 전에
      const user_id = jwtDecode(token).user_id
      console.log(jwtDecode(token))
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted () {
    this.checkLoggedIn()
    this.getTodos()
  },
}
</script>
```



###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
    <div class="card-body">
      <span>{{ todo.title }}</span>
    </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      }
    }
  }
</script>

<style>

</style>
```



##### :large_blue_diamond: CREATE

###### todo-front/src/components/TodoInput

```vue
<template>
  <div class="todo-input">
    <form class="input-group mb-3">
      <input type="text" class="form-control">
      <button type="submit" class="btn btn-primary mx-2">+</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'TodoInput',
  }
</script>

<style>

</style>
```



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput/>
    <TodoList :todos="todos" /> 
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
    ...
```

- component 등록, 태그 추가



###### TodoInput.vue

```vue
<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="createTodo"> <!-- prevent : 기본적인 리다이렉트를 막음 -->
      <input type="text" class="form-control" v-model="title">
      <button type="submit" class="btn btn-primary mx-2">+</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'TodoInput',
    data() {
      return {
        title: '' // empty
      }
    },
    methods: {
      createTodo() {
        this.$emit('createTodo', this.title)
        this.title = '' // 보내고 난 후 초기화
      }
    },
  }
</script>

<style>

</style>
```





#### FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가. (`FormData.append()`)
- `FormData.append(name, value)` 
- **name** : value 에 포함되는 데이터 필드 이름
- **value** : 필드 값



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <!-- 왼쪽, 자식리스트(props) 오른쪽, 받는 todos -->
    <TodoInput @createTodo="createTodo"/> <!-- 왼쪽 : 부모 component에서 실행할 method, 오른쪽 : 받아온 데이터-->
    <TodoList :todos="todos" /> 
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: [], // 여기에 todolist 가 올 것
    }
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) { // 인증된 사용자가 아니라면
        router.push('/login') // 로그인 폼으로 보낼 것
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token //JMT(공백)
        }
      }
      // axios를 하기 전에
      const user_id = jwtDecode(token).user_id
      console.log(jwtDecode(token))
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      this.$session.start() // 세션 활성화
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT '+token
        }
      }
      const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()

      // Postman의 body로 들어가는 코드
      requestForm.append('user', user_id)
      requestForm.append('title', title) // createTodo 의 title (자식이 보낸 인자)

       axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, requestHeader)
        .then(res => {
          this.todos.push(res.data)
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted () {
    this.checkLoggedIn()
    this.getTodos()
  },
}
</script>
```



##### :large_blue_diamond: UPDATE & DELETE

- DELETE

###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
    <div class="card-body">
      <span>{{ todo.title }}</span>
      <span @click="deleteTodo(todo)">🗑️</span>
    </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      },
    },
    methods: {
      deleteTodo(todo) {
        this.$session.start()
        const token = this.$session.get('jwt')
        const requestHeader = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  }
</script>

<style>

</style>
```

- **[Winodw Emoji](https://emojipedia.org/wastebasket/)**

![image](https://user-images.githubusercontent.com/52684457/69198013-a590d400-0b76-11ea-8e43-ade186975fe2.png)

- 쓰레기통 버튼을 누르면 요청한 url( <u>`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader</u> )과 빈 값의 data를 확인 가능 (삭제가 되었기 때문에 빈 값)

- 하지만 아직 실시간으로 반영이 되지 않는다.

  **=>** Array 에서 특정 아이템을 삭제

#####  **`splice()`** 

- 배열의 기존 요소를 삭제 혹은 교체하거나 새 요소를 추가하여 배열의 내용을 변경

**문법** 

- `Array.splice(시작 index, 삭제할 요소 수, 배열에 추가할 요소)`

- `splice(start, deleteCount, [item1, item2, item3...])`

  1. ##### start

     - 배열의 변경을 시작할 index
     - 배열의 길이보다 큰 값이면 시작 인덱스틑 배열의 길이로 설정
     - 음수인 경우 배열의 가장 마지막에서 시작
     - 절대 값이 배열의 길이보다 큰 경우는 0으로 설정

  2. ##### deleteCount

     - 배열에서 제거할 요소의 수
     - 생략할 경우 start 부터 모든 요소를 제거
     - 0 이하인 경우 어떤 요소도 삭제하지 않음. 이때는 최소한 하나의 추가할 새로운 요소 지정

  3. ##### item1, item2, item3...

     - 비열에 추가할 요소
     - 추가할 아무 요소도 지정하지 않으면 요소를 제거만 한다.
     - 즉, 추가할 요소를 지정하지 않으면 원본 배열의 특정 인덱스에서 몇개의 요소를 삭제 할지 정한다.

###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
    <div class="card-body">
      <span>{{ todo.title }}</span>
      <span @click="deleteTodo(todo)">🗑️</span>
    </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      },
    },
    methods: {
      deleteTodo(todo) {
        this.$session.start()
        const token = this.$session.get('jwt')
        const requestHeader = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
        .then(res => {
          console.log(res)
          const targetTodo =  this.todos.find(function(el) {
            return el === todo // element와 todo의 배열과 같은것을 return
          })
          const idx = this.todos.indexOf(targetTodo) // targetTodo 의 index
          if (idx > -1) {
            this.todos.splice(idx, 1)
          }
        })
        .catch(err => {
          console.log(err)
        })
      },
    },
  }
</script>

<style>

</style>
```

- 서버를 껐다 켜면, 바로 삭제가되는 것을 확인 가능하다.
- 당시 `Note that the development build is not optimized.
    To create a production build, run npm run build.` 문구가 떠서 run build를 했더니 콘솔의 오류가 없어 졌다.



- UPDATE

###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
    <div class="card-body">
      <span @click="updateTodo(todo)" :class="{complete: todo.completed }">{{ todo.title }}</span>
      <span @click="deleteTodo(todo)">🗑️</span>
    </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      },
    },
    methods: {
      deleteTodo(todo) {
        this.$session.start()
        const token = this.$session.get('jwt')
        const requestHeader = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
        .then(res => {
          console.log(res)
          const targetTodo =  this.todos.find(function(el) {
            return el === todo // element와 todo의 배열과 같은것을 return
          })
          const idx = this.todos.indexOf(targetTodo) // targetTodo 의 index
          if (idx > -1) {
            this.todos.splice(idx, 1)
          }
        })
        .catch(err => {
          console.log(err)
        })
      },
      updateTodo(todo) {
        this.$session.start()
        const token = this.$session.get('jwt')
        const requestHeader = {
          headers: {
            Authorization: 'JWT ' + token
          }
        }
        const requestForm = new FormData()
        // 수정 전 기존 로직에서 데이터를 보내고 FormData에 담아야 한다.
        requestForm.append('id', todo.id)
        requestForm.append('title', todo.title)
        requestForm.append('user', todo.user)
        requestForm.append('completed', !todo.completed) // true | false기 때문에 ! (즉각 반영하기 위함)
        
        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, requestHeader)
          .then(res => {
            console.log(res)
            todo.completed = !todo.completed
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  }
</script>

<style>
.complete {
  text-decoration: line-through;
  color: rgb(146, 143, 143);
}
</style>
```

- `todo.completed = !todo.completed` 구문을 넣지 않으면 화면에 바로 반영이 되지 않는다.

- 이제 텍스트를 클릭하면 바로 ~~중앙선~~ 이 생기면서 흐릿해진다.
  **=>** \<style>

 

#### :large_blue_diamond: Logout

###### App.vue

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <a @click.prevent="logout" href="#">Logout</a> <!-- prevent로 로그아웃 메서드만 작동하도록 -->
    </div>
    <div class="row justify-content-center">
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```

- 로그인 여부에 따른 메뉴 바가 달라져야 할 필요가 있을 것 같다.



##### `update`

타입

- function

상세

- 데이터가 변경되어 DOM이 re-render 되고 patch 되면 호출된다.
  (DOM 변화에 반응)
- DOM의 변화는 일반적으로 데이터의 변경에 의해 re-render 되는 시점에 일어난다.
- 데이터의 변화(상태의 변화)에 반응하기 위해서는 computed 나 watch를 사용하는 것이 좋다.



###### App.vue

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <!-- router 속성 안의 to로 인해 연결 -->
      <div v-if="isAuthenticated">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="#">Logout</a> <!-- prevent로 로그아웃 메서드만 작동하도록 -->
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <div class="row justify-content-center">
      <router-view class="col-6"/>
  </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated: this.$session.has('jwt')
    }
  },
  updated () {
    // DOM 이 re-render 될 때 다시 토큰의 존재 여부를 확인
    this.isAuthenticated = this.$session.has('jwt')
  },
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```

- div 태그 닫는것을 주의하자.



### :blue_heart: Vuex

- Status 관리를 위해 탄생
- 컴포넌트 간의 통신 혹은 데이터 전달을 유기적으로 관리
- 컴포터는 간의 통신 혹은 이벤트 등의 관계를 한곳에서 관리하기 쉽게 구조화

```
현재 todo 프로젝트에서는 Auth 정보(로그인 혹은 로그아웃)은 django로 요청을 보낼 때 항상 필요하기 때문에, 결국 요청을 수행하는 모든 컴포넌트에서 알고 있어야 하고 그 정보를 내가 필요한 순간에 활용할 수 있어야 한다.
```

> 1. state
>    - 상태(데이터)
> 2. Getters
>    - computed
> 3. Mutations
>    - methods
>    - state를 변경하기 위해서 반드시 동기적은 method 만 사용 가능 (비동기 함수는 쓸 수 없음)
>    - 첫번째 인자는 항상 state, 호출은 commit 으로
> 4. Actions
>    - 모든 methods
>    - 비동기 처리가 가능한 methods
>    - **주의 사항** : mutations와 구분된 이유는 다양한 컴포넌트에서 vuex 를 통해 상태과니, 메서드 호출 등을 하게 될텐데 그 때 동기와 비동기를 구분하기 위해, 
>    - 첫번째 인자는 항상 context(state/commit/dispatch 등), 호출은 dispatch로 된다.



- vue ui를 켜서 공식 vuex 플러그인 설치
- src 폴더 내에 store라는 폴더가 생성된것을 확인가능

- store 폴더 내에 modules라는 파일을 생성 후 그 안에 auth.js 파일 생성

###### sotre/index.js

```js
import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
  }
})
```



###### store/auth.js

```js
import jwtDecode from 'jwt-decode'

const state = { // 동기적 함수
  token = null, // 처음에는 토큰이 없으므로
}

// data(state) 를 변경하지 않음
// data 를 원본 그대로 혹은 가공된 데이터를 사용
const getters = {
  isLoggedIn: function(state) {
    // state 토큰에 따라 로그인이 되어있는지 안되어있는지 만드는 함수
    return state.token ? true : false
  },
  requestHeader: function(state) {
    return {
      headers: {
        Authorization: 'JWT' + state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null // 있을때만 user.id를 가져오고, 없으면 null
  }
}

// 상태(토큰)을 받아와서 state를 update
const mutations = {
  setToken: function(state, token) {
    state.token = token // 새로받은 토큰을 할당 (state.token이 인자의 token)
  },
}

// 비동기 로직 (axtios 로 django 서버에 로그인 / 로그아웃 요청)
const actions = {
  // commit은 첫번째 인자로 mutations에 정의한 함수를 받는다.
  // 두번째 인자로 토큰을 받아서, mutations에 정의 된 함수를 통해 state를 변경한다.
  login: function(options, token) {
    options.commit('setToken', token)
  },
  // 로그아웃의 경우 추가로 받는 인자는 없고 token의 상태를 null로 변경
  logout: function(options) {
    options.commit('setToken')
  }
}

export default {
  state,
  mutations,
  actions,
  getters,
}
```



###### auth.js

```js
import jwtDecode from 'jwt-decode'

const state = { // 동기적 함수
  token: null, // 처음에는 토큰이 없으므로
  loading: false,
}

// data(state) 를 변경하지 않음
// data 를 원본 그대로 혹은 가공된 데이터를 사용
const getters = {
  isLoggedIn: function(state) {
    // state 토큰에 따라 로그인이 되어있는지 안되어있는지 만드는 함수
    return state.token ? true : false
    // 있을때만 user.id를 가져오고, 없으면 null
  },
  requestHeader: function(state) {
    return {
      headers: {
        Authorization: 'JWT ' + state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  }
}


// 상태(토큰)을 받아와서 state 를 update
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading:function(state, status) {
    state.loading = status
  }
}

// 비동기 로직 (axtios 로 django 서버에 로그인 / 로그아웃 요청)
//  options
// action 에서 사용할 수 있도록 만든 객체 /vuex 에서 제공하는 actions 함수에서 사용할 수 있는 option 들이 있는 객체
const actions = {
  // commit은 첫번째 인자로 mutations에 정의한 함수를 받는다.
  // 두번째 인자로 토큰을 받아서, mutations에 정의 된 함수를 통해 state를 변경한다.
  login: function(options, token) {
    options.commit('setToken', token)
  },
  // 로그아웃의 경우 추가로 받는 인자는 없고 token 의 상태를 null 로 변경
  logout: function(options) {
    options.commit('setToken')
  },
  startLoading: function(options) {
    options.commit('setLoading', true)
  },
  endLoading: function(options) {
    options.commit('setLoading', false)
  }
}


export default {
  state,
  mutations,
  actions,
  getters,
}
```

- auth.js 가 준비 되었으면 필요없는 코드를 줄일 수 있다.



###### App.vue

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <div class="row justify-content-center">
      <router-view class="col-6"/>
  </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  // data() {
  //   return {
  //     isAuthenticated: this.$session.has('jwt')
  //   }
  // },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn
    }
  },
  // updated () {
  //   // DOM 이 re-render 될 때 다시 토큰의 존재 여부를 확인
  //   this.isAuthenticated = this.$session.has('jwt')
  // },
  methods: {
    logout() {
      // this.$session.destroy()
      // 지우는 것이 아닌, action으로 로그아웃을 구현해 놓음
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```



###### Home.vue

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <!-- 왼쪽 : 부모 component에서 실행할 method, 오른쪽 : 받아온 데이터-->
    <TodoInput @createTodo="createTodo"/>
    <!-- 왼쪽, 자식리스트(props) 오른쪽, 받는 todos -->
    <TodoList :todos="todos" />
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex'

export default {
  name: 'home',
  components: {
    TodoList, TodoInput
  },
  data() {
    return {
      todos: [], // 여기에 todolist 가 올 것
    }
  },
  computed: {
    // spread 문법 => 각각의 getters
    // mapGetthers 함수의 인자로 들어가는 배열에는 getters 에서 정의한 함수들 중에서 가지고 오고 싶은 getter 들을 작성
    // mapGetters : vuex에서 제공하는 특수메서드, ... : (배열을 가져오는 축약어)
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  methods: {
    checkLoggedIn() {
      // this.$session.start()
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
        .then(res => {
          console.log(res)
          this.todos = res.data.todo_set
        })
        .catch(err => {
          console.log(err)
        })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()
      // Postman의 body로 들어가는 코드
      requestForm.append('user', this.userId)
      requestForm.append('title', title) // createTodo 의 title (자식이 보낸 인자)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
        .then(res => {
          this.todos.push(res.data)
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted() {
    this.checkLoggedIn(),
    this.getTodos()
  },
}
</script>
```



###### TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body">
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">🗑️</span>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      },
    },
    computed: {
      requestHeader: function() {
        return this.$store.getters.requestHeader
      }
    },
    methods: {
      deleteTodo(todo) {
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, this.requestHeader)
          .then(res => {
            console.log(res)
            const tartgetTodo = this.todos.find(function(el) {
              return el === todo // element와 todo의 배열과 같은것을 return
            })
            const idx = this.todos.indexOf(tartgetTodo) // targetTodo 의 index
            if (idx > -1) {
              this.todos.splice(idx, 1)
            }
          })
          .catch(err => {
            console.log(err)
          })
      },
      updateTodo(todo) {
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // }
        const requestForm = new FormData()
        requestForm.append('id', todo.id)
        requestForm.append('title', todo.title)
        requestForm.append('user', todo.user)
        requestForm.append('completed', !todo.completed) // true | false기 때문에 ! (즉각 반영하기 위함)

        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, this.requestHeader)
          .then(res => {
            console.log(res)
            todo.completed = !todo.completed
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  }
</script>

<style>
.complete {
  text-decoration: line-through;
  color: rgb(112, 112, 112)
}
</style>

```



###### LoginForm.vue

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">

      <!-- screen reader only 시각 장애인에게 로딩중인 것을 알려주는 것, 우리들 눈에는 none screen으로 보임 -->
      <span class="sr-only">Loading...</span>
    </div>

    <!-- prevent => 기본적인 활동으로 redirect하게 하지 않은 것 -->
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger" role="alert">
        <!-- errors 값이 true값 이라면 -->
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <!-- 키값이 필요하기 때문에 enumerate 형식으로 써주어야 함 -->
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input 
          type="text" 
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력해주세요."
          v-model="credentials.username"
          >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
          type="password" 
          class="form-control"
          id="password" 
          placeholder="비밀번호를 입력해주세요."
          v-model="credentials.password"
          >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import router from '../router'

  export default {
    name: 'LoginForm',
    data() {
      return { // 객체로 해야 네임스페이스, 즉 충돌이 되지않고 공간이 나눠진다.
        credentials: {
          username: '',
          password: '',
        },
        // loading: false,
        errors: [],
      }
    },
    computed: {
      loading: function() {
        return this.$store.state.loading
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // 알아서 바뀔 것이기 때문에 이제 필요 x
          // this.loading = true
          this.$store.dispatch('startLoading') // startLoading => true로 바꿔줌 
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
          .then(res => {
            // this.$session.start()
            // this.$session.set('jwt', res.data.token)
            this.$store.dispatch('endLoading')
            this.$store.dispatch('login', res.data.token)
            // 로그인 후 메인 페이지로 이동하게 되는 것 
            router.push('/')
          })
          .catch(err => {
            // this.loading = false
            this.$store.dispatch('endLoading')
            console.log(err)
          })
        } else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        // error 에 누적되어있는 값을 초기화
        this.errors = []

        // 검증 form
        // id를 입력하지 않는 경우 (비어있는 경우)
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        // if (this.credentials.password.length < 8) {
        //   this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        // }
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>

<style>

</style>
```

- vue session을 사용하다가 store로 바꾸었기 때문에 session이 유지되지 않는다. 그렇기 때문에 새로고침(F5)를 하면 로그아웃이 된다.
- 세션이 하는 역할을 전부 vuex로 바꾸어서 이러한 현상이 일어나는 것



##### `vue-session`

- vuex 는 `vue-session`의 대체가 아니고 서로 하는 일이 다름

- vuex 는 메서드와 data의 대체라고 생각

















