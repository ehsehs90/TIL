- Static files 기본 경로
  - 기본적으로 애플리케이션 안에 있는 `static`디렉토리를 탐색해서 정적파일을 가져온다
- {% load static %}
  - 해당 페이지에 정적 파일들을 불러와서 사용하겠다고 선언
  - 일반적으로는 HTML 문서 상단에 위치. 상속받는 {% extends %} 태그가 존재하면 , 얘 밑에 위치한다
- {% static %}
  - 해당하는 경로에 있는 파일에 대해, 장고가 접근할 수 있는 절대 URL 경로를 생성한다.
  - 실제 파일이 위치한 경로는 아님 
  - 127.0.0.1:8000**/static/**articles/images/sample.png

## Static files 경로 커스터마이징

```python
#settings.py
```









## 미디어

- config - `urls,py`

```python
from django.conf import settings

from django.conf.urls.static import static



\# static()

\# 첫번째 인자 :  어떤 URL 을 정적으로 추가할 지 (MEDIA file)

\# 두번째 인자 :  실제 해당 미디어 파일은 어디에 있는지?

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

