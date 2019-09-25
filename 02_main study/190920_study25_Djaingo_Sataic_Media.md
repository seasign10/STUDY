# :tv: STATIC / MEDIA

**기본 파일의 경로** : app_name/templates/app_name/index.html

**satatic 파일의 경로** : app_name/static/app_name/sample.png

- name space(static안의 app_name)를 읽지 못하고 static까지만 읽을 수 있다.



![image](https://user-images.githubusercontent.com/52684457/65290151-fc832880-db88-11e9-878e-8475f0426162.png)

- 폴더 생성위치와 이름을 잘 확인하고 넣어주어야 한다.
  - app의 static폴더는 migrations 폴더과 같은 선상에 있어야 한다.
  - project의 assets폴더는 templates와 같은 선상에 있어야 한다,  
    **===>** 이유는 아래의 `settings.py` 코드 를 확인해보자.
    - 즉 둘다 해당 폴더의 최상위에 있어야 한다.



![image](https://user-images.githubusercontent.com/52684457/65290766-803e1480-db8b-11e9-8063-617644b558ff.png)

- static 파일 적용의 예, static 이후의 경로를 적용시켜주면 된다.



##### settings.py

```python
# 실제 파일이나 디렉토리가 아니고, URL 로만 존재하는 단위
STATIC_URL = '/static/'

# 개발 단계에서 사용하는 실제 정적 파일이 위치한 경로를 지정하는 설정
# bootstrap, 외부 템플릿 등을 저장하기 위해 경로를 만듦
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'crud', 'assets'),
]
```

- 외부 경로에 의한 static 파일의 적용은 경로를 직접 만들어 주어야 한다. 가장 마지막에 추가해주자.



## :framed_picture: image upload

#### :grey_question: NULL

- **기본 값 : False**
- DB와 관련되어 있다. (Databased-related)
- 주어진 컬럼이 NULL 값을 가질 것인지를 결정
- Not null **=>** null = False
  null은 null이라는 문자열이 아닌, null이라는 data type이다.



#### :grey_question: blank

- **기본 값 : False**
- 데이터 유효성과 관련되어 있다. (Validation-related)
- `full_clean()/is_valid()` 처럼 유효성 검사 메서드가 호출될 때 유효성 검사에 사용



`null=True, blank=False`

- DB 내에서는 해당 필드가 NULL을 사용하지만, 웹 사이트 에서는 HTML INPUT 태그에 `required` 속성이 필요하다라는 것을 의미한다.



```django
   <label for="title">TITLE</label>
   <input type="text" name="title" id="title" required><br>
```

- input에 required 값을 주게 되면

  ![image](https://user-images.githubusercontent.com/52684457/65290622-f68e4700-db8a-11e9-9dcc-d7526d04bb13.png)

  빈 값이 넘어 갈 때, 알림 문구가 뜨면서 글이 생성되지 않는다.



****

##### :warning: 주의사항

- 문자열 기반 필드(CharField, TextField...)에서는 `null=True` 금지
- 이렇게 정의하게 되면 문자열 기반 필드는 데이터 없음에 대한 값이 2가지가 된다. None과 빈 문자열을 갖게 된다.
- 데이터 없음에 대한 조건이 2가지면 중복이기 때문에 문자열 기반 필드는 NULL이 아닌 빈문자열을 사용하는게 django의 컨벤션이다.

```python
class Person(models.Model):
    name = models.TextField(blank=True) # null=True 는 금지
    birth = models.DateField(null=True, blank=True)
    # 문자열 기반 필드가 아닌 숫자 필드이기 때문에 가능
```

****

##### models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    
    # image ==> 이미 만들어진 테이블에 추가되었기 때문에 테이블 순서상 가장 마지막에 붙는다.
    # class Article에서 가운데 작성한 이유는
    # 아래의 create_at과 update_at는 models.py에서 보기에 마지막에 붙는게 보기 좋기 때문
    image = models.ImageField(blank=True) # 빈값이 허용이 되는 컬럼이 되어 사진오류가 나지 않음
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})
```

- `admin.py `에서도 image 추가해주는 것을 잊지말자.



![image](https://user-images.githubusercontent.com/52684457/65290963-5cc79980-db8c-11e9-8f2d-6c8d2271e163.png)

**Pillow**

- image 필드를 사용할 때 필수로 필요한 패키지

![image](https://user-images.githubusercontent.com/52684457/65290878-f6db1200-db8b-11e9-9ae9-398654dad1e8.png)

- DB파일을 보면 image가 생긴 것을 확인 할 수 있다.



```django
    <label for="image">IMAGE</label>
    <input type="file" name="image" id="image"><br>
```

- 이미지를 추가하는 태그(`type="file"`)를 넣으면



![image](https://user-images.githubusercontent.com/52684457/65291610-250e2100-db8f-11e9-8f12-25cbebe68537.png)

- 모든파일로 설정 되어있는 것을 확인 할 수 있는데,

```django
<input type="file" name="image" id="image" accept="image/*">
<!-- image/* 이미지에 관련된것, * 모두, 파일 검증까지는 되지않기 때문에 다른 형식도 올릴 수 있다. -->
```

- `accept="image/*"`  를 설정 해주면

![image](https://user-images.githubusercontent.com/52684457/65291591-1293e780-db8f-11e9-8000-387ea15acfb1.png)

- 이미지 파일로 지정 되어있는 것을 확인 할 수 있다.



![image](https://user-images.githubusercontent.com/52684457/65291811-eb89e580-db8f-11e9-8c65-14d12d4f0bcb.png)

- 이미지를 업로드 하면 이미지 파일의 이름이 같이 생성된 것을 확인 할 수 있다.



하지만,

![image](https://user-images.githubusercontent.com/52684457/65296835-c356b280-dba0-11e9-9752-5cba1774b7b0.png)

- 업로드 된 파일의 특정 저장소가 없기 때문에 최상단에 저장되어있는 것을 확인 할 수 있다.

- 경로를 설정해주자!

  ##### settings.py

  ```python
  # STATIC_URL과 비슷한 역할을 한다.
  # 업로드 된 파일(stored files)의 IRL 주소를 만들어주는 역할
  # STATIC_URL과 값이 달라야 한다.
  # MEDIA URL이 없었기 때문에 http://127.0.0.1:8000/articles/4/Vacation.jpg 와 같은 이상한 곳에 사진이 존재하게 됨
  MEDIA_URL = '/media/'
  
  # STATICFILES_DIRS 와 비슷한 역할을 한다.
  # 실제 파일이 업로드 되면 어디에 저장될지 정하는 실제 경로
  # STATICFILES_DIRS 와 값이 달라야 한다.
  # 개발 단계에서 사용하는 경로이므로, 실제 배포 단계에서는 다른 경로를 설정을 해야 한다.
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

  - 이미지가 들어간 게시글을 작성을 하게 되면

  ![image](https://user-images.githubusercontent.com/52684457/65299554-f1d98b00-dbaa-11e9-8699-f22a7151f574.png)

  

- 





![image](https://user-images.githubusercontent.com/52684457/65292283-b8e0ec80-db91-11e9-91c0-f85c54fa4b01.png)

- 하지만 이미지가 뜨지 않는 상황이 발생하는데, 이는 `form` 에 `enctype="multipart/form-data"` 을 추가해주면 된다.

![image](https://user-images.githubusercontent.com/52684457/65292329-ef1e6c00-db91-11e9-8ba2-6ed22151522b.png)

- 해결된 모습

  **enctype** 문서 **=>** https://developer.mozilla.org/ko/docs/Web/HTML/Element/form





##### urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# settings.MEDIA_ROOT => 실제 경로
# 첫번째 인자 (settings.MEDIA_URL) : 어떤 URL을 정적으로 추가할지 (Media file url)
# 두번째 인자 (document_root) : 실제 해당 미디어 파일이 어디에 존재하는지
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT #=> 이렇게도 사용이 가능하다
```

- `urls.py`에서 static의 경로를 설정 해준다.

`article.image.url` == `/media/sample.jpg`



:dog: **Django 공식 문서 | Managing static files**

**=>** https://docs.djangoproject.com/en/2.2/howto/static-files/

이미지도 edit을 통해 새로운 이미지로 수정할 수는 있지만, text와는 다르게 수정할 때 이미지를 무조건 업로드 하지 않으면 에러가 발생한다. (글만 수정하는 건 안된다는 의미)

- 이미지는 바이너리 데이터(하나의 덩어리)라서 텍스트처럼 일부만 수정하는게 불가능. 그렇기 때문에 html input 태그에 value속성으로 수정하는 방식이 아니고, 새로운 사진으로 덮어 씌우는 방법을 사용
- `<input type="file">` 가 `vlaue=""` 를 지원하지 않는다.

- 굳이 글만 수정하고 싶다면 이전과 똑같은 이미지를 업로드 하면 된다.



![image](https://user-images.githubusercontent.com/52684457/65293647-e67c6480-db96-11e9-904c-34d54f43c126.png)

:stop_sign: **문제점** : 이미지 필드 설정 이전에 작성했던 게시글의 detail 페이지가 동작하지 않는다. (article.image.url을 불러오지 못하기 때문, 빈 값을 가지고 있다.)

- **해결 #1** : static파일로 이미지가 없을 때 대신 사용할 이미지를 미리 넣어둠.

  **detail.html**

  ```python
    {% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.url }}">
    {% else %}
      <img src="articles/images/No.jpg" alt="no_img">
    {% endif %}
  ```

  - ifelse문을 사용한다. (no image 파일도 있어야 함.)

  ![image](https://user-images.githubusercontent.com/52684457/65294144-addd8a80-db98-11e9-8cf0-e1ed62944abd.png)

- **해결 #2** : 템플릿에서 `{% if %}` 문으로  `article.image` 가 존재하는 경우만 이미지를 출력하도록.



## :framed_picture: image resizing

- Pillow

- pilkit - pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리 `pip install pilkit`

- django-imagekit : 이미지 helper를 제공하는 django app  `pip install django-imagekit`

  ```python
  INSTALLED_APPS = [
      'articles.apps.ArticlesConfig',  # local party
      'jobs.apps.JobsConfig',          # local party
      'imagekit'                       # third party
      'django_extensions',             # django app
      ...
  ```

  

##### :warning: **주의사항**

- 설치 순서가 중요.

1. ##### html 태그로 직접 사이즈 조정

   - 원본은 그대로 저장되어 있고 보여지는 사이즈만 조정하는 것이기 때문에 근본적인 해결책이 아니다. (이미지가 100%가 들어가면 서버 비용이 비효율 적이다)

2. ##### 업로드 할 때 이미지 자체를 resizing 해서 저장

   ##### models.py

   ```python
   from imagekit.models import ProcessedImageField, ImageSpecField
   # ImageSpecField 원본을 불러서 원본으로 부터 자르는 작업을 해서 원본도 저장이 된다.
   from imagekit.processors import Thumbnail # Thumbnail은 잘라주는 기능
   ```

   :stop_sign: 우선 위의 코드를 `import` 해준다.

   ​      그리고 `models.py` 의 image를 재 설정 할 것

   

   - 2-1. 원본 저장 X **/** 썸네일 저장 O

     ```python
     image = ProcessedImageField(
     	processors=[Thumbnail(200, 300)], # 처리할 작업 목록
     	format='JPEG', # 저장 포맷
     	options={'quality': 90}, # 추가 옵션들
     	upload_to='articles/images', 
         # 저장 위치(MEDIA_ROOT/article/images) / media폴더는 생략되어 있다
     )
     ```

     - `ProcessedImageField()` 에 인자로 들어가 있는 값들은 `migrations` 이후에 추가되거나 수정이 되더라도 `makemigrations` 를 하지 않아도 된다.

     

   - 2-2. 원본 저장 O **/** 썸네일 저장 O	

     ##### models.py

     ```python
      image = models.ImageField(blank=True)
         image_thumbnail = ImageSpecField(
             # 위의 image로 부터 만들어 지기 때문에 서로 연결을 시켜주어야 한다.
             source='image',
             
             processors=[Thumbnail(200, 300)],
             format='JPEG',
             options={'quality': 90},
         )
     ```

     - 이 방법은 직접 호출하지 않으면 썸네일 이미지가 뜨지않고 원본 이미지가 뜬다.

     ##### detail.html

     ```django
      <img src="{{ article.image_thumbnail.url }}" alt="썸네일">
      <!-- url로 직접 호출 -->
     
       <h1 class="text-center">DETAIL</h1>
       {% if article.image %}
         <img src="{{ article.image.url }}" alt="{{ article.url }}">
       {% else %}
         <img src="{% static 'articles/images/No.jpg' %}" alt="no_img">
       {% endif %}
     ```

     ![image](https://user-images.githubusercontent.com/52684457/65295704-29d9d180-db9d-11e9-83c9-ce390244e022.png)

     - 원본사진만 저장이되고 썸네일은 캐시값으로 저장이 된다.

       ![image](https://user-images.githubusercontent.com/52684457/65296354-1e87a580-db9f-11e9-81a0-939e07c4e170.png)

       처음 이미지를 불러 올때에는 django 서버에서 불러 오기 때문에 메모리를 잡아 먹지만

       ![image](https://user-images.githubusercontent.com/52684457/65296332-12034d00-db9f-11e9-899f-47634326e11d.png)

       새로 고침을 하게되면 크롬에 캐시가 자동 저장되어있기 때문에 django에서 직접 가져올 필요 없어진다. => 메모리 소모가 줄어듦

       ![image](https://user-images.githubusercontent.com/52684457/65299621-349b6300-dbab-11e9-8e11-0bb701dc98a4.png)

       - 2-1과, 2-2의 방법으로 생성된 이미지 파일 폴더를 확인 할 수 있다.



## :framed_picture: image upload custom

##### models.py

*(class Article 위에)*

```python
def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'
```



*(class Article 안에)* `upload_to=articles_images_path,` 를

```python
upload_to='articles/images',
```

- 속성값만 바꿨기 때문에 migration 할 필요가 없다. 사이트를 켜서 사진업로드 글을 올리면 

  ![image](https://user-images.githubusercontent.com/52684457/65300069-20f0fc00-dbad-11e9-9b83-dd9aa16e75a0.png)

  - None 폴더 안에 이미지가 생성 된 것을 볼 수 있다.



`intance.pk` 는 처음 레코드가 작성되는 순간에는 PK 값이 없기 때문.

`media/articles/image/None/images` 로 저장이 되버린다.

- 실제 개발에선 로그인을 통해 유저 정보를 받고, `instance.user.pk` 또는

  `instance.user.username` 처럼 업로드한 유저의 정보로 폴더를 구조화하는 경우가 많다.

#### :fish: favicon

- 파비콘 아이콘 https://www.flaticon.com/
  32pixel

- 모든 기기에 대응하기 위한 소스를 뽑아주는곳 https://realfavicongenerator.net/

  select your favicon ficture *(사이즈 확인!)*

###### base.html

```django
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="shortcut icon" href="{% static 'articles/favicon/fish.png' %}">
  <title>Document</title>
```

- bootstrap 아래에 `<link rel="shortcut icon" href="{% static 'articles/favicon/fish.png' %}">`

  ![image](https://user-images.githubusercontent.com/52684457/65301030-9f02d200-dbb0-11e9-803f-8559b8ad8fa2.png)

- 강력 새로고침을 하면 파비콘을 확인할 수 있다.































