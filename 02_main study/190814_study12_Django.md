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



> **major 패치** - 커다란 틀의 베이스가 패치되어서 이미 있는 코드를 다 수정해야할 가능성이 높다.
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
>     # app 등록 순서 (Djaingo가 제공하는 스타일 가이드)
>     # 1. local apps
>     # 2. Third party apps (ex. beautiful soap 과 같은 apps)
>     # 3. Django apps
>     'pages.apps.PagesConfig', #  Local apps(1.)
>     # pages라는 폴더에, apps라는 파일에 PagesConfig
>     'django.contrib.admin', # 여기서 아래의 6가지가 Django의 기본 apps (3.)
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
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

- pages 라는 파일을 생성



![](https://user-images.githubusercontent.com/52684457/62989243-307c7700-be82-11e9-87d8-3f25d247639d.png)

- setting 파일에서 pages.apps.PagesConfig를 추가





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
def hello(request, name): # name은 변수, 이름이 달라도 상관이 없다.
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,} # 
    # 오른쪽의 name이 함수 인자로 받은 name / , 트레일링 컴마는 잊지않고 작성
    return render(request, 'hello.html', context)
```

