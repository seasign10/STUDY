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