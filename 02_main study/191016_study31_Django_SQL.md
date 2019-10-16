# :dog:Django : SQL



## :large_blue_diamond: 데이터베이스(DB)

- 데이터베이스(*database, DB*)는 **체계화된 데이터의 모임**이다. 작성된 목록으로써 여러 응용 시스템들의 통합된 정보들을 저장하여 운영할 수 있는 공용 데이터들의 묶음이다. 즉, 여러 사람이 공유하여 사용할 목적으로 통합, 관리하는 데이터의 집합이다.

|              장점              |                     단점                      |
| :----------------------------: | :-------------------------------------------: |
|       데이터 중복 최소화       |           데이터베이스 전문가 필요            |
|          데이터 공유           |                많은 비용 부담                 |
|  일관성, 무결성, 보안성 유지   |          데이터 백업과 복구가 어려움          |
|       최신의 데이터 유지       |                시스템의 복잡함                |
|      데이터의 표준화 가능      | 대용량 디스크로 엑세스가 집중되면 과부하 발생 |
| 데이터의 논리적, 물리적 독립성 |                                               |
|       용이한 데이터 접근       |                                               |
|     데이터 저장 공간 절약      |                                               |

- **SQLite** : 서버가 아닌 응용  프로그램에 넣어 사용하는 비교적 가벼운 데이터 베이스
  Oracle과 같은 기업에서 사용하는 SQL를 제외 하면 MYSQL다음으로 개인 사용량이 많다.

