from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# articles/views.py

def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles':articles}
    return render(request, 'articles/index.html',context)




def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('/articles/index')


#view.py : Variable Routing 적용
# 사용자로부터 요청한 url로부터 게시글 pk값을 건네받는다

def detail(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request,'articles/detail.html', context)


def delete(request,article_pk):
    article= Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('/articles/index')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)



def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)

    article.title=request.POST.get('title')
    article.content = request.POST.get('content')
    
    # 3. DB저장
    
    article.save()
    # 4. 저장 끝났으면 게시글 Detail로 이동시키기
    return redirect(f'/articles/{article.pk}/')