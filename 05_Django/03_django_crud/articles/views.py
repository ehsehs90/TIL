from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context =  {'articles': articles}
    return render(request, 'articles/index.html', context)

#사용자에게 작성 폼을 보여주는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.GET.get('title')
    content= request.GET.get('content')


    article = Article(title=title, content=content)
    article.save()
    
    return render(request,'articles/create.html')
