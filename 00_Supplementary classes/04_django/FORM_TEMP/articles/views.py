from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
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
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:login')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article_id = article_pk
                comment.save()
        return redirect('articles:detail', article_pk)
    else:
        redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = get_object_or_404(Comment, pk=comment_pk)
            comment.delete()
            return redirect('articles:detail', article_pk)
    else:
        redirect('accounts:login')
