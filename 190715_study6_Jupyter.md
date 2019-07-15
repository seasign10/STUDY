```python
jupyter - install

$ pip install jupyterlab
$ python -m notebook
$ git pull => 강사님이 올린 자료 받기
```

![capture55](https://user-images.githubusercontent.com/52684457/61192026-15381380-a6ec-11e9-85c8-5152c35e30bb.PNG)

##### ~/을 넣지 않으면 그게 깔린 파일에서만 명령어가 적용 됨

**환경 변수파일**을 만들었기 때문에  **source**를 해줘야 함.
=> 배쉬rc에서 쥬피터를 일일히 명령어를 길게 치는 불편함(jupyter notebook)을 줄이기 위해 jp라는 단축기를 만들어 줌





> ###### edit mode(초록색) 쉬프트 엔터하면 커맨드 모드가 됨
>
> - ctrl + enter = 현재 셀 실행
> - shift + enter = 실행 + 다음 셀 선택 ( 다음 셀이 없으면 새로운 셀 생성) -> 셀이 적용됨
> - alt + enter = 실행 + 다음 셀 생성

> ###### command(파란색) 더블클릭하면 에딧모드가 됨 => h를 누르면 단축키 목록이 뜸
>
> - 잘못된 셀을 생성 할 시 esc를 눌러 에딧모드를 나와 d 더블 클릭하면 삭제가 된다.
> - 커맨드 모드 상태로 z를 누르면 실수로 셀을 지우는 명령이 취소가 된다.
> - a를 누르면 위에 셀이 생기고 b를 누르면 아래로 셀이 쭉쭉 생긴다.
> - shift 누른상태로 다중 셀 선택을 하고 dd(d 더블 클릭)를 누르면 선택된 셀이 삭제 됨.
> - ctrl + s 저장
> - m 기본값이 파이썬으로 되어있는 셀을 마크다운으로 바꿔줌.





![](https://user-images.githubusercontent.com/52684457/61192027-15381380-a6ec-11e9-942f-129a852fdcaa.png)

- 쥬피터가 무한 루프에 빠질 시 (ex.while 명령문) restart & clear를 해준다.

- 그리고 지저분한 프린터 값 등을 지울 때에도 유용 하다.



> ###### programing font
>
> 고정폭이 프로그래밍 프로그램 끼리 같음, 반드시 있어야 함.
>
> 
>
> Hello world? 1lI| 0Oo
>
> ```font
> Hello world? 1lI| 0Oo (원래 숫자 0에는 안에 점이 찍혀 있음.)
> ```
>
> L 과 I 등 구분을 위해 폰트의 가독성과 명확한 구분이 좋아야 함
>
> 그리스어 물음표(;)와 세미콜론(;)은 모양이 같아서 구분이 어려움



> ###### 프로그래밍 폰트 다운 받는 곳
>
> FIRA CODE / hack font 서치 하면 됨
>
> HACK CODE
>
> Source CODE Pro



- ###### Hack Code Font 설치 방법

![](https://user-images.githubusercontent.com/52684457/61192029-15381380-a6ec-11e9-8eaf-5c8624622abe.PNG)

![](https://user-images.githubusercontent.com/52684457/61192028-15381380-a6ec-11e9-88d5-eb845b81482b.PNG)

컴퓨터를 재 부팅을 한 후

![](https://user-images.githubusercontent.com/52684457/61192174-6bf21d00-a6ed-11e9-9b45-7722d3f72152.PNG)

=> 쥬피터를 확인하면 적용 되어 있다. (고정폭 글꼴 = 프로그래밍 글꼴)

![](https://user-images.githubusercontent.com/52684457/61192258-0eaa9b80-a6ee-11e9-8334-cc280326fd4f.PNG)

=>vs에 적용 하는 방법 (Hack 폰트는 Hack, 만 추가 하면 된다. 추가해야될 적용 문구는 각 폰트 사이트 마다 다르다. 앞 문구가 가장 첫번째로 로딩이 되고 로딩이 되지않으면 그 다음 폰트로 로딩이 된다.)



##### 파이썬 PEP8 스타일 가이드

구글링 하면 한글 자료도 많이 있음. 



>###### [jupyter extension](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) 구글링하면 깃허브가 뜸
>
>###### bash에
>
>- ```
>  pip install jupyter_contrib_nbextensions
>  ```
>
>- ```
>  jupyter contrib nbextension install --user
>  ```
>
>  이 둘을 설치 한 후 쥬피터를 실행,
>
>![1563160098053](https://user-images.githubusercontent.com/52684457/61194128-8c74a400-a6fa-11e9-8671-db604879e88b.PNG)
>
>위와 같이 설정하면 쥬피터 파일 왼쪽에 목록이 생긴다.

그리고 쥬피터를 저장 할 때마다 저장 데이터가 쌓이는데, 지저분하지 않게 gitignore.io 에서 쥬피터 노트북을 검색 해서 .gitignore 생성 해준다. 이미 .gitignore에 쥬피터가 기입되어있으면 중복해서 쓰지 않도록 조심하자.



### 오늘의 배운 것들은 jupyter notebook으로 마저 확인 하자!