![image](https://user-images.githubusercontent.com/52684457/66879041-87740900-eff7-11e9-91cf-ffd7fc546db6.png)

![image](https://user-images.githubusercontent.com/52684457/66879565-98257e80-eff9-11e9-9eff-83f0a283f9e4.png)

- `sqlite3 tutorial.sqlite3` : tutorial이라는 데이터 베이스 설정 
  (새로운 db파일을 만들기 위한 이름 지정 **혹은** 이미 있는 db로 sqlite 실행)

- `.databases` : db 파일 생성 (새로 db파일을 만들 시에 사용)

- 저장된 csv(소문자)를 불러와서 example이라는 이름으로 import

- `.headers on` / `.mode column`을 적용하기 전과 후

  - 아무것도 적용하지 않음

  ```sqlite
  sqlite> SELECT * FROM news;
  1번 제목|1번 내용||1
  title|content|2019-10-16 14:11:38|1
  ```

  - `.mode column` 만 적용

  ```sqlite
  sqlite> SELECT * FROM news;
  1번 제목       1번 내용                   1
  title       content     2019-10-16  1
  ```

  - `.headers on` 만 적용

  ```sqlite
  sqlite> SELECT * FROM news;
  title|content|created_at|subtitle
  1번 제목|1번 내용||1
  title|content|2019-10-16 14:11:38|1
  ```

  - 둘 다 적용

  ```sqlite
  sqlite> SELECT * FROM news;
  title       content     created_at  subtitle
  ----------  ----------  ----------  ----------
  1번 제목       1번 내용                   1
  title       content     2019-10-16  1
  
  ```

  - 사용자가 보기에 좀 더 깔끔해졌다.

- sqlite3 실행

  **참고 문서**[https://github.com/seasign10/STUDY/blob/master/02_main%20study/190821_study14_Django_Model_Admin.md](https://github.com/seasign10/STUDY/blob/master/02_main study/190821_study14_Django_Model_Admin.md)
  
- ##### SQLite는 RDBMS에 속한다. RDBMS의 특징

  - 관계형 데이터베이스 관리 시스템
    1. 모든 데이터를 2차원 테이블로 표현
    2. 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
    3. 상호 관련성을 가진 테이블의 집합
    4. 만들거나 이용하기도 비교적 쉽고, 확장이 매우 용이



![image](https://user-images.githubusercontent.com/52684457/66879750-842e4c80-effa-11e9-92dd-0185034a5bd0.png)

- 스키마 조회
  `scheme` : 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조

![image](https://user-images.githubusercontent.com/52684457/66879601-c905b380-eff9-11e9-8a08-90621acb2b69.png)

- `BLOB` : 데이터 타입 X **=>** 큰 데이터 덩어리
- `INTEGER`, `TEXT`, `DATETIME` 을 주로 사용

`.` : sqlite3 프로그램의 기능을 실행하는 것

`;` : 세미콜론 까지가 하나의 명령(Query)으로 간주 (:warning: 명령어 마칠 때 필수)

`.tables` 로 생성된 테이블이나 삭제된 테이블을 계속 확인하길 권장 (친절하게 오류를 알려주지 않음)

`CTRL` + `C` OR `Z` : `... >` 에서 나올 수 있다.

`.exit` : sqlite에서 나올 수 있다.

`.nullvalue ‘NULL’` : 값을 넣지 않았을 때 NULL로 출력

- SQL 문법은 소문자로 작성해도 된다. (<u>단, 대문자를 권장</u>)
- 하나의 DB에는 여러개의 table이 존재

![image](https://user-images.githubusercontent.com/52684457/66880212-edaf5a80-effc-11e9-88bb-a752d3492acc.png)

`DROP TABLE` : 테이블 삭제

### :cookie: DATA 추가 (INSERT)

```sqlite
sqlite> CREATE TABLE classmates (
   ...> name TEXT,
   ...> age INT,
   ...> address TEXT );
sqlite> .table
classmates  example
sqlite> INSERT INTO classmates (name, age)
   ...> VALUES ('홍길동', 23);
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         23
sqlite> INSERT INTO classmates (name, age, address)
   ...> VALUES ('홍길동', 30, '서울');
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         23
홍길동         30          서울
```

- table 생성(`CREATE TABLE`) 후, 
  데이터를 집어넣는(`INSERT INTO`) 과정과 

  확인하는(`SELECT * FROM`) 과정

- `INSERT INTO classmates VALUES ('홍길동', 30, '서울');` 도 가능

****

#### :grey_question: ID는 어디에?

- 생성 시 아이디를 넣지 않았지만 숨겨진 id(*sql이 자동으로 지정*)가 존재하고 있다.

  `SELECT rowid, * FROM`

  ```sqlite
  sqlite> SELECT rowid, * FROM classmates;
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동         23
  2           홍길동         30          서울
  ```

  - `rowid`는 64bit 정수 타입의 유일한 식별 값
  - id( `INTEGER PRMARY` 만 사용 가능)가 rowid로 대체

  ```sqlite
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT NOT NULL,
     ...> age INT NOT NULL,
     ...> address TEXT NOT NULL );
  sqlite> .table
  classmates  example
  sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  Error: NOT NULL constraint failed: classmates.address
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울'
  );
  ```

  - **특정 데이터(datebase)가 꼭 필요한 정보라면 공백으로 비워두면 안된다.** (NOT NULL 설정)

    빈 스트링이나 null값으로라도 들어가야 한다.

  ```sqlite
  sqlite> INSERT INTO classmates VALUES ('꿈돌이', 30, '대전');
  Error: table classmates has 4 columns but 3 values were supplied
  ```

  - rowid는 직접 명시하지 않아도 자동으로 입력해주지만, id를 `INTEGER PRMARY` 로 만들어 줬기 때문에 직접 명시하지 않으면 입력해주지 않는다.

- `NOT NULL`을 설정하여 `table`을 다시 만들자.

```sqlite
sqlite> CREATE TABLE classmates (
   ...> name TEXT NOT NULL,
   ...> age  INT NOT NULL,
   ...> address TEXT NOR NULL );
sqlite> .tables
classmates  example
sqlite> INSERT INTO classmates VALUES ('홍길동',30,'서울'), ('꿈돌이',33,'대전), ('아리랑',50,'한국'), ('조나단',29,'미국');
   ...> ';
Error: near "아리랑": syntax error
        INSERT INTO classmates VALUES ('홍길동',30,'서울'), ('꿈돌이',33,'대전'), ('아리랑',50,'한국'), ('조나단',29,'미국');
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         30          서울
꿈돌이         33          대전
아리랑         50          한국
조나단         29          미국
```

- `'` 과 같은 오타를 주의하자. `';` 를 입력하면 빠져나올 수 있다.



### :mag: 가져오기 (SELECT)

```sqlite
sqlite> SELECT rowid, name FROM classmates;
rowid       name
----------  ----------
1           홍길동
2           꿈돌이
3           아리랑
4           조나단
```

- `SELECT rowid, name FROM classmates;` : rowid, name 조회

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1;
rowid       name
----------  ----------
1           홍길동
```

- 특정 값 불러오기 

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 3;
rowid       name
----------  ----------
1           홍길동
2           꿈돌이
3           아리랑
```

- 특정 값 까지의 목록을 다 가져온다. 하나의 값만 가져온다면?

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid       name
----------  ----------
3           아리랑
```

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 3 OFFSET 1;
rowid       name
----------  ----------
2           꿈돌이
3           아리랑
4           조나단
```

- `OFFSET` : ~ 이후 부터
- `LIMIT` : ~ 만큼(까지)만 출력하고 잘라내기

```sql
sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
rowid       name
----------  ----------
1           홍길동
```

- address가 서울인 목록을 rowid와 name을 가져온다.
- `WHERE column=value`

```sqlite
sqlite> SELECT DISTINCT age FROM classmates;
age
----------
30
33
50
29
```

- `SELECT DISTINCT` : 중복 없이 값을 가져온다.



### :no_entry_sign: 삭제 (DELETE)

- 중복이 불가능한(UNIQUE)값인 ID를 기준으로 삭제하는 것을 권장

```sqlite
sqlite> DELETE FROM classmates WHERE rowid=4;
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         30          서울
꿈돌이         33          대전
아리랑         50          한국
```

- rowid가 4였던 조나단이 삭제 된 것을 확인 가능

```sqlite
sqlite> INSERT INTO classmates VALUES ('바나나',30,'제주');
sqlite> SELECT rowid, * FROM classmates;
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         30          서울
2           꿈돌이         33          대전
3           아리랑         50          한국
4           바나나         30          제주
```

- SQLite는 기본적으로 일부 행을 삭제하고 새 행을 삽입하면 삭제 된 행의 값을 재사용하려고 시도한다.
- 물론 상황에 따라서 재사용하지 않도록 하게 하는 방법도 있다.
  **=>** 자동증가속성(AUTOINCREMENT)을 부여
- `AUTOINCREMENT `를 사용해보자

```sqlite
sqlite> CREATE TABLE tests (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL );
sqlite> INSERT INTO tests (id, name) VALUES (1, '홍길동'), (2, '장백수');
sqlite> SELECT * FROM tests;
id          name
----------  ----------
1           홍길동
2           장백수
sqlite> DELETE FROM tests WHERE id=2;
sqlite> INSERT INTO tests (name) VALUES ('김첨지');
sqlite> SELECT * FROM tests;
id          name
----------  ----------
1           홍길동
3           김첨지
```

- id값이 재사용되지 않은 것을 확인 가능
- 하지만 **SQLite**에서는 특정한 요구사항(재사용하지 못하게 하는)이 없다면 **AUTOINCREMENT 속성을 사용하지 않아야** 한다고 한다. 
  예) row id의 최대값은 64비트 8바이트 실수의 최대값
  9,223,372,036,854,775,807 (922경) 이 상황에서 INSERT INTO를 한다면
  1. AUTOINCREMENT 가 없을 때 : 중간에 없는 ID를 재사용하므로 에러가 나지 않을 것 (마지막 row가 도달했을 때 ~~100%~~)
  2. AUTOINCREMENT 가 있을 때 : 최대 레코드를 넘어서기 때문에 에러가 발생



### :fountain_pen: 수정 (UPDATE)

```sqlite
sqlite> UPDATE classmates
   ...> SET name='홍길동',address='미국'
   ...> WHERE rowid=4;
sqlite> SELECT * FROM classmates;
name        age         address
----------  ----------  ----------
홍길동         30          서울
꿈돌이         33          대전
아리랑         50          한국
홍길동         30          미국
```

- id가 4인 레코드를 수정한 결과 값



### WHERE, expression

#### 1. WHERE 심화

- 특정한 TABLE에서 특정 조건의 COLUMN만 가져오기

```sqlite
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables
classmates  example     tests       users
sqlite> .headers on
sqlite> SELECT * FROM users;
1|정호|유|40|전라북도|016-7280-2855|370
2|경희|이|36|경상남도|011-9854-5133|5900
3|정자|구|37|전라남도|011-4177-8170|3100
4|미경|장|40|충청남도|011-9079-4419|250000
5|영환|차|30|충청북도|011-2921-4284|220
6|서준|이|26|충청북도|02-8601-7361|530
7|주원|민|18|경기도|011-2525-1976|390
...
995|승현|김|20|경기도|011-1954-7183|930
996|지연|이|29|경상남도|016-7945-6460|210
997|경수|최|33|충청남도|011-2783-3991|85000
998|시우|고|15|제주특별자치도|016-3732-8726|270
999|성호|최|28|충청북도|010-5772-9832|6700
1000|예은|장|31|경기도|016-5653-5019|8400
```

- 새로운 csv를 users라는 이름으로 import 후 table 확인



```sqlite
sqlite> SELECT * FROM users WHERE age >= 30;
1|정호|유|40|전라북도|016-7280-2855|370
2|경희|이|36|경상남도|011-9854-5133|5900
3|정자|구|37|전라남도|011-4177-8170|3100
4|미경|장|40|충청남도|011-9079-4419|250000
5|영환|차|30|충청북도|011-2921-4284|220
8|예진|김|33|충청북도|010-5123-9107|3700
13|하은|남|32|전라북도|016-9544-1490|35000
14|영일|김|35|전라남도|011-4448-6198|720
17|병철|고|34|충청남도|016-2455-8207|440
21|동현|신|36|경상북도|010-1172-2541|4700
24|숙자|권|33|경상남도|016-4610-3200|230
26|영식|이|39|경상북도|016-2645-6128|400000
...
985|선영|장|35|전라북도|010-2357-5281|17000
986|수빈|임|34|제주특별자치도|016-2457-1505|32000
989|지현|이|35|전라북도|010-2984-2421|1800
992|경수|김|39|전라남도|011-4344-6657|3700
993|명자|이|37|제주특별자치도|010-4359-8236|280
997|경수|최|33|충청남도|011-2783-3991|85000
1000|예은|장|31|경기도|016-5653-5019|8400
```

- **나이가 30이상인** 사람들의 목록을 불러오는 방법



```sqlite
sqlite> SELECT first_name FROM users WHERE age >= 30;
정호
경희
정자
미경
영환
예진
...
경수
명자
경수
예은
```

- 나이가 30이상인 사람들의 **이름만** 불러오는 방법



```sqlite
sqlite> SELECT age, last_name FROM users WHERE age >= 30 and last_name="김";
33|김
35|김
38|김
37|김
```

- **두 가지 이상의 조건을 만족**하는 방법 : 나이가 30이상, 성씨가 김씨인 사람



#### 2. Expression

```sqlite
sqlite> SELECT COUNT(*) FROM users;
1000
```

- user(table)의 총 갯수 
  column을 지정하지 않으려면 *를 삽입해주면 된다.



```sqlite
sqlite> SELECT AVG(age) FROM users WHERE age >= 30;
35.1763285024155
```

- 30세 이상의 사람들의 평균나이 구하는 방법
- `AVG()`, `SUM()`, `MIN()`, `MAX` : 이 표현식은 기본적으로 숫자(INTEGER)일때만 가능



```sqlite
sqlite> SELECT first_name, MAX(balance) FROM users;
선영|990000
```

- users에서 계좌 잔액(balance)가 가장 높은 사람과 액수



```sqlite
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
153541.425120773
```

- 30세 이상의 계좌 잔액 평균



#### 3. LIKE

- 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환

![image](https://user-images.githubusercontent.com/52684457/66888614-40e3d600-f01a-11e9-9956-940acfa542d9.png)

- `2_3_%` / `2_%3_%` 의 조건은 다르다. 전자는 무조간 세번째가 3이지만 후자는 앞의 % 때문에 세번째가  3일지 아닐지 모른다. 
  *예시로 20035를 생각해보자.*

```sqlite
sqlite> SELECT * FROM users WHERE age LIKE '2%';
6|서준|이|26|충청북도|02-8601-7361|530
9|서현|김|23|제주특별자치도|016-6839-1106|43000
10|서윤|오|22|충청남도|011-9693-6452|49000
12|미정|류|22|충청남도|016-4336-8736|52000
15|지원|박|24|경상북도|02-3783-1183|35000
19|성민|김|26|충청남도|011-6897-4723|6100
23|서준|김|26|강원도|02-4610-2333|6900
25|유진|이|24|경기도|010-2349-9997|270000
31|시우|이|25|경상남도|02-6546-9558|460
...
995|승현|김|20|경기도|011-1954-7183|930
996|지연|이|29|경상남도|016-7945-6460|210
999|성호|최|28|충청북도|010-5772-9832|6700
```

- 20대의 사람만 뽑아오는 방법, 하지만 2살(한 자리 수)이 껴있다면 `2_%` 로 두 자리를 확실하게 해주는 것이 좋다.



```sqlite
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';
6|서준|이|26|충청북도|02-8601-7361|530
15|지원|박|24|경상북도|02-3783-1183|35000
23|서준|김|26|강원도|02-4610-2333|6900
31|시우|이|25|경상남도|02-6546-9558|460
34|영자|백|27|전라북도|02-3971-7686|630000
...
977|정남|박|17|충청남도|02-1230-2269|89000
981|광수|장|18|제주특별자치도|02-4566-1764|930000
987|준영|이|21|충청북도|02-2685-2468|200
```

- 02로 시작하는 사람들의 번호를 뽑는 방법
- `02%` 로 하게 되면 0234 와 같은 (그럴 일은 없지만 확실하게 해주기 위해) 숫자가 걸리므로 하이픈(`-`)을 입력한 후, `%`를 넣어준다. `02-` 뒤에는 아무 숫자가 와도 상관없기 때문



```sqlite
sqlite> SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';
서준|이
서준|김
민준|윤
예준|김
현준|최
서준|김
서준|김
현준|황
예준|박
예준|김
예준|김
현준|최
민준|박
현준|송
서준|이
서준|김
서준|김
현준|윤
민준|강
현준|유
서준|김
서준|김
민준|이
서준|박
민준|김
민준|이
예준|이
서준|김
현준|유
민준|한
민준|오
```

- users에서 first_name이 준으로 끝나는 사람의 first_name과 last_name



```sqlite
sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%';
240|현준|황|37|충청북도|011-5114-9343|220
```

- 전화번호 가운데가 5114인 사람, 양옆에 하이픈을 넣어주어야 번호의 가운데 숫자라는 것을 명확히 할 수 있다.



### ORDER

#### 1. 정렬(ORDER)

```sqlite
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
11|서영|김|15|제주특별자치도|016-3046-9822|640000
59|지후|엄|15|경상북도|02-6714-5416|16000
61|우진|고|15|경상북도|011-3124-1126|300
125|우진|한|15|강원도|011-8068-4814|3300
144|은영|이|15|전라남도|010-5284-4904|78000
196|지훈|김|15|전라북도|02-9385-7954|760
223|승현|장|15|충청북도|016-5731-8009|450
260|주원|김|15|전라남도|02-4240-8648|6300
294|은정|이|15|경상북도|010-6099-6176|5900
295|정수|강|15|충청북도|02-7245-5623|500
```

- user에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아내기
- `ORDER BY` : ~(특정 칼럼)의
- `ASC LIMIT` : `ASC`(오름차순)는 때에 따라 생략가능 `LIMIT` ~까지만 놔두고 자르기



```sqlite
sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;
295|정수|강|15|충청북도|02-7245-5623|500
61|우진|고|15|경상북도|011-3124-1126|300
998|시우|고|15|제주특별자치도|016-3732-8726|270
791|현숙|곽|15|충청남도|016-7423-1481|710000
11|서영|김|15|제주특별자치도|016-3046-9822|640000
196|지훈|김|15|전라북도|02-9385-7954|760
260|주원|김|15|전라남도|02-4240-8648|6300
315|예준|김|15|충청남도|02-9726-5034|76000
331|예준|김|15|충청북도|016-3898-3279|150000
359|서영|김|15|강원도|010-4016-6803|53000
```

- 나이 순, 성 순으로 오름차순 정렬로 상위 10개 뽑아내기



```sqlite
sqlite> SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
선영|김
상현|나
정호|이
상철|이
지아|최
준서|박
미영|문
하윤|고
은정|유
서윤|안
```

- 계좌잔액 순으로 내림차순 정렬하여 해당하는 사람이름 10개 뽑아내기

```sqlite
sqlite> SELECT * FROM users ORDER BY balance DESC LIMIT 10;
627|선영|김|37|전라북도|02-1610-2940|990000
124|상현|나|30|경상북도|010-4571-2869|99000
235|정호|이|20|전라북도|011-1193-3920|99000
259|상철|이|17|전라북도|011-3990-3978|99000
500|지아|최|16|전라북도|02-4150-9018|9900
768|준서|박|17|전라남도|010-9213-9802|9900
296|미영|문|31|전라남도|016-3620-8275|980000
327|하윤|고|32|제주특별자치도|02-7876-4073|980000
357|은정|유|17|강원도|016-8867-7897|980000
751|서윤|안|29|경상남도|011-2018-8263|980000
```

- `*`(전체)를 확인해보면 계좌 잔액이 내림차순 되는 것을 확인 가능
  여기서 계좌 내림차순이 이상한것을 확인이 가능한데,  `.schema users`( `.schema tablename` ) 스키마 조회로 `balance` 가 `INTEGER ` 이 아닌 `TEXT` 타입인 것을 확인이 가능
- `DESC` : 내림 차순





#### 2. 변경(ALTER)

```sqlite
sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL );
sqlite> .tables
articles    classmates  example     tests       users
sqlite> INSERT INTO articles VALUES ('1번 제목', '1번 내용');
sqlite> ALTER TABLE articles RENAME TO news;
sqlite> .tables
classmates  example     news        tests       users
sqlite> ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL;
Error: Cannot add a NOT NULL column with default value NULL
```

- `ALTER TABLE` 를 사용하여 테이블의 이름을 바꾼 뒤 확인 (articles **=>** new)
- 하지만 새로운 컬럼(`created_at`)을 `DATETIME` 으로 추가 하려하자 에러가 발생

- 기존 데이터에 NOT NULL 조건으로 인해 NULL 값으로 새로운 컬럼이 추가될 수 없으므로 DEFAULT값을 주거나, 기존의 NOT NULL값을 제거 해야 함



1. NOT NULL 값 제거

```sqlite
sqlite> ALTER TABLE news ADD COLUMN created_at DATETIME;
sqlite> INSERT INTO news VALUES ('title', 'content', datetime('now', 'localtime'));
sqlite> SELECT * FROM news;
1번 제목|1번 내용|
title|content|2019-10-16 14:11:38
```



2. DEFAULT 값 주기

```sqlite
sqlite> ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
sqlite> .mode column
sqlite> SELECT * FROM news;
title       content     created_at  subtitle
----------  ----------  ----------  ----------
1번 제목       1번 내용                   1
title       content     2019-10-16  1
```

