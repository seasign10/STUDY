# :dog: Django : CRUD 체계화

###### 학습을 하기 전에...

`pip freeze > requirements.txt` : 환경 변수를 저장하는 방법,  `git push`를 하기전 설정을 반드시 해 주자.

`pip install -r requirements.txt` : 파일을 `clone`하게되면 사라져있는 환경변수를 재설정 해줄 수 있다.



## :rocket: URL Namespace

1. ##### 하드코딩 URL 제거

   `{% url %} template tag`

   >  **ex)**
   >
   > `<a href="/articles/{{ article.pk }}">[DETAIL]</a>`
   >
   > `<a href="{% url 'detail' article.pk %}">[DETAIL]</a>`
   >
   > 위의 `{{ article.pk }}` 처럼 받는 값은 url 뒤에 `,(콤마)`를 사용하지 않고 `띄어쓰기`**로 구분**을 준다.

   **문제점**

   - app이 여러개가 되면 단순히 <u>url name만 가지고는 어떤 app의 url인지</u> 알 수 없다.

   - **문제점 해결** : app의 `urls.py`에 `app_name`을 선언한다.

     > **ex)**
     >
     > `return redirect(f'/articles/{article.pk}')`
     >
     > **=>** `return redirect('articles:update', article.pk)`
     >
     > 
     >
     > `<form action="/articles/create/" method="POST">`
     >
     > **=>** `<form action="{% url 'articles:creat' %}" method="POST">`



