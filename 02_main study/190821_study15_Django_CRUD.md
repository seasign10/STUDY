# :dog: CRUD



> **C**REATE
>
> **R**EAD
>
> **U**PDATE
>
> **D**ELETE



## :paw_prints: CREATE

##### :mushroom: view?

1. 글을 쓰는페이지 view (new) - 입력 받는 페이지
2. 작성된 글을 받아서 db에 저장하는 역할을 하는 view (create)



- 이용할 html 작성

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">Articles</h1>
<hr>
{% endblock %}
```

```django
<!-- new.html -->
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">NEW</h1>
  <form action="/articles/create/" method="GET">
    <label for="title">TITLE</label>
    <input type="text" name="title" id="title"><br>
    <label for="content">CONTENT</label>
    <textarea name="content" id="content" cols="30" rows="5"></textarea><br>
    <input type="submit" value="submit!">
  </form>
{% endblock  %}
```

```django
<!-- create.html -->
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">성공적으로 글이 작성되었습니다.</h1>
{% endblock %}
```



- urls.py에 html 함수를 등록

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # ''아무것도 입력하지 않았기 때문에 articles/만으로도 접속이 가능하다.
    path('new/', views.new),
    path('create/', views.create),
]
```



- models.py에서 db 테이블에 가져올 구성값 설정

```python
# articles/models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



> #### :mushroom: __str\_\_ 쓰는 이유?
>
> ```python
> def __str__(self):
>  return self.title
> ```
>
> - 위의 함수를 사용하는 이유는 값을 가져올때 관리자 페이지든 직접 만들어서 사용하는 html에서든 그대로 값을 출력하면  `<Article: Article object (1)>` 페이지에서 이런식으로 내용이 그대로 출력이된다. 
> - models.py 에서 가장 먼저 읽히는 인덴트 값을 가져오게 되는데, 여기서의 models.py는 title이 먼저 사용되어 있다. 그래서 self.title로 값을 가져오는 것 
> - 이 함수를 적용시켜주어야 우리가 흔히 보는 편안한 값으로 페이지를 볼 수 있다.
>
> 
>
> - 현재는 str함수를 주석처리를 해놔도 제대로 켜지는것을 볼 수 있는데, admin.py에 밑의 코드를 적용시켜줘서 제대로 보이는 것이다. 
>
>   ```python
>   class ArticleAdmin(admin.ModelAdmin):
>       list_display = ('pk', 'title', 'content', 'created_at', 'update_at')
>   
>   admin.site.register(Article, ArticleAdmin)
>   ```





```python
# articles/views.py

from IPython import embed
from django.shortcuts import render
from .models import Article # 현재 폴더(dir)의 models에 있는 Article 가져오기

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # embed() 구간에서 멈춘 후 request를 까볼 것.
    # embed() # 일시정지
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 1 번째 방법
    # article = Article()
    # article.title = title # create 함수 안의 title과는 다름
    # article.content = content
    # article.save()

    # 2 번째 방법
    article = Article(title=title, content=content)
    article.save()

    # 3 번째 방법
    # Article.objects.create(title=title, content=content)
    # # return값이 바로 나오기 때문에 save기능이 따로 없다. 변수를 담을 수 없음.

    return render(request, 'articles/create.html')
```

![](https://user-images.githubusercontent.com/52684457/63478473-e4a28100-c4c4-11e9-9204-92e74c06a9fd.png)

- create가 받는 값 request를 알아보기 위해 ipython의 embed 사용



- python manage.py createsuperuser` 으로 관리자(admin) 등록

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'update_at')

admin.site.register(Article, ArticleAdmin)
```

```python
def get_all_fields(self):
    return tuple(field.name for field in self._meta.get_fields())
# get_fields() 필드를 전부 가져오는 함수

class ArticleAdmin(admin.ModelAdmin):
    list_display = get_all_fields(Article)
    # field가 너무 많을 경우 이런방법을 사용하면 간단하게 가져올 수 있다.
```



## READ

![](https://user-images.githubusercontent.com/52684457/63480398-b4f77700-c4cc-11e9-9939-03dbc19cdf15.png)

- GET 으로 값을 받았기 때문, POST로 바꿔주자.

```python
# articles/views.py

from IPython import embed
from django.shortcuts import render, redirect # redirect 
from .models import Article # 현재 폴더(dir)의 models에 있는 Article 가져오기

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')# DB 가 변경, ORM이기 때문에 이 방법을 권유
    # articles = Article.objects.all[::-1] # python 이 변경
    # 여기서 Article에 빨간 줄이 표시 될 수도 있는데 신경쓰지 않아도 된다.
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title') # POST 방식으로 값을 받는다
    content = request.POST.get('content') # 이것 또 한 위와 동일

    article = Article(title=title, content=content)
    article.save()

    return redirect('/articles/') # 메인 페이지
