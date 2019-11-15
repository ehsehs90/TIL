from django.contrib import admin
from .models import Movie, Rating


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title','description','poster','created_at','user')
admin.site.register(Movie, MovieAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk','score', 'content', 'created_at','user')
admin.site.register(Rating, RatingAdmin)