![](https://user-images.githubusercontent.com/52684457/65103681-eac74700-da09-11e9-81e3-dff340725918.png)

- `app_name = '앱 이름'` : app name을 설정해줌으로서 다른 app의 동일 name과 충돌이 일어나지 않게 한다.
- path안의 `name='url name'` 를 설정해줌으로서 다른 수많은 코드들을 일일히 수정(하드 코딩) 할 필요 없이, name값만 따라오게 만든다.





# :information_source: HTTP

#### :cookie: **쿠키** : 브라우저가 가지고 있는 정보

- 보안에 취약해서 서버가 쿠키를 가지고있는 개념이 따로 생김 **=>** *세션*
- 사용자 기록과 같은 데이터를 예로 들 수 있다.

#### **:key: 세션** : 서버가 가지고 있는 정보

- 회원 정보 등, 보안에 취약하면 안되는 개인정보들은 서버가 가지고 있다.
- 회원 탈퇴를 하는 경우에 회원 정보 쿠키를 삭제하는 것이 세션



------



#### :earth_asia: URI : 통합 자원 식별자

- 인터넷에 자원을 나타내는 유일한 주소
- 인터넷에서 요구되는 기본조건으로서 http에 항상 붙어다닌다.



#### :earth_americas: URL : 파일식별자

- 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약



###### ex)

![](https://user-images.githubusercontent.com/52684457/65112606-359d8a80-da1b-11e9-9be8-5b6414a28847.png)

![](https://user-images.githubusercontent.com/52684457/65112655-61b90b80-da1b-11e9-9225-5dcb3669827a.png)



### :warning: HTTP 응답 코드

![image](https://user-images.githubusercontent.com/52684457/65112961-439fdb00-da1c-11e9-8453-c04dbd6fd6bb.png)

![image](https://user-images.githubusercontent.com/52684457/65112974-4995bc00-da1c-11e9-9efc-e016c0e082f5.png)

![image](https://user-images.githubusercontent.com/52684457/65112933-2834d000-da1c-11e9-9222-85a2bc6d176f.png)

**PUT** : 자원의 전체 교체, 자원내 모든 필드영역 필요

​         (만약 일부만 전달할 경우, 그외의 필드 모두 null or 초기값 처리)

**PATCH** : 자원의 부분 교체, 자원내 일부 필드영역 필요

![image](https://user-images.githubusercontent.com/52684457/65113174-261f4100-da1d-11e9-817b-b49a31606b08.png)



#### :stop_sign: REST

- 구성 요소 상호작용의 규모 확장성(scalability of component interactions)
- 인터페이스의 범용성 (Generality of interfaces)
- 구성 요소의 독립적인 배포(Independent deployment of components)
- 중간적 구성요소를 이용해 응답 지연 감소, 보안을 강화, 레거시 시스템을 인캡슐레이션 (Intermediary components to reduce latency, enforce security and encapsulate legacy systems)



###### REST 중심 규칙 

- URI는 정보의 자원을 표현해야 한다.
- 자원에 대한 행위는 HTTP Method로 표현한다. (즉 행위가 들어간 경로는 restful하지 않다.)

**기본**

1. 슬래시(/)는 계층 관계를 나타내는데 사용

2. URI에는 소문자를 사용

3. 파일 확장자는 포함시키지 않음

4. 밑 줄(_)대신 하이픈(-)을 활용

5. ~~주소 마지막에 슬래시(/)를 포함하지 않음~~ 
   **=>** Django는 처리가 되어있기 때문에 주소 끝에 슬래시(/)가 붙어있어도 주소 접속이 가능
        근래에는 슬래시 처리가 되어있는 프레임워크들이 많아짐



- GET POST PATCH DELETE 중에서 실제로 HTTP 에서는 공식적으로 **GET POST**만 공식적으로 사용된다.

- PATCH와 DELETE는 공식적으로 지원되는 method가 아니다.
  **=>** Django에서도 동일



**IPYthon**을 사용하여 구조를 확인하기

- https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installation

- 위의 주소에서 Django의 확장자를 설치해줄 수 있는 코드를 확인한다.

-  `pip install django-extensions` 를 터미널에서 설치

  ```python
  INSTALLED_APPS = (
      ...
      'django_extensions',
  )
  ```

  - `'django_extensions'` 을 아래의 이미지 처럼 추가해서 등록해준다.

![](https://user-images.githubusercontent.com/52684457/65114254-0e49bc00-da21-11e9-8389-65d7d37f18dd.png)

![image](https://user-images.githubusercontent.com/52684457/65114185-c7f45d00-da20-11e9-90db-1bad98423402.png)

- `from IPYthon import embed`
- embed에서 걸린 페이지는 무한 로딩에 걸리면서 위와 같은 이미지를 확인 가능하다.



#### :thumbsup: RESTful?!

같은 주소로 들어가는데 GET, POST에 따라 각각 행동을 다르게 해야 한다.
**=>** *(NEW + CREATE) / EDIT(GET) + UPDATE(POST)*

> GET articles/create/ 글을 작성하는 페이지
>
> POST articles/create/ 글이 실제로 작성
>
> **=>** 비효율 적인 url하나를 지우게 되는 것



**view.py**

- 헷갈리지 않기 위해 `new.html`을 `create.html` 로, `edit.html`을 `update.html` 로 수정

```python
# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk) # 메인 페이지
    #NEW
    else:
        return  render(request,'articles/create.html')
```

```python
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title') # 기존의 값을 바꾸는것
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)
```

>  `<form action="{% url 'articles:create' %}" method="POST">`
>
> `<form action="" method="POST">`
>
> `<form method="POST">`
>
> - form tag에 action이 없다면, 현재 머물고 있는 URL로 요청하기 때문에 위의 세가지 코드는 전부 다 동일하게 작동 된다.
> - 보통은 `action` 값을 비워두기만 한다.



**urls.py**

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # NEW(GET) + CREATE(POST)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'), # EDIT(GET) + UPDATE(POST)
]
```

![image](https://user-images.githubusercontent.com/52684457/65119980-e873e580-da27-11e9-8846-f46f08cc8aec.png)

- new라는 함수와 urls를 사용하지 않기 때문에 페이지 오류가 난다. 통합된 create로 설정해준다.



> **Delete**가 **GET**방식으로 받게 된다면, 주소에서 규칙만 찾아서 페이지 사용하자 악용할 가능성이 높다.
>
> - delete 버튼이 기능을 하는 html에서 아래의 사항을 수정해준다.
>
> ```django
> <a href="{% url 'articles:delete'  article.pk %}" onclick="return confirm('게시글이 삭제 됩니다.')">[DELETE]</a>
> ```
>
> - 위의 <u>a태그는 GET방식만 지원</u>하기때문에 **form태그를 사용**해준다.
>
> ```django
>   <form action="{% url 'articles:delete' article.pk %}" method="POST">
>     {% csrf_token %}
>     <input type="submit" value="DELETE" onclick="return confirm('게시글이 삭제 됩니다.')">
>   </form>
> ```
>
> `onclick="return confirm('내용')"` : 게시물을 삭제하기 전에 한 번 물어보는 알림 창이 뜨게 한다.
>
> ```python
> def delete(request, pk):
>     article = Article.objects.get(pk=pk)
>     if request.method == 'POST':
>         article.delete()
>         return redirect('/articles/') 
>     else:
>         return redirect(article)
> ```
>
> POST 방식이라면 작동, 아니라면 해당 페이지에 머무르도록 한다.





#### :black_circle: Model Instance Method

`get_absolute_url()` 

- 특정 모델에 대해 detail view를 작성할 경우

- detail url을 완성하자마자 사용하는 것을 권장한다.

- 반복되는 코드가 줄고 보다 간결해진다

- `get_absolute_url()` 를 model에 추가하게 되면 아래와 같이 admin에서 사이트에서 보기 버튼이 생기는데,

  ![image](https://user-images.githubusercontent.com/52684457/65203867-5fac8680-dac7-11e9-91ec-d6d43896976f.png)

  ![image](https://user-images.githubusercontent.com/52684457/65203880-6affb200-dac7-11e9-9694-00225dfed0f9.png)

  - 바로 해당 페이지로 이동할수 있는 기능이다.

  

`redirect(모델 인스턴스)` 를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출

```python
from django.urls import reverse

class Article(models.Model):
    ...
    title = models.CharField(max_length=20)
    
    def __str__(self):
        ...
        return

	def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        
        # return reverse('articles:detail', args=[self.pk]) 
        # articles/pk값/ => 문자열로 나타난다.
        
        # return reverse('articles:detail', kwargs={'key': self.pk})
        return reverse('articles:detail', kwargs={'pk': self.pk})

        # 주의 사항
        # reverse 함수에 args 와 kwargs를 동시에 인자로 보낼 수 없다.
```

- `return redirect('articles:detail', article.pk)` 를 `redirect(articles)`로 축약이 가능해진다.

  ```django
  <!-- index.html -->
  {% extends 'base.html' %}
  
  {% block content %}
  <h1 class="text-center">Articles</h1>
  <a href="{% url 'articles:create' %}">[NEW]</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title}}</p>
    <p>글 내용: {{ article.content }}</p>
    
    <a href="{{ article.get_absolute_url }}">[DETAIL]</a>
    <!-- <a href="/articles/{{article.pk}}">[DETAIL]</a> -->
    <!-- 위, 아래 같은 코드 -->
    <hr>
  {% endfor %}
  {% endblock %}
  ```

  



#### :black_circle: ​URL Reverse를 수행하는 함수들

1. ##### reverse()

- return 값 : string(문자열)

  ```python
  reverse('articles:index') # '/articles/'
  ```

2. ##### redirect()

- return 값 : HttpResponseRedirect (객체)

- 내부적으로 `resolve_url()`을 사용

- view 함수에서 특정 url로 돌려보내고자 할 때 사용

  ```python
  redirect('articles:article')
  # '<HttpResponseRedirect status_code=200, "text/html; charset=utf-8, url="/articles/"'
  ```

3. ##### url template tag(`{% url %}`)

- 내부적으로 `reverse()` 를 사용



> #### :file_folder: 2번째 app : jobs
>
> - faker를 이용한 site만들기 => https://faker.readthedocs.io/en/stable/
> - git hub에서 언어 설정도 확인이 가능하다 -> https://github.com/joke2k/faker
>
> 
>
> ##### 해당 요구 조건
>
> 1. models
>    - name : 20자 제한
>    - past_job : 제한 없음
>
> 2. View 2개
>    - index / past_life
>
> ##### 포인트
>
> - 입력된 이름이 DB에 있는지 없는지
> - 있다면 기존 DB에서 그대로 가져와서 출력
> - 없다면 faker를 통해 생성된 새로운 직업과 함께 db에 저장
>
> ###### GIPHY
>
> **=>** https://giphy.com/ 회원가입 후
>
> **=>** https://developers.giphy.com/dashboard/ 개발자 전용 사이트로 접속
>
> 키 값을 받은 후 `.env` 파일을 생성해서 키 값 입력 `키이름=''` *(띄어쓰기 없이)*
>
> 
>
> 터미널에서 `django-admin startproject jobs .` 로 `app` 생성
>
> `settings.py` 에서의 `app` 등록
>
> 프로젝트의 `urls.py` 에서 `app` inclue
>
> `app` 에 `templates` 폴더를 생성후 안에 app이름의 폴더를 또 생성, 그 안에 html 작성
>
> ###### model.py
>
> ```python
> from django.urls import reverse
> from django.db import models
> 
> # Create your models here.
> class Job(models.Model):
>     name = models.CharField(max_length=20)
>     past_job = models.TextField()
> 
>     def __str__(self):
>         return self.name
> ```
>
> 
>
> ###### admin.py
>
> ```python
> from django.contrib import admin
> from .models import Job
> 
> # Register your models here.
> class JobAdmin(admin.ModelAdmin):
>     list_display = ('pk', 'name', 'past_job',)
> 
> admin.site.register(Job, JobAdmin)
> ```
>
> 
>
> ###### urls.py
>
> ```python
> from django.urls import path
> from . import views
> 
> app_name = 'jobs'
> urlpatterns = [
>     path('', views.index, name='index'),
>     path('past_life/', views.past_life, name='past_life'),
> ]
> ```
>
> 
>
> - pip install `decouple`, `faker`, `requests` 
>
> ###### views.py
>
> ```python
> import requests
> from pprint import pprint
> from django.shortcuts import render
> from decouple import config
> from faker import Faker
> from .models import Job
> # Create your views here.
> 
> def index(request):
>     return render(request, 'jobs/index.html')
> 
> def past_life(request):
>     # 사용자로부터 이름 데이터를 받음.
>     name = request.POST.get('name')
> 
>     # db에 매칭되는 name 가져오기
>     # .get()이 더 간단하지만 해당 값이 없을 경우 에러가 발생한다. => 주로 pk값 가져올 때에만 사용
>     # filter : 값의 개수에 상관없이 무조건 쿼리셋으로 가져옴. (리스트 형식)
>     person = Job.objects.filter(name=name).first()
> 
>     # db에 person이 있는지 없는지 판단
>     if person: # db에 기존 이름이 있다면
>         past_job = person.past_job
>     else: # db에 기존 이름이 없다면 (person이 빈 쿼리셋(==False))
>         faker = Faker()
>         past_job = faker.job()
>         person = Job(name=name, past_job=past_job) # 새로운 레코드를 추가한다.
>         person.save()
> 
>     # GIPHY (past_job 을 API에 요청을 보내서 응답을 받음)
>     GIPHY_API_KEY = config('GIPHY_API_KEY')
>     url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
>     data = requests.get(url).json()
>     try:
>         image = data.get('data')[0].get('images').get('original').get('url')
>     except IndexError:
>         image = None
> 
>     context = {'person': person, 'image': image,}
>     return render(request, 'jobs/past_life.html', context)
> ```
>
> - json 값을 pprint로 확인하기에는 역부족, 
>
>   **=>** http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1
>
>   여기서 자신의 키값과, 나올법한 검색어로 대체해서 확인해보자.
>
> - https://developers.giphy.com/docs/api/endpoint#search
>
>   ![image](https://user-images.githubusercontent.com/52684457/65133599-dac95a80-da3d-11e9-9c5a-8a7f5d31e06c.png)
>
>   ![image](https://user-images.githubusercontent.com/52684457/65133706-09dfcc00-da3e-11e9-9acc-84771fba7cd5.png)
>
>   ```django
>   <!-- index.html -->
>   {% extends 'base.html' %}
>   
>   {% block content %}
>     <h1 class="text-center">당신의 전생을 알려드립니다.</h1>
>     <form action="{% url 'jobs:past_life' %}" method="POST" class="text-center">
>       {% csrf_token %}
>       <label for="name">이름을 입력하세요</label>
>       <input type="text" id="name" name="name">
>   
>       <input type="submit" value="입력">
>     </form>
>   {% endblock content %}
>   ```
>
>   ```django
>   <!-- past_life.html -->
>   
>   ```



























