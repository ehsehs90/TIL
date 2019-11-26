[Skip to content](https://github.com/Sunaaaa/TIL/blob/master/Django/django_11_21_pagination_search.md#start-of-content)

-  Watch [1](https://github.com/Sunaaaa/TIL/watchers)
-  Star[2](https://github.com/Sunaaaa/TIL/stargazers)
-  Fork[1](https://github.com/Sunaaaa/TIL/network/members)

# [Sunaaaa](https://github.com/Sunaaaa)/**[TIL](https://github.com/Sunaaaa/TIL)**

[ Code](https://github.com/Sunaaaa/TIL)[ Issues 22](https://github.com/Sunaaaa/TIL/issues)[ Pull requests 0](https://github.com/Sunaaaa/TIL/pulls)[ Actions](https://github.com/Sunaaaa/TIL/actions)[ Projects 0](https://github.com/Sunaaaa/TIL/projects)[ Wiki](https://github.com/Sunaaaa/TIL/wiki)[ Security](https://github.com/Sunaaaa/TIL/security/advisories)[ Insights](https://github.com/Sunaaaa/TIL/pulse)

*Branch:* master 

## [TIL](https://github.com/Sunaaaa/TIL)/[Django](https://github.com/Sunaaaa/TIL/tree/master/Django)/**django_11_21_pagination_search.md**

[Find file](https://github.com/Sunaaaa/TIL/find/master)Copy path

[![@Sunaaaa](assets/39547788.png)](https://github.com/Sunaaaa) [Sunaaaa](https://github.com/Sunaaaa) [Pagination 마크다운 이미지](https://github.com/Sunaaaa/TIL/commit/778d90d156a9e18ebaf83df5194c69db5be97bc1)[778d90d](https://github.com/Sunaaaa/TIL/commit/778d90d156a9e18ebaf83df5194c69db5be97bc1) 6 days ago

**1** contributor

582 lines (337 sloc) 14.3 KB

[Raw](https://github.com/Sunaaaa/TIL/raw/master/Django/django_11_21_pagination_search.md)[Blame](https://github.com/Sunaaaa/TIL/blame/master/Django/django_11_21_pagination_search.md)[History](https://github.com/Sunaaaa/TIL/commits/master/Django/django_11_21_pagination_search.md)

 

# Pagination & Search

## 1. Pagination

> index 페이지에 줄줄이 많은 게시글이 있는데, 이를 페이지로 분리하여 정리해보자!
>
> - 현재 index 페이지
>
>   [![1574297501466](assets/69303818-bcf8bb80-0c61-11ea-94e0-73add990cd72.png)](https://user-images.githubusercontent.com/39547788/69303818-bcf8bb80-0c61-11ea-94e0-73add990cd72.png)



### 1.1 View

> User가 요청한 페이지만 화면에 보이도록 view 함수를 수정해보자!



- views.py

  1. articles를 Paginator에 넣기

     `Paginator(전체 리스트, 보여줄 갯수)`

     ```
     paginator = Paginator(articles, 4)
     ```

  2. User가 요청한 page 가져오기

     User가 Query String `page`로 원하는 page를 입력한 값을 가져온다.

     ```
     page = request.GET.get('page')
     ```

  3. 해당하는 page의 article만 가져오기

     `dir(articles)` , `dir(articles.paginator)`

     ```
     articles = paginator.get_page(page)
     ```

  - index views 함수

    - 한 페이지에 4개의 게시글을 보이도록 설정한다.

      ```
      from django.core.paginator import Paginator
      
      def index(request):
      
          articles = Article.objects.all()
          paginator = Paginator(articles, 4)
          page = request.GET.get('page')
          articles = paginator.get_page(page)
      
          context = {
              'articles' : articles,
          }
          return render(request, 'articles/index.html', context)
      ```

- 실행 화면

  - index 페이지 초기화면

    - 총 7개 중 4개의 게시글만 보인다.

      [![1574300576691](assets/69303825-c1bd6f80-0c61-11ea-82c5-339e28e8778f.png)](https://user-images.githubusercontent.com/39547788/69303825-c1bd6f80-0c61-11ea-82c5-339e28e8778f.png)

  - URL을 통해 Query String `page=2`를 작성하여 두번째 페이지로 이동한다.

    [![1574300706171](assets/69303831-c41fc980-0c61-11ea-89ae-b6d37daa6f53.png)](https://user-images.githubusercontent.com/39547788/69303831-c41fc980-0c61-11ea-89ae-b6d37daa6f53.png)

  - URL을 통해 Query String `page=1`를 작성하여 다시 첫번째 페이지로 이동한다.

    [![1574300710589](assets/69303836-c97d1400-0c61-11ea-9d0c-0ef0ba51876f.png)](https://user-images.githubusercontent.com/39547788/69303836-c97d1400-0c61-11ea-9d0c-0ef0ba51876f.png)



### 1.2 Template

> URL에 page를 작성하여 보는것은 매우 이상하기 떄문에 페이지 버튼을 만들어보자!
>
> ```
> dir(articles)
> 
> dir(articles.paginator)
> 
> ```
>
> 부트스트랩 [참고](https://getbootstrap.com/docs/4.3/components/pagination/)



**상황에 맞게 페이지 버튼을 조작해보자**

**[ index.html ]**

- Pagination Component

  ```
  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
      <li class="page-item">
        <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
      </li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item">
        <a class="page-link" href="#">Next</a>
      </li>
    </ul>
  </nav>
  ```

  - 실행 화면

  [![1574300880663](assets/69303972-43ad9880-0c62-11ea-9885-f651e641d95a.png)](https://user-images.githubusercontent.com/39547788/69303972-43ad9880-0c62-11ea-9885-f651e641d95a.png)



- **첫 페이지에는 'Previous' 버튼이 없어야 한다.**

  ```
  {% if articles.has_previous %}
  <!-- 이전 버튼 -->
  <li class="page-item">
      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
  </li>
  {% endif %}
  ```

  - 실행 화면

    - URL에 `page=1`을 작성하여 'Previous' 버튼이 사라지는 것을 확인한다.

      [![1574300956422](assets/69303838-cb46d780-0c61-11ea-848f-0cbf7eb7340c.png)](https://user-images.githubusercontent.com/39547788/69303838-cb46d780-0c61-11ea-848f-0cbf7eb7340c.png)

- **마지막 페이지에는 'Next' 버튼이 없어야한다.**

  - `articles.has_next`

    ```
    <!-- 다음 버튼 -->
    {% if articles.has_next %}
    <li class="page-item">
        <a class="page-link" href="#">Next</a>
    </li>
    {% endif %}
    ```

  - 실행 화면

    - URL에 `page=2` 를 작성하여 'Next' 버튼이 사라지는 것을 확인한다.

      [![1574300989645](assets/69303842-cd109b00-0c61-11ea-9c57-58558825d01f.png)](https://user-images.githubusercontent.com/39547788/69303842-cd109b00-0c61-11ea-9c57-58558825d01f.png)

- **URL이 아닌 'Previous' 또는 'Next' 버튼을 통해서 페이지를 이동하자!**

  - `articles.previous_page_number`

  - `href=" {% url 'articles:index' %}?page={{articles.previous_page_number}}`

    ```
    {% if articles.has_previous %}
        <!-- 이전 버튼 -->
        <li class="page-item">
            <a class="page-link" href="{% url 'articles:index' %}?page={{articles.previous_page_number}}" tabindex="-1" aria-disabled="true">Previous</a>
        </li>
    {% endif %}
    
    <!-- 페이지 버튼 -->
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    
    <!-- 다음 버튼 -->
    {% if articles.has_next %}
        <li class="page-item">
            <a class="page-link" href=" {% url 'articles:index' %}?page={{articles.next_page_number}} ">Next</a>
        </li>
    {% endif %}
    ```

  - 실행 화면

    - index 페이지 초기화면

      - 'Previous' 버튼은 보이지 않는다.

        [![1574301377182](assets/69303853-d1d54f00-0c61-11ea-8199-6ed9dafd11b7.png)](https://user-images.githubusercontent.com/39547788/69303853-d1d54f00-0c61-11ea-8199-6ed9dafd11b7.png)

    - 'Next' 버튼을 누르면 두번째 페이지로 이동한다.

      [![1574301416906](assets/69303865-e74a7900-0c61-11ea-8b3c-7f0b8fbb746c.png)](https://user-images.githubusercontent.com/39547788/69303865-e74a7900-0c61-11ea-8b3c-7f0b8fbb746c.png)

    - 'Previous' 버튼을 누르면 다시 첫번째 페이지로 이동한다.

      [![1574301436461](assets/69303872-ea456980-0c61-11ea-9f1c-c425bd860619.png)](https://user-images.githubusercontent.com/39547788/69303872-ea456980-0c61-11ea-9f1c-c425bd860619.png)

- **원하는 페이지의 번호 버튼을 클릭하여 해당 페이지로 이동하자!**

  - 페이지의 범위

    ```
    <h1>{{articles.paginator.page_range}}</h1>
    ```

    [![1574301709081](assets/69303873-ec0f2d00-0c61-11ea-8e60-7043c70de730.png)](https://user-images.githubusercontent.com/39547788/69303873-ec0f2d00-0c61-11ea-8e60-7043c70de730.png)

  - 페이지 수만큼 페이지 번호 버튼이 생성한 뒤, 특정 페이지 번호 버튼을 클릭하면 해당 페이지로 이동한다.

    `href="{% url 'articles:index' %}?page={{num}}"`

    ```
    {% for num in articles.paginator.page_range %}
    <li class="page-item">
        <a class="page-link" href="{% url 'articles:index' %}?page={{num}}">{{num}}</a>
    </li>    
    {% endfor %}
    ```

  - 실행 화면

    - index 페이지 초기화면

      - 총 페이지의 수는 2개이므로, 1과 2 페이지 숫자 버튼이 'Previous' 와 'Next' 버튼 사이에 생성된다.

        [![1574302196645](assets/69303874-efa2b400-0c61-11ea-9812-3c01c6a5b174.png)](https://user-images.githubusercontent.com/39547788/69303874-efa2b400-0c61-11ea-9812-3c01c6a5b174.png)

    - 페이지 숫자 2 버튼을 누르면 두번째 페이지로 이동한다.

      [![1574302257981](assets/69303882-f5989500-0c61-11ea-8b17-52c55689b148.png)](https://user-images.githubusercontent.com/39547788/69303882-f5989500-0c61-11ea-8b17-52c55689b148.png)

    - 페이지 숫자 1 버튼을 누르면 다시 첫번째 페이지로 이동한다.

    [![1574302266578](assets/69303877-f3363b00-0c61-11ea-85fd-08cd563188c4.png)](https://user-images.githubusercontent.com/39547788/69303877-f3363b00-0c61-11ea-85fd-08cd563188c4.png)

- **현재 페이지에 맞게 페이지 버튼을 active 하자!**

  - index.html

    - DTL로 버튼의 `class` 속성을 작성한다.

      - `{% if num == articles.number %} active {% endif %}` : 현재 페이지 번호와 `num`이 같으면 해당 버튼을 activate한다.

        ```
        <!-- 페이지 버튼 -->
        {% for num in articles.paginator.page_range %}
        <li class="page-item {% if num == articles.number %} active {% endif %} ">
            <a class="page-link" href="{% url 'articles:index' %}?page={{num}}">{{num}}</a>
        </li>    
        {% endfor %}
        ```

  - 실행 화면

    - index 페이지 초기화

      [![1574325626580](assets/69321382-5cc84080-0c86-11ea-9f0a-4a58511a2937.png)](https://user-images.githubusercontent.com/39547788/69321382-5cc84080-0c86-11ea-9f0a-4a58511a2937.png)

    - 두번째 페이지

      [![1574325661038](assets/69321383-5e920400-0c86-11ea-83d0-854a90b35414.png)](https://user-images.githubusercontent.com/39547788/69321383-5e920400-0c86-11ea-83d0-854a90b35414.png)



## 2. Search

> 특정 검색어를 입력받아, 검색어를 포함하는 게시글을 보여주는 검색 기능을 구현해보자!
>
> - 부트스트랩 https://getbootstrap.com/docs/4.3/components/forms/ 의 Form grid 참고
> - 부트스트랩 https://getbootstrap.com/docs/4.3/components/list-group/ 의 With badges 참고



### 2.1 Template

> 검색 키워드를 입력받는 input 과 검색을 수행할 검색 버튼이 있는 form을 생성한다.
>
> - 부트스트랩 https://getbootstrap.com/docs/4.3/components/forms/ 의 Form grid 참고
>
> 검색 결과는 검색 키워드가 포함된 게시글과 해당 게시글의 댓글 갯수를 보여준다.
>
> - 부트스트랩 https://getbootstrap.com/docs/4.3/components/list-group/ 의 With badges 참고



**[ index.html ]**

```
<form class="mb-4" action="{% url 'articles:search' %}">
    <div class="row justify-content-center">
        <div class="col-12 col-sm-9  col-md-10 mb-3">
            <input type="text" name="query" class="form-control" placeholder="Search">
        </div>
        <div class="col-6 col-sm-3  col-md-2">
            <input type="submit" class="form-control btn btn-warning" value="검색">
        </div>
    </div>
</form>
```

- 반응형으로 브라우저의 크기에 따라 form의 모양을 적절하게 변하도록 설정한다.

  - 브라우저 최소화 된 크기

    [![1574302521473](assets/69303885-f92c1c00-0c61-11ea-993c-89ad14e119fe.png)](https://user-images.githubusercontent.com/39547788/69303885-f92c1c00-0c61-11ea-993c-89ad14e119fe.png)

  - 브라우저 중간 크기

    [![1574302531345](assets/69304066-99824080-0c62-11ea-863b-cbf43a09a3b1.png)](https://user-images.githubusercontent.com/39547788/69304066-99824080-0c62-11ea-863b-cbf43a09a3b1.png)

  - 브라우저 최대화 된 크기

    [![1574302543032](assets/69303892-ffba9380-0c61-11ea-82ff-0c8ce29ef1a5.png)](https://user-images.githubusercontent.com/39547788/69303892-ffba9380-0c61-11ea-82ff-0c8ce29ef1a5.png)



**[ search.html ]**

- `badges`가 달려있는 list-group

  - 검색 결과가 있는 경우

    - `{{ forloop.counter }} `: 반복 수 -> 검색 결과로 나오는 게시글의 번호를 부여한다.
    - `{{article.comment_set.all|length}}` : 해당 게시글의 댓글 갯수

  - 검색 결과가 없는 경우

    - 검색 결과가 없다는 text를 보인다.

      `{% empty %}검색 결과가 없습니다.`

      ```
      {% extends 'base.html' %}
      
      {% block body %}
      <h1> "{{query}}"로 검색한 결과</h1>
      <hr>
      <a href="#" class="list-group-item list-group-item-action">
          <ul class="list-group">
              {% for article in articles %}
              <a href="{% url 'articles:detail' article.pk %}" class="mb-3 list-group-item list-group-item-action">
                  <li class="list-group-item d-flex justify-content-between align-items-center">
                      [{{ forloop.counter }}] {{article.title}}
                      <span class="badge badge-warning badge-pill">
                          {{article.comment_set.all|length}}
                      </span>
                  </li>
              </a>
              {% empty %}
              <p>검색 결과가 없습니다.</p>
              {% endfor %}
          </ul>
          </div>
      
      {% endblock  %}
      ```



### 2.2 View

- views.py

  1. 사용자가 입력한 검색어 가져오기

     ```
     query = request.GET.get('query')
     ```

  2. DB에서 query가 포함된 제목을 갖는 article 가져오기

     - 결과가 0 (없다) 또는 1 이상 (여러 개) 이기 때문에 `filter` 사용

       - `__contains` : 지정한 문자열 포함하는 자료검색

       - `__icontains` : 지정한 문자열 포함하는 자료검색 (대소문자 구별 X)

         ( **`_`가 2개!!!!**)

  3. context로 검색 키워드 `query`와 `query`를 포함하는 게시글 리스트`articles`를 전달한다.

     ```
     return render(request, 'articles/search.html', context)
     ```

  - search views 함수

    ```
    def search(request):
        
        query = request.GET.get('query')
    
        articles = Article.objects.filter(title__icontains=query)
    
        # 3. context로 전달
        context = {
            'articles' : articles,
            'query' : query,
        }
        return render(request, 'articles/search.html', context)
    ```

### 2.3 Url

- urls.py

  ```
  from django.urls import path
  from . import views
  
  app_name="articles"
  urlpatterns = [
      .
      .
      path('search/', views.search, name="search"),
  ]
  ```



- 실행 화면

  - index 페이지 초기화면

    - 검색 키워드를 입력하는 input 창과 검색 버튼이 있다.

      [![1574309258691](assets/69303894-01845700-0c62-11ea-9088-4279dcc6d149.png)](https://user-images.githubusercontent.com/39547788/69303894-01845700-0c62-11ea-9088-4279dcc6d149.png)

    - 새로운 글을 추가하기

      - 제목 : "폴킴 안녕" 게시글 작성

        [![1574309575212](assets/69303898-03e6b100-0c62-11ea-9910-bb7cbc13aa3e.png)](https://user-images.githubusercontent.com/39547788/69303898-03e6b100-0c62-11ea-9910-bb7cbc13aa3e.png)

      - 게시글 생성 완료 (두번째 페이지)

        [![1574309584373](assets/69303903-06490b00-0c62-11ea-8c12-bd93afc2015d.png)](https://user-images.githubusercontent.com/39547788/69303903-06490b00-0c62-11ea-8c12-bd93afc2015d.png)

      - 제목 : "폴킴 Spell" 게시글 작성

        [![1574309597358](assets/69303906-0943fb80-0c62-11ea-99c1-c326a6336658.png)](https://user-images.githubusercontent.com/39547788/69303906-0943fb80-0c62-11ea-99c1-c326a6336658.png)

      - 게시글 생성 완료 (세번째 페이지)

        [![1574309606219](assets/69303912-0b0dbf00-0c62-11ea-8a05-15e9e83f4dc3.png)](https://user-images.githubusercontent.com/39547788/69303912-0b0dbf00-0c62-11ea-8a05-15e9e83f4dc3.png)

    - 제목이 "폴킴"인 게시글을 검색한다.

      [![1574309661435](assets/69303919-0fd27300-0c62-11ea-94e1-f5b39ef9bec6.png)](https://user-images.githubusercontent.com/39547788/69303919-0fd27300-0c62-11ea-94e1-f5b39ef9bec6.png)

  - search.html

    - 제목에 "폴킴"을 포함하는 게시글의 목록을 보인다.

      [![1574309816844](assets/69303921-1103a000-0c62-11ea-8e81-ed6f80b33b55.png)]