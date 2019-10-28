# :earth_asia: HTTP

1. 비연결지향( connectionless )
2. 상태정보 유지 X ( stateless, 무상태 ) : 연결이 끊어지는 순간 클라이언트와 서버간의 통신이 끝남 ( *즉, 각각 완벽하게 독립적* )

### :cookie: 쿠키(cookie)

- 클라이언트의 로컬에 저장되는 키, 값의 작은 데이터 파일
- 웹페이지에 접속하면 요청한 웹페이지를 서버로부터 받고 쿠키를 로컬에 저장하고, 클라이언트가 재요청시에 웹페이지 요청과 함께 쿠키 값도 함께 전송
- 아이디 자동완성 
  공지 메세지 하루 안보기(*쿠키가 하루동안만 저장되는 경우*)
  팝업 안보기 체크
  비로그인 장바구니에 담기(*쿠키를 지우면 같이 지워짐*) 등
  **편의를 위하되 지워지거나 유출되어도 큰 일은 없을 정보들을 저장**

### :open_file_folder: 세션(session)

- 사이트와 특정 브라우저( *클라이언트* ) 사이의 상태를 유지시키는 것

- 일정 시간동안 같은 브라우저로부터 들어오는 일련의 요구를 하나의 상태로 보고 상태를 유지하는 기술

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 session id를 쿠키를 사용해 저장. 클라이언트가 서버에 다시 접속하면 해당 쿠키(session id가 담긴)를 이용해 서버에 session id를 전달하여 인증을 받게 된다.

  - 서버 측에서 클라이언트에게 session id(임시 키) 발급, 그 아이디를 클라이언트 측에서 들고 있고 쿠키에 담아 서버로 보내 어떤 사용자인지 서버가 인식함(session id : 중요정보에 접근하기 위한 키)
  - session id가 없으면 서버는 새로운 사용자라고 인식하게 됨

- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다. 실질적인 session의 database에 기본 설정 값으로 저장된다. (이는 쿠키 안에 데이터를 저장하는 것보다 더 보안에 유리하고, 쿠키는 악의적인 사용자들에게 취약하기 때문)

- 세션을 남발하면 사용자가 많은 서버일 경우 서버 부하가 발생한다.

- 쿠키를 지우면 로그아웃이 되는 이유

  **=>** 서버에서는 session에 사용자 로그인 정보를 가지고 있지만, 그것이 내꺼라는 걸 증명할 session id가 쿠키에서 사라졌기 때문이다.



****

**즉,** 

✔ 쿠키 : 클라이언트 로컬에 파일로 저장

✔ 세션 : 서버에 저장(이때 session id는 쿠키의 형태로 클라이언트의 로컬에 저장)

****



#### :moneybag: 캐시(cache)

- 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에는 임시로 저장
- 사용자의 컴퓨터 또는 중간 역할을 하는 서버에 저장



