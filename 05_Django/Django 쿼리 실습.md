# 1. 

- 쿼리실습

- ```shell
  $ python manage.py shell_plus (django-extension)앱등록
  ```

- ```shell
  user1 = User.objects.create(name='Kim')
  user2 = User.objects.create(name='Lee')
  article1 = Article.objects.create(title='1글', user=user1)
  article2 = Article.objects.create(title='2글', user=user1)
  article3 = Article.objects.create(title='3글', user=user2)
  c1 = Comment.objects.create(content='1글1댓글', user=user1, article=article1)
  c2 = Comment.objects.create(content='1글2댓글', user=user2, article=article1)
  c3 = Comment.objects.create(content='1글3댓글', user=user1, article=article1)
  c4 = Comment.objects.create(content='1글4댓글', user=user2, article=article1)
  c5 = Comment.objects.create(content='2글1댓글', user=user1, article=article2)
  c6 = Comment.objects.create(content='!1글5댓글', user=user2, article=article1)
  c7 = Comment.objects.create(content='!2글2댓글', user=user2, article=article2)
  ```

  

  1. 1번사람이 작성한 게시글을 다 가져오면?

     ```shell
     $ user1.article_set.all()
     ```

     

  2. 1번 사람이 작성한 모든 게시글에 달린 댓글 가져오기

     ```shell
     In[2]: for article in user1.article_set.all()
     	   		for comment in article.comment_set.all()
     				print(comment.content)
     Out[2]: 1글1댓글
           1글2댓글
           1글3댓글
           1글4댓글
           !1글5댓글
           2글1댓글
           !2글2댓글      
     ```

     

  3.  2번 댓글을 작성한  User는?

     ```shell
           In [] : c2.user
           Out[] : <User: Lee>
           
           In [] : c2.user.pk
           Out[] : 2
     ```

     

  4. 2번 댓글을 작성한 User의 이름은?

     ```shell
     $ c2.user.name
     ```

     

  5.  2번 댓글을 작성한 사람의 모든 게시글은?

     ```python
     In[14]: c2.user.article_set.all()
     Out[14]: <QuerySet [<Article: 3글>]>
     ```

  6.  1번 글의 첫번째 댓글을 작성한 사람의 이름은?

     ```shell
     In []: article1.comment_set.all()[0].user.name
     Out[]: 'Kim'
     ```

     ```shell
     In[15]: article1.comment_set.first().user.name
     Out[15]: 'Kim'
     ```

     

# 2. Many to Many

