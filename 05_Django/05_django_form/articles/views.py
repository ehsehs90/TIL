import hashlib
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    else:
        gravatar_url = None

    articles = Article.objects.all()[::-1]
    context =  {'articles': articles,'gravatar_url':gravatar_url,}
    return render(request, 'articles/index.html', context)


#로그인 안한상태로 create 로직에 접근하면 접근 못하게 하기
@login_required
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
    # 하나의 Article 에 있는 comments 가져오기 
    comments = article.comment_set.all()
    context = {'article': article,
                'comment_form': comment_form,
                'comments': comments,
                 }
    return render(request,'articles/detail.html',context)

# @login_required
# 이렇게 쓰게 될 경우 get요청으로 가기 떄문에 405 에러 발생 ! 따라서 함수로직 안에 넣어준다
@require_POST
def delete(request, article_pk):    
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)    
        article.delete()    
    return redirect('/articles/index/')

@login_required
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


# def comments_create(request, article_pk):
#     article = get_object_or_404(Article, pk = article_pk)
#     if request.method =='POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # save 메서드 -> 선택인자 : (기본값) commit =True
#             # DB에 바로 저장되는것을 막아준다
#             comment = comment_form.save(commit=False)
#             # 여기까지 객체는 만들어졌지만 DB에는 반영이 안된 상태
#             # form에서 메다데이터를 article 까지 보이게하면 사용자가 게시글을 선택해 댓글을 담기는 이상한 상황이 발생한다
#             # 따라서 article 은 view함수 내에서 처리하도록 한다  (아래코드)
#             comment.article =article
#             comment.save()
#             return redirect('articles:detail', article.pk)
#     return redirect('articles:detail', article.pk)

@require_POST
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
                # save 메서드 -> 선택인자 : (기본값) commit =True
                # DB에 바로 저장되는것을 막아준다
            comment = comment_form.save(commit=False)
                # 여기까지 객체는 만들어졌지만 DB에는 반영이 안된 상태
                # form에서 메다데이터를 article 까지 보이게하면 사용자가 게시글을 선택해 댓글을 담기는 이상한 상황이 발생한다
                # 따라서 article 은 view함수 내에서 처리하도록 한다  (아래코드)
            comment.article =article
            comment.save()
        return redirect('articles:detail', article.pk)
    

# def comments_delete(request, article_pk, comment_pk):
#     article = get_object_or_404(Article, pk = article_pk)
#     if request.method =='POST':
#         comment = article.comment_set.get(pk=comment_pk)
#         comment.delete()
#         return redirect('articles:detail', article_pk)
#     else:
#         return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    #article._pk comment_pk 둘다 필요할까? 둘 중 하나 필요할까?
    # 일단 comment_pk 가 있어야 db에서 삭제가됨.
    # 그럼 article_pk 는 필요할까..? 네
    # 삭제 로직 끝난 후 detail.html 로  redirect 하려면 article_pk 필요하니까
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)   
        comment = article.comment_set.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
      