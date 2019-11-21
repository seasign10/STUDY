- 중앙 주소 repository 생성

```bash
$ git init # init 부여
$ git remote add origin https://github.com/seasign10/teamplay.git # 중앙 주소
$ touch text.md # markdown 생성
$ git status # 수정사항 확인
$ git add . # 수정 적용
$ git commit -m "커밋 이름" # commit
$ git push -u origin master # push
```

- 기초 작업 



****



- 중앙 주소에서 포크를 가져온 후, 작업 할 때 

```bash
$ git clone 포크 주소
$ git remote -v #연결 확인
$ git remote add upstream 중앙 주소
```

- (origin은 fork에 연결되어있기때문에 중앙 주소(포크가아닌 원래 주소)에 연결하기 위한 이름으로 origin이 아닌 upstream을 사용



```bash
$ git branch 브랜치 이름 # 브랜치 만들기
$ git checkout 브랜치 이름 # 해당 브랜치로 이동
#######
$ git checkout -b 브랜치 이름 # 브랜치를 생성과 동시에 이동
$ git branch -d 브랜치 이름 # 삭제
```

- master가 아닌, branch로 작업을 해야 함.



- 브랜치를 push

```bash
$ git add .
$ git commit -m "커밋 이름"
$ git push origin 브랜치 이름
```

- 이 후, 해당 페이지로 들어가 알람을 확인 후, 보낼 메세지와 함께 push 보내기



****



- 중앙 주소 관리자는 repository에서 Pull request(pull 요청)을 수정 사항을 확인 후 (커밋 이름을 클릭하면 볼 수 있다.) 반영하고자 할 때 Merge를 하면 된다. merge 과정에서 commit 이름을 바꿀 수 있다.



- pull을 받기위해서는 organization repository 생성 후, 그곳에서

```bash
$ git remote add upstream 중앙 주소 # 중앙 주소에 연결
```



- master에서 다음 아래와 같이 pull을 받는다.

```bash
$ git pull upstream master
```









