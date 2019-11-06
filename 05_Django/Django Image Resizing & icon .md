## Image Resizing

- python & Django 이미지 관련 라이브러리

  ```shell
  #설치 순서 주의! (의존성 있음)
  ```

  - `pillow`: PIL (Python Image Library) 프로젝트에서 fork 되어서 나온 라이브러리. Python3를 지원하지 않기 때문에 Pillow를 많이 씀

  - `pilkit`: Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리

    다양한 Processors 지원

    - Thumbnail
    - Resize
    - Crop ....

  - `django-imagekit`: 이미지 썸네일Helper

- INSTALLED_APPS 등록

```python
#settings.py
INSTALLED_APPS = [
    ....
    'imagekit',
    ....
]
```





`pillow`

`pilkit`

`django-imagekit`

```python
#models.py
from imagekit.models import ProcessedImageField
from imagekit.processprs import Thumbnail
```

```python
   image = ProcessedImageField(
        processors=[Thumbnail(200, 300)],   # 처리할 작업
        format='JPEG',                       # 이미지 포멧
        options={'quality':90},              # 각종 추가 옵션
        upload_to='articles/images/',        # 저장위치
        #실제 경로 -> MEDIA_ROOT/articles/images
    )


```

- 모델링
- Migration

```shell
$ python manage.py makemigration
$ python manage.py migrate
```





- 