# :dog: Django : axios

- JS의 비동기적 시스템을 적용



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

**shortcut =>** ``<img v-bind:src="vueImage"` **=>**`<img :src="vueImage"`
`v-bind` 생략 가능



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













