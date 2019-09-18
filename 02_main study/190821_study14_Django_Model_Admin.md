

# :dog:Django : Model

### :paw_prints: 스키마 

###### Database를 구성하는 레코드의 크기, 키(key)의 정의, 레코드와 레코드의 관계, 검색 방법 등을 정의한 것.

- **pk**(primary key) 각 행(레코드)의 고유값으로서 반드시 설정하여야 함 (중복X)

- 가로줄: 행(row), 레코드

- 세로줄: 열, 컬럼(Colum)



### :paw_prints:SQL

- DDL, DML, DCL 총 세가지가 있다.

>그 중 오늘 사용할 것은 CRUD 이다.
>
>- Create
>- Read
>- Update
>- Delete



### :paw_prints: ORM

- 데이터 베이스를 객체화 시킨 것
- 파이썬 코드로 SQL코드 명령어를 사용하면 ORM이 번역해주는 방식
- DataBase의 행, 열, pk등을 객체화 시켜서 해석
  - SQL을 건드는 것이아닌, 파이썬으로 코드를 작성해서 ORM을 통해 SQL명령어로 번역

> ###### 장점
>
> - sql을 몰라도 DB(database) 사용이 가능
> - sql의 절차적인 접근이 아닌 객체 지향적 접근 가능
> - 매핑 정보가 명확하여 *<u>ERD</u>를 보는 것에 대한 의존도를 낮출 수 있다.
>   - ERD(*Entity Relationship Diagram*) : 존재하고 있는 것들의 관계를 그림으로 표현한 것
>     여기서 '존재하고 있는 것들'이란 데이터를 말한다. 초반 개발 시 ERD를 작성하고 시작한다.
> - ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용할 수 있다. 개발자는 객체에 집중함으로써 해당 DB에 종속될 필요 없이 자유롭게 개발할 수 있다.

> ###### 단점
>
> - ORM만으로 완전히 거대한 서비스를 구현하기가 어렵다.
>   - sql을 사용할 수 밖에없는 지점이 생긴다.
>   - 사용하기는 편하지만, 설계를 매우 신중하게 해야한다.
>   - 프로젝트의 규모가 커질 경우 난이도가 올라가게 된다.
>   - 순수 SQL보다 약간의 속도 저하가 생길 수 있다.
> - 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다.

> #### "결론"
>
> **<u>생산성</u>**
>
> - ORM을 사용하여 얻게되는 생산성은 약간의 성능 저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문
> - 장점으로 인한 생산성 증가가 훨씬 크기 때문에 현대에는 대부분의 프레임워크들이 ORM을 사용하고 있다.
> - 즉, 우리는 DB를 객체(Object) - 인스턴스(instance)로 조작하기 위해 ORM을 배운다.



## :seedling: Model의 개념

- 모델은 단일한 데이터에 대한 정보를 가지고 있다.
- 필수적인 필드(컬럼, 열)와 데이터(레코드, 행)에 대한 정보를 포함한다. 일반적으로 각각의 **모델(클래스)**은 단일한 데이터베이스 **테이블과 매핑(연결, 연동)**된다.
- 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)를 의미**
- 사용자가 저장하는 데이터들의 필수적인 필드와 동작(behavior, 구체적 행동)을 포함



##### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length` 는 필수 인자
- 필드의 최대 길이(문자)이며 DB와 django의 유효성 검사(값을 검증)에서 사용됨
- 텍스트 양이 많을 경우 `TextFeild()` 로 사용(대체 해야함)



##### TextField()

- 글의 수가 많을 때 사용
- max_length 옵션을 줄 수 있지만 모델과 실제 DB에는 적용되지 않는다. 길이 제한을 주고 싶다면 `CharField() `를 사용해야 한다.



##### DateTimeFeild()

- 시간과 날짜를 기록하기 위한 필드
  - `auto_now_add=True`
    - django ORM 이 최초 INSERT(테이블에 데이터 입력)시에만 현재 날짜와 시간 작성
    - **최초 생성 일자 **가 들어간다.
  - `auto_now=True`
    - django ORM이 SAVE를 할 때마다 현재 날짜와 시간 작성
    - **최종 수정 일자 **가 기록이 된다.