![image](https://user-images.githubusercontent.com/52684457/67169194-f16c2400-f3e4-11e9-8e7e-5aa7a556daa2.png)

- 개발자도구를 사용하면 쿠키 확인이 가능, 



![image](https://user-images.githubusercontent.com/52684457/67169250-4314ae80-f3e5-11e9-8135-d16d8cb8b569.png)

- views에서 index를 들어가자마자 바로 embed값을 준 후, 
  shell이 켜진 터미널에 `request.session` 값을 확인하면 자세한 정보를 알아내기가 어렵다.

- **dir** 함수를 이용해 `magic method`를 까보면 `_session`이라는 매직 매서드를 확인 할 수 있다.

- `request.session._session`

  ```shell
  {'_auth_user_id'': '1',
   '_auth_user_backend': '~~~',
   '_auth_user_hash': '~~~'}
  ```

  - 이 값을 이용해 방문 횟수를 설정할 수 있다.

###### views.py

```python
def index(request):
    # session에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(즉 방문한적이 없다면 = 첫 방문) 0 값을 가져오도록 한다.
    visits_num = request.session.get('visits_num', 0)
    # 그리고 가져온 값을 session에 visits_num 에 매번 1씩 증가한 값으로 할당한다.
    request.session['visits_num'] = visits_num + 1
    # session data 안에 있는 새로운 정보를 수정했다면 django는 수정한 사실을 알아채지 못하기 때문에 다음과 같이 설정.
    request.session.modified = True
	# 여기까지의 구문이 추가 되고, 아래의 context에 마저 받은 값을 저장




    articles = Article.objects.all()
    context = {'articles': articles, 'visits_num': visits_num}
    return render(request, 'articles/index.html', context)
```

- django 공식문서 참고 (session) https://docs.djangoproject.com/en/2.2/topics/http/sessions/#when-sessions-are-saved

  ```python
  # settings.py
  
  # 모든 곳에서 request.session.modified = True 를 기본 값으로 사용하고 싶다면
  # 다음과 같이 설정을 추가하면 된다. (현재는 뷰에서 설정해서 필요 X)
  # SESSION_SAVE_EVERY_REQUEST = True
  ```

  ```python
  <p><b>나의 방문 횟수 : {{ visits_num }}{% if visits_num == 1 %} time{% else %} times{% endif %}</b></p>
  ```

  - `index.html` 에서 이 구문을 추가하면 방문 횟수를 추가할 수 있게 된다.
  - 하지만 admin에서 로그아웃을 했을때, 로그인을 다시 해서 들어갔을 때, 재방문에 대한 카운트가 제대로 되지 않는다 (*세션이 그때마다 다른 값으로 주어져서 각각 다른 유저로 인식 됨 : 계정 고유의 방문 횟수가 아닌, 비회원 + admin 방문 총 누적 횟수가 나옴*) **이것을 해결하기 위해서는 ??** 



# 새로운 앱 (user app => accounts)

```bash
$ python manage.py startapp accounts
```

- 유저앱을 만들때에는 왠만하면 `accounts`로 설정 해주는게 좋다.
  ( *심화 과정에서 차이가 벌어진다.* )
- settings 에서 `'articles.apps.ArticlesConfig',` 추가 (앱 등록)

- project  urls에서  `path('accounts/', include('accounts.urls')),` 추가
- model은 쓸 필요가 없다. 여태까지 사용한 django 내부에 있는 유저 기능들을 이용





## :key: sign up

##### Authentication(인증) - 신원 확인 

(<u>우리가 현재 실습 할 것</u>)

- 자신이 누구인지 주장하는 사람의 신원을 확인하는 것

##### Authorization(권한, 허가) -권한 부여

- 가고싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정



```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)
```

- `views.py` 세팅
- django 내부에 있는 `UserCreationForm` 를 사용
  **공식 문서** : https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.forms



```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

- `urls.py` 세팅



```django
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block content %}
  <h1>회원가입</h1><hr>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='회원가입' reset='Cancel' %}{% endbuttons %}
  </form>
{% endblock content %}
```

- 다른 app(*기존 base 페이지, 현재 만드는 것은 user 페이지*)안에 있는 `base.html`을 가져와서 사용
- `bootstrap4`은 `articles`의 `form.html` 에서 가져오거나,
  https://pypi.org/project/django-bootstrap4/ *자료 확인*



## :closed_lock_with_key: log in

- session을 create



###### views.py

```python
from django.contrib.auth import login as auth_login # 추가

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)
```

- `login`이라는 함수를 사용할 것

  **공식 문서** : https://docs.djangoproject.com/en/2.2/topics/auth/default/#how-to-log-a-user-in

  - 하지만 이미 뷰함수에 있는 이름과 겹치기 때문에 `as` 를 사용하여 함수 이름을 변경
    (*되도록 유저 뷰함수는 변경시키지 않는게 좋다.*)

- urls.py에  `path('login/', views.login, name='login'),`  추가



```django
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block content %}
  <h1>로그인</h1><hr>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='로그인' reset='Cancel' %}{% endbuttons %}
  </form>
{% endblock content %}
```

- signup을 그대로 가져오면 된다. 회원가입 **=>** 로그인으로만 글씨를 바꿔주자.

- `article/base.html` 에서 `<h3>Hello, {{ user.username }}</h3><hr>`를 추가하면 회원이름을 불러와서 인삿말을 추가할 수 있다.
  [공식 문서](https://docs.djangoproject.com/en/2.2/topics/auth/default/#user-objects) 를 확인하면 `username` 이라는 값을 사용하면 된다는 것을 알 수 있다.





## :door: log out

- session을 delete

  **공식 문서** : https://docs.djangoproject.com/en/2.2/topics/auth/default/#how-to-log-a-user-out

###### views.py

```python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

