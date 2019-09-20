# :dog: Django : Relationship Fields

#### :key: Foreignkey

*문서 내에 코드작업 중, `article_id`가 Foreignkey*

##### 개념

- 외래 키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합), 참조하는 측의 변수는 참조되는 측의 테이블의 키를 가리킨다.
- 하나(또는 복수)의 다른 테이블의 기본 키 필드를 가리키는 데이터의 참조 무결성을 확인하기 위하여 사용된다.



##### 특징

- 외래 키의 값으로는 부모 테이블에 존재하는 키의 값만 넣을 수 있다.
- 외래 키를 사용하여 부모테이블의 유일한 값을 참조한다(부모 테이블의 기본 키, 참조 무결성)



`on_delete`

- ForeignKey의 필수 인자이며, 참조하고있는 부모 객체가 사라졌을 때 어떻게 처리할 것인지 정의,

1. `CASCADE` : **부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제**한다.
2. `PROTECT` : 참조가 되어있는 경우 오류가 발생
3. `SET_NULL` : 부모 객체가 삭제 됐을 때 참조하는 모든 값을  NULL로 치환, (db상에  NOT NULL 조건이 있다면 불가능)
4. `SET_DEFAULT` : 모든 값이 DEFAULT로 설정한 값으로 치환(db상에 DEFAUL 조건 값이 있어야 함)
5. `SET()` : 특정 함수 호출(직접 만든 함수나 내장함수)
6. `DO_NOTHING` : 아무것도 하지 않음. (단, DB상에 필드에 대한 ON DELETE 제한 조건을 따로 설정해야 한다.)



## :handshake: Relationship Fields

1. **ForeignKey** - 1:N 관계에서 성립
2. **ManyToManyField** - M:N 관계에서 성립
3. **OneToOneField** - 1:1 관계에서 성립 (보통 개인 페이지에서 사용하지만 잘 사용되는 편은 아니다.)



### :file_cabinet: Metadata

- `class Meta`와 같이 선언하여 모델에 대한 모델-레벨의 메타데이터를 선언 할  수 있다.

- 유용한 기능들 중 하나는 쿼리할 때 반환되는 기본 레코드 순서를 제어하는 것이다. (`ordering`)

  ```python
  class Meta:
      # 알파벳 순(A-Z) 으로 content를 정렬한 후
      # 작성일(created_at) 별로 가장 나중에 작성된 것 부터 정렬
      ordering = ['content', '-created_at']
  ```

- META : 데이터에 대한 데이터

  *(ex) 사진(하나의 데이터)에 저장되어있는 기본정보(데이터)들, 기종, 장소, 픽셀 ...등등*
  **=>** 공식 문서 : https://docs.djangoproject.com/en/2.2/ref/models/options/



**:warning:  이 외 코드 정리는 문서 아래에 존재하므로 참고바람**

- 아래의 이미지는 `models.py`에서 설정을 끝낸 후 `makemigration`한 상태

![image](https://user-images.githubusercontent.com/52684457/65200562-3ccba380-dac2-11e9-8877-a2271d1f9bdd.png)

- 새로운 migrations를 만들고나면 새로 추가된 Comment에 대한 설정을 확인 할 수 있다. `articles.Article`를 보면 연결된 부모 객체를 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/52684457/65200623-7ac8c780-dac2-11e9-9bdd-9aafb48ed78a.png)

- 직관성이 떨어지는 이름을 사용하면 어떤 부모를 참조하는지 어렵기 때문에, 참조하는 부모 객체의 소문자 단어를 사용하길 권장된다.



------

#### :repeat: 참조 방향성

1. ##### 1쪽에서 N을 참조(역참조)

   - `article.comment` 형태로는 가져올 수 없다. 게시글에 몇 개의 댓글이 있는지 django ORM 이 보장할 수 없기 때문. (본질적으로 Article 모델에 Comment 와의 관계에 대해 작성된 것이 존재하지 않는다.)

   - `article.comment_set` 로 접근할 수 있다.

2. ##### N쪽에서 1을 참조하는 경우

   - 댓글의 입장에서 `comment.article` 이 가능한 이유는 어떠한 댓글이든 반드시 자신이 참조하는 article이 있으므로 이와 같이 접근할 수 있다.