*=***>>>>>** Feild는 각각 외워서 쓰기보다 찾아서 사용
 **=>** https://docs.djangoproject.com/en/2.2/ref/models/fields/



### :seedling: Model Logic

- DB 칼럼과 어떠한 타입으로 정의할 것인지에 대해 `django.db` 모듈의 `models` 의 상속을 받아서 적용
- 각 모델은 `django.db.models.Moel` **클래스의 서브 클래스**로 표현된다. (자식 클래스)

- 모든 필드는 **기본적으로 NOT NULL 조건**이 붙는다. (NULL 값이 들어갈 수 없다.)
  - :mushroom: **NULL ?** 
    - 구조적 질의 언어 (SQL)에서 데이터베이스 내의 데이터 **값이 존재하지 않는다**는 것을 지시하는데 사용되는 특별한 표시어
- 각각의 **클래스 변수**들은 **모델의 데이터베이스 필드**를 나타낸다.

> https://github.com/django/django 
> **=>** https://github.com/django/django/blob/master/django/db/models/base.py
> **=>** `class Model(metaclass=ModelBase):`



##### :paw_prints: Migrations : 이주, 이동, 설계도를 데이터베이스로 이주

1. ###### `migrations`

   - makemigrations 명령어는 모델(model.py)을 작성/변경한 사항을 django에게 알리는 작업
     (ORM에 보낼 PYTHON 코드 설계도를 작성)

   - 테이블에 대한 설계도(django ORM이 만들어줌)를 생성

     ```bash
     $ python manage.py makemigrations
     ```

     

2. ###### `migrate`

   - migrations로 만든 설계도를 기반으로 `db.sqlite3` DB에 반영한다.
     *실제 DB 테이블을 생성*

     ```bash
    $ python manage.py migrate
     ```
     
   - **모델에서의 변경사항들과 DB 스키마가 동기화**를 이룬다.

     
   
  ###### :mushroom: 동기화를 하기 전에 ...

```bash
 $ python manage.py sqlmigrate app_name 0001
```
   - 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 볼 수 있다.
     (필수는 x 궁금하다면 확인 가능)

  ```bash
$ python manage.py showmigrations
  ```

 - [X]는 안된 것이 아니라, 체크된 것
 - migrations 설계도들이 migrate 되었는지(동기화가 되었는지) 안되었는지 확인



###### <u>model에 관련된 실행을 할 때에는 서버를 꺼주고 관리를 하는 것이 가장 안전</u>