- `urls.py` **=>** `path('logout/', views.logout, name='logout'),` 추가





#### :hand: 로그인 사용자에 대한 접근 제한 [Authentication](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#authentication-in-web-requests)

- django는 세션과 미들웨어를 통해 인증 시스템을 request 객체에 연결한다.
- request 는 현재 사용자를 나타내는 모든 요청에서 `request.user` 를 제공한다.

`is_authenticated`

- user model의 속성(attributes)들 중 하나
- 사용자가 인증 되었는지 알 수 있는 방법
- User 에는 항상 True / AnonymousUser 에 대해서만 항상 False
- 단, 이것은 권환(permission)과는 관련이 없으며 사용자가 활동중(active)이거나 유효한 세션(valid session / 불러온 세션이 아닌, django가 부여한 세션)을 가지고 있는지도 확인하지 않는다. 
- 일반적으로  `request.user`에서 이 속성을 사용하여 middle ware의 `django.contrib.sessions.middleware.SessionMiddleware` 를 통과했는지 확인한다.



****

`articles/views.py`의 `index` 함수에서 `embed`



1. 비로그인 상태에서 (세션을 지운 후)

> ###### request.user
>
> request.user.is_anonymous
>
> - True
>
> request.user.is_authenticated
>
> - False
>
> request.user.is_superuser
>
> - False



2. admin으로 로그인 상태에서

> ###### request.user
>
> resquest.user.is_anonymous
>
> - False
>
> request.user.is_authenticated
>
> - True
>
> request.user.is_superuser
>
> - True



3. 일반 로그인 상태에서

> ###### request.user
>
> resquest.user.is_anonymous
>
> - False
>
> request.user.is_authenticated
>
> - True
>
> request.user.is_superuser
>
> - False



****

#### :eyes: 회원이면 로그아웃, 비회원은 로그인, 회원가입 항목

###### articles/base.html

```django
{% if user.is_authenticated %}
  <h3>
    Hello, {{ user.username }}
    <a href="{% url 'accounts:logout' %}">로그아웃</a>
  </h3>
  {% else %}
    <a href="{% url 'accounts:login' %}">로그인</a>
    <a href="{% url 'accounts:signup' %}">회원가입</a>
  {% endif %}
```

- `if` 문 추가



#### :eye_speech_bubble: 회원만 새 글을 작성할 수 있도록 수정

###### index.html

```django
{% if user.is_authenticated %}
  <a href="{% url 'articles:create' %}">[NEW]</a>
  {% else %}
  <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
```

> ###### request 생략 가능
>
> request.user.is_authenticated **=>** user.is_authenticated
>
> request.user.username **=> **user.username

- 하지만 articles/create url주소로 들어가면 아직 새 글을 작성이 가능하다.



##### :heart_decoration: 데코레이터(decorator)를 사용

 이전에 사용한 `require_POST`는 method권한을 조절해주는 데코레이터

