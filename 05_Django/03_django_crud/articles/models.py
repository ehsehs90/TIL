from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    # blank=True : 공백 가능 #원래대도라면 새로운 필드를 추가하고 나면 makemigrations 할때, 어떤 값을 넣을건지 Django가 물어본다.
    #기본적으로 blank=False 이기 때문이다
    # blank =true -> '빈 문자열이 들어가도 된다'
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'



class Comment(models.Model):
    # related_name: 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set형식으로 불러온다
    # related_name 이라는 값을 설정해서 _set명령어를 임의로 변경할 수 있다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str(self):
        return self.content