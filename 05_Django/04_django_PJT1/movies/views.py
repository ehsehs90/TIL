from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {'movies':movies}
    return render(request, 'movies/index.html', context) 