지금 사용할 데코레이터는 유저가 인증이 되어있는지 안되어있는지 확인해주는 기능
**=>** `from django.contrib.auth.decorators import login_required` [공식문서 ](https://docs.djangoproject.com/en/2.2/topics/auth/default/#the-login-required-decorator)

- articles의 `views.py`에 `import` 후,  `create, update`위에 `@login_required` 할당

  - `delete, comment` 함수들은 아래에서 계속

  ```python
  @login_required
  def create(request):
      ...
      
  @login_required
  def update(request, article_pk):
      ...
  ```

![image](https://user-images.githubusercontent.com/52684457/67177224-92b8a180-f408-11e9-9ce9-acd13bad0937.png)



##### `next` query string parameter

- @login_required 데코레이터가 기본적으로 인증 성공 후 사용자를 리다이렉트 할 경로를 next 라는 문자열 매개 변수에 저장
- 우리가 url로 접근하려고 했던 그 주소가 로그인하지 않으면 볼 수 없는 곳이라서, django가 로그인 페이지로 강제로 리다이렉트 했는데, 로그인을 다시 정상적으로 하고 나면 원래 요청했던 주소로 보내주기 위해 keep 해주는 것



로그아웃 상태에서 강제로 `articles/create` url로 접속했을때(위의next 함수있는 상태)로 `login` 함수 `embed`

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid:
            auth_login(request, form.get_user())
            # embed()
            ...
```

> request.GET
>
> request.GET.get('next')

`request.GET.get('next')` 이 값을 사용하면 next값의 redirect 주소를 설정해줄 수 있다.

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        ...
    return render(...)
```





- 하지만 지금은 `comment` 함수들에있는 `@required_POST` 와 `@login_required` 는 로직상 에러가 발생한다.

- `@required_POST` 가 있는 함수에 `@login_required` 가 설정된다면 로그인 이후  "next" 매개변수를 따라 해당 함수로 다시 `redirect` 되면서 `@required_POST` 때문에 `405 error`가 발생

- `@login_required` 대신 함수 내에 `if request.user.is_authenticated:` 구문 추가

  ```python
  @require_POST
  def delete(request, article_pk):
      if request.user.is_authenticated:
          ...
          
  @require_POST
  def comments_create(request, article_pk):
      if request.user.is_authenticated:
          ...
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      if request.user.is_authenticated:
          ...
  ```



- 비인증 상태에서의 댓글을 삭제를 한다면 401 에러가 뜬다
  **=>** https://developer.mozilla.org/ko/docs/Web/HTTP/Status/401

- 좀더 시멘틱하게 바꿔주기 위해서

  ```python
  from django.http import Http404, HttpResponse
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk)
          comment.delete
          return redirect('articles:detail', article_pk)
      return HttpResponse('You are Unauthorized', status=401)
  ```

  `return HttpResponse('You are Unauthorized', status=401)` 를 추가





#### :heavy_check_mark: 회원가입과 동시에 로그인 작동

- `AuthenticationForm` 에서는 `get_user()`로 유저를 뽑아왔지만, 모든 폼에서 `get_user()` 로 유저를 뽑아올수 없음,
- `form.save()` 안에 객체가 있는것을 확인 **=>** 리턴 값에 유저값이 있는 것을 이용해서 변수에 저장

###### views.py

```python
def signup(request):
    if request.user.is_authenticated: # 인증된 유저라면,
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            # form.save()를 통해 반환된 User 클래스의 인스턴스를 auth_login의 인자로 전달
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated: # 인증된 회원이라면,
        return redirect('articles:index')
```





## :no_entry_sign: 회원 탈퇴

logout과 다르게 세션이 아닌 DB를 날려버리는 것

###### account/views.py

```python
@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```



###### articles/base.html

```django
<form action="{% url 'accounts:delete' %}" method="POST" style="display: inline;">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴" class="btn btn-danger">
</form>
```

- 로그아웃 옆에 버튼형식으로 넣어준 회원탈퇴 버튼



## :pen: 회원 수정

[공식 문서](https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.forms.UserChangeForm)

###### base.html



###### Before views.py

```python
from django.contrib.auth.forms import UserChangeForm

def update(request):
    if request.method == 'POST':
        pass
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/update.html', context)
```

![image](https://user-images.githubusercontent.com/52684457/67180265-0f04b200-f414-11e9-8d24-62267e2919f6.png)

- 관리자 권한까지 가지게 되므로 적절하지 않다.
- 수많은 정보들 중에서 몇가지만 수정할 수 있도록 지정해주는 것이 필요하다.



#### `get_user_model()`

- `User` 를 직접 참조하는 대신 `from django.contrib.auth import get_user_model` 를 사용하여 User model을 참조해야 한다.
  [django github](https://github.com/django/django/blob/master/django/contrib/auth/forms.py)

  [User](https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L132) - 빈 껍데기 인것을 확인 가능

  ![image](https://user-images.githubusercontent.com/52684457/67180054-52aaec00-f413-11e9-88d5-8db95cd2cc54.png)

  [AbstractUser](https://github.com/django/django/blob/2f72480fbd27896c986c45193e1603e35c0b19a7/django/contrib/auth/models.py#L316) - 세 가지 정보를 가짐 (권한이 줄어들지만 편함)

  [AbstractBaseUser](https://github.com/django/django/blob/2f72480fbd27896c986c45193e1603e35c0b19a7/django/contrib/auth/base_user.py#L47) - 두 가지 정보를 가짐 (권한이 늘어나지만 만들게 많음)

- 이 함수는 현재 활성화(active) 된 User model을 return 한다.

![image](https://user-images.githubusercontent.com/52684457/67180114-90a81000-f413-11e9-85cf-80dfafc99a1d.png)

- [기본 속성 5 가지](https://docs.djangoproject.com/en/2.2/topics/auth/default/#user-objects)



###### models.py

![image](https://user-images.githubusercontent.com/52684457/67180717-5fc8da80-f415-11e9-913b-70ccadebc60c.png)

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # return 값이 User
        fields = ('email', 'last_name', 'first_name',)
```



###### After views.py

```python
from . forms import CustomUserChangeForm

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/update.html', context)
```

![image](https://user-images.githubusercontent.com/52684457/67180210-dcf35000-f413-11e9-9dbe-6f10782aded0.png)

```python
from django.contrib.auth.decorators import login_required

@login_required
def update(request):
    ...
```

- 데코레이터까지 넣어줌으로서 로그인한 상태에서만 정보수정 페이지에 들어갈 수 있도록 한다.

  

## :1234: 비밀번호 변경

[PasswordChangeForm](https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.forms.PasswordChangeForm)

###### accounts/views.py

```python
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/change_password.html', context)
```

- 비밀번호 변경 후 로그아웃 되는 현상

  - 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하게 않게 되어 버렸기 때문.

  - DB에서는 정보에서 비밀번호가 바뀌고 세션 또한 바뀌었지만 세션이 이를 따라가지 못함

  - 세션을 잡아줄수 있는 것이 필요
    **=>** [update_session_auth_hash()](https://docs.djangoproject.com/en/2.2/topics/auth/default/#session-invalidation-on-password-change) 

    [`update_session_auth_hash`**(***request***,** *user***)**](https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.update_session_auth_hash)

    - 현재 사용자의 인증 세션이 무효화 되는 것을 막고, 세션을 유지한 상태로 업데이트
    - 현재 request 와 새로운 session hash 가 생긴 업데이트 된 user 객체를 적절히 업데이트

```python
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return ...
    else:
        ...
    return ...
```

- `update_session_auth_hash(request, form.user)` 추가
- 비회원의 비밀번호 변경 페이지에 접속하지 못하도록 `@login_required` 입력



## :card_file_box: template 정리

- signup, login, update, change_password html이 전부 같은 틀이므로, 하나의 html 파일로 정리해 줄 수있다.

  ###### auth_form.html

  ```django
  {% extends 'articles/base.html' %}
  {% load bootstrap4 %}
  
  {% block content %}
  
  {% if request.resolver_match.url_name == 'signup' %}
    <h1>회원가입</h1><hr>
  {% elif request.resolver_match.url_name == 'login' %}
    <h1>로그인</h1><hr>
  {% elif request.resolver_match.url_name == 'update' %}
    <h1>회원정보 수정</h1><hr>
  {% else %}
    <h1>비밀번호 변경</h1><hr>
  {% endif %}
  
  
    <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form %}
      {% buttons submit='submit' reset='Cancel' %}{% endbuttons %}
    </form>
  {% endblock content %}
  ```

  

  ###### views.py

  ```python
  from IPython import embed
  from django.contrib.auth.decorators import login_required
  from django.views.decorators.http import require_POST
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as auth_logout
  from django.contrib.auth import update_session_auth_hash
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
  from . forms import CustomUserChangeForm
  # Create your views here.
  
  def signup(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {'form': form,}
      return render(request, 'accounts/auth_form.html', context)
  
  
  def login(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect(request.GET.get('next') or 'articles:index')
      else:
          form = AuthenticationForm()
      context = {'form': form,}
      return render(request, 'accounts/auth_form.html', context)
  
  
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  
  @require_POST
  def delete(request):
      request.user.delete()
      return redirect('articles:index')
  
  @login_required
  def update(request):
      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      context = {'form': form,}
      return render(request, 'accounts/auth_form.html', context)
  
  @login_required
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {'form': form,}
      return render(request, 'accounts/auth_form.html', context)
  ```

  - accounts의 html을 전부 auth_form.html로 연결해준다.

