# :dog: Django : simple review

1. gitignore 생성 : `vscode` , `django`

   **=>** https://www.gitignore.io/

   

2. 환경 변수 만들기 `python -m venv venv` 
   *뒤의 venv는 환경 변수 이름*

   

3. vscode 에서 `F1` **=>** `Python : Select Interpreter` **=>** 자신이 만든 환경변수 선택

   

4. 터미널을 작동시키면 `source` 적용된 환경변수를 볼 수 있다.

   

5. `python pip list` : 현재 제대로 된 환경 변수에 위치하는지 확인, 
   `python -m pip install --upgrade pip  `이 뜨면 설치 진행을 해주어도 된다.

   

6. `pip install django` : django 설치

   

7. project 생성 : `django-admin startproject crud . ` 
   여기서 crud는 프로젝트 이름
   .은 현재위치에 프로젝트 생성

   

8. 프로젝트 파일의 `settings.py` 에서
    `LANGUAGE_CODE` 과 `TIME_ZONE` 설정을 한국으로 지정

   => `'ko-kr'` `'Asia/Seoul'`

   

9. `python manage.py runserver` : 서버 연결이 제대로 되는지 실행

   

10. `python manage.py startapp articles` : 새로운 app을 만든다.
    articles는 app이름

    

11. articles(app)에서 `templates` 폴더를 만들고 그 안에 articles폴더를 또 만든다.
    즉, app 폴더 안에, templates안에 app파일과 동일한 이름의 폴더
    여기서 hrml작업을 할 것

    

12. articles에서 urls/py를 따로 만들어준다. 

    - ```python
      from django.urls import path
      from . import views 
      
      urlpatterns = [
      ]
      ```

      

13. project의 `urls.py`에서 새로 만든 app을 path로 include 해준다. 

    - ```python
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('articles/', include('articles.urls')),
          path('admin/', admin.site.urls),
      ]
      ```

    

14. app파일에 있는 `models.py` 에서 class를 생성한다.
     `class Appname(models.Model):`  **=>** 이 때, class의 이름 앞자리는 대문자여야 한다.
    편의상 app이름으로 클래스를 설정해준다.

    

15. 클래스 안에 magic method인 `__str__`를 설정해주어야 값이 .............

    

16. .................. (수정중)







# :palm_tree: Branch

##### git 의 브랜치(branch)는 매우 가볍다.

**=>** branch (나뭇가지의 비유적 표현)

순식간에 브랜치를 만들고 브랜치 사이를 이동 할 수 있다.
git이 가지고온 혁신 중 하나는 브랜치 기능을 매우 쓸만한 수준까지 만들었다는 것이다.



rm -rf .git (부여된 git이 사라짐)



![](https://user-images.githubusercontent.com/52684457/64665775-b47c4b80-d48e-11e9-80d8-3866c2d13267.png)

![](https://user-images.githubusercontent.com/52684457/64665776-b514e200-d48e-11e9-92e8-48baf455db53.png)

![](https://user-images.githubusercontent.com/52684457/64665777-b514e200-d48e-11e9-9737-29d494c2e28e.png)

- commit을 합치려는 쪽에서 병합을 하기 때문에 보통 master에서 병합이 진행된다.





# :ballot_box_with_check: 상황

## 1.fast-forwark

![](https://user-images.githubusercontent.com/52684457/64674266-56aa2c80-d4ab-11e9-83a4-898e6e5fa090.png)

1. feature/test branch 이동

   ```bash
   $ git checkout -b feature/test
   $ (feature/test)
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch test.md
   $ git add .
   $ git commit -m "Complete test.md"
   ```

3. master 이동

   ```bash
   $ git checkout master
   $ (master)
   ```

4. master에 병합

   ```bash
   $ git merge feature/test
   ```

5. 결과

   - 단순히 HEAD 가 최신 COMMIT 으로 이동
   - feature/test branch 생성 이후 master branch 의 이력에 변화가 없었기 때문

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```

---

### 2. merge commit 

1. feature/login branch 이동

   ```bash
   $ git checkout -b feature/login 
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch login.md
   $ git add .
   $ git commit -m "complete login.md"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 생성

   ```bash
   $ touch master.md
   $ git add .
   $ git commit -m "fix master.md"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/login
   ```

6. 자동으로 merge commit 발생

   ```bash
   Merge branch 'feature/login'
   
   # Please enter a commit ...
   ...
   ```

   - Vim 에디터로 열림
   - 메세지를 수정하고자하면 `i` 로 편집 모드로 바꾼다음에 COMMIT 을 수정하고
   - `esc` + `:wq` 를 통해 저장 및 종료

7. commit 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   ```

   ```bash
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/login
   ```

---

### 3. merge conflict

1. feature/article branch 생성 및 이동

   ``` bash
   $ git checkout -b feature/article
   ```

2. 작업 완료 후  commit

   ```bash
   # 충돌을 만들어 낼 파일에 코드를 작성
   $ git add .
   $ git commit -m "fixed minor update"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 만들기

   ```bash
   # feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
   $ git add .
   $ git commit -m "fixed master update"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/article
   ```

6. merge confict 발생

   ```bash
   $ git merge feature/article
   Auto-merging a.txt
   CONFLICT ...
   Automatic merge faild; fix conflicts and then commit result.
   ```

7. 충돌 확인 및 해결

   ```bash
   # 충돌이 일어난 파일 열기
   # 그럼 아래와 같은 내용이 있다.
   
   <<<<<<<< HEAD
   master 에서 작성한 내용
   ========
   feature/article 에서 작성한 내용
   >>>>>>>> feature/article
   
   # 원하는 코드로 수정
   ```

8. merge commit 진행

   ```bash
   $ git add .
   $ git commit
   ```

   - commit 메세지는 미리 작성되어 있음

9. commit 그래프 확인

   ```bash
   $ git log --oneline --graph
   *   7238aa2 (HEAD -> master) Merge branch 'feature/article'
   |\
   | * 8e84920 (feature/article) fix a.txt
   * | 28faf63 fix a.txt in master
   |/
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

10. branch 삭제

    ```bash
    $ git branch -d feature/article
    ```

    

------

- 같은파일에 서로 다른 줄을 수정하면 충돌이 일어나지 않는다.



# :family_man_man_boy_boy: 협업하기 위해서는

### 1) feature branch workflow - 소규모

- pull request

![](https://user-images.githubusercontent.com/52684457/64674264-56119600-d4ab-11e9-91fe-5f175670d9c2.png)



### 2) forking workflow - 대규모, 오픈소스 기여

![](https://user-images.githubusercontent.com/52684457/64674265-56119600-d4ab-11e9-86cf-821a3bbe7e4c.png)

- git remote add upstream 중앙 원격 저장소 주소 (origin은 이미 있는 이름이므로 다른 이름으로)

- git checkout -b feature/login

- git push -u origin feature/login



> 중앙에서 병합을 했다면, 다른 팀원들은 master 브랜치를 pull 받아야 한다.
>
> 기능 개발을 끝내고 master에 바로 병합시키는게 아니라, 브랜치를 중앙 원격 저장소에 올리고(push) master에 병합을 요청(merge)



