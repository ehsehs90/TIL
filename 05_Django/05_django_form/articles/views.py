from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.

def index(request):
    articles = Article.objects.all()[::-1]
    context =  {'articles': articles,}
    return render(request, 'articles/index.html', context)
   

def create(request):
    if request.method =='POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다
        # 인스턴스에 데이터를 채워서 , 유효성 검증을 진행한다
        form = ArticleForm(request.POST)
        
        if form.is_valid(): #form이 유효성 검증을 마치면 dic 형태로 바뀐다
            article =form.save() 
            #모델 폼을 쓰면 로직이 간단해진다.
            # cleaned_data 를 통해 딕셔너리 안 데이터를 검증한다
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title = title, content=content)
            
        return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()

    #form 으로 전달받는 형태가 2가지
    #1. GET 요청 -> 비어있는 폼 전달
    #2. 유효성 검증 실패 -> 에러 메세지를 포함한 채로 폼 전달

    context={'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # 첫번째인자 class 두번째인자 pk
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {'article': article,
                'comment_form': comment_form,
                 }
    return render(request,'articles/detail.html',context)


def delete(request, article_pk):
    # article= Article.objects.get(pk=article_pk)
    article = Article.objects.get(pk=article_pk)
    if request.method =='POST':
        article.delete()    
        return redirect('/articles/index/')    
    else:

        return redirect('articles:detail',article.pk)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        #유효성검사
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail',article.pk)    
    else:
        form = ArticleForm(instance=article)
       
        # form = ArticleForm(initial={
        #     'title' : article.title,
        #     'content' : article.content
       
        # form 에 들어오는 두가지 형식
        # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
        # 2. POST -> is_valid 가 False가 리턴됐을 때, 오류메세지 포함해서 사용자에게 던져줌
    context ={'form': form,
            'article': article,
            }
    return render(request, 'articles/form.html',context)


def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method =='POST':
        pass
