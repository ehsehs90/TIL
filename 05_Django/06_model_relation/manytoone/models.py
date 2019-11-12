from django.db import models

# Create your models here.
class User(models.Model):
    name= models.TextField()

    def __str__(self):
        return f'{self.name}'