# :dog: Django : Form

> project name : myform
>
> app name : articles



### :film_projector: progject : myform

###### settings.py

```python
# app 등록
INSTALLED_APPS = [
    'articles.apps.ArticlesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 한국어로 변환
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



###### urls.py

```python
from django.contrib import admin
# include를 추가 import
from django.urls import path, include

urlpatterns = [
    # app의 urls.py를 등록
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
```



### :film_strip: app : articles

###### models.py

```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})
```



###### admin.py

```python
from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)
```



****



###### views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all() # Meta Data로 ordering을 역순으로 했기 때문에 그대로 가져와도 최신순이 위로 쌓이게 된다.
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리 과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # form이 유효한지 체크한다.
        if form.is_valid(): # 유효성 검사
            # form.cleaned_data 로 정제된 데이터를 받는다.
            title = form.cleaned_data.get('title') # 유효성을 통과한 정제된 data
            content = form.cleaned_data .get('content')
            article = Article.objects.create(title=title, content=content)
        return redirect(article)

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # # return redirect('articles:index')
        # # models에서 absolute를 만드는 순간
        # return redirect(article) # 인스턴스 객체를 넣으면 detail.html로 간다.
    else:
        form = ArticleForm()
    # 상황에 따라 context 에 넘어가는 2가지 form
    # 1. GER : 기본 form 
    # 2. POST : 검증에 실패 후의 form (is_valid에서 튕겨져 나왔을 때 ==> isvaild == False)
    context = {'form': form,}
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)
```

`is_valid`

- Form 객체의 유효성 검사를 하는데 가장 중요한 역할
- Form 객체가 생성되면, 유효성 검사를 하고 유효한지 아닌지 여부를 boolean으로 반환



`cleaned_data`

- 유효성 검사 후 깔끔하고 정제된 dict 형태에서 데이터를 가져오는 방법
- `request.POST.get()` 은 이제 절대 추천하지 않는다. 
  - 보안상의 문제가 크기 때문



