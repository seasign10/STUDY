

# :dog:Django

##### :seedling: 100% Python으로 코드를 잘해야 하기 때문에 (python으로 이루어진 framework)

- 다용도 (Versatile)
- 안전 (Secure) *- 보안 관련 / 사이트 위조 ... 기본적 보장*
- 확장 가능성 (Scalable) 
- 완결성 (Complete)
- 쉬운 유지보수 (Maintainable)
- 포터블 (Portable) *- 다양한 운영체제에서 작성 가능 (OS를 가리지 않음)*





> ###### Opinionated (독선적) :paw_prints:
>
> 프레임워크가 지키는 약속이 높을수록 개발자의 자유도가 떨어짐, 유연하지 못한 해결책을 제시할 수 있음 (대부분의 )
>
> ###### Unopinionated (관용적)
>
> 개발자가 처음부터 끝까지 개인적으로 손 볼것이 많다. 개발자의 성격에 따라 달라질 폭이 넓음.
>
> Java는 관용적이기 때문에 생산성이 떨어져 경쟁력 또한 떨어지는 추세.
>
> 
>
> **=>** **Django**는 **다소 독선적**인 프레임워크





##### :fallen_leaf: 웹 서비스를 제작하는 두가지 방법

|     A-Z 모두 직접 하기     |                       프레임워크 사용                        |
| :------------------------: | :----------------------------------------------------------: |
| URL, DB, Mapping, 보안 ect | 기본적인 구조나 필요한 코드들은 제공, 좋은 웹 서비스를 만드는 것에 집중 |



> *ex) ver. 1.37.2* **=>** major.middle.minor
>
> 
>
> **major 패치** - 커다란 틀의 베이스가 패치되어서 이미 있는 코드를 다 수정해야할 가능성이 높다.
>
> **middle 패치** - 새로운 기능이나, 새로운 모듈 패치
>
> **minor 패치** - 버그 픽스 에러 수정과 같은 패치. 부분 수정만 해주면 된다. (큰 영향x)
>
> 
>
> MVC (v-view 사용자가 보는 화면)
>
> **MTV** (model 데이터를 관리 template 사용자가 보는 화면 view 중간 관리자)
>
> MVC, MTV 결론적으로는 기능은 같지만 **Django에서 차별화를 두기 위해** 이름을 다르게 지정함.





##### :paw_prints: Django의 가장 일반화된 작동원리

**view** - 요청이 들어와서 model에게 요구

**model** - 찾아서 view에게 전달

**template** - view에게 전달 받아서 사용자에게 보여줌 (HTML)





#### :seedling: Django를 하기 전에

