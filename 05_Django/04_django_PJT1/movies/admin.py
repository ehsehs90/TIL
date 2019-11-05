from django.contrib import admin

# Register your models here.

from .models import Movie, Comment


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title','title_en','audience','open_date','genre','watch_grade','score','poster_url','description')
admin.site.register(Movie, MovieAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at',)
admin.site.register(Comment, CommentAdmin)
