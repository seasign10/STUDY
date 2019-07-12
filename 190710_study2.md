[TOC]







> ### 이스케이프 문자열
>
> #\n : 개행문자(다음 줄 이동)
> #\t : 탭문자(Tap)
> #\\ : 백슬래쉬를 사용하기 위해 (출력 : \ )
> #\' : 따옴표
> #\" : 쌍따옴표



## 텍스트 읽고 쓰기

**w**는 전체 덮어쓰기 **a**는 추가하기 **r**은 프로그램이 문자배열 등을 수정을 가능케하기 위한 읽기작업이 필요하다. (print와 다른 의미)

```python
# 1. 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할때 r: 읽기 / w: 쓰기(+덮어씌워짐) / a: 추가
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
        # n은 enter의 약자
f.close()
# with 구문 (context manager)
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

# writelines() : list를 넣어주면, 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt', 'w') as f:
    # w는 덮어 씌우기의 의미여서 그대로 적용 시켜도 됨
    f.writelines(['0\n', '1\n', '2\n', '3\n'])
    #writelines를 읽을 때 하나 밖에 읽지 못하기 때문에 여러 list를 [](대괄호)로 묶어 주어야 읽을 수 있다.
    #\n을 사용 함으로써 붙어있는 숫자들을 아래로 나열 할 수 있다.

    
```



```python
# read() : 개행문자를 포함한 하나의 문자열 (통째로 읽어옴 : 단점 - 수정이 힘듦)
with open('with_ssafy.txt', 'r') as f:
    # 박스에 담기
   all_text = f.read()
   print(all_text)

    
# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄 (read()의 단점 보완)
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        #.strip을 사용함으로서 이스케이프 문자열이나, \n을 가진것을 없애줌으로 문자열의 간격을 줄여줌 ->(\n)x2를 (\n)x1로 변환시켜줌\
        # rstrip, lstrip, .strip 3가지가 있으나 여기서는 간단히 .strip으로 해결해 줌.

```



