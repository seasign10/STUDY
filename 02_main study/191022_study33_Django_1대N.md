

# :dog: django - User : Article

`AUTH_USER_MODEL = 'auth.User'` settings.py 에서는 찾아 볼 수 없지만 이미 내부적으로 설정이 되어있기 때문에 (*default 값으로 사용할 때에는*) 굳이 기입할 필요가 없다. 

### :earth_africa: django가 서버가 켜질 때 초기화 순서

1. `INSTALLED_APPS` 의 각 항목을 import 합니다. (단, 위에서 아래로)

   - 이 과정에서 직간접적으로 모델을 import해선 안된다.
   - 1번 단계에서 app을 import 하는 동안 불필요한 제약들을 피하기 위해 이 단계에서는 모델을 가져오지 않는다.

2. 각 어플리케이션의 models를 import 한다.

   - 2단계가 완료되면 `get_model()` 과 같은 모델에서 작동하는 API들을 사용할 수 있다.
     `get_user_model()`

     - **return 값** : class

     `settings.AUTH_USER_MODEL`

     - **return 값** : srt

3. `App_Config` 의 `ready()` 메서드를 실행한다.

   - 2단계가 완료된 후에야 `get_user_model()`을 사욜할 수 있는데 아직 accounts app 이 INSTALLED_APP의 작성 순서 때문에 아직 inport가 완료되지 않은 상황이라 `get_user_model()` 이 어떤 User model을 return 해야 하는지  django가 알 수 없는 상태.

4. **결론** 

   - 모든 곳에서 User model을 호출 할 때는 `get_user_model()`
   - 단, `models.py` 에서만 `settings.AUTH_USER_MODEL` 

