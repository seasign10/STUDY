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
    

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user: # 글이 본인 것이라면
            article.delete()
            return redirect('articles:index')
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


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if article.like_user.filter(pk=user.pk).exists():
        article.like_user.remove(user)
    else:
        article.like_user.add(user)
    return redirect('articles:index')
    

