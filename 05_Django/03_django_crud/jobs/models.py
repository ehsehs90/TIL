from django.db import models

# Create your models here.
class Jobs(models.Model):
    name=models.CharField(max_length=40)
    past_job=models.TextField()


    def __str__(self):
        return f'[{self.pk}] {self.name}'