> ###### 유효성 검사 (IPython)
>
> - `pip install IPython` 후 `from IPython import embed`
>
> ![image](https://user-images.githubusercontent.com/52684457/65564994-a7308800-df89-11e9-9794-4fc5f8f8ee86.png)
>
> - 직접 유효성 검증을 했을때 `vaild`의 값이 **True**로 변하는 것을 확인 할 수 있다.
>
> ```python
> Out[6]:
> ['__class__',
>  '__delattr__',
>  '__dict__',
>  '__dir__',
>  '__doc__',
>  '__eq__',
>  '__format__',
>  '__ge__',
>  '__getattribute__',
>  '__getitem__',
>  '__gt__',
>  '__hash__',
>  '__html__',
>  '__init__',
>  '__init_subclass__',
>  '__iter__',
>  '__le__',
>  '__lt__',
>  '__module__',
>  '__ne__',
>  '__new__',
>  '__reduce__',
>  '__reduce_ex__',
>  '__repr__',
>  '__setattr__',
>  '__sizeof__',
>  '__str__',
>  '__subclasshook__',
>  '__weakref__',
>  '_bound_fields_cache',
>  '_clean_fields',
>  '_clean_form',
>  '_errors',
>  '_html_output',
>  '_post_clean',
>  'add_error',
>  'add_initial_prefix',
>  'add_prefix',
>  'as_p',
>  'as_table',
>  'as_ul',
>  'auto_id',
>  'base_fields',
>  'changed_data',
>  'clean',
>  'cleaned_data', # 이용 할 코드
>  'data',
>  'declared_fields',
>  'default_renderer',
>  'empty_permitted',
>  'error_class',
>  'errors',
>  'field_order',
>  'fields',
>  'files',
>  'full_clean',
>  'get_initial_for_field',
>  'has_changed',
>  'has_error',
>  'hidden_fields',
>  'initial',
>  'is_bound',
>  'is_multipart',
>  'is_valid',
>  'label_suffix',
>  'media',
>  'non_field_errors',
>  'order_fields',
>  'prefix',
>  'renderer',
>  'use_required_attribute',
>  'visible_fields']
> ```
>
> ![image](https://user-images.githubusercontent.com/52684457/65565001-abf53c00-df89-11e9-8b5f-34d67f691253.png)



> ###### 404 Error
>
> 서버 에러 응답 **=>** https://developer.mozilla.org/ko/docs/Web/HTTP/Status
>
> ```python
> def detail(request, article_pk):
>     try:
>         article = Article.objects.get(pk=article_pk)
>     except Article.DoesNotExist:
>         raise Http404('No Article matches the given query.')
>     context = {'article': article,}
>     return render(request, 'articles/detail.html', context)
> ```
>
> ![image](https://user-images.githubusercontent.com/52684457/65564808-0510a000-df89-11e9-82dc-15fff4248038.png)
>
> - 이 구문을 한줄로 처리할 수 있는 방법은 아래와 같다.
>
>   ```python
>   from django.shortcuts import render, get_object_or_404
>   
>   def detail(request, article_pk):
>       article = get_object_or_404(Article, pk=article_pk)
>       context = {'article': article,}
>       return render(request, 'articles/detail.html', context)
>   ```
>
>   ![image](https://user-images.githubusercontent.com/52684457/65564792-faeea180-df88-11e9-926f-5a09fcfbb52a.png)
>
>   `get_object_or_404`
>
>   - 해당 객체가 있다면 `objects.get()`을 실행하고, 없으면 **ObjectDoesNotExist** 예외가 아닌 **Http404(HttpResponseNotFound)** 를 raise 한다.
>
>   ###### :question: 왜 404 erre가 나올 상황에 django는 500 error를 발생시켰을까?
>
>   - `.get()` 메서드는 조건에 맞는 데이터가 없는 경우에 에러를 나타내게 설계되어 있다. **코드 단계에서 발생한 에러에 대해서는 브라우저는 500 Internal Server Error**로 인식
>   - 클라이언트 입장에서 `서버에 오류가 발생하여 요청을 수행할 수 없다(500)` 라는 원인이 명확하지 않은 에러를 마주하기 때문에 올바른 에러를 예외처리하고 발생시키는 것 또한 개발에서 중요한 요소중 하나이다.
>
> ###### get_list_or_404
>
> ```python
> from django.shortcuts import render, get_list_or_404
> 
> def detail(request, article_pk):
>     article = get_list_or_404(Article) 
>     context = {'article': article,}
>     return render(request, 'articles/detail.html', context)
> ```
>
> ![image](https://user-images.githubusercontent.com/52684457/65565100-e3fc7f00-df89-11e9-8936-be28bed71729.png)
>
> - 빈 값을 보여준다. 메인 페이지에는 적합하지 않다.



###### :page_facing_up: Forms ad HTML

- `as_p()` : 각 필드가 단락(paragraph)으로 렌더링
- `as_ul()` : 각 필드가 목록 항목(list item)으로 렌더링
- `as_table()` : 각 필드가 테이블 행으로 렌더링

**=>** 문제점 : 일일히 꾸며주기가 어렵다.

- form에 대한 공식 문서 : https://docs.djangoproject.com/en/2.2/topics/forms/

- Looping over the form’s fields

  ```django
  1.
  {{ form.title.label_tag }}
  {{ form.title }}
  {{ form.content.label_tag }}
  {{ form.content }}
  
  2.
  {% for field in form %}
    {{ field.label_tag }}
    {{ field }}
  {% endfor %}
  ```



`widget`

- django form을 사용하면 기본적으로 field에 맞는 default widget을 사용한다.
- 그런데 다른 widget을 사용하고 싶다면 widget 인자를 통해 field를 새로 정의할 수 있다.
- template에서 작성하는 것이 아니라 `form.py`에서 작성, 즉 html 에서 작성하는 것을 여기서 작성하는 것
- bootstrap 적용시 class를 사용해야 하는데 이럴 때 widget을 사용



```python
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # embed()
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        form = ArticleForm(initial=article.__dict__)

    # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기화된 form
    context = {'form': form,}
    return render(request, 'articles/create.html', context)
```

- 위의 `def update` 에서 `embed()`를 사용하여 구조를 까보자

  update 버튼을 누르게 되면 무한 로딩에 걸리면서 IPython이 실행된다.

  ![image](https://user-images.githubusercontent.com/52684457/65571514-f2ee2c00-df9f-11e9-8375-725ae9b937fd.png)

  ```python
  Out[2]:
  ['DoesNotExist',
   'MultipleObjectsReturned',
   '__class__',
   '__delattr__',
   '__dict__', # 이용 할 코드
   '__dir__',
   '__doc__',
   '__eq__',
   '__format__',
   '__ge__',
   '__getattribute__',
   '__getstate__',
   '__gt__',
   '__hash__',
   '__init__',
   '__init_subclass__',
   '__le__',
   '__lt__',
   '__module__',
   '__ne__',
   '__new__',
   '__reduce__',
   '__reduce_ex__',
   '__repr__',
   '__setattr__',
   '__setstate__',
   '__sizeof__',
   '__str__',
   '__subclasshook__',
   '__weakref__',
   '_check_column_name_clashes',
   '_check_constraints',
   '_check_field_name_clashes',
   '_check_fields',
   '_check_id_field',
   '_check_index_together',
   '_check_indexes',
   '_check_local_fields',
   '_check_long_column_names',
   '_check_m2m_through_same_relationship',
   '_check_managers',
   '_check_model',
   '_check_model_name_db_lookup_clashes',
   '_check_ordering',
   '_check_property_name_related_field_accessor_clashes',
   '_check_single_primary_key',
   '_check_swappable',
   '_check_unique_together',
   '_do_insert',
   '_do_update',
   '_get_FIELD_display',
   '_get_next_or_previous_by_FIELD',
   '_get_next_or_previous_in_order',
   '_get_pk_val',
   '_get_unique_checks',
   '_meta',
   '_perform_date_checks',
   '_perform_unique_checks',
   '_save_parents',
   '_save_table',
   '_set_pk_val',
   '_state',
   'check',
   'clean',
   'clean_fields',
   'content',
   'created_at',
   'date_error_message',
   'delete',
   'from_db',
   'full_clean',
   'get_absolute_url',
   'get_deferred_fields',
   'get_next_by_created_at',
   'get_next_by_updated_at',
   'get_previous_by_created_at',
   'get_previous_by_updated_at',
   'id',
   'objects',
   'pk',
   'prepare_database_save',
   'refresh_from_db',
   'save',
   'save_base',
   'serializable_value',
   'title',
   'unique_error_message',
   'updated_at',
   'validate_unique']
  ```

  ![image](https://user-images.githubusercontent.com/52684457/65571573-1e711680-dfa0-11e9-866a-955347e3b4fd.png)

  - article에 대해 dict 형태로 출력되는 모습을 확인할 수 있다.



`initial`

- form 나타날 때 해당 필드의 초기 값
- HTML input 태그의 `value` 속성을 사용했던 것과 동일
- 초기 값을 설정하는 인수는 <u>딕셔너리 자료형</u>이어야 한다.



****



###### urls.py

```python
from django.urls import path
from . import views # 같은 위치 내의 views를 import

app_name = 'articles' # url name 지정
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
]
```



###### forms.py

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    # max_length를 지정하지 않으면 텍스트 필드로 사용이가능하다.
    # model과는 달리 form에는 text field가 없다.
    content = forms.CharField()
```

- 세부 값을 설정할 수 있다.

  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=10, 
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title',
                  'placeholder': 'Enter the title',
              }
          )
      )
      # max_length를 지정하지 않으면 텍스트 필드로 사용이가능하다.
      # model과는 달리 form에는 text field가 없다.
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content',
                  'placeholder': 'Enter the content',
                  'rows': 5,
                  'cols': 50,
              }
          )
      )
  
  ```

  ![image](https://user-images.githubusercontent.com/52684457/65565497-0216af00-df8b-11e9-99ed-2215c2080d3b.png)

- title이 제목으로, content가 내용으로 설정된 것, 그 외 class설정 등을 확인 할 수 있다.



##### :open_file_folder: app폴더 안에 templates\articles 폴더를 생성

> ### :file_folder: templates\articles
>
> ###### base.html
>
> ```python
> <!DOCTYPE html>
> <html lang="ko">
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <meta http-equiv="X-UA-Compatible" content="ie=edge">
>   <title>Document</title>
> </head>
> <body>
>   {% block content %}
>   {% endblock content %}
> </body>
> </html>
> ```
>
> 
>
> ###### index.html
>
> ```python
> {% extends 'articles/base.html' %}
> 
> {% block content %}
>   <h1>Articles</h1>
>   <a href="{% url 'articles:create' %}">[NEW]</a>
>   {% for article in articles %}
>     <p>{{ article.pk }}</p>
>     <p>{{ article.title }}</p>
>     <a href="{{ article.get_absolute_url }}">[DETAIL]</a>
>   {% endfor %}
> {% endblock content %}
> ```
>
> 
>
> ###### create.html
>
> ```python
> {% extends 'articles/base.html' %}
> 
> {% block content %}
>   <h1>CREATE</h1>
>   <form action="" method="POST"> <!-- 현재 주소로 submit이 보내질것이기 때문에 빈값으로 지정해도 된다. -->
>     {% csrf_token %}
>     {{ form.as_p }} <!-- form.as_p 대신 form만 쓰게 되면 옆으로 붙어서 페이지에 표시 된다. -->
>     <!-- input과 label태그를 사용하지 않아도 자동으로 적용이 된다. -->
>     <input type="submit" value="CREATE">
>   </form>
> {% endblock content %}
> ```
>
> 
>
> ###### detail.html
>
> ```python
> {% extends 'articles/base.html' %}
> 
> {% block content %}
>   <h1>DETAIL</h1>
>   <hr>
>   <p>{{ article.pk }}</p>
>   <p>{{ article.title }}</p>
>   <p>{{ article.content }}</p>
>   <p>{{ article.created_at|date:"SHORT_DATE_FORMAT" }}</p>
>   <p>{{ article.updated_at|date:"M, j, Y" }}</p>
>   <a href="{% url 'articles:index' %}">[BACK]</a>
> {% endblock content %}
> ```
>
> - date 공식 문서 **=>** https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#date
>
>   추가 문서 **=>** https://www.php.net/manual/en/function.date.php









# :dog: Django : ModelForm

- 일반  form과 다르게 Model로 부터 Form을 자동으로 생성하는 기능

- form class 안에 Meta 클래스를 정의하고, Meta 클래스 안에 Model 속성에 해당하는 모델 클래스를 지정한다. 즉, 어떤 모델을 기반으로 form을 작성할 것인지를 지정하는 것이다.
- 일반 Form에 비해 모델 정의를 다시 하지 않아서 쉽고 간결하게 작성 가능하다.



- 기존에 작성한  form과 아래 새로 작성한 form은 같은 기능을 한다.

  ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article # 이 모델을 통해 form을 만들면 되겠다는 명령
          # fields = ('title', 'content',)
          fields = '__all__'
          # exclude = ('title',) # title을 제외한 모든 필드를 사용
  ```

  - 여기서 `content`는 `textarea` 형태로 바뀐 것을 확인할 수 있는데

  ![image](https://user-images.githubusercontent.com/52684457/65571467-c9350500-df9f-11e9-9a8e-b0aaa206c6fa.png)

  - 이는 `models.py`를 그대로 가져왔기 때문이다.
  - `TextField()`의 기본값은 `textarea`를 가지고 있다.



###### forms.py

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article # 이 모델을 통해 form을 만들면 되겠다는 명령
        # fields = ('title', 'content',)
        fields = '__all__'
        # exclude = ('title',) # title을 제외한 모든 필드를 사용

        
        # Meta 클래스에서 값을 지정해줘도 가능은 하지만 되도록이면 이 클래스는 필수적인 요소만 들어가서 짧은것이 권장이 된다. 밑의 코드를 위로 빼주면 위와 같은 코드가 완성이 된다.
        # wigets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }
```

- Form class를 반드시 forms.py에 작성할 필요는 없다.
  - 하지만 공식문서는 이 방식을 권유하고 있다.
    (되도록 해당 app폴더 안에 `forms.py`에 작성하는 것이 바람직)



###### views.py

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/create.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)
```

- 길었던 코드가 많이 생략된 것을 확인 할 수 있다.
  *(create.html **=>** form.html 로 rename)*
- django가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의하게 된다.
- 어떤 모델의 레코드를 만들어야 할지 이미 알고 있으므로 유효성 검사 후 바로 저장(`save()`)가 가능하다.

![image](https://user-images.githubusercontent.com/52684457/65573008-c557b180-dfa4-11e9-89b2-5721a1dc4209.png)

```python
Out[2]:
['COOKIES',
 'FILES',
 'GET',
 'META',
 'POST',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_current_scheme_host',
 '_encoding',
 '_get_full_path',
 '_get_post',
 '_get_raw_host',
 '_get_scheme',
 '_initialize_handlers',
 '_load_post_and_files',
 '_mark_post_parse_error',
 '_messages',
 '_read_started',
 '_set_post',
 '_stream',
 '_upload_handlers',
 'body',
 'build_absolute_uri',
 'close',
 'content_params',
 'content_type',
 'csrf_processing_done',
 'encoding',
 'environ',
 'get_full_path',
 'get_full_path_info',
 'get_host',
 'get_port',
 'get_raw_uri',
 'get_signed_cookie',
 'headers',
 'is_ajax',
 'is_secure',
 'method',
 'parse_file_upload',
 'path',
 'path_info',
 'read',
 'readline',
 'readlines',
 'resolver_match', # 이용 할 코드
 'scheme',
 'session',
 'upload_handlers',
 'user',
 'xreadlines']
```

![image](https://user-images.githubusercontent.com/52684457/65573069-de606280-dfa4-11e9-8370-4fc2808faa4c.png)

- `resolver_match` : url에 대한 정보를 수집할 수 있다. django가 알아들을 수 있도록 url사이에 낀 번역기 정도로 생각하면 된다. 

- `url_name`, `app_name`, `namespace` 등을 확인 할 수 있다.

- 여기서 `url_name`을 이용해보자

  ```python
  In [4]: request.resolver_match.url_name
  Out[4]: 'create'
  ```

  



#### :question: CREATE ? UPDATE ?

- <u>정확한 분기 표현</u>을 해주기 위해서 위에서 추출한 값(`resolver_match.url_name`)과 if문을 사용할 것

###### form.html (before - create.html)

```django
{% extends 'articles/base.html' %}

{% block content %}

  {% if request.resolver_match.url_name == 'create' %}
    <h1>CREATE</h1>
  {% else %}
    <h1>UPDATE</h1>
  {% endif %}
  
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="CREATE">
  </form>
  <hr>

  {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'articles:index' %}">[BACK]</a>
  {% else %}
    <a href="{{ article.get_absolute_url }}">[BACK]</a>
  {% endif %}
{% endblock content %}
```

- 하지만 `article.get_absolute_url` 에서 에러가 난다.
  **=>** `views.pt`를 확인하면 context에서 가져올 `article`이 없기 때문이다.

  ![image](https://user-images.githubusercontent.com/52684457/65576491-081d8780-dfad-11e9-9383-2e75e889ffa5.png)

  - 빈 값이 뜨는 것을 확인 가능

    

  ```python
  context = {'form': form, 'article': article,}
  ```

  - 이미 함수안에 article이 있어서 가져오기만 하면된다.  `'article': article,` 를 가져오자.



#### :heavy_exclamation_mark: 해결! 하지만?

- bootstrap을 사용하기에 막막한 상황이 발생하게 되는데 이를 도와주는 라이브러리가 있다.
  https://django-bootstrap4.readthedocs.io/en/latest/

  1. ***Installation***

  ```bash
  $ pip install django-bootstrap4
  ```

  ###### settings.py

  - 라이브러리 추가하기

  ```python
  INSTALLED_APPS = [
      'articles.apps.ArticlesConfig',
      'bootstrap4', # 추가 (외부 라이브러리)
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  2. ***Quickstart > Example template***
     https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html

  ```django
  {# Load the tag library #}
  {% load bootstrap4 %}
  
  {# Load CSS and JavaScript #}
  {% bootstrap_css %}
  {% bootstrap_javascript jquery='full' %}
  
  {# Display django.contrib.messages as Bootstrap alerts #}
  {% bootstrap_messages %}
  
  {# Display a form #}
  <form action="/url/to/submit/" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
      <button type="submit" class="btn btn-primary">
        Submit
      </button>
    {% endbuttons %}
  </form>
  
  {# Read the documentation for more information #}
  ```

  - 문서를 참고하여 작성하자

###### base.html

```django
{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}
    {% bootstrap_javascript jquery='full' %}
  </div>
</body>
</html>
```



###### form.html

```django
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block content %}

  {% if request.resolver_match.url_name == 'create' %}
    <h1>CREATE</h1>
  {% else %}
    <h1>UPDATE</h1>
  {% endif %}
  
  <form action="" method="POST"> <!-- 현재 주소로 submit이 보내질것이기 때문에 빈값을 해도 된다. -->
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
      <button type="submit" class="btn btn-primary">CREATE</button>
    {% endbuttons %}
  </form>
  <hr>

  {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'articles:index' %}">[BACK]</a>
  {% else %}
    <a href="{{ article.get_absolute_url }}">[BACK]</a>
  {% endif %}
{% endblock content %}
```

- `{% load bootstrap4 %}`이 `base.html`에서만 적용이 되고 `form.html` 까지 가져오지 못하기 때문에 `form.html` 에서도 따로 load를 해주자.
  **:warning: extends 아래에 작성해야한다. (무조건 extends는 가장 위)**





###### :purple_heart: bootstrap 적용

form.html

```django
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block content %}

  {% if request.resolver_match.url_name == 'create' %}
    <h1>CREATE</h1>
  {% else %}
    <h1>UPDATE</h1>
  {% endif %}
  
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form layout='horizontal' %}
    {% buttons submit='OK' reset='Cancel' %}{% endbuttons %}
  </form>
  <hr>

  {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'articles:index' %}">[BACK]</a>
  {% else %}
    <a href="{{ article.get_absolute_url }}">[BACK]</a>
  {% endif %}
{% endblock content %}
```

- 이 외 https://django-bootstrap4.readthedocs.io/en/latest/templatetags.html 에서 여러가지를 참고할 수 있다.





#### :right_anger_bubble: create comment

공식 문서 **=>** https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#the-save-method

save() method 문서에서 해결책을 찾을 수 있다.

- save()에서 바로 저장을 해버리기 때문에 수정할 틈이 없다.

  ![image](https://user-images.githubusercontent.com/52684457/65584838-7c135c00-dfbc-11e9-9f69-076593ed2bee.png)