```

- 사실상 create는 필요없는 사이트기 때문에 index로 가는 작업을 해준다.

- `'articles/index.html'`

```text
 하지만 index로 돌아갔지만 글이 보이지 않는다. 그 이유는 페이지 자체를 index가 맞지만 url은 아직 create에 머물러있다. 왜냐하면 페이지는 전환이 됐지만, url은 돌아가지 못했기 때문이다
```



##### index.html로 돌아가기 위해서는 render을 return하는 것이 아닌 redirect를 사용해야 한다.



```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">Articles</h1>
<!-- a태그를 넣어줌으로써 new.html을 new/입력을 일일히 치지않아도 링크를 타고 편리한게 html 사이트 이동을 할 수 있게 되었다. -->
<a href="/articles/new">[NEW]</a>
<hr>
{% for article in articles %} 
<!-- for문을 돌리지 않으면 아래의 내용이 하나만 출력이 된다. list형식의 all()은 for문을 돌려줄 수 있다. -->
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title}}</p>
  <p>글 내용: {{ article.content }}</p>
  <hr>
{% endfor %}
{% endblock %}
```

```django
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">NEW</h1>
  <form action="/articles/create/" method="POST"> <!-- GET대신 POST -->
    {% csrf_token %} <!-- 인증된 사이트라는 것을 인증하기위해 csrf token 추가 -->
    <label for="title">TITLE</label>
    <input type="text" name="title" id="title"><br>
    <label for="content">CONTENT</label>
    <textarea name="content" id="content" cols="30" rows="5"></textarea><br>
    <input type="submit" value="submit!">
  </form>
{% endblock  %}
```



### :mushroom: GET => POST

> ###### 글을 작성할 때 GET이 아닌 POST를 쓰는 3가지 이유
>
> 1. 사용자는 django에게 **HTML파일을 줘!(GET)**가 아니라, **~한 레코드(글)을 생성해줘!(POST)** 이기 때문에 GET 보다는 POST 요청이 더 알맞다.
> 2. 데이터는 URL에 노출되면 안된다. (우리가 URL(주소창)에 접근하는 방식은 모두 GET)
>    query의 형태를 통해 DB schema를 유추할 수 있게 되고 이는 보안의 측면에서 매우 취약하게 된다.
> 3. 모델(DB)를 조작하는 친구는 GET이 아닌 POST 요청
>    - DB를 수정하는 것은 매우 중요한 일이고 그에 따른 **최소한의 신원확인이 필요**
>    - GET으로 동작하게 된다면 악성사용자가 URL만으로 글을 작성, 수정, 삭제 할 수 있게된다.
>
> ####  :mushroom: Redirect
>
> - POST 요청은 HTML 문서를 render하는게 아니라, `~좀 처리해줘 (요청)` 의 의미이기 때문에 요청을 처리하고 나서 이 결과를 보기위한 페이지로 넘겨줘야 한다.
>
> ###### POST 요청으로 변경 후 변화하는 것
>
> - form을 통해 전송한 데이터를 받을때도 `request.POST` 로 받아야 한다.
> - 글이 작성되면 실제로 URL에 데이터가 나타나지 않게 된다.
> - html 문서를 요청하는게 아니기 때문에 html 문서를 받아볼 수 있는 다른 페이지로 redirect 하게 된다.



###### DETAIL

- 상세페이지 작성

```python
# articles/views.py
# variable routing
from django.shortcuts import render, redirect # redirect 
from .models import Article

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect(f'/articles/{ article.pk }/')
    # fstr을 이용해서 detail.html로 이동하는 처리방식
    # return redirect('/articles', article.pk) # 위아래 동일

def detial(request, pk):
    article = Article.objects.get(pk=pk) # 단일 값을 가져오려면 filter는 부적합, Article이가진 pk : detail함수에서 인자로 받는 pk
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)
```

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detial)
]
```



```django
<!-- detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">DETAIL</h1>
  <h2>{{ article.pk }} 번째 글</h2>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="/articles/">[BACK]</a> <!-- 다시 되돌아가는 버튼, index.html -->
{% endblock content %}
```

```django
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">Articles</h1>
<a href="/articles/new">[NEW]</a>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title}}</p>
  <p>글 내용: {{ article.content }}</p>
  <!-- 일일히 번호를 URL에 적용하기 번거로우니 DETAIL버튼을 만든다. -->
  <a href="/articles/{{ article.pk }}">[DETAIL]</a>
  <hr>
{% endfor %}
{% endblock %}
```