:arrow_forward: **1:N 에서 N쪽에서 1을 참조하는 것은 어렵지 않음**

```python
comment.article
comment.article_id
...
```



:small_red_triangle_down: **역참조(1쪽에서 N을 참조하는 경우)**

```python
article.comment # error
```

```shell
In [1]: dir(article)
Out[1]: 
['DoesNotExist',
 'MultipleObjectsReturned',
 '__class__',
 '__delattr__',
 '__dict__',
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
 'comment_set', # django에서 자동으로 생성해준 Method => 이 해당 메서드를 이용해주면 된다.
 'content',
 'created_at',
 'date_error_message',
 'delete',
 'from_db',
 'full_clean',
 'get_absolute_url',
 'get_deferred_fields',
 'get_next_by_created_at',
 'get_next_by_update_at',
 'get_previous_by_created_at',
 'get_previous_by_update_at',
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
 'update_at',
 'validate_unique']
```



![image](https://user-images.githubusercontent.com/52684457/65209807-1a428600-dad4-11e9-9246-487918ef2532.png)

*(shell의 숫자가 이어지지 않는 것은 오류부분을 잘라냈기 때문이다. 염두하여 참고바람)*

![image](https://user-images.githubusercontent.com/52684457/65207534-db5d0200-dacc-11e9-8085-fb054df213ed.png)



### :keyboard: 코드 중간 정리

:warning: 모든 코드가 아닌 지난 markdown에 이어 살을 덧붙이는 작업을 하는 중이므로, <u>수정된 파일만 기재되어</u> 있다. 그 이외의 코드는 이전 markdown을 참고바람

##### **model.py**

```python
from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # 객체를 반환하는 redirect와는 달리 revers는 articles/pk값/ => 문자열로 나타난다.
        # return reverse('articles:detail', args=[self.pk]) 
        # return reverse('articles:detail', kwargs={'key': self.pk})
        return reverse('articles:detail', kwargs={'article_pk': self.pk})

        # 주의 사항
        # reverse 함수에 args 와 kwargs를 동시에 인자로 보낼 수 없다.
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk'] # 가장 최신 댓글이 위로 올라오도록

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'
```

- `class Comment` 의  `article = models.ForeignKey(Article, on_delete=models.CASCADE)` 에서 ` related_name='comments'` 를 추가해주면 ` 'comment_set'` 대신 사용할 수 있으나, 1:1에서는 잘 쓰지 않는다. 보통 M:N에서 사용한다. 

  

##### **admin.py**

```python
from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'update_at',)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'update_at', 'article_id',)

admin.site.register(Comment, CommentAdmin)
```



##### **view.py**

```python
from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect # redirect 
from .models import Article, Comment # 현재 폴더(dir)의 models에 있는 Article, Comment 가져오기

# Create your views here.
def index(request):
    # embed()
    articles = Article.objects.order_by('-pk')
    # DB 가 변경, ORM이기 때문에 이 방법을 권유
    # articles = Article.objects.all[::-1] # python 이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect(article) # 메인 페이지
    #NEW
    else:
        return  render(request,'articles/create.html')

    
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk) 
    # 단일 값을 가져오려면 filter는 부적합, Article이가진 pk : detail함수에서 인자로 받는 pk
    comments = article.comment_set.all() # 특정 article 에 있는 comment를 가져와야 한다.
    context = {'article': article, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('/articles/') 
    else:
        return redirect(article)

    
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title') # 기존의 값을 바꾸는것
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)
        
        
def comment_create(request, article_pk):
    # 댓글을 달 게시글
    article = Article.objects.get(pk=article_pk) 
    # 추후에 댓글을 삭제하기위한 대비, 댓글과 댓글이 달린 게시글의 값 둘 다 필요하다
    if request.method == 'POST':
        # pass # pass를 먼저 코드를 작성 후에 GET방식을 받고, 나중에 수정해주는 것이 좋다.
        # form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content) 
        # content는 부모의 객체를 가지고 있기때문에 부모의 객체를 먼저 넣어주어야한다.
        # article=article에서 알아서 pk값이 들어간다.
        comment.save()
        return redirect(article)
        # return redirect('article:detail' artucke.pk)
        # return redirect('article:detail' artucke_pk)

    else:
        return redirect(article)

def comment_delete(request, article_pk, comment_pk):
    # comments = article.comment_set.all()
    # article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    # return redirect(article) # 어차피 같은곳으로 return하기 때문에
    # if문 밖에서 쓰면 불필요한 반복문을 줄일 수 있다.
    return redirect('articles:detail', article_pk)

```



##### **urls.py**

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    
    path('create/', views.create, name='create'), 
    # NEW(GET) + CREATE(POST)
    
    path('<int:article_pk>/', views.detail, name='detail'),
    
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    
    path('<int:article_pk>/update/', views.update, name='update'), 
    # EDIT(GET) + UPDATE(POST)
    
    path('<int:article_pk>/comment/', views.comment_create, name='comment_create'),
    # DETAIL(GET) + CREATE(POST)
    
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```



##### **detail.html**

```html
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">DETAIL</h1>
  <h2>{{ article.pk }} 번째 글</h2>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.update_at }}</p>
  <hr>
  <h4>댓글</h4><hr>

  <!-- 댓글 출력 -->
  <p><b>{{ comments|length }}개의 댓글</b></p>

  {% for comment in comments %}
  	<li>{{ comment.content }} | {{ comment.created_at }}
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}"style="display: inline;" method="POST">
        <!-- inline 속성을 부여함으로서 submit의 위치를 comment의 바로 옆으로 배치해준다.-->
        {% csrf_token %}
        <input type="submit" value="DELETE" onclick="return confirm('댓글이 삭제 됩니다.')">
      </form>
    </li>
  {% empty %}
    <p><b>작성된 댓글이 없습니다.</b></p>
    <hr>
  {% endfor %}

  <!-- 댓글 작성 form -->
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="content">CONTENT</label>
    <input type="text" name="content"> <!-- id는 label을 위한것이고 name으로 딕셔너리로 부르는 것 -->
    <input type="submit" value="SUBMIT">
  </form>
  
  <hr>
  
  <a href="{% url 'articles:update' article.pk %}">[EDIT]</a>
  
  <!-- a태그는 GET방식 밖에 지원하지 않음. -->
  <!-- <a href="{% url 'articles:delete'  article.pk %}" onclick="return confirm('게시글이 삭제 됩니다.')">[DELETE]</a> -->
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE" onclick="return confirm('게시글이 삭제 됩니다.')">
  </form>
  <a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock content %}