![image](https://user-images.githubusercontent.com/52684457/67252735-38265080-f4af-11e9-93e0-59b3b9be9af2.png)

- 아이디 값이 1이 없다면 1로 지정할 수 없으니 DB 테이블을 보고 가지고 있는 값으로 지정

![image](https://user-images.githubusercontent.com/52684457/67252783-6efc6680-f4af-11e9-85ba-c8975c665ba4.png)

- 보이지 말아야 할 항목이 보인다.

  선택적으로만 보여주도록 바꾸자면, aritlces의 `forms.py`에서  `fields = '__all__'` 를 수정해주어야 한다.

  ```python
  class Meta:
          model = Article
          fields = ('title', 'content',)
  ```

  - 항목은 사라졌으나 CREATE에서 새로운 글을 작성 시, 에러가 뜬다.

  ![image](https://user-images.githubusercontent.com/52684457/67252971-5f315200-f4b0-11e9-911a-d840e14a72f8.png)

  

###### aticles/views.py

```python
@login_required
def create(request):
    ...
	if form.is_valid():
        article = form.save(commit=False)
        # article.user_id = request.user.pk
        # 객체를 가져올 수 있다면 객체 자체를 그대로 넣어준다.
        article.user = request.user
        article.save()
        return redirect(article)
```

- `{{ article.user }}` 로 유저 정보를 html로 불러올 수도 있다.



**detail.html** 에서 본인만 글을 수정, 삭제 할 수 있도록 설정

```django
{% if request.user == article.user %}
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  {% endif %}
```

- `if` 문을 추가
- 하지만 버튼만 지운 것일 뿐, 완전히 막은 것은 아니다.
- request는 생략가능하지만 직관성이 떨어지기 때문에 붙여주는게 좋다.



###### articles/views.py

- delete와, update 함수에서 설정

```python
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated: # 인증이 된 회원인지 아닌지 검열 후,
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user: # 게시글이 본인인지 아닌지 검사
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) 
    if request.user == article.user: # 게시글이 본인인지 아닌지 검사
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        context = {'form': form, 'article': article,}
        return render(request, 'articles/form.html', context)
```



- comment도 설정 해주어야 하니, `models.py`에서 `class Article` 처럼 `class Comment` 에서도 user 값을 넣어주어야 한다.
- `user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)` 

![1571707101056](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571707101056.png)

- id값이 정상적으로 생성 되었는지 DB를 확인



###### articles/views.py

```python
if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user_id = request.user
            comment.save()
```

- 우선 모델에서 user 값을 추가했기 때문에 user_id를 `comments_create` 에 추가해주어야 한다.

```django
{% if user.is_athenticated %}
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value="COMMENT">
</form>
{% else %}
  <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인 하세요]</a>
{% endif %}
```

- 비 회원은 댓글을 달지 못하도록 가린다.
  - 인증이 된 회원인지 if 문을 넣어준다.



```python
  {% for comment in comments %}
    <div>
      댓글 {{ forloop.revcounter }} : {{ comment.content }}
      {% if request.user == comment.user %}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST"  style="display: inline;">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
        <hr>
      {% else %}
        댓글 {{ forloop.revcounter }} : {{ comment.content }} <hr>
      {% endif %}
    </div>
  {% empty %}
    <p><b>댓글이 없습니다.</b></p>
  {% endfor %}
```

- 본인이 쓴 댓글이 아니면 삭제할 수 없도록 delete 버튼 에 if문 추가
  `{% if request.user == comment.user %}`



```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete
            return redirect('articles:detail', article_pk)
        else:
            return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)
```

- 내부적으로도 접근하지 못하도록 설정했다.



- `UserCreationForm` 이 코드를 기준으로 상속을 받을 것

###### accounts/forms.py

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password1', 'password2', 'password3')
    class Meta(UserCreationForm): # UserCreationForm 의 Meta를 상속 받을 수 있음
        # model은 이미 가지고 있기 때문에 생략 가능,
        fields = UserCreationForm.Meta.fields + ('email',)
        # UserCreationForm의 Meta에 있는 fields + ...
```



###### accounts/views.py

```python
from . forms import CustomUserChangeForm, CustomUserCreationForm
# from django.contrib.auth.forms 에 있는 UserCreationForm 은 forms.py의 CustomUserCreationForm 으로 대체
# 함수 signup 의 UserCreationForm 도 동일하게 대체
```



****

## :person_with_blond_hair: Gravatar

(*쉬어 가기*)

유저의 프로필 이미지를 gravatar로 설정해보자.

![image](https://user-images.githubusercontent.com/52684457/67257428-db369480-f4c6-11e9-9542-c12455749c30.png)

###### articles/views.py

```python
def index(request):
    if request.user.is_authenticated:
        gravatar_url = hashlib.mb5(request.user.email.encode('utf-8').lower().strip()).haxdigest()
    else:
        gravatar_url = None
        
        ...
        
        context = {'articles': articles,...,'gravatar_url': gravatar_url,}
        ...
```

- `lower()` : 대문자를 소문자로
- `strip()` : 공백 제거



###### base.html

```django
{% if user.is_authenticated %}
  <img src="https://s.gravatar.com/avatar/{{ gravatar_url }}?s=80" alt="img">
 ...
{% endif %}
```

- 하지만 이 작업을 정보수정, 비밀번호 변경 페이지 등에서 확인을 하면 이미지를 제대로 불러오지 않는 일이 생긴다.

  - articles/view.py 에서 모든 페이지에 대한 함수에서 `gravatar_url` 작업을 번거롭게 해주어야 한다.

  

이 작업을 최소화 하기 위하여 **filter를 커스텀** 해보자.  [filter](https://docs.djangoproject.com/ko/2.2/howto/custom-template-tags/#custom-template-tags-and-filters)

![image](https://user-images.githubusercontent.com/52684457/67255813-eeddfd00-f4be-11e9-8af5-0766cc3b782b.png)

- django 공식 문서를 참고하여 양식을 따른다.
  - app파일 안에 `templatetags` 폴더를 만들고 안에 `__init__.py`와 filter를 만들어줄 파일을 생성한다. 이름을 `gravatar.py`로 진행할 것이다.

###### gravatar.py

```python
import hashlib # 필요한 함수 import

# register = template.Library()까지 django 공식문서 양식 (위의 링크 참조)
from django import template 

register = template.Library() # 기본 템플릿 라이브러리에

# 아래의 함수를 추가한다.
@register.filter # django 가 인식하도록 데코레이터 추가, => 필터로 인식이 됨
def makemd5(email): # filter 앞의 인자 (이름은 크게 상관 없음)
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()
```



###### base.html

```django
 {% if user.is_authenticated %}
  <img src="https://s.gravatar.com/avatar/{{ user.email|makemd5 }}?s=80" alt="img">
...
```

- `request.user.email` (`request 생략 가능`) 뒤에 filter를 넣어준다. `|makemd5`

- 회원이 입력해놓은 자신의 정보 이메일에 따라 gravatar 프로필 이미지가 뜨는 것을 확인 할 수 있다.



****

## :handshake: Model relationships

1. ##### Many-to-one

2. ##### Many to many

   - User : Article = M :  N (다대다 관계)
   - User는 여러개의 Article 에 Like 할 수 있고
   - Article 은 여러 User 로 부터 Like를 받을 수 있다.





**Modeling**은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.

#### 1. 1:N의 생성

- 환자와 의사의 예약 시스템 구축 외주를 받았다면 **=>** **의사1 : 환자 N**

###### :heavy_check_mark: models.py

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
class Patient(models.Model):
    name = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```



###### :heavy_check_mark: power_shell

```powershell
In [1]: doctor1 = Doctor.objects.create(name='Justin')

In [2]: doctor2 = Doctor.objects.create(name='zzulu')

In [3]: patient1 = Patient.objects.create(name='tak', doctor=doctor1)

In [4]: patient2 = Patient.objects.create(name='harry', doctor=doctor2)

In [5]: doctor1
Out[5]: <Doctor: 1번 의사 Justin>

In [6]: doctor2
Out[6]: <Doctor: 2번 의사 zzulu>

In [7]: patient1
Out[7]: <Patient: 1번 환자 tak>

In [8]: patient2
Out[8]: <Patient: 2번 환자 harry>

In [9]: patient3 = Patient.objects.create(name='tak', doctor=doctor2)

In [10]: patient3
Out[10]: <Patient: 3번 환자 tak>

In [11]: patient3.doctor.name
Out[11]: 'zzulu'

In [12]: patient4 = parient.objects.create(name='harry', doctor=doctor1, doctor2)
  File "<ipython-input-12-af58ce8853a7>", line 1
    patient4 = parient.objects.create(name='harry', doctor=doctor1, doctor2)
                                                                   ^
SyntaxError: positional argument follows keyword argument


In [13]: patient4 = parient.objects.create(name='harry', doctor=doctor1, doctor=doctor
    ...: 2)
  File "<ipython-input-13-bd6e195b4975>", line 1
    patient4 = parient.objects.create(name='harry', doctor=doctor1, doctor=doctor2)
                                                                   ^
SyntaxError: keyword argument repeated
```

- 예약을 여러 의사한테 받을 수 없고(intrger만 받는 테이블은 ,(콤마)를 사용할 수 X)

- 수정하려면 새로운 값을 넣는 방법 말곤 수정 방법이 없다.

- **1:N의 한계**

  **=>** 중개모델 생성  (*불필요한 레코드 생성을 줄여주기 위해 예약수정 : 필드 반복생성,*)



#### 2. 중개모델 생성

****

###### 예시

- ##### doctor

|  id  |  name  |
| :--: | :----: |
|  1   | Justin |
|  2   | zzulu  |



- ##### patient

|  id  | name  |
| :--: | :---: |
|  1   |  tak  |
|  2   | harry |



- 중개 모델 (**reservation**)

|  id  | doctor_id | patient_id |
| :--: | :-------: | :--------: |
|  1   |     1     |     1      |
|  2   |     1     |     2      |
|  3   |     2     |     1      |

****



###### :heavy_check_mark: models.py

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
class Patient(models.Model):
    name = models.TextField()
    # 아래의 중개모델 생성이 대신 역할을 해주기 때문에 외래키가 필요없다.

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

- 역참조를 한쪽 방향만 가능하게 된다.



#### 3. 중개모델을 직접 거치지 않고 바로 가져오기 (직접 참조)

- `Through` option
- MTOM 필드는 실제 물리적인 필드가 DB에 생기는 것이 아니다.

###### :heavy_check_mark: models.py

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
class Patient(models.Model):
    name = models.TextField()
    # manytomany(through option)를 가지고있는 patient만 doctor을 _set을 사용하지 않고 역참조 가능
    # => doctors.all()
    doctors = models.ManyToManyField(Doctor, through='Reservation')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

- `patient1 = Patient.objects.get(pk=1)` => 환자1 불러옴
  `doctor1 = Doctor.objects.get(pk=1)` => 의사1 불러옴

- `patient1.doctors.all()` 
  **=>** 환자1의 모든 의사를 **조회할 수 있다.**

- `doctor1.patients.all()`

  **=>** 의사1의 모든 환자를 **조회할 수 없다.**



#### 4. Doctor도 patients로 참조하기

- `related_name` : doctor는 필드가 없기 때문에 그대로 역참조를 하기 힘든 부분을 개선
  - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러 올지에 대해 정의한다.
  - 필수적으로 사용하는건 아니지만, 필수적인 상황이 발생할 수 있다.

###### :heavy_check_mark: models.py

```python
class Patient(models.Model):
    name = models.TextField()
    # manytomany(through option)를 가지고있는 patient만 doctor을 _set을 사용하지 않고 역참조 가능
    # => doctors.all()
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

```powershell
In [1]: doctor1 = Doctor.objects.get(pk=1) # doctor1 불러옴

In [2]: doctor1.patient_set.all()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-2-e81b89c43a95> in <module>
----> 1 doctor1.patient_set.all()

AttributeError: 'Doctor' object has no attribute 'patient_set'

In [3]: doctor1.patients.all()
```

- `patient_set` 은 `related_name`을 설정해준 순간 사라진다.

****

- ##### doctor

  - `related_name` : Doctor => patients

|  id  |  name  |
| :--: | :----: |
|  1   | Justin |
|  2   | zzulu  |



- ##### patient

  - `through` option : Patient => doctors

|  id  | name  |
| :--: | :---: |
|  1   |  tak  |
|  2   | harry |

****

- 이제 서로를 직접 참조할 수 있게 되었다.

```python
# 인스턴스 생성
In [1]: doctor1 = Doctor.objects.create(name='justin') 

In [2]: patient1 = Patient.objects.create(name='tak')

# 조회
In [3]: doctor1 
Out[3]: <Doctor: 1번 의사 justin>

In [4]: patient1
Out[4]: <Patient: 1번 환자 tak>

# doctor1 에 patient1을 add
In [6]: doctor1.patients.add(patient1)

    
# 서로 참조, 연결되어있는 것을 확인 할 수 있다.
In [7]: doctor1.patients.all()
Out[7]: <QuerySet [<Patient: 1번 환자 tak>]>

In [8]: patient1.doctors.all()
Out[8]: <QuerySet [<Doctor: 1번 의사 justin>]>

    
# add한 값을 지우기
In [9]: patient1.doctors.remove(doctor1)

# 두 곳에서 전부 찾아 볼 수 없음
In [10]: patient1.doctors.all()
Out[10]: <QuerySet []>

In [11]: doctor1.patients.all()
Out[11]: <QuerySet []>
```

- `doctors = models.ManyToManyField(Doctor, related_name='patients')`
  ` through='Reservation',` **=>** 삭제
- `class Reservation(models.Model):` **=>** 삭제
- `makemigrations`, `migrate`





#### 5. 중개모델이 필요없어지는 것은 아니다.

- 예약한 시간 정보를 담는다거나 하는 경우(*== 추가적인 필드가 필요한 경우*)에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.



# :heart: LIKE 기능 구현

- user는 여러 article에 좋아요를 누를 수 있고
- article은 여러 user로 부터 좋아요를 받을 수 있다.

> `article.user` **=>** 게시글을 작성한 유저 **1:N**
>
> `article.like_users` **=>** 게시글을 좋아요한 유저 **M:N**
>
> `user.like_articles` **=>** 유저가 좋아요를 누른 게시글(역참조, `related_name`) **M:N**
>
> - blank=True (*좋아요가 0개인 경우 즉, 빈 값을 허용해야 함*)
> - num=True 는 다르다.
>
> `user.article_set` **=>** 유저가 작성한 게시글 (겹치게 되는 상황이 옴) **1:N**

###### articles/models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    ...
	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    # 물리적 필드가 DB에 생기는 것이 아닌, 중개테이블이 생긴다.
```

![image](https://user-images.githubusercontent.com/52684457/67264612-93c00080-f4e6-11e9-9ae1-8424856deb14.png)



#### :black_heart: 좋아요 출력

- 방법은 두가지가 있다.

###### articles/views.py ==> `in`

```python
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속 유저가 있다면 좋아요를 취소
    if request.user in article.like_users.all():
        article.like_users.remove(request.user) # 좋아요 취소
    else:
        article.like_users.add(request.user) # 좋아요 활성
    return redirect('articles:index')
```

###### articles/views.py ==> `filter`

```python
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # get 유일한 값만 출력, filter 값이 없어도 빈값 출력
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```



- 좋아요 갯수 세는 법

> `article.like_users.all|length`
>
> `article.like_users.all|count`





- 이제 하나의 html이 무거워졌기 때문에 나중에 관리에 어려움을 겪는다. 

  **=>** 역할별로 파티션 나누기

###### index.html

```django
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Articles</h1>
  <p><b>나의 방문 횟수 : {{ visits_num }}{% if visits_num == 1 %} time{% else %} times{% endif %}</b></p>
  {% if user.is_authenticated %}
  <a href="{% url 'articles:create' %}" class="btn btn-primary">NEW</a> <hr>
  {% else %}
  <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
  {% for article in articles %}
    {% include 'articles/_article.html' %}
    <br>
  {% endfor %}
{% endblock content %}
```

- `{% include 'articles/_article.html' %}` 를 사용해서 분할한 html을 연결해주면 된다.

######  _article.html

```python
<div class="card">
  <div class="card-header">작성자 : {{ article.user }}</div>
  <div class="card-body">
    <h5 class="card-title">제목 : {{ article.title }}</h5>
    <p class="card-text">{{ article.pk }} <b>번째 글</b></p>
    <p class="card-text">
      <a href="{% url 'articles:like' article.pk %}">
        {% if user in article.like_users.all %}
        <i class="fas fa-fire-alt" style="color: orange;"></i><br>
        {% else %}
        <i class="fas fa-fire-alt" style="color: gray;"></i><br>
        {% endif %}
      </a>
      <b>{{ article.like_users.all|length }}명</b>이 이 글을 좋아합니다.
    </p>

    <a href="{{ article.get_absolute_url }}" class="btn btn-primary">DETAIL</a>
  </div>
</div>
```



- 비로그인이 좋아요를 누를수 없게 방지하려면 함수 `like`위에 데코레이터 `@login_required`를 붙여준다.



##### << 결과 페이지 >>

![image](https://user-images.githubusercontent.com/52684457/67264344-cd443c00-f4e5-11e9-825a-c43b2158eb72.png)



# :person_frowning: 프로필 설정

###### accounts/views.py

```python
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username) # 하나의 값만 가져올 때
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)
```

- url path **=>** `path('<username>/', views.profile, name='profile'),`

- `<username>/` 이라는 주소는 임의의 문자열이기 때문에 url 최상단에 있으면 위에서 다 걸려 아래의 나머지 페이지들이 `page not found` 에러가 뜬다.



> ###### 앞으로 할 것
>
> 1. 유저가 장성한 게시글 목록
> 2. 유저가 작성한 댓글목록
> 3. 정렬은 모두 최근에 작성한 것 부터
> 4. 각 게시글의 부가정보(좋아요, 댓글의 수)



- 인스턴스 person을 이용해보자.

  ###### profile.html

  ```django
  {% extends 'articles/base.html' %}
  
  {% block content %}
  <h1 class="text-center">{{ person.username }}'s Profile</h1>
  <hr>
  
  <br>
  <h3 class="text-center">{{ person.username }}이 작성한 글</h3>
  {% for article in person.article_set.all %}
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ article.content }}</h5>
      <p class="card-text">{{ article.like_users.count }}명이 좋아하는 글</p>
      <p class="card-text">{{ comments|length }}개의 댓글</p>
      <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">DETAIL</a>
    </div>
  </div>
  {% endfor %}
  
  <br>
  <h3 class="text-center">{{ person.username }}이 작성한 댓글</h3>
  {% for comment in person.comment_set.all %}
  <div class="card">
    <div class="card-body">
      <blockquote class="blockquote mb-0">
        <p>{{ comment.content }}</p>
        <footer class="blockquote-footer">{{ comment.created_at }}</footer>
      </blockquote>
    </div>
  </div>
  {% endfor %}
  
  {% endblock content %}
  ```

  - `person.article_set.all` 과 `person.comment_set.all` 는 함수 view에서 `context`로 담아서 가져와도 상관이 없다.
  - 갯수를 세는데에는 `count`와 `length` 둘다 사용할 수 있다.



```django
{% extends 'articles/base.html' %}

{% block content %}

<h1 class="text-center">{{ person.username }}'s Profile</h1>
<hr>
<br>


<h3 class="text-center">{{ person.username }}이 작성한 글</h3>
<div class="row">
  {% for article in articles %}
  <div class="col-4 my-2">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ article.content }}</h5>
        <p class="card-text">{{ article.like_users.count }}명이 좋아하는 글</p>
        <p class="card-text">{{ comments|length }}개의 댓글</p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">DETAIL</a>
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<br>
<h3 class="text-center">{{ person.username }}이 작성한 댓글</h3>
<br>

<div class="row">
  {% for comment in comments %}
  <div class="col-4 my-2">
    <div class="card">
      <div class="card-body">
        <blockquote class="blockquote mb-0">
          <p>{{ comment.content }}</p>
          <footer class="blockquote-footer">{{ comment.created_at }}</footer>
        </blockquote>
      </div>
    </div>
  </div>
  {% endfor %}
</div>

{% endblock content %}
```





##### `with` template tag

- 복잡한 변수를 더 간단한 이름으로 저장(캐시)하며, 여러번 DB를 조회할 때 (특히 비용이 많이 드는) 유용하게 사용 가능

```python
{% with articles=person.article_set.all %}
  <!-- {% with person.article_set.all as article %} 과 동일 -->
  <!-- with가 한번 조회 했기 때문에 계속 all이 조회되지 않아 반복 요청을 줄일 수 있다. -->
  {% for article in articles %} 
  <div class="col-4 my-2">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ article.content }}</h5>
        <p class="card-text">{{ article.like_users.count }}명이 좋아하는 글</p>
        <p class="card-text">{{ comments|length }}개의 댓글</p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">DETAIL</a>
      </div>
    </div>
  </div>
  {% endfor %}
{% endwith %}
```

- 하지만 조기 최적화는 프로그래밍에서 악의 근원이다.
- 최적화 보다 중요한 것을 제쳐두고 효율적인 코드에 시간을 낭비하는것은 문제가  된다.
  ( *코드는 코드 자체적으로도 빨라야 하지만, 더 중요한 것은 다른 개발자들이 읽기 쉬워야한다.* )



##### :black_medium_small_square: nav bar

- nav bar 추가 + template를 한번 더 정리 

  ###### base.html

  ```python
  {% load bootstrap4 %}
  {% load gravatar %}
  
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/e7c9242ec2.js" crossorigin="anonymous"></script>
    {% bootstrap_css %}
    <title>Document</title>
  </head>
  <body>
    {% include 'articles/_nav.html' %}
    
    <div class="container">
      {% block content %}
      {% endblock content %}
      {% bootstrap_javascript jquery='full' %}
    </div>
  </body>
  </html>
  ```

  ###### _nav.html

  ```python
  {% load gravatar %}
  
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <img src="https://s.gravatar.com/avatar/{{ user.email|makemd5 }}?s=80" width="30" height="30"
      class="d-inline-block align-top" alt="img">
    {% if user.is_authenticated %}
    <a class="navbar-brand" href="{% url 'articles:index' %}">&nbsp; Hello, {{ user.username }}</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:profile' user.username %}">활동조회</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:update' %}">정보수정</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:change_password' %}">비밀번호변경</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:logout' %}">로그아웃</a>
        </li>
        <li>
          <form action="{% url 'accounts:delete' %}" class="nav-item nav-link" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴" class="btn btn-danger"  onclick="return confirm('회원탈퇴를 하시겠습니까?')">
          </form>
        </li>
      </ul>
    </div>
  {% else %}
    <a class="navbar-brand" href="{% url 'articles:index' %}">Hello!</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
  
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:login' %}">로그인</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:signup' %}">회원가입</a>
      </ul>
    </div>
  {% endif %}
  </nav>
  ```

  - bootstrap을 활용해서 간편하게 넣자
  - `<input type="submit" value="회원탈퇴" class="btn btn-danger"  onclick="return confirm('회원탈퇴를 하시겠습니까?')">`
    회원탈퇴 input에 `onclick`을 넣어 실수로 회원탈퇴를 하지않도록 추가했다.

  ###### (추가) detail.html / _article 을 bootstrap으로 꾸민 모습

  1. ##### detail.html

  ```python
  {% extends 'articles/base.html' %}
  
  {% block content %}
  <h1>DETAIL</h1>
  <hr>
  <p>{{ article.pk }}</p>
  <p>작성자 : {{article.user}}</p>
  <p>{{ article.title }}</p>
  <p>{{ article.content }}</p>
  <p>{{ article.created_at|date:"SHORT_DATE_FORMAT" }}</p>
  <p>{{ article.updated_at|date:"M, j, Y" }}</p>
  {% if request.user == article.user %}
  <a href="{% url 'articles:update' article.pk %}" class="btn btn-primary">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST" style="display: inline;">
    {% csrf_token %}
    <input type="submit" value="DELETE" class="btn btn-primary">
  </form>
  {% endif %}
  <hr>
  <!-- 댓글 출력 -->
  {% for comment in comments %}
  <div>
    댓글 {{ forloop.revcounter }} : {{ comment.content }}
    {% if request.user == comment.user %}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" style="display: inline;">
      {% csrf_token %}
      <input type="submit" value="DELETE" class="btn btn-light">
    </form>
    <hr>
    {% else %}
    댓글 {{ forloop.revcounter }} : {{ comment.content }}
    <hr>
    {% endif %}
  </div>
  {% empty %}
  <p><b>댓글이 없습니다.</b></p>
  {% endfor %}
  <hr>
  <!-- 댓글 입력 -->
  {% if user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit" value="COMMENT" class="btn btn-primary">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요</a>
  {% endif %}
    <br>
    <a href="{% url 'articles:index' %}" class="btn btn-primary">BACK</a>
  {% endblock content %}
  ```

  2. ##### _article.html

  ```python
  <div class="card">
    <div class="card-header">
    작성자 : <a href="{% url 'accounts:profile' article.user %}"><b>{{ article.user }}</b></a>
    </div>
    <div class="card-body">
      <h5 class="card-title">제목 : {{ article.title }}</h5>
      <p class="card-text">{{ article.pk }} <b>번째 글</b></p>
      <p class="card-text">
        <a href="{% url 'articles:like' article.pk %}">
          {% if user in article.like_users.all %}
          <i class="fas fa-fire-alt" style="color: orange;"></i><br>
          {% else %}
          <i class="fas fa-fire-alt" style="color: gray;"></i><br>
          {% endif %}
        </a>
        <b>{{ article.like_users.all|length }}명</b>이 이 글을 좋아합니다.
      </p>
  
      <a href="{{ article.get_absolute_url }}" class="btn btn-primary">DETAIL</a>
    </div>
  </div>
  
  ```

  



# :rainbow: Follow

[AbstractUser](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L316)

- `AUTH_USER_MODEL = 'auth.User'` 기본값 (*settings.py*)
   **=>** `AUTH_USER_MODEL = 'accounts.User'`



###### accounts/models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # django 는 맞춤 모델을 참조하는 AUTH_USER_MODEL 설정 값을  제공함으로써
    # 기본 User 모델을 오버라이드 하도록 할 수 있다.
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
```



- `class User` 를 생성함으로써 새로 생긴 테이블을 볼 수 있다.
  ![image](https://user-images.githubusercontent.com/52684457/67351357-45633e00-f588-11e9-80e2-718bca3c5a76.png)

  

- 스키마를 확인 해보면,

```sqlite
sqlite> .schema accounts_user_followers
CREATE TABLE IF NOT EXISTS "accounts_user_followers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "from_user_id" integer NOUTOINCREMENT, "from_user_id" integer NOT NULL REFERENCES "accounts_user" ("id") DEFERRABL
T NULL REFERENCES "accounts_user" ("id") DEFERRABLE INITIALLY DEFERRED, "to_user_id" integer NOT NULL REFERENCES "accounts_user"ERRABLE INITIALLY DEFERRED);
 ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "accounts_user_followers_from_user_id_to_user_id_ad929616_uniq" ON "accounts_user_followers" ("from_user_id"CREATE INDEX "accounts_user_followers_from_user_id_1e8ec42b" ON "accounts_user_followers"
, "to_user_id");
CREATE INDEX "accounts_user_followers_from_user_id_1e8ec42b" ON "accounts_user_followers" ("from_user_id");
CREATE INDEX "accounts_user_followers_to_user_id_6dddd47f" ON "accounts_user_followers" ("to_user_id");
```

- `from_user_id` 와 `to_user_id` 이 생성된 것을 확인 할 수있다.



- 모든 DB파일과 migrations를 지웠기 때문에 다시 `createsuperuser` 로 관리자 계정 생성 후

  ###### accounts/admin.py

  ```python
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  # Register your models here.
  admin.site.register(User, UserAdmin)
  ```

  

![image](https://user-images.githubusercontent.com/52684457/67352117-0e8e2780-f58a-11e9-8b98-1b3955b26637.png)

- 새로운 항목이 생긴것을 확인 가능

- 하지만 페이지에서 회원가입을 하게되면 오류가 뜬다.

  ![image](https://user-images.githubusercontent.com/52684457/67352270-82c8cb00-f58a-11e9-8938-aadaa32a6a16.png)

- [맞춤  User 모델 대체하기](https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#substituting-a-custom-user-model)

- [Custom users and the built-in auth forms](https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms)
  [`UserCreationForm`](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)

  [`UserChangeForm`](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#django.contrib.auth.forms.UserChangeForm)

- 나머지 form들은 가리킬 곳을 잘 바라보고있지만 위에 두 코드는 auth user(기본유저만 바라보고 커스텀 유저를 바라보지 못 함)만 바라보고 있기 때문에 재설정 해주어야 한다.

  ###### accounts/forms.py

  ```python
  # Meta 정보가 auth.user를 바라보도록 상속받아 되어있었지만 
  # accounts.user를 바라보도록 수정하기위해서는 get_user_model()를 직접 추가해주면 된다.
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm):
          model = get_user_model() #accounts.User
          fields = UserCreationForm.Meta.fields + ('email',)
  ```

  

###### articles/views.py

```python
@login_required # 비회원 팔로우 x
def follow(request, article_pk, user_pk):
    # 게시글 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 접속 유저
    user = request.user

    if person != user: # 회원 자기자신에게 팔로워 하지 못하게
        # 내(user)가 게시글 유저(person) 팔로워 목록에 이미 존재 한다면,
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)

    # if user in person.follower.all():
```

- url **=>** `path('<int:article_pk>/follow/<int:user_pk>', views.follow, name='follow'),`

- ` def detail` 에

  ```python
  def detail(request, article_pk):
      ...
      person = get_object_or_404(get_user_model(), pk=article.user_id) 
      # user.pk도 가능하지만 가능한 최소화 하는게 좋다.
  	...
  	context = {..., ..., 'person': person,}
      return render(request, 'articles/detail.html', context)
  ```

  **추가**

![image](https://user-images.githubusercontent.com/52684457/67360088-f923f800-f59f-11e9-8b4e-a046493cc95c.png)

###### detail.html

```html
{% extends 'articles/base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<p>{{ article.pk }}</p>
<p>작성자 : {{article.user}}</p>
<p>{{ article.title }}</p>
<p>{{ article.content }}</p>
<p>{{ article.created_at|date:"SHORT_DATE_FORMAT" }}</p>
<p>{{ article.updated_at|date:"M, j, Y" }}</p>
{% if request.user == article.user %}
<a href="{% url 'articles:update' article.pk %}" class="btn btn-primary">UPDATE</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST" style="display: inline;">
  {% csrf_token %}
  <input type="submit" value="DELETE" class="btn btn-primary">
</form>
{% endif %}
<hr>

<!-- 댓글 출력 -->
{% for comment in comments %}
<div>
  댓글 {{ forloop.revcounter }} : {{ comment.content }}
  {% if request.user == comment.user %}
  <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" style="display: inline;">
    {% csrf_token %}
    <input type="submit" value="DELETE" class="btn btn-light">
  </form>
  <hr>
  {% else %}
  댓글 {{ forloop.revcounter }} : {{ comment.content }}
  <hr>
  {% endif %}
</div>
{% empty %}
<p><b>댓글이 없습니다.</b></p>
{% endfor %}
<hr>

<!-- 댓글 입력 -->
{% if user.is_authenticated %}
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% comment %} {{ comment_form }} {% endcomment %}
    {{ comment_form.content.label_tag }} &nbsp; {{ comment_form.content }}
    <input type="submit" value="COMMENT" class="btn btn-primary">
  </form>
{% else %}
  <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요</a>
{% endif %}
  <hr>
  {% include 'articles/_follow.html' %}
  <hr>
  <a href="{% url 'articles:index' %}" class="btn btn-primary">BACK</a>
{% endblock content %}
```

- detail 아래에 follow 카드를 추가할 것
  `{% include 'articles/_follow.html' %}`



###### _follow.html

```django
<div class="jumbotron text-center">
  <h1 class="display-4">{{ person.username }}</h1> <!-- article.user도 가능 -->
  <p class="lead">
    팔로잉 : {{ person.followings.all|length }} <br>
    팔로워 : {{ person.followers.all|length }}
  </p>
  <hr class="my-4">
  <!-- 본인은 follow 버튼을 볼 수 없다. 자기자신을 follow 불가능 -->
  {% if user != article.user %}
    <!-- 유저가 상대방 팔로워 목록에 없다면 -->
    {% if user in person.follower.all %}
    <a class="btn btn-primary btn-lg" href="{% url 'articles:follow' article.pk person.pk %}" role="button">Unfollow</a>
    {% else %}
    <a class="btn btn-primary btn-lg" href="{% url 'articles:follow' article.pk person.pk %}" role="button">Follow</a>
    {% endif %}
  {% endif %}
</div>
```

- `with` template

  ```python
  <div class="jumbotron text-center">
    <h1 class="display-4">{{ person.username }}</h1>
    {% with followigns=person.followings.all followers=person.followers.all %}
    <p class="lead">
      팔로잉 : {{ followings|length }} <br>
      팔로워 : {{ followers|length }}
    </p>
    <hr class="my-4">
    {% if user != article.user %}
      {% if user in followers %}
      <a class="btn btn-primary btn-lg" href="{% url 'articles:follow' article.pk person.pk %}" role="button">Unfollow</a>
      {% else %}
      <a class="btn btn-primary btn-lg" href="{% url 'articles:follow' article.pk person.pk %}" role="button">Follow</a>
      {% endif %}
    {% endif %}
    {% endwith %}
  </div>
  ```







#### 최종 views.py

###### accounts/views.py

```python
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from . forms import CustomUserChangeForm, CustomUserCreationForm
from articles.models import Article, Comment
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated: # 인증된 유저라면
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

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)
```

###### articles/views.py

```python
from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    visits_num = request.session.get('visits_num', 0)
    request.session['visits_num'] = visits_num + 1
    request.session.modified = True
    articles = Article.objects.all()
    context = {'articles': articles, 'visits_num': visits_num,}
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    comment_form = CommentForm() 
    context = {'article': article, 'comment_form': comment_form, 'comments': comments, 'person': person,}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) 
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        context = {'form': form, 'article': article,}
        return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk 
            comment.user_id = request.user.pk
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return redirect('articles:detail', article_pk)
        else:
            return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')


def follow(request, article_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)
```





