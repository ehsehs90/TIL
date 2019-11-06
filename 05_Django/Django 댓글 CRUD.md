## 댓글 CRUD



### 댓글 만들기(C)

- `views.py` `urls.py` `detail.html`

- `views.py` : 이 게시글을 참조하고 있는 모든 comment 가져오기

  - ```python
    article.comment_set.all()
    ```

  - ```python
    from .models import Article, Comment
    
    # 댓글 생성 뷰 함수
    def comments_create(request, article_pk):
        #게시글 정보를 들고 옴
        article = Article.objects.get(pk=article_pk)
        if request.method == 'POST':
        #POST 로 들어오면 db에 저장
        #Comment 인스턴스 ㅋ하나 만든다 -> import 해서 불러와야 쓸 수 있음
            comment = Comment()
            #필요한건? article, content 
            comment.content = request.POST.get('content')
            comment.article = article
            comment.save()
            #댓글 생성이 끝나면 게시글 상세글로 return 해준다
            return redirect('articles:detail',article_pk)
        #POST방식이 아닌 이상한 방식으로 보내면 그냥 redirect시킨다.
        else:
            return redirect('articles:detail',article_pk)
    ```

- `urls.py`

  - ```python
     path('<int:article_pk>/comments/', views.comments_create, name='comments_create')
    ```

- `detail.html`

  - ```html
    <hr>
    {% comment %} 댓글 장석 Form {% endcomment %}
    <!-- 우리가 가야할 곳 : articles:comments_create -->
    <form action ="{% url  'articles:comments_create' article.pk %}"  method="POST" >
      {% csrf_token %}
    <input type="text"  col="20" name="content" >
    <input type = "submit" value="댓글등록">
    </form>
    
    ```

    



### 댓글 보여주기(R)

- `detail.html`에 **for문**으로 띄워 보낸다

  - 이때 comments를 사용하기 위해서는 detail 함수 context에 comments를 같이 담아 보내야 한다

- ```javascript
  {% for comment in comments %}
  <p>
      [((comment.pk))] {{comment.content}}
  </p>
  {% endfor %}
  ```





### 댓글 지우기(D)

- `detail.html`
- `views.py`

```python
def comments_delete(request, article_pk, comment_pk):
    #article._pk comment_pk 둘다 필요할까? 둘 중 하나 필요할까?
    # 일단 comment_pk 가 있어야 db에서 삭제가 필요함
    # 그럼 article_pk 는 필요할까..? 네
    # 삭제 로직 끝난 후 detail.html 로  redirect 하려면 article_pk 필요하니까
   

    if request.method =='POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('articles:detail', article_pk)
```

- `urls.py`

```python
path('<int:article_pk>/<int:comment_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    
```

