1. **폴더** 생성 *(BASE_DIR)*

2. **git bash**

   - `python -m venv venv`

3. vscode 열어서 **환경변수** 적용

   - terminal `source venv/Script/activate`

4. `pip list`로 환경변수 확인

5. `pip install django` **django** 설치

6. `django-admin startproject articles .` **app 생성**

   - app 이름 : <u>articles</u>, <u>account</u> (*user app*)

7. **settings.py** 설정

   > ###### INSTALLED_APPS : app 등록
   >
   > `'articles.apps.ArticlesConfig',`
   >
   > `'accounts.apps.AccountsConfig',`

   > `LANGUAGE_CODE = 'ko-kr'`
   >
   > `TIME_ZONE = 'Asia/Seoul'`

8. **articles/models.py** 설정

   ```python
   from django.db import models
   from django.conf import settings
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
   
       class Meta:
           ordering = ('-pk',)
       
       def __str__(self):
           return self.title
           
   class Comment(models.Model):
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       content = models.CharField(max_length=30)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       class Mate:
           ordering = ('-pk',)
   
       def __str__(self):
           return self.content
   ```

   - **만약** 명세서에 오래된 순으로 나열을 하라는 조건이 붙어있으면 `Meta`값의 `ordering`을 `('pk')`로 명시하면 된다.
   - `user`, `like_user` 은 좋아요 기능을 넣기위해서 추가
   - comment 의 `article`은 글의 번호를 알아야 각 글내의 댓글이 구분이 가기 때문에

9. **articles/forms.py** 설정

   ```python
   from django import forms
   from .models import Article, Comment
   
   class ArticleForm(forms.ModelForm):
   
       class Meta:
           model = Article # 이 모델을 통해 form을 만듦
           fields = ('title', 'content',)
   
   class CommentForm(forms.ModelForm):
   
       class Meta:
           model = Comment
           fields = ('content',)
   ```

   - 꾸미는 기능을 넣지않고 그대로 사용하려면 굳이 title, content 등 재 입력 할 필요가 없다.

10. `python manage.py`  `makemigrations`, `migrate`

    - `createsuperuser` 도 생성

11. **articles/admin.py** 설정

    ```python
    from django.contrib import admin
    from .models import Article, Comment
    
    # Register your models here.
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    admin.site.registe(Article, ArticleAdmin)
    
    class CommentAdmin(admin.ModelAdmin):
        list_display = ('pk', 'content', 'created_at', 'updated_at',)
    admin.site.register(Comment, CommentAdmin)
    ```

12. **articles/views.py** (**CRUD**)

    ```python
    from django.shortcuts import render, redirect, get_object_or_404
    from django.contrib.auth import get_user_model
    from django.contrib.auth.decorators import login_required
    from django.views.decorators.http import require_POST
    from .models import Article, Comment
    from .forms import ArticleForm, CommentForm
    
    # Create your views here.
    def index(request):
        articles = Article.objects.all()
        context = {'articles': articles,}
        return render(request, 'articles/index.html', context)
    
    @login_required
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:index')
        else:
            form = ArticleForm()
        context = {'form': form,}
        return render(request, 'articles/form.html', context)
    
    
    def detail(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comment_set.all()
        person = get_object_or_404(get_user_model(), pk=article.user_id)
        comment_form = CommentForm() # comment 폼
        context = {'article': article, 'comments': comments, 'person': person, 'comment_form': comment_form,}
        return render(request, 'articles/detail.html', context)
        
    @login_required # is_authenticated 대신
    def delete(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user: # 글이 본인 것이라면
            article.delete()
        else:
            return redirect('articles:index')
        return redirect('articles:index')
    
    @login_required
    def update(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:index')
            else:
                form = ArticleForm(instance=article)
        else:
            return redirect('articles:index')
        context = {'form': form,}
        return render(request, 'articles/form.html', context)
    ```

13. **html**

    ```django
    <!-- base.html -->
    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
    </head>
    <body>
      {% block content %}
      {% endblock content %}
    </body>
    </html>
    
    
    
    
    <!-- index -->
    {% extends 'articles/base.html' %}
    
    {% block content %}
    <h1>INDEX</h1><hr>
    <a href="{% url 'articles:create' %}">NEW</a><hr>
    {% for article in articles %}
      <p>제목 : {{ article.title }}</p>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a><hr>
    {% endfor %}
    
    {% endblock content %}
    
    
    
    
    
    <!-- form.html -->
    {% extends 'articles/base.html' %}
    
    {% block content %}
    {% if request.resolver_match.url_name == 'create' %}
      <h1>CREATE</h1><hr>
    {% else %}
      <h1>UPDATE</h1><hr>
    {% endif %}
    
    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="submit">
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
    {% endblock content %}
    
    
    
    
    
    <!-- detail.html -->
    {% extends 'articles/base.html' %}
    
    {% block content %}
    <h1>DETAIL</h1><hr>
    <p>작성자 : {{ article.user }}</p>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <p>{{ article.created_at }}</p>
    <p>{{ article.updated_at }}</p>
    
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    
    <a href="{% url 'articles:index' %}">BACK</a>
    {% endblock content %}
    ```

    



회원가입, 로그인, 로그아웃, 좋아요, 댓글 생성 삭제, crud