> ##### :mushroom: 유효성 검사를 하지않으면 빈값도 그대로 받기 때문에, 제목과 내용을 빈값으로 넘겨도 글이 작성이 된다.
>
> - try문을 통해 빈값(혹은 다른 오류)을 막을 수 있다.
>
> ```python
> # articles/views.py
> 
> from django.core.exceptions import ValidationError
> 
> def create(request):
>     try:
>         title = request.POST.get('title')
>         content = request.POST.get('content')
>         article = Article(title=title, content=content)
>         article.full_clean() # 전체적으로 검증 (유효성 검증)
>     except ValidationError:
>         raise ValidationError('Error')
>     else: # full_clean에서 검증하고 아무런 문제가 없을때 넘어온다.
>         article.save()
>     return redirect(f'/articles/{ article.pk }/') # 메인 페이지
> ```
>
> ![](https://user-images.githubusercontent.com/52684457/63482214-102c6800-c4d3-11e9-8ef4-a467ef159193.png)
>
> - 굳이 오류 설정을 자세히 하지 않아도 django에서 오류 메세지를 띄워준다.
>
> ```python
> # articles/models.py
> 
> from django.db import models
> 
> # Create your models here.
> class Article(models.Model):
>     title = models.CharField(max_length=20)
>     # 기본값을 조절해서 오류를 조절할 수 있다.
>     # 위와같이 max_length=20같은 값들은 유효성 검사를 해야만 검증되는 것이지
>     # 설정 되어있다고해서 무조건 오류가 나지 않는다.(유효성 검사에서 확인되는 부분)
>     content = models.TextField()
>     created_at = models.DateTimeField(auto_now_add=True)
>     updated_at = models.DateTimeField(auto_now=True)
> 
>     def __str__(self):
>         return self.title
> ```
>
> - models.py에서 기본 값을 정해주면 오류 범위를 정해줄 수 있다.
> - **full_clean()**
>    - https://docs.djangoproject.com/en/2.2/ref/models/instances/#validating-objects





## :paw_prints: UPDATE

###### DELETE > UPDATE 순으로 작업을 한 후 작성한 것이니 유의바람.

- DELETE 목차 먼저 보길 권장



```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    # 밑의 세 줄(title, content, save)은 create 함수에서 그대로 가져와서 수정한 것
    article.title = request.POST.get('title')
    # 기존의 값을 바꾸는것이기 때문에, title이아닌 article.title로 해주어야 한다.
    # 현재 값을 불러서 바꾸는 형식 (그렇지 않으면 새로운 값을 받아서 새 글이 작성된다.)
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}')
```

- ORM 에서 article.~~을 불러와서 수정하면 그 해당 불러온 값이 수정이 되었다.



```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detial),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]
```

```django
<!-- edit.html -->

{% extends 'base.html' %}
<!-- 수정이나 작성이나 구조자체는 똑같음, new.html 복사함. -->

{% block content %}
  <h1 class="text-center">NEW</h1>
  <form action="/articles/{{ article.pk }}/update/" method="POST">
    {% csrf_token %} 
    <label for="title">TITLE</label>
      
     <!-- value값을 주어 이전에 작성되었던 글을 불러온다. 그렇지않으면 빈 입력값만 온다. -->
    <input type="text" name="title" id="title" value="{{article.title}}"><br>
    <label for="content">CONTENT</label>
      
    <!-- textarea는 위와 같은 기능이 없기 때문에 태그안에 입력해준다. -->
    <textarea name="content" id="content" cols="30" rows="5">{{ article.content }}</textarea><br>
    <input type="submit" value="submit!">
  </form>
  <!-- 수정 도중에 나갈수 있는 버튼 -->
  <a href="/articles/{{ article.pk }}/">[BACK]</a>
{% endblock  %}
```

```django
<!-- detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">DETAIL</h1>
  <h2>{{ article.pk }} 번째 글</h2>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="/articles/{{ article.pk }}/edit">[EDIT]</a> <!-- 수정 버튼 -->
  <a href="/articles/{{ article.pk }}/delete">[DELETE]</a> <!-- 삭제 버튼 -->
  <a href="/articles/">[BACK]</a> <!-- 다시 되돌아가는 버튼 -->
{% endblock content %}
```









## :paw_prints: DELETE

##### :mushroom: view?

1. 수정하는 페이지 view (edit)
2. 직접 모델에 수정 요청을 보내는 view (update)



- GET방식으로 지우는 기능을 만들면 URL에서 적정값만 입력해도 삭제가 된다

  - 그렇기 때문에 POST로 값을 받아야 한다.

    


- POST방식으로 값을 받아 처리하는 것이 복잡하기 때문에
  편의상아래의 방법은 GET방식으로 코드를 짠 것.

```python
# articles/views.py
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/') # DB를 건드렸기 때문에 render는 적합하지 않음
    # 또한 지우는 작업이기 때문에 다른 별개의 창(html)이 필요하지 않음
```

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detial),
    path('<int:pk>/delete/', views.delete),
]
```

```django
<!-- detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">DETAIL</h1>
  <h2>{{ article.pk }} 번째 글</h2>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <!-- 삭제 버튼을 추가 했다. -->  
  <a href="/articles/{{ article.pk }}/delete">[DELETE]</a> 
  <a href="/articles/">[BACK]</a> <!-- 다시 되돌아가는 버튼 -->
{% endblock content %}
```