```

- `onclick="return confirm('내용')"` 값을 주게되면
  ![image](https://user-images.githubusercontent.com/52684457/65296636-05cbbf80-dba0-11e9-84d6-5d599ab0cb65.png)

  실행을 하기 전, 알림창으로 실행을 할 것인지 한번 더 물어 본다.

### :balloon: comment 관련 추가 사항

1. ##### 댓글 개수 출력

   ```django
     <p><b>{{ comments|length }}개의 댓글</b></p>
     <!-- comments로 넘어온 인스턴스가 없다면 아래의 상황을 쓰지만 좋은 코드는 아니다. 
     view에서 처리를 다 해준 후 넘어오는 것이 가장 바람직 하다. -->
     <p><b>{{ article.comment_set.all|length }}개의 댓글</b></p>
     <p><b>{{ comments.count }}개의 댓글</b></p>
   ```

   - 두 번째와, 세 번째는 쿼리를 날려보낸다. 가장 흔히 사용되는 방법은 첫 번째 방법이다.
   - 세 번째와 같은 경우는 count 메서드가 호출되면서 comment 모델 쿼리를 한번 더 db에 보내기 때문에 작은 차이지만 더 느리다. 첫 번째, 두 번째는 쿼리문을 한 번만 쓰게되는데 세 번째는 두 번을 쓰게된다.

2. ##### 댓글이 없는 경우 대체 문장 출력

   ```django
    {% empty %}
       <p><b>작성된 댓글이 없습니다.</b></p>
   ```

   - comment를 출력하는 for문안에 `{% endfor %}` 를 삽입해준다.







