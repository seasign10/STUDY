[TOC]

# SQL과 django ORM

## 기본 준비 사항

```bash
# 폴더구조

TIL
	00_StartCamp
	...
	04_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * django project : `sql`

  * django app : `users`

  * `django_extensions` 설치 및 등록

  * users.csv 파일에 맞춰 `models.py` 작성 및 migratation

    ```python
    # users/models.py
    
    from django.db import models
    
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate 
    ```

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM user_users;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   >>> User.objects.create(first='해인', last_name='이', age=25, country='경상북도', phone='010-0000-0000', balance=999999999)
   ```

   ```sql
   -- sql
   sqlite> INSERT INTO users_user VALUES (102, '길동', '홍', 30, '대동여지도', '019-0000-0000', 7);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   >>> User.objects.get(pk=101)
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   >>> user = User.objects.get(pk=101)
   >>> user.last_name = '김'
   >>> user.save()
   ```

      ```sql
   -- sql
   sqlite> UPDATE users_user SET first_name='철수' WHERE id=101;
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   >>> User.objects.get(pk=101).delete()
      (1, {'users.User': 1})
   ```
   
   ```sql
   -- sql
   DELETE FROM users_user WHERE id=101;
   ```
   
   
---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   >>> User.objects.all().count()
   101
   
   # 또는
   >>> len(User.objects.all())
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
   101
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   >>> User.objects.filter(age=30).values('first_name')
   <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}, {'first_name': '길동'}]>
   ```

   - type을 찍어보면 query set으로 나오는데, 하나하나 뜯어서 볼 수 있다.

   - ```python
     print(User.objects.filter(age=30).values
        ...: ('first_name').query)
     SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30
     ```

     - sql문으로 어떻게 들어가게 되는지 볼 수있다.

      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE age == 30;
   "영환"
   "보람"
   "은영"
   "길동"
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용
      https://docs.djangoproject.com/en/2.2/ref/models/querysets/#gt

   ```python
   # orm
   >>> User.objects.filter(age__gte=30).count()
   44
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age >= 30;
   44
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   >>> User.objects.filter(age__lte=20).count()
   23
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age <= 20;
   23
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   >>> User.objects.filter(age=30, last_name='김').count()
   1
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age = 30 AND last_name="김";
   1
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   - https://docs.djangoproject.com/en/2.2/ref/models/querysets/#q-objects
   - https://docs.djangoproject.com/en/2.2/topics/db/queries/#complex-lookups-with-q

   ```python
   # orm
   >>> User.objects.filter(Q(age=30)) | User.objects.filter(Q(last_name='김'))
   <QuerySet [<User: 영환>, <User: 예진>, <User: 서현>, <User: 서영>, <User: 영일>, <User: 옥
   자>, <User: 광수>, <User: 성민>, <User: 정수>, <User: 서준>, <User: 은주>, <User: 명자>, <User: 미
   영>, <User: 보람>, <User: 은영>, <User: 우진>, <User: 순옥>, <User: 진우>, <User: 현지>, <User: 영
   호>, '...(remaining elements truncated)...']>
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE age = 30 OR last_name="김";
   5,"영환","차",30,"충청북도",011-2921-4284,220
   8,"예진","김",33,"충청북도",010-5123-9107,3700
   ...
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   >>> User.objects.filter(phone__startswith='0
      ...: 2-').count()
   24
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT (*) FROM users_user WHERE phone LIKE '02-%';
   COUNT (*)
   24
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   >>> User.objects.filter(country='강원도', last_name='황').values('first_name')
<QuerySet [{'first_name': '은정'}]>
   # .first_name().get('first_name') 를 붙이면 결과 값
   # '은정'
   ```
   
      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황';
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   >>> User.objects.order_by('-age')[:10]
   Out[13]: <QuerySet [<User: 정호>, <User: 미경>, <User: 성현>, <User: 상훈>, <User: 민서>, <User:
   영식>, <User: 미경>, <User: 영일>, <User: 승민>,
   <User: 현지>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
   id|first_name|last_name|age|country|phone|balance
   1|정호|유|40|전라북도|016-7280-2855|370
   4|미경|장|40|충청남도|011-9079-4419|250000
   ...
   65|민서|송|40|경기도|011-9812-5681|51000
   26|영식|이|39|경상북도|016-2645-6128|400000
   ...
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   >>> User.objects.order_by('age')[:10]
   <QuerySet [<User: 서영>, <User: 지후>, <User: 우진>, <User: 은정>, <User: 성훈>, <User: 유진>, <User: 영호>, <User: 광수>, <User: 정수>, <User: 진호>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY age ASC LIMIT 10;
   id|first_name|last_name|age|country|phone|balance
   11|서영|김|15|제주특별자치도|016-3046-9822|640000
   59|지후|엄|15|경상북도|02-6714-5416|16000
   61|우진|고|15|경상북도|011-3124-1126|300
   22|은정|황|16|강원도|016-5956-2725|7000
   ...
   54|영호|하|16|강원도|011-8615-2227|6100
   18|광수|김|17|충청북도|016-4058-7601|94000
   ...
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   >>> User.objects.order_by('balance', '-age')[:10]
<QuerySet [<User: 길동>, <User: 우진>, <User: 보람>, <User: 재현>, <User: 영환>, <User: 숙자>, <User: 미경>, <User: 우진>, <User: 명자>, <User: 준호>]>
   ```
   
   - 우선으로 내림차순 할
   
   ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
   id|first_name|last_name|age|country|phone|balance
   102|길동|홍|30|대동여지도|019-0000-0000|7
   99|우진|성|32|전라북도|010-7636-4368|150
   48|보람|이|28|강원도|02-2055-4138|210
   100|재현|김|25|경상북도|016-1252-2316|210
   5|영환|차|30|충청북도|011-2921-4284|220
   24|숙자|권|33|경상남도|016-4610-3200|230
   92|미경|박|35|경상북도|010-5203-5705|300
   61|우진|고|15|경상북도|011-3124-1126|300
   46|명자|김|23|전라남도|011-3545-5608|330
   38|준호|심|28|충청북도|016-6703-7656|340
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   >>> User.objects.order_by('-last_name', '-first_name')[4]
<User: 길동>
   ```
   
      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
   id|first_name|last_name|age|country|phone|balance
   102|길동|홍|30|대동여지도|019-0000-0000|7
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   >>> User.objects.aggregate(Avg('age'))
   Out[17]: {'age__avg': 28.247524752475247}
   ```

   - shell_plus여서 `import`되어 있어서 바로 가능하지만 원래 import해주어야 한다. 
     https://docs.djangoproject.com/en/2.2/ref/models/querysets/#avg
   - ㅇ

   ```python
   >>> User.objects.aggregate(avg_vlaue=Avg('age'))
   {'avg_vlaue': 28.247524752475247}
   ```

   - 이름을 바꿀 수도 있다.

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user;
   AVG(age)
   28.2475247524752
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   >>> User.objects.filter(last_name='김').aggregate(Avg('age'))
   {'age__avg': 28.782608695652176}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user WHERE last_name='김';
   AVG(age)
   28.7826086956522
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   >>> User.objects.filter(country='강원도').aggregate(Avg('balance'))
   {'balance__avg': 157895.0}
   ```

   ```sql
   -- sql
   sqlite> SELECT AVG(balance) FROM users_user WHERE country='강원도';
   AVG(balance)
   157895.0
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   >>> User.objects.aggregate(Max('balance'))
   {'balance__max': 1000000}
   ```

      ```sql
   -- sql
   sqlite> SELECT MAX(balance) FROM users_user;
   MAX(balance)
   1000000
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   >>> User.objects.aggregate(Sum('balance'))
{'balance__sum': 14425047}
   ```
   
      ```sql
   -- sql
   sqlite> SELECT SUM(balance) FROM users_user;
   SUM(balance)
   14425047
      ```