![](https://user-images.githubusercontent.com/52684457/61099965-37892180-a49f-11e9-9ad2-bbcc774f4c69.png)

Python String To List => 구글링하면 코드 값 찾는데에 도움을 줌



> #### BeautifulSoup 을 병합한 응용 문제
>
> ```python
> import requests
> from bs4 import BeautifulSoup
> 
> url = 'https://www.naver.com/'
> 
> # 1. 요청 보내서 html 파일 받고
> 
> html = requests.get(url).text
> 
> # 2. 뷰숲으로 정체
> 
> soup = BeautifulSoup(html, 'html.parser')
> 
> # 3. select 메서드로 사용해서 list 를 얻어낸다
> 
> rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a .ah_k')
> for i in rank:
>     print(i.text)
> # 4. 뽑은 list를 with 구문으로 잘 작성해보자.(txt)
> 
> with open('naver_rank.txt', 'w') as f:
>     for i in rank:
>         f.write(f'{i.text}\n')
>        
> 
> # 3-1) # slect 메서드로 사용해서 list 를 얻어낸다 - (순위 + 검색어.ver)
> 
> searchings = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')
> 
> 
> # 4-1) 뽑은 list 를 with 구문으로 잘 작성해보자.(txt) - (순위 + 검색어.ver)
> with open('naver_search.txt', 'w', encoding='utf-8') as f:
>     for searching in searchings:
>         rank = searching.select_one('span.ah_r').text
>         keyword = searching.select_one('span.ah_k').text
>         f.write(f'{rank}위: {keyword}\n')
> 
> ```
>
> ![](C:\Users\student\Desktop\study_files\capture\capture18.PNG)



### 응용 문제

### 

```python
'''
문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오
'''
#str-string 문자열
str = input('문자를 입력해주세요.')

# 아래에 코드를 작성해 주세요.

print(f'첫 글자는 {str[0]}, 마지막 글자 {str[-1]}.')


```



```python
'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.

#int('100') => 100

for i in range(numbers):
    print(i+1)
```



```python
'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.

#if 2로 나눈 나머지가 있으면:
if number % 2 == 0:
# ==0은 굳이 필요 없음 -> why? : 어차피 나누면 1이거나 0이기 떄문에 / 2로 나누면 남은 게 없다는 뜻의 조건식
    print('짝수입니다.')
else:
    print('홀수입니다.')
#    True(1,2...) / False(0)


#2로 나누면 남은 게 1이라는 뜻
#보통 true는 1이나 2,3 등 다른 값, false는 0을 인식하므로 그걸 이용해서 식을 짤 수 있음
if number % 2:
    print('홀수입니다.')
else:
    print('짝수입니다.')
 
```



```python
'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

# 아래에 코드를 작성해 주세요.

#각각 True, False를 낼 때. 하지만 윗 문제는 한 과목이라도 라는 조건이 명시 되어 있음.

# if a >= 90:
#     print('True')
# else:
#     print('False')

# if b > 80:
#     print('True')
# else:
#     print('False')

# if c > 85:
#     print('True')
# else:
#     print('False')

# if d >= 80:
#     print('True')
# else:
#     print('False')


if a >= 90 and b > 80 and c > 85 and d > 80:
    print(True)
else:
    print(False)
```



```python
'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요.
# 문자열 => 리스트로 형변환을 하는게 포인트.

print(prices)
prices.split(';')

# # .split() 리스트 안에 기준을 세워 줄 수 있음. (ex) A = [1;2;3] print(A) -> 1 2 3 / A.split(';') -> 1, 2, 3 즉 ('')안의 문자를 기준으로 쪼개는 것 


# '9' '100' '20' => 100 20 9

makes = prices.split(';')

boxes = []
for make in makes:
    boxes.append(int(make))
# 리스트에 요소를 추가하는 메서드 .append()
# list.append(1) 리스트에 1을 추가한다.
print(boxes)
boxes.sort(reverse=True)
# .sort는 오름차순 (낮은 수 부터) 내림차순 하려면 reverse를 해야함
for box in boxes:
    print(box)
```





## HTML / CSS

**html** - 페이지 내에서 우클릭 - 페이지 소스보기 하면 보이는 코드들

**css** - html을 꾸며주는 요소

![](https://user-images.githubusercontent.com/52684457/60948828-caef1500-a32e-11e9-99c4-e20f56934521.png)



**\<head>, \<p>**는 자동 enter가 됨

**\<ol>** odered list 숫자, 알파벳 등 순서가 있는 목록을 만드는데 사용

**\<ul>** unordered list  순서가 필요 없는 목록을 만드는데 사용

**\<li>** list item ol과 ul의 각 항목들을 나열 할 때에 사용하는 태그

**\<h1>** 글씨 크기

**\<body>** 에서 보통 문서를 작성 함

**\<br>** 엔터



**! 입력 후, Tap을 누르면 자동 완성 된다.** =>  INDEX.HTML

![](https://user-images.githubusercontent.com/52684457/61018804-00e5d500-a3d3-11e9-8e5a-2d7bd0687f0d.PNG)

DOCTYPE html => 이것은 html의 문서다

html은  **''대신 ""사용**

lang 은 language의 약자. en => ko 하면 언어설정을 한국어로 할 수 있다.





> #### 이제 자신만의 홈페이지를 만들어 보자
>
> 기본적으로 github에서는 사용자당 하나씩 Free로 주소를 제공해준다.
>
> **새로운 Repositories**를 만들어 이름을 [사용자_이름.github.io]로 기입한다.
>
> ![](https://user-images.githubusercontent.com/52684457/60960036-3becf780-a344-11e9-9aae-75630638e27e.PNG)
>
> *(나중에 프로파일에 추가해주면 좋다.)*
>
> **탬플릿을 꾸미기는데 도움되는 사이트**
>
> https://startbootstrap.com/
>
> ![](https://user-images.githubusercontent.com/52684457/60956636-2b398300-a33e-11e9-9c75-c4ec1a86c0e2.PNG)
>
> 무료 탬플릿 사이트에 들어가서 마음에드는 디자인을 다운받아준다 -> 압축 형식
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/60960037-3c858e00-a344-11e9-871d-88f0392227dd.PNG)
>
> 'index'라는 폴더를 우클릭해서 Visual Studio Code를 실행시켜준다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/60960040-3d1e2480-a344-11e9-86b4-2cb31fae3607.PNG)
>
> Ctrl + F 키로 키워드를 검색하다보면 특정 키워드를 바꿀 수 있는 값을 찾을 수 있다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/60960042-3e4f5180-a344-11e9-98d4-d7e79451479d.PNG)
>
> 프로필 사진도 바꿀 수 있다.
>
> *여기서 Vsc를 저장해주면 'index'라는 파일을 새로고침 할 때 마다 어떻게 바뀌었는지 알 수 있지만 실제 홈페이지에서는 바로 적용 되지 않는다.
>
>  => git bash로 [사용자_이름.github.io]로 만들어둔 레지토리에 연결(git init, remote)을 시켜 git push작업을 한다.
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/60960041-3db6bb00-a344-11e9-8bdd-f6d5b4389698.PNG)
>
> 그럼 'index'에 적용되었던 탬플릿들이 실제 주소에도 적용된 모습을 볼 수 있다.
>
> (개인에 따라 주소가 받아지는 속도, 탬플릿이 적용되는 시간 등은 차이가 날 수 있다.)



