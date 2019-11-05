from django.db import models

# Create your models here.
class Movie (models.Model):
    title =models.CharField(max_length=60)
    title_en = models.CharField(max_length=60)
    audience = models.IntegerField()
    open_date = models.CharField(max_length=8 ,null=True)
    genre =models.CharField(max_length=60)
    watch_grade = models.CharField(max_length=60)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'


class Comment (models.Model):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering=['-pk',]

    def __str(self):
        return self.content