> 1) 파일들이 많아져서 목록을 보기 힘들다면 : Material Icon Theme (확장자 추천 = 필수 x )
>
> ![](https://user-images.githubusercontent.com/52684457/63145137-277dd800-c031-11e9-95b8-a4a0598a4dbf.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/63145149-2fd61300-c031-11e9-8cbd-b98d4f511461.png)
>
> - 파일 아이콘들이 더 알아보기 쉽게 바뀐다.



> 2) **환경변수 설정**
>
> ![](https://user-images.githubusercontent.com/52684457/62986397-5ef45500-be76-11e9-971d-95c62577e5f0.png)



> #### :mushroom: 환경 변수는 왜 설정 하는 것인가?
>
> ##### 의존성
>
> 1. 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 無
>
> 2. 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 無
>
> 3. 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경속에서만 모듈을 관리하고, 앱을 실행 시키기위해 가상환경을 설정
>
> 4. 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른환경을 만드는 방식으로 진행



> ###### 환경 변수 설정
>
> ![](https://user-images.githubusercontent.com/52684457/62986565-1d17de80-be77-11e9-9e15-313ae1e57a51.png)
>
> git ignore 사이트를 이용해서 .gitignore 파일을 생성 **=>** https://www.gitignore.io/
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62986584-2e60eb00-be77-11e9-8393-2bd4ae95914b.png)
>
> > ###### python -m venv (가상환경 경로+이름)
> >
> > => python -m venv ssafy (내가 현재 있는 곳에 ssafy라는 가상환경을 만들 것)
>
> 코드를 복사해서 붙여넣기를 하면 /* 이런 코드가 붙은 것을 확인 할 수 있다. 필요가 없으니 없애준다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62986590-3f116100-be77-11e9-9a03-98f692489270.png)
>
> - 우리는 이 환경 변수코드를 사용할 것
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62987259-d11a6900-be79-11e9-8c61-afe4d9a2d40c.png)
>
> - study1_Git_and_Visual_Studio_Code.md 파일에서 만든 환경변수 venv는 우리가 편하기 위해 만든 환경변수 이름일 뿐 여기서 사용하는 venv와 혼동하면 안된다.
> - 위의 밑줄 그어진 venv도 환경변수 이름이다. (다른 이름을 지정해줘도 상관 x)
> - 아래의 source를 할때에 venv를 지정해준 환경 변수 이름경로로 들어가주면 된다.
>
> 
>
> 이번에 업데이트 (July 2019)에서 파이썬에서 환경변수를 내장할 수 있게 되었다.
>
> - `"terminal.integrated.cwd": "${workspaceFolder}"`
>
> - ![](https://user-images.githubusercontent.com/52684457/62988554-cbc01d00-be7f-11e9-8ceb-d37a7b43e284.png)
> - 코드를 추가 해주면 된다.
>
> 
>
> #### :mushroom: 만약 터미널이 켜지지 않는다면?
>
> ![](https://user-images.githubusercontent.com/52684457/62988552-cb278680-be7f-11e9-928b-b1a70eb056aa.png)
>
> - 터미널이 아직도 켜지지 않는다면
>   1. vscode 재시작 
>   2. interpreter venv 작동
>   3. 터미널 단축키 동작 확인
>
> 
>
> #### :seedling: 잘 켜지는 것이 확인 되었다면
>
> ![](https://user-images.githubusercontent.com/52684457/62987260-d1b2ff80-be79-11e9-95c3-0928cc4338ba.png)
>
> - 위의 경로로 들어가서
>
> ![](https://user-images.githubusercontent.com/52684457/62987258-d11a6900-be79-11e9-81cc-91a5560d145f.png)
>
> - 사용할 환경변수를 선택해주면 된다. 아래의 파란 바에있는 이름이 바뀌는 것을 확인 할 수 있다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62988553-cbc01d00-be7f-11e9-83b0-a94fe07cee47.PNG)
>
> - 버전 확인
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62988555-cbc01d00-be7f-11e9-833f-60c443253d2c.png)
>
> - Django 설치와 버전확인, 기본적인 셋팅
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62988556-cbc01d00-be7f-11e9-8312-5361c53029a1.png)
>
> - 설치요청이 오면 설치를 한다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62988557-cc58b380-be7f-11e9-94e4-8e1e72ab4e5c.png)
>
> ![](https://user-images.githubusercontent.com/52684457/62988558-cc58b380-be7f-11e9-8c8f-b1db843a3c06.png)
>
> Django 설치가 성공적인것을 확인 할 수 있다!
>
> 
>
> ```python
> INSTALLED_APPS = [
>  # app 등록 순서 (Djaingo가 제공하는 스타일 가이드)
>  # 1. local apps
>  # 2. Third party apps (ex. beautiful soap 과 같은 apps)
>  # 3. Django apps
>  'pages.apps.PagesConfig', #  Local apps(1.)
>  # pages라는 폴더에, apps라는 파일에 PagesConfig
>  'django.contrib.admin', # 여기서 아래의 6가지가 Django의 기본 apps (3.)
>  'django.contrib.auth',
>  'django.contrib.contenttypes',
>  'django.contrib.sessions',
>  'django.contrib.messages',
>  'django.contrib.staticfiles',
> ]
> 
> # Internationalization
> # => I18n 국제화 작업
> LANGUAGE_CODE = 'ko-kr'
> 
> TIME_ZONE = 'Asia/Seoul'
> # 이렇게 변경해주면 한글화가 된다.
> ```
>
> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones = 국제 표준시의 표기를 알 수 있다.
>
> ctrl + F => Seoul을 검색하면 Asia/Seoul이 뜨는 것을 알 수 있다. (한국 서울 기준 시간으로 설정 됨)
>
> 
>
> **python manage.py runserver** 을 입력하면 Django 서버가 실행 된다.







##### :seedling: ​지금 할 과정

> urls -> view -> template -> page
>
> (model은 생략 - data base 無)



#### :seedling: 코드 작성 순서

1. views : 만들고자 하는 view 함수 작성
2. urls : views에서 만든 함수에 주소를 연결
3. templates : 해당 view 함수가 호출 될 때, 보여질 페이지



![](https://user-images.githubusercontent.com/52684457/62988560-cc58b380-be7f-11e9-9d46-c2237884a3b7.png)

- #### pages 라는 app을 생성



![](https://user-images.githubusercontent.com/52684457/62989243-307c7700-be82-11e9-87d8-3f25d247639d.png)

- setting 파일에서 pages.apps.PagesConfig를 추가 (app을 등록해야함)
- filename.app.**F**ilename**C**onfig





#### F1 => open setting json

- 설정을 해주지 않으면 Django에서 Beautify가 작동하지 않음
- 이전 html에서는 기본값만으로도 작동이 가능했지만 Django에서는 작동을 제대로 하지 않음

![444](https://user-images.githubusercontent.com/52684457/62991304-12b31000-be8a-11e9-8080-be1a2219dabd.PNG)

![](https://user-images.githubusercontent.com/52684457/62991299-12b31000-be8a-11e9-8f71-8f2c1371afd5.PNG)



![](https://user-images.githubusercontent.com/52684457/62991302-12b31000-be8a-11e9-8f3f-704d8ff3b798.PNG)

![](https://user-images.githubusercontent.com/52684457/62991300-12b31000-be8a-11e9-9796-85bd1729ab2d.PNG)

```json
{
    "terminal.integrated.cwd": "${workspaceFolder}",
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "window.zoomLevel": 0,
    "editor.fontFamily": "Hack, Fira Code, Consolas, 'Courier New', monospace",
    "[html]": {
        "editor.tabSize": 2
    },
    "[css]": {
        "editor.tabSize": 2
    },
    "[django-html]": { // 아래 django-html을 추가한것으로 인해 spacebar을 2로 설정
        // 편하게 하기 위함
        "editor.tabSize": 2
    },

    //django
    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {"django-html": "html"},

    
    //beautify
    "beautify.language": {
        "js": {
        "type": ["javascript", "json"],
        "filename": [".jshintrc", ".jsbeautifyrc"]
        // "ext": ["js", "json"]
        // ^^ to set extensions to be beautified using the javascript beautifier
        },
        "css": ["css", "scss"],
        "html": ["htm", "html", "django-html"]
        // ^^ providing just an array sets the VS Code file type
    }
}
```

> 나중에 작업이 복잡해지면 왼쪽 현재 폴더를 띄우는 창을 사용하는 빈도가 줄어든다.
>
> **Ctrl + P** 를 누르면 **빠른 화면 전환**이 가능하다.





#### :paw_prints: 코드 작성 순서에 따라...



###### view : 만들고자 하는 함수 생성

```python
# django imports style guide
# 1. standard library (ex. random)
# 2. third-party (ex. requests)
# 4. Django
# 5. local django

import random
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'pick': pick,})
# 앞의pick은 templates에서 가져오는 pick (다른 것), 통상적으로 이름을 똑같이 맞춤.
# 다음 값을 받기위한 준비를 하기 위해서 값이 한개만 있더라도 ,를 적어준다.


def image(request):
    return render(request, 'image.html')

```



###### urls.py : views에서 만든 함수에 주소를 연결

```python
from django.contrib import admin
from django.urls import path
from pages import views # 생성한 app pages 폴더 안의 views.py 파일

urlpatterns = [
    path('image/', views.image), # url 경로 마지막에 / 를 붙이는 습관
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index), 
    path('admin/', admin.site.urls),
]
```



###### templates : 해당 view 함수가 호출 될 때, 보여질 페이지

```html
<!-- index.html -->
<h1>Hi Django!</h1>


<!-- introduce.html -->
<h1>introduce page 입니다.</h1>


<!-- dinner.html -->
<h1>오늘 저녁은 {{ pick }}!</h1>
<!-- Django tamplates language, Jinja가 아님-->



<!-- image.html -->
<img src="https://picsum.photos/500/500.jpg" alt="랜덤">  
```



------



### :paw_prints: variacle routing

- 동적 라우팅

```python
# views.py
def hello(request, name): # name은 변수, 이름이 달라도 상관이 없다.
    context = {'name': name} # 오른쪽의 name이 함수 name
    return render(request, 'hello.html', context)
```

```python
# urls.py
urlpatterns = [
    path('hello/<str:name>/', views.hello), # str은 기본값이기 때문에 생략 가능 => <name>
    path('admin/', admin.site.urls),
]
```



```html
<!-- hello.html -->
<h1>안녕하세요, {{ name }}</h1>
```



![](https://user-images.githubusercontent.com/52684457/62992038-f06ec180-be8c-11e9-9ac6-a8f9d39a27aa.png)

dinner의 함수와 합쳐서 수정해보자 !

```python
# views.py
import random
from django.shortcuts import render

def hello(request, name): # name은 변수, 이름이 달라도 상관이 없다.
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,} # 
    # 오른쪽의 name이 함수 인자로 받은 name / , 트레일링 컴마는 잊지않고 작성
    return render(request, 'hello.html', context)
```





###### variable routing 을 응용해보자.

1. ###### 자기소개 - 이름과 나이를 받아서 출력 (introduce 확장)

```python
# views.py
def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)
```

```python
# urls.py
urlpatterns = [
    path('introduce/<name>/<int:age>/', views.introduce),
    path('admin/', admin.site.urls),
]
```

```html
<!-- introduce.html -->
<h1>안녕하세요, 이름은 {{ name }} 나이는 {{ age }}살 입니다. </h1>
```





2. ###### 숫자 2개를 받아 두 수의 곱셈 결과를 출력 (times)

```python
# views.py
def times(request, num1, num2):
    mul = num1 * num2
    context = {'mul': mul, 'num1': num1, 'num2': num2,}
    return render(request, 'times.html', context)
```

```python
# urls.py
urlpatterns = [
    path('times/<int:num1>/<int:num2>/', views.times),
    path('admin/', admin.site.urls),
]
```

```html
<!-- times.html -->
<h1> {{ num1 }} 곱하기 {{ num2 }}는 {{mul}}입니다. </h1>
```





3. ###### 반지름 값을 받아 원의 넓이 출력 (area)

```python
# views.py
def area(request, r):
    area = (r ** 2) * 3.14
    context = {'r': r, 'area': area,}
    return render(request, 'area.html', context)
```

```python
# urls.py
urlpatterns = [
    path('area/<int:r>/', views.area),
    path('admin/', admin.site.urls),
]
```

```html
<!-- area.html -->
<h1>반지름의 길이가 {{ r }} 인 원의 넓이는 {{area}} 입니다. </h1>
```





------



## :dog: Django Template Language (DTL)

- django template 에서 사용하는 내장 template system
- 조건, 반복, 변수 치환, 필터 등 많은 기능을 제공한다.
- https://docs.djangoproject.com/en/2.2/ref/templates/language/
- https://docs.djangoproject.com/en/2.2/topics/templates/#the-django-template-language

*flask는 Jinja2*



```python
import random # 위 아래 같은 standard library 이다
# 이럴 때에는 더 짧은 것을 위에 써준다. (스타일 가이드)
from datetime import datetime
from django.shortcuts import render

def template_language(request):
    menus = ['잡채밥', '짬뽕', '마라탕', '마랴텐지투이',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'bansns', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)
```

```python
urlpatterns = [
    path('template_language/', views.template_language),
    path('admin/', admin.site.urls),
]
```

```html
<h3>1. 반복문</h3>
{% for menu in menus %}
<p> {{ menu }} </p>
{% endfor %}
<hr>

<!-- forloop는 DTL for 문 안에서 자동으로 생기는 객체 -->
{% for menu in menus %}
<p>{{ forloop.counter }} {{ menu }}</p>
{% endfor %}
<hr>

<!-- 비어있으면 자동으로 아래 코드를 읽는다. -->
{% for user in empty_list %}
<p>{{ user }}</p>
{% empty %} 
<p>현재 가입된 유저가 업습니다.</p>
{% endfor %}
<hr>
<hr>

<h3>2. 조건문</h3>
{% if '짬뽕' in menus %}
<p>짬뽕은 사골육수지!</p>
{% endif %}
<hr>

{% for menu in menus %}
{{ forloop.counter }} 번째 도는중..
  {% if forloop.first %}
  <p>잡채밥 + 당면듬뿍</p>
  {% else %}
  <p>{{ menu }}</p>
  {% endif %}
{% endfor %}
<hr>
<hr>

<!-- <=, >=, ==, !=, >, <, in, not in, is 모두사용 가능 -->
<h3>3. legth filter</h3>
{% for message in messages %}
  {% if message|length > 5 %}
  <p>{{ message }}, 글자가 너무 길어요</p>
  {% else %}
  <p>{{ message }}, {{ message|length }}</p>
  {% endif %}
{% endfor %}
<hr>
<hr>

<!-- 이미 정의되어 있는 변수 호출은 % 태그를 사용한다. -->
<h3>4. lorem ipsum</h3>
{% lorem %}
<hr>
{% lorem 3 w %}
<hr>
{% lorem 4 w random %}
<hr>
{% lorem 2 p %}
<hr>
<hr>

<h3>5. 글자수 제한</h3>
<p>{{ my_sentence|truncatewords:3 }}</p> <!-- 공백까지 한꺼번에 포함해서 한글자 -->
<p>{{ my_sentence|truncatechars:3 }}</p> <!-- 한 글자씩 -->
<hr>
<hr>

<h3>6. 글자 관련 필터</h3>
<p>{{ 'abc'|length }}</p>
<p>{{ 'abc'|upper }}</p>
<p>{{ 'ABC'|lower }}</p>
<p>{{ my_sentence|title }}</p>
<p>{{ 'abc def'|capfirst }}</p>
<p>{{ menus|random }}</p>
<hr>
<hr>

<!-- 더 많은 연산 관련 기능은 django math filters 라이브러리가 필요 -->
<h3>7. 연산</h3>
<p>{{ 4|add:6 }}</p>
<hr>
<hr>

<h3>8. 날짜표현</h3>
<p>{{ datetimenow }}</p> 
<p>{% now "DATETIME_FORMAT" %}</p> <!-- 기본적으로 내장되어있는 함수 -->
<p>{% now "SHORT_DATETIME_FORMAT" %}</p> <!-- 만약 처음 시작 할 때 setting.Time_ZONE 값을 한국 시간으로 정해주지 않으면 미국 시간으로 나온다. -->
<p>{% now "DATE_FORMAT" %}</p>
<p>{% now "SHORT_DATE_FORMAT" %}</p>
<hr>
{% now "Y년 m월 d일 (D) h:i" %}
<hr>
{% now "Y" as current_year %}
Copyright {{ current_year }}
<hr>
{{ datetimenow|date:"SHORT_DATE_FORMAT" }}
<hr>
<hr>

<h3>9. 기타</h3>
<p>{{ 'google.com'|urlize}}</p> <!-- a태그와 비슷한 기능 -->


{% comment %} <!-- -->는 Django 주석이 아니다. 그렇기 때문에 {% %}태그가 들어가면 페이지가 열리지 않는다. / 현재 편의상 <!-- --> 사용 {% endcomment %}
```

- django math filters - https://pypi.org/project/django-mathfilters/
  - 기본적으로 연산같은 경우는 views에서 전부 처리하는 것이 좋은 예
  - 하지만 굳이 사용하겠다면 위의 사이트에서 외장 함수를 가져다 써야한다.



##### :paw_prints: DTL을 응용해보자!

> ######  isitgwangbok?
>
> - views - isitgwangbok
> - 현재 시점이 광복절이라면 오늘은 광복절입니다 라고 출력
> - 아니라면 오늘은 광복절이 아닙니다. 를 출력
>
> 3. ###### 
>
> ```python
> # views.py / 최대한 view 에서 계산
> from datetime import datetime
> from django.shortcuts import render
> 
> def isitgwangbok(request):
>     today = datetime.now()
>     if today.month == 8 and today.day == 15:
>         result = True
>     else:
>         result = False
>     context = {'result': result,}
>     return render(request, 'isitgwangbok.html', context)
> ```
>
> ```python
> # urls.py
> urlpatterns = [
>     path('isitgwangbok/', views.isitgwangbok),
>     path('admin/', admin.site.urls),
> ]
> ```
>
> ```html
> <!-- isitgwangbok.html -->
> {% if result %}
> <p>오늘은 광복절 입니다.</p>
> {% else %}
> <p>오늘은 광복절이 아닙니다.</p>
> {% endif %}
> ```



##### :paw_prints: form tag를 사용해보자 !

- 요청과 응답을 받는 페이지를 만들 것



###### 요청 페이지(throw)

```python
# views.py
def throw(request):
    return render(request, 'throw.html')
```

```python
# urls.py
urlpatterns = [
    path('throw/', views.throw),
    path('admin/', admin.site.urls),
]
```

![](https://user-images.githubusercontent.com/52684457/63136467-263ab400-c00d-11e9-9170-b8ae2f5c15c6.png)

```html
<!-- throw.html -->
<form action="/catch/" method="GET"> <!-- GET은 기본 값이라 안써도 상관없음(소문자로 적어도 됨), 시맨틱은 대문자로 쓰는게 좋음, 검색창의 form을 찾아보면 method="get"을 사용하는 것을 알 수있다. catch의 앞 / 는 필수 get을 받는 방식 -->
  <label for="message">THROW</label>
  <input type="" id="message" name="message">  <!-- name으로 보내는게 아니라 id로 label에 보냄 -->
  <input type="submit"> <!-- action쪽으로 신호를 보낼 것 -->
</form>
```



###### 반응 페이지(catch)

```python
# views.py
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    # message 신호를 받을 코드(message라는 dictionary를 받음), 여기서의 get은 값을 받아오는 것. GET != get
    context = {'message': message,}
    return render(request, 'catch.html', context)
```

```python
# urls.py
urlpatterns = [
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('admin/', admin.site.urls),
]
```

```html
<!-- catch.html -->
<h1>catch 에서 보낸 {{ message }} 를 받았습니다.</h1>
```

![](https://user-images.githubusercontent.com/52684457/63136969-597e4280-c00f-11e9-8b83-696e15eba1ad.png)



![](https://user-images.githubusercontent.com/52684457/63136944-47040900-c00f-11e9-9eda-37a8d64b5af3.png)

- 밑 줄 그어진 부분만 바꿔도 값이 바뀌는 것을 확인 할 수 있다.





### :mushroom: request?

Request and response objects => https://docs.djangoproject.com/en/2.2/ref/request-response/

- 위의 링크를 참고해서 여러 코드를 사용해보면 원하는 값을 볼 수 있다.

*ex)*

![](https://user-images.githubusercontent.com/52684457/63137204-212b3400-c010-11e9-85f3-9e1ad5be4664.png)

![](https://user-images.githubusercontent.com/52684457/63137289-98f95e80-c010-11e9-8275-9d6e53c483b1.png)

*pprint(request.meta)*











#### ARTII => http://artii.herokuapp.com/

##### :paw_prints: ARTII API를 이용하여 영문을 독특하게 바꿔주는 페이지를 만들어 보자!



![](https://user-images.githubusercontent.com/52684457/63137505-82073c00-c011-11e9-92d2-3e8714f5dedd.png)

- ASCII art API도 GET을 사용하는 것을 알 수 있다.
- 예제를 보면 어떠한 방식으로 할지 가이드가 되어있다.
- font를 여러가지를 사용해보기 위해서 font_list 값을 얻어  random.choice를 할 것. (font_list를 클릭하면 볼 수 있다.)



###### 외부 라이브러리 pip install requests 설치를 해주어야 한다.

```python
# views.py
import random
import requests
from pprint import pprint
from django.shortcuts import render

def catch(request):
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.method)
    # pprint(request.GET)
    # pprint(request.meta)
    message = request.GET.get('message') # message 신호를 받을 코드(message라는 dictionary를 받음), 여기서의 get은 값을 받아오는 것. GET != get
    context = {'message': message,}
    return render(request, 'catch.html', context)



def art(request):
    return render(request, 'art.html')

def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    # 3. str 을 list로 바꾼다.
    fonts = fonts.split('\n') # enter를 기준으로 나누기

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text # .text를 해주어야 필요한 text값만 뽑아낼 수 있다.

    context = {'response': response,}
    return render(request, 'result.html', context)
```



![](https://user-images.githubusercontent.com/52684457/63138133-399d4d80-c014-11e9-864e-8c12de802eb3.png)

![](https://user-images.githubusercontent.com/52684457/63137773-7d8f5300-c012-11e9-89c9-d811ab5c7f53.png)

*result를 아직 return하지 않았지만 값을 확인하기 위해서 url에 미리 `path('reault/', views.result),`를 입력해준뒤 저장(ctrl+s)을 하면 값을 볼 수 있다.*

```python
# urls.py
urlpatterns = [
    path('result/', views.result),
    path('art/', views.art),
    path('admin/', admin.site.urls),
]
```

```html
<!-- view.html -->
<h1>ASCII ART에 오신걸 환영합니다. ^_____^</h1>
<pre>{{ response }}</pre> <!-- pre tag를 붙여주지 않으면 값을 제대로 받지 못함. -->

<!-- result.html -->
<form action="/result/" method="GET">
  <label for="word">영단어를 입력하세요.</label>
  <input type="text" name="word">
  <input type="submit" value="만들기">
</form>
```

###### 결과)

![](https://user-images.githubusercontent.com/52684457/63138139-4326b580-c014-11e9-8ebd-6c1eaf3eb72e.png)

![](https://user-images.githubusercontent.com/52684457/63138126-2f7b4f00-c014-11e9-842d-b8b326e177d2.png)



#### :mushroom: GET의 한계?

- GET은 짧은 텍스트만 넘겨줄 수 있기 때문에, 이미지나 파일 등 긴 값을 보낼 수 없음.

- login과 같이 개인정보는 주소창에 드러나면 안되기 때문에 post방식으로 head 가 아닌 body안에 담아서 값을 보내야 함.



##### :paw_prints: POST를 사용해보자!

```python
# views.py
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,} # 값을 원래는 저장해야하지만 출력값만 보기위해서 쓰여진 코드, 실제로 보안코드를 출력해서는 안된다.
    return render(request, 'user.create.html', context)
```

```python
# urls.py
urlpatterns = [
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('admin/', admin.site.urls),
]
```

```html
<!-- user_new.html -->
<form action="/user_create/" method="POST">
  <label for="name">아이디</label>
  <input type="text" id="name" name="name"><br>
  <label for="pwd">패스워드</label>
  <input type="password" id="pwd" name="pwd">
  <input type="submit" value="가입">
</form>

<!-- user_create.html -->
<p>아이디 : {{ name }}</p>
<p>패스워드 : {{ pwd }}</p>
```

- 여기까지 했다면 `가입` 버튼을 눌렀을 때, 403오류가 뜨는 것을 볼 수있다.

![](https://user-images.githubusercontent.com/52684457/63139394-280a7480-c019-11e9-83d1-b602a6290958.png)

**403 Forbidden** => https://developer.mozilla.org/ko/docs/Web/HTTP/Status/403

-  권한이 없으면 페이지를 표시할 수 없다.
- POST는 사용자가 인증된 사용자라는 것을 알려주어야 한다.

**CSRF** => https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EA%B0%84_%EC%9A%94%EC%B2%AD_%EC%9C%84%EC%A1%B0



![](https://user-images.githubusercontent.com/52684457/63139705-2f7e4d80-c01a-11e9-9279-6291fb62fbb6.png)

- site에서 hidden으로 되어있는 곳들이 해당 site에서 로그인을 하고있다는 인증을 볼 수 있는데
- 같은site에 이 값이 없다면 위조 site일 가능성이 높다.



![](https://user-images.githubusercontent.com/52684457/63139738-4a50c200-c01a-11e9-84dd-6a8c2b70c5e5.png)

- framework가 없으면 일일히 해줬어야 할 작업
- Django에서 보안처리가 되어있다. Flask와 같은 곳에서는 일일히 작업을 해주어야 한다.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', 보안을 끈 것
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

- 보안을 끄면

![](https://user-images.githubusercontent.com/52684457/63140573-4a05f600-c01d-11e9-8c8c-c6330ac7e5b3.png)

- Forbidden이 활성화 되지 않는 것을 알 수 있다. (하지만 POST타입으로 인해 주소창에 정보가 뜨진 않는다.)

- 이러한 것을 방지하기 위해서

  - `{% csrf_token %}` 를 추가 ( 안전한 상태로 접속할 수 있다. )

  - ```python
    <form action="/user_create/" method="POST">
      {% csrf_token %}
      <label for="name">아이디</label>
      <input type="text" id="name" name="name"><br>
      <label for="pwd">패스워드</label>
      <input type="password" id="pwd" name="pwd">
      <input type="submit" value="가입">
    </form>
    ```

    

  - ![](https://user-images.githubusercontent.com/52684457/63139830-a9aed200-c01a-11e9-9151-b8f2624efd94.png)

- csrf_token을 넣어 줌으로서 hidden타입이 생긴것을 볼 수 있다. value 값은 매번 바뀐다.

![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565925420622.png)

- 원래의 get방식은 값을 2가지 밖에 넘기지 못하지만 여기서 token값까지 세가지의 값이 넘어가는 것을 알 수있다.



#### :mushroom: csrf : 사이트간 요청 위조

- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격 방법.
- Django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token 으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다. ( *403 Error* )



------



### :dog: static 정적파일

- image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 그대로 보여주면 되는 파일들
- 동적 파일은 사용자 요청에 의한 유동성이 있지만 정적 파일은 그렇지 않다.



##### :paw_prints: img와 css를 넣어보자!

```html
{% load static %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
   <!-- 폴더 경로가 static으로 되어있므로 경로에는 static을 굳이 넣어줄 필요가 없다.  --> 
</head>
<body>
  <h1>Static 파일 실습</h1>
  <img src="{% static 'images/image.jpg' %}" alt="static_img">
</body>
</html>
```

```css
/* static 폴더안에 images폴더와 동일선상에 stylesheets라는 파일에 생성, style.css */
h1 {
  color: palevioletred;
}
```



![](https://user-images.githubusercontent.com/52684457/63144188-b50af900-c02c-11e9-8960-da3891b6d5d2.png)

- static 폴더에 pasges라는 앱과 혼동되지 않도록 한번더 안에 images폴더를 더 만들고 그 안에 이미지를 넣어준다.

##### 결과)

![](https://user-images.githubusercontent.com/52684457/63144748-454a3d80-c02f-11e9-8d13-bb07ced7960b.png)







#### :paw_prints: utilities 라는 또 다른 앱(app)을 만들어보자!

- `python manage.py startapp utilities`

###### setting.py

```python
INSTALLED_APPS = [
    'utilities.apps.UtilitiesConfig'
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] # 등록을 먼저 한 상태에서 app을 만들면 (선등록을 하면) 에러가 나니 조심!
```

- `'utilities.apps.UtilitiesConfig'` 를 추가
- 하지만 중간 name space를 지정해주어야 위에서 부터 읽힐 때 pages가 안읽히는 과정을 없애 줄 수 있다. 



```python
# utilities/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
```

```python
# utilities/urls.py
from django.urls import path
from . import views # from 자기자신에

urlpatterns = [
    path('index/', views.index) # 자기자신에 있는 index
]
```

```html
<!-- utilities/index.html -->
<h1>두번째 장고 실습 !!!</h1>
```

- 이쯤에서 pages에 있는 index.html이 읽히지 않을 것



**app은 여러개 만들 수 있지만 urls.py가 할 일이 많아지기 때문에, app에 urls의 기능을 나눠줘야 한다**

###### urls.py

```python
from django.contrib import admin
from django.urls import path, include # inclue를 import
from pages import views

urlpatterns = [
    path('utilites/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

- 원래 urls.py에 있던 pages의 path들을 각각 app폴더의 urls.py로 세부역할들을 가져가고 최상위에 있는 urls.py에는 app을 include를 해주기만 하면 된다.

###### pages/urls.py (pages라는 앱 폴더 안에 urls.py를 따로 생성. 직접만들어 주어야 한다)

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 원래 app url 은 아래로 작성해 나간다.
    # setting.py에서의 app 등록과 같은 것들은 위로 계속 쌓아가지만 얘만 유일하게 아래로 작성한다.
    # alt 키를 누른채로 방향키를 위 아래로 움직이면 한 줄씩 방향키대로 자리가 바뀐다.
    path('index/', views.index),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello), # str은 기본값이기 때문에 생략 가능 => <name>
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
```

- 작업이 다 되면 해당페이지에서 다른페이지로 요청을 보내는 파일들이 *404 error* 가 난다. 왜 ?

  **=>** 경로가 바뀌었기 때문

- 새로운 urls.py를 pages폴더 안에 생성했기 때문에 경로가 바뀌었음을 알 수 있다.

![](https://user-images.githubusercontent.com/52684457/63145482-96a7fc00-c032-11e9-8fa2-e20bbc8a5b93.png)

- `pages/` 가 추가로 덧붙은 모습을 주소창에서 확인 할 수 있다.







------



## :dog: Django namespace

###### template / static 이름공간

- **Django는 templates폴더 까지는 읽어주는데**, 거기에 <u>경계를 두는 작업을 해야</u>, 다른 앱, 같은이름의html이 겹쳐도 각각의 app을 선택해서 경로를 들어갈 수 있도록 해줄 수 있다.

- **pages 앱 폴더 안에 templates안**에, **pages라는 폴더 (app폴더와 똑같은 이름)**를 새로 만들어서 그 안에 원래 templates 폴더에있던 파일들(html)을 옮겨주는 작업을 해야한다.

![](https://user-images.githubusercontent.com/52684457/63146348-9bba7a80-c035-11e9-836d-da8a5342a8cd.png)

- 경로에 공간을 주었기 때문에 app의 views.py에 들어있는 함수안에 `appname/` 을 넣어 수정해주어야 한다.
- 하지만 바꿨음에도 불구하고 요청이 제대로 되지 않는 html이 있다.

###### - 경로를 수정해주자!

*ex - throw.html)*

```python
<form action="/pages/catch/" method="GET">
  <label for="message">THROW</label>
  <input type="" id="message" name="message"> 
  <input type="submit">
</form>
```

- 요청을 보내는 html에서는 대상 html의 위치도 바뀌었으니 `/pagese/` 를 입력해준다.
  - <u>( 앞 슬래쉬 잊지말기 ! )</u>





![](https://user-images.githubusercontent.com/52684457/63146718-df61b400-c036-11e9-9fa0-1e46d199fa95.png)

- static 또한 pages파일을 만들어서 넣어주는 작업을 해준다.
- 위에서 만든 이미지와 css를 넣은 주소도` pages/`를 넣어줘야 한다.

###### - 경로를 수정해주자!

*ex - static_example.html)*

```python
{% load static %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="{% static 'pages/stylesheets/style.css' %}">
   <!-- 폴더 경로가 static으로 되어있므로 경로에는 static을 굳이 넣어줄 필요가 없다.  --> 
</head>
<body>
  <h1>Static 파일 실습</h1>
  <img src="{% static 'pages/images/image.jpg' %}" alt="static_img">
</body>
</html>
```

- static 파일의 경로를  `pasges/` 를 붙인다.



#### :seedling: ​Template Inheritance : 상속

```python
# setting.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 00_django_intro 그 자체 (경로로 가져다 쓰기 좋다.)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')], # 장고가 모르는 추가경로를 만들 것
        'APP_DIRS': True, # True가 없으면 위의 templates를 모으는 작없이 없어진다.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



###### base.html

- project와 동일 선상 위치에 templates 폴더를 만들어준다. 그 안에서 base.html 생성

  ![](https://user-images.githubusercontent.com/52684457/63148397-053d8780-c03c-11e9-9cce-3493ec06e3a0.png)

  - Bootstrap을 이용하여 상속을 해보자

```python
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    {% block css %}
    {% endblock %}
</head>

<body>
  <h1 class="text-center">Template Inheritance</h1>
  <hr>
  <div class="container">
    {% block content %}
    {% endblock %}
    <!-- 닫힐때 content를 굳이 마저 쓰지 않아도 된다. 여러개의 block일때 헷갈리지 않기위해서 사용함.-->
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

- 이 파일을 사용하여 다른 html에 상속을 시키기위해서는 html 기본태그를 사용하지 않아도 된다. *( !+Tap )*

**적용 ex)**

![](https://user-images.githubusercontent.com/52684457/63148409-0ec6ef80-c03c-11e9-80af-f9629dd1df93.png)

```html
<!-- static_example.html -->
{% extends 'base.html' %}
{% load static %}

{% block css %}
  <link rel="stylesheet" href="{% static 'pages/stylesheets/style.css' %}">
{% endblock %}

{% block content %}
  <h1>Static 파일 실습</h1>
  <img src="{% static 'pages/images/image.jpg' %}" alt="static_img">
{% endblock %}
```

- load 태그만 올려주고 아래의 css는 따로 block content와 다른 block으로 세분화 해줄 수 있다. 

- 다른 html 파일들은 html 기본구성 태그들*( !+Tap )*을 지운 채 

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <!-- 내용 -->
  {% endblock %}
  ```

  - 이런 구성을 응용해주면 된다. 아래는 예시이다.

  ```html
  <!-- pages/index.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Hi Django!</h1>
    <h2>{{ test }}</h2>
  {% endblock %}
  ```

  







































































```python
# views.py

```

```python
# urls.py
urlpatterns = [
    
    path('admin/', admin.site.urls),
]
```

```html
<!-- .html -->

```