![](https://user-images.githubusercontent.com/52684457/63395394-88752980-c3fe-11e9-8005-6f7853d40259.png)

![](https://user-images.githubusercontent.com/52684457/63395475-d68a2d00-c3fe-11e9-9bf4-ea638cec3049.png)

`python manage.py makemigrations` **=>** model에 작성한 설계도를 업데이트 하는 것



- db.sqlite3 파일이 비어있는 것을 확인 할 수 있다. ( **참고로 db또한 gitignore에 포함 된다. 올리면 안됨!!** )

  - 그래서  github으로 clone을 받으면 테이블은 비어있다.

  ![](https://user-images.githubusercontent.com/52684457/63395697-865f9a80-c3ff-11e9-9300-689839e0ed30.png)

  - **F1** 키를 눌러서

  ![image](https://user-images.githubusercontent.com/52684457/63395770-c161ce00-c3ff-11e9-951b-2743e68cce6a.png)

  ![](https://user-images.githubusercontent.com/52684457/63395787-d0e11700-c3ff-11e9-81ce-c3437e0b61c3.png)

  ![](https://user-images.githubusercontent.com/52684457/63395816-ed7d4f00-c3ff-11e9-8560-b65e9f2a717d.png)

  - **이 때** F1 키를 눌러서 SQLiteL: Open Database, db.sqlite3 (즉 위의 작업 반복)을 실행해주어야 db.sqlite3에 목록이 아래처럼 생겨난다. (DB table)

  ![](https://user-images.githubusercontent.com/52684457/63395963-72686880-c400-11e9-8a09-5cdfab3025b4.png)



#### :seedling: Model 변경 시 작성 순서

1. `models.py` : 작성 및 변경(생성 / 수정)
2. `makemigrations` : migrations 파일 만들기(설계도)
3. `migrate` : 실제 DB에 적용 및 동기화(이 때 테이블이 생성 됨)

- 테이블의 이름은 app 이름과 model에 작성한 class 이름이 조합되어져서 자동으로 만들어진다. 
  (**<u>모두 소문자</u>** )

- 모델의 클래스 변수들은 **반드시 소문자**로 작성한다.



> ###### 수정 하기 위해서...
>
> - 우선 shell을 끈다.
> - models.py에서 변수를 수정한 후 저장. 그리고 `python manage.py makemigrations`
>
> ![](https://user-images.githubusercontent.com/52684457/63404468-52e03880-c41e-11e9-89ec-652c37020510.PNG)
>
> - `python manage.py migrate`
>
> ![](https://user-images.githubusercontent.com/52684457/63404469-52e03880-c41e-11e9-8da9-e45ab4eee385.PNG)
>
> - 수정한 사항을 확인 할 수 있다.
>
> ![](https://user-images.githubusercontent.com/52684457/63404470-52e03880-c41e-11e9-8733-71bd7b95a296.PNG)
>
> 
>
> ###### 큰 오류가 생겼을 때에는 아예 수정이 불가해서 삭제해야하는 경우가 생긴다.
>
> -  0001, 0002 . . . 같이 번호 붙은 설계도를 전부 지우기
>    <u>이 해당 파일에서 수정하면 절대 안됨!!</u>
>
> - 데이터베이스를 마저 삭제 **=>** db.sqlite



```python
# models.py

from django.db import models

# Create your models here.
class Article(models.Model): # models.Model의 상속을 받는다.
    # 클래스 변수 (DM의 필드), 4개의 colum을 만듦, 소문자로 만들어야 한다.

    # id(프라이머리 키)는 기본적으로 처음 테이블 생성이 자동으로 만들어진다'
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10) # 글자수를 제한하는 문자열로 들어갈 것, 최대 10글자
    content = models.TextField() # 위와 달리 제한이 없는 대규모 필드
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간을 계산해주는 필드
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'
    
```

- app폴더 articles(복수형)와 models.py 의 class Article을 헷갈리지 말자!
  - Article에서 인스턴스를 생성할때에는 article로 작성하였으니 유의하자.

------



### :mushroom: SQLite



###### Mac은 sqlite가 기본으로 설치되어있다.

 ```bash
$ sqlite3 db.sqlite3
 ```

- sql에서는 sql문법을 사용해야한다.
- python 문법으로 sql을 이용하기 위해서는 shell을 이용해야 한다. 



###### 윈도우에서는 sqlite가 설치되어 있지 않아서 직접 설치해주어야 한다.

![](https://user-images.githubusercontent.com/52684457/63399030-320de800-c40a-11e9-9ad2-9648eb828273.PNG)

- https://www.sqlite.org/download.html
- 자신의 사양에 맞는 32, 86bit 중 하나 (첫번째, 두번째)를 받고 나머지 아래의 tools를 받는다.



![](https://user-images.githubusercontent.com/52684457/63399031-320de800-c40a-11e9-91f2-547611f6d2a7.PNG)

- 내 컴퓨터 C드라이브에 들어가서, sqlite 폴더를 새로 생성



![](https://user-images.githubusercontent.com/52684457/63399034-33d7ab80-c40a-11e9-9046-51e2e422ea35.PNG)

- 다운로드 받았던 파일의 압축을 풀어준 후, 5개의 파일을 확인 하고 5개의 파일만 남겨준다. 
  (압축파일은 휴지통으로)



![](https://user-images.githubusercontent.com/52684457/63399039-36d29c00-c40a-11e9-8ffe-6dbb06ae2170.png)

- 시스템 환경 변수에서 위와 같이 설정해준다.



![](https://user-images.githubusercontent.com/52684457/63399035-33d7ab80-c40a-11e9-86d0-e0c6dcbfe1b1.PNG)

- 윈도우에서는 winpty sqlite3 이라는 명령어를 일일히 쳐주어야 실행이 된다.



![](https://user-images.githubusercontent.com/52684457/63399040-376b3280-c40a-11e9-9933-fa6b937d82ac.png)

- 환경 변수를 이용해 좀더 편리한 명령어(Mac과 동일하게)를 사용해도 실행 되도록 위와 같이 설정 해 준다.



![](https://user-images.githubusercontent.com/52684457/63399041-376b3280-c40a-11e9-9e07-bb4c6dc05603.PNG)

- <u>sqlite3</u> db.sqlite3 (밑 줄은 위에서 직접 바꾼 명령어 => winpty sqlite3)
- .table을 입력하면 테이블을 확인 할 수 있다.



![](https://user-images.githubusercontent.com/52684457/63399044-376b3280-c40a-11e9-8caf-46ff46d0b338.PNG)

- 위의 명령어를 입력하면 비어있는 상태를 볼 수 있다.



------



## :paw_prints: CRUD (DB API 조작)

1. Django Shell
   -  django 프로젝트 설정이 로딩된 파이썬 shell
   - 일반 파이썬 shell로는 django 환경에 접근 불가
   - 즉, django 프로젝트 환경에서 파이썬 shell을 활용한다고 생각하면 된다.



###### :mushroom:조작하기전에...

`pip install ipython` **=>** 파이썬을 컬러링 해줌으로써 보기 좀 더 편하게 만들어 줌

![](https://user-images.githubusercontent.com/52684457/63399046-3803c900-c40a-11e9-92bf-74f5a88a96bc.PNG)

- `$ python manage.py shell` (파이썬 문법으로 SQL을 이용하기 위해) 명령어로 shell을 켰을 때, 
  넘버링이 되어 보기 편하고, 컬러링이 되어 구별이 쉽다.



### :paw_prints: CREAT

> ( **C**REAT )
>
> QuerySet 기본 개념
>
> - 전달 받은 객체의 목록
>   - QuerySet : 쿼리 Set 객체
>   - Query : 단일 객체
> - DB로 부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
> - Query를 던지는 Language를 활용해서 DB에게 데이터에 대한 조작을 요구
>
> 
>
> `QuerySet`
>
> - object 사용하여 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체
> - 단일한 객체를 반환(리턴)할 때는 테이블(class)의 인스턴스로 리턴 됨
>
> `objects`
>
> - Model Manager 와 Django Model 사이의 Query 연산의 인터페이스 역할을 해주는 친구
> - 즉, `models.py`에 설정한 클래스(테이블)을 불러와서 사용할 때 DB와의 인터페이스 역할(쿼리를 날려주는)을 하는 매니저
> - 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다.
> - DB ---------- objects ---------- Python Class(models.py)
> - Manager(objects)를 통해 **데이터를 조작(메서드)**할 수 있다.



##### 데이터 객체를 만드는(생성, CREAT) 하는 3가지 방법

1. ###### 첫번째 방식

   - 일반적으로 사용하는 방식

   ```python
   $ python manage.py shell
   # SQL
   # INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
   # INSERT INTO articles_article (title, content) VALUES ('first', 'django!')
   
   >>> article = Article() # Article class 로부터 article 인스턴스 생성
   >>> article.title = 'first' # 인스턴스 변수(title)에 값을 할당
   >>> article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
   
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >>> article
   <Article: Article object (None)>
   >>> Article.objects.all()
   <QuerySet []>
   
   # save를 하고 확인해보면 저장된 것을 확인 할 수 있다.
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   
   # 인스턴스 article을 활용하여 변수에 접근할 수 있다.(저장된 값 확인)
   >>> article.title
   'first'
   >>> article.content
   'django!'
   >>> article.create_at
   datetime.datetime(2019, 8, 21, 2, 43, 56, 247827, tzinfo=<UTC>)
   ```

   ![](https://user-images.githubusercontent.com/52684457/63399922-fc1e3300-c40c-11e9-848f-d1d9aa9829f1.png)

   ( *위의 이미지는 content, context 오타를 내서 값이 입력되지 않았다. 변수명을 바꾸어주기 위해서는 위의 Model변경시 순서 내용을 따라하면 된다.* )

   - shell에서는 article이라는 클래스가 없는 상태기 때문에 테이블에서 import해서 불러와주어야 한다.
     `from articles_models import Article`
   - **save를 반드시** 해주어야 위 처럼 테이블이 생겨난다. (시간은 UTC기준)
     save를 하지않고 인스턴스로 조작만하면 만들어지기만 하고 db에 전송되지 않은 상태

2. ###### 두번째 방식

   ```python
   >>> article = Article(title='second', content='django!!')
   >>> article.save()
   ```

3. ###### 세번째 방식

   - create는 **검증**을 하는틈이 없기 때문에 잘 사용 하지 않는다.

   ```python
   >>> Article.objects.create(title='third', content='django!!!')
   ```

   - **유효성 검사**

     - save 전에 `full_clean()` 메서드를 통해 article 이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아볼 수 있다.

     - models.py에 필드 속성과 옵션에 따라 검증을 진행한다.

       ![](https://user-images.githubusercontent.com/52684457/63404467-5247a200-c41e-11e9-92ef-a45cb2d79707.PNG)

     

> article.id : 생성한 id를 확인하는 값
>
> ###### article.pk : 저장되는 순간에 생기는 값 



### :paw_prints: READ​

> 테이블 내용을 전부 조회( **R**EAD )
>
> - DB에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
> - 만약에 레코드가 하나라면, 인스턴스 단일 객체로 반환
>   두 개 이상이면  QuerySet 형태로 반환
>
> 
>
> Python input **=>** <u>Article.objects.all()</u> **=>** article이라는 클래스에 있는 all이라는 매서드를 실행
>
> DB에 전달되는 명령어 **=>** <u>SELECT * FROM articles_article;</u>
>
> - 위 아래 동일한 코드지만 ORM으로 번역이 되어서 들어감

```python
# 1. SELECT * FROM articles_article;
# 1. DB에 있는 모든 글 가져오기
>>> Article.objects.all()



# 2. SELECT * FROM articles_article WHERE title='first';
# 2. DB에 저장된 글 중에서 title이 first인 글만 가져오기
>>> Article.objects.filter(title='first')



# 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
# 3. DB에 저장된 글 중에서 title에 first 인 글 중에서 첫번째 글만 가져오기
>>> Article.objects.all().first()
>>> Article.objects.all().last() # 마지막 값



# 4-1. SELECT * FROM articles_article WHERE id=1;
# 4-1. DB에 저장된 글 중에서 PK가 1인 글만 가져오기
>>> Article.objects.get(pk=1)
# PK만 .get() 으로 가져올 수 있다. (.get()은 값이 중복이거나, 일치하는 값이 없으면 에러를 발생시킨다.) 즉, pk 에만 사용하자. 

# 4-2. filter의 경우 존재하지 않으면 에러가 아닌 빈 쿼리셋을 반환한다. 마치 딕셔너리에서 value를 꺼낼 때 []방식으로 꺼내냐 혹은 .get으로 꺼내냐 하는 차이와 유사
>>> Article.objects.filter(pk=100) # pk=없는 값 
<QuerySet []>

# 4-3. filter / get
# filter 자체가 여러 값을 가져올 수 있기 때문에 django가 개수를 보장하지 못한다. 그래서 0개, 1개라도 무조건 쿼리셋으로 반환한다.

# id를 가져올때 .get , filter은 빈값만 출력 대신 filter은 리스트로 나오기때문에 for문으로 돌릴수있음.



# 5-1. 오름차순
# SELECT * FROM articles_article ORDER BY title ASC;
>>> Article.objects.order_by('pk')

# 5-2. 내림차순
# SELECT * FROM articles_article ORDER BY title DESC;
>>> Article.objects.order_by('-pk')



# 6. 쿼리셋은 리스트 자료형은 아니지만, 리스트에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능
>>> Article.objects.all()[2]
>>> Article.objects.all()[1:3]



# 7. LIKE / startswith / endswith
# django ORM은 이름(title)과 필터(contains)를 더블언더스코어(__)로 구분한다.
# 더블언더스코어 == 던더(dunder)스코어

# LIKE
>>> Article.objects.filter(title__contains='fir') # fir 포함

# startswith
>>> Article.objects.filter(title__contains='fir') # fir로 시작

# endswith
>>> Article.objects.filter(title__contains='!') # !로 끝나는
```



### :paw_prints: UPDATE

> ( **U**PDATE )
>
> - 값을 변경하는 것

```python
# article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
>>> article = Article.objects.get(pk=1)

>>> article.title = 'byebye'

>>> article.save()
```



### :paw_prints: DELETE

> ( **D**ELETE )
>
> - 새로운 아이디가 생성될 때
>   지워진 값의 아이디에 생성될까, 마지막 값의 뒤에 생성될까?
> - 지워졌다는것은 문제가 생겨서 지운것이라고 판단되어 지워진 아이디값에 같은 아이디로 재 생성하지 않고 **다음 아이디 값**을 생성한다.

```python
# article 인스턴스 객체를 생성후 .delete() 메서드를 호출
>>> article = Article.object.get(pk=1)

>>>article.delete()
```

- 핵심은 우리는 ORM을 통해 클래스의 인스턴스 객체로 DB를 조작할 수 있다는 것!
- 앞으로 CRUD 로직을 직접 작성하면서 위에서 배운 코드들을 다시 활용하게 될 것



![](https://user-images.githubusercontent.com/52684457/63407245-fe8d8680-c426-11e9-811c-11591e9b37a6.PNG)



------



## :seedling: ADMIN

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지.
- `models.py` 에 작성한 클래스를 `admin.py` 에 등록하고 관리
- record 생성 여부 확인에 매우 유용, 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자 페이지에서 사용할 수 있다.



![](https://user-images.githubusercontent.com/52684457/63407244-fe8d8680-c426-11e9-8783-50f6ef78c738.png)

- 관리자 site에 접속하기위해서는 관리자 계정을 만든다. ('/admin')



```python
from django.contrib import admin
from .models import Article  # 명시적 상대경로 표현

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다. 대부분 튜플로 작성되어 있다.
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    
    # 필더를 만드는것, created_at은 시간별로 필터링을 해준다.
    list_filter = ('created_at',)

    # 링크를 거는것 (클릭하면 해당 content 수정 페이지로 이동)
    list_display_links = ('content',)

    # 바로 수정가능하게 만드는 것
    list_editable = ('title',)

    # 값을 넣지 않으면 기본값 100
    list_per_page = 2

admin.site.register(Article, ArticleAdmin) # ArticleAdmin 만들고 레지스터에 등록

```

![](https://user-images.githubusercontent.com/52684457/63406993-698a8d80-c426-11e9-8f66-2c7084801057.png)

- Articles, `admin.site.register` 로 페이지를 만들어 준 것
- 인증 및 권한에 사용자에 들어가면 사용자 정보를 알 수 있다. 
  여기서도 관리가 계정의 비밀번호는 암호화된 코드로 이루어져 있다.

![](https://user-images.githubusercontent.com/52684457/63407017-77d8a980-c426-11e9-8341-e956410e1987.png)

- ARTICLES의 Articles에 들어온 화면
- admin.py에서 수정한 사항들이 적용되어 있다.

> ###### 그 외의 코드를 사용하고 싶다면 문서를 참고 !
>
> **=>** https://docs.djangoproject.com/en/2.2/ref/contrib/admin/



#### 관리자 변경 목록(change list) 커스터마이징

1. ###### list_display

   - admin 페이지에서 우리가 models.py에 정의한 각각의 속성(column)들의 값(레코드)을 보여준다.

2. ###### list_filter

   - 특정 필드에 의해 변경목록을 필터링 할 수 있게 하는 filter 사이드바를 추가한다.
   - 표시되는 필터의 유형은 필드의 유형에 따라 다르다.

3. ###### list_display_links

   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫 번째 필드에 링크가 적용)

4. ###### list_editable

   - 목록 상에서 직접 수정할 필드 적용

5. ###### list_per_page

   - 한 페이지에 표시되는 항목 수를 제어 (기본값 : 100)

> #### Django extensions (확장자)
>
> https://django-extensions.readthedocs.io/en/latest/
>
> - Django-extension 은 커스텀 확장 tool이다.
> - Django app 구조로 되어있기 때문에 프로젝트에 사용하기 위해서는 app등록 과정을 거쳐야한다.
>
> ![](https://user-images.githubusercontent.com/52684457/63408909-08b18400-c42b-11e9-96a9-3762f93597d1.png)
>
> - 기존 shell과는 달리 shell_plus는 기존에 import된 것을 다 불러 주기 때문에 일일히 import 해주던 shell보다 편리하다.











