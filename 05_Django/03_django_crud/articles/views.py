from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context =  {'articles': articles}
    return render(request, 'articles/index.html', context)

# #사용자에게 작성 폼을 보여주는 함수
# def new(request):
#     return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):

    #POST 요청일 경우 ->
    if request.method == 'POST':
        # 사용자 폼 건네받기
        title = request.POST.get('title')
        content= request.POST.get('content')
        image = request.FILES.get('image')
        print('ffff')
        # db에 인스턴스 채우기
        article = Article(title=title, content=content, image=image)
        # 저장
        article.save()        

    
    #return render(request,'articles/create.html')
     #   return redirect(f'/articles/{article.pk}/')
        return redirect(f'/articles/{article.pk}')
    
    #GET 요청일 경우 ->
    else :
        return render(request, 'articles/create.html')
    

# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {'article' : article ,
                'comments' : comments}
    return render(request,'articles/detail.html', context)


def delete(request, article_pk):
    article= Article.objects.get(pk=article_pk)
    article.delete()
    

    return redirect('/articles/index/')


# 사용자한테 게시글 수정 폼을 전달 cc
# 사용자가 게시글을 수정할 때 원래의 게시글 내용이 필요하다 - article_pk값필요

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)


## 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    #POST 요청 -> DB에 요청사항 반영
    if request.method == "POST":

        # 1. 수정할 게시글 인스턴스 가져오기
        #      
        # 2. 폼에서 전달받은 데이터 덮어쓰기
        article.title=request.POST.get('title')
        article.content = request.POST.get('content')    
        # 3. DB저장    
        article.save()
        # 4. 저장 끝났으면 게시글 Detail로 이동시키기
        return redirect(f'/articles/{article.pk}/')

    #GET 요청 -> 사용자에게 수정 Form 전달
    else :       
        context = {'article': article}
        return render(request, 'articles/update.html', context)



# 댓글 생성 뷰 함수
def comments_create(request, article_pk):
    #게시글 정보를 들고 옴
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
    #POST 로 들어오면 db에 저장
    #Comment 인스턴스 ㅋ하나 만든다 -> import 해서 불러와야 쓸 수 있음
        comment = Comment()
        #필요한건? article, content 
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
        #댓글 생성이 끝나면 게시글 상세글로 return 해준다
        return redirect('articles:detail',article_pk)
    #POST방식이 아닌 이상한 방식으로 보내면 그냥 redirect시킨다.
    else:
        return redirect('articles:detail',article_pk)


def comments_delete(request, article_pk, comment_pk):
    #article._pk comment_pk 둘다 필요할까? 둘 중 하나 필요할까?
    # 일단 comment_pk 가 있어야 db에서 삭제가 필요함
    # 그럼 article_pk 는 필요할까..? 네
    # 삭제 로직 끝난 후 detail.html 로  redirect 하려면 article_pk 필요하니까
   

    if request.method =='POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('articles:detail', article_pk)