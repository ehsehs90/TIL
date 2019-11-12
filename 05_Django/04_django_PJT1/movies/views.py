from django.shortcuts import render,redirect
from .models import Movie, Comment

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {'movies':movies}
    return render(request, 'movies/index.html', context) 


#  'student/detail.html',

def new(request):
    return render(request, 'movies/new.html')



def create(reqeust):    
    title = reqeust.POST.get('title')
    title_en = reqeust.POST.get('title_en')
    audience = reqeust.POST.get('audience')
    open_date = reqeust.POST.get('open_date')
    genre = reqeust.POST.get('genre')
    watch_grade = reqeust.POST.get('watch_grade')
    score = reqeust.POST.get('score')
    poster_url = reqeust.POST.get('poster_url')
    description = reqeust.POST.get('description')
    movie = Movie(title=title,title_en=title_en,audience=audience,watch_grade=watch_grade,
    open_date=open_date, genre=genre,score=score,poster_url=poster_url,description=description)
    
    movie.save()


    return redirect('/movies/index/')
## 동적바인딩
def detail(request, movie_pk):
    # context={}
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    context = {'movie' : movie,
                'comments': comments}
    
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context ={'movie':movie}
    
    return render(request, 'movies/edit.html',context)

def update(reqeust, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)

    movie.title = reqeust.POST.get('title')
    movie.title_en = reqeust.POST.get('title_en')
    movie.audience = reqeust.POST.get('audience')
    movie.open_date = reqeust.POST.get('open_date')
    movie.genre = reqeust.POST.get('genre')
    movie.watch_grade = reqeust.POST.get('watch_grade')
    movie.score = reqeust.POST.get('score')
    movie.poster_url = reqeust.POST.get('poster_url')
    movie.description = reqeust.POST.get('description')
    # movie.movie = Movie(title=title,title_en=title_en,audience=audience,
    # open_date=open_date, genre=genre,score=score,poster_url=poster_url,description=description)
    
    movie.save()
    return redirect(f'/movies/{movie.pk}/')

def delete(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    

    return redirect('/movies/index/')


def comment_create(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    if request.method=="POST":
        comment = Comment()
        comment.content=request.POST.get('content')
        comment.title = movie
        comment.user= request.user
        comment.save()

        return redirect(f'/movies/{movie.pk}/',movie_pk)
    else:
        return redirect('/movies/detail/.html',movie_pk)


def comments_delete(request, movie_pk,comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method =="POST":
        comment=Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect(f'/movies/{movie.pk}/',movie_pk)
    else:
        return redirect('/movies/detail.html',movie_pk)
       