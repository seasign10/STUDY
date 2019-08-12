# :card_file_box:  Algorithm : String

- A라는 글자를 글자 모양 그대로 미트맵으로 저장하는 방법을 사용하지 않는한(이 방법은 메모리 낭비가 심함) 각 문자에 대해서 대응되는 숫자를 사용
  - *ex) 000000 == 'a', 000001 == 'b'*

- 하지만 네트워크가 발전되기 전 각 지역별로 지정된 문자가 달라 해석이 달라지는 문제가생김
  - 혼동을 피하기 위해 표준안을 만들기로함 => <u>ASCII 코드</u>

```python
print(ord('A')) # ASCII 코드
print(chr(65))  # 알파벳

for i in range(65, 65+26):
    print(chr(i), end=' ')
```

- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII형식을 사용

- 인터넷이 미국에서 국한된것이 아닌 전 세계로 발전하면서 ASCII를 만들었을 때의 문제와 같은 문제가 발생

  - 자국의 코드체계를 타 국가가 가지고 있지 않으면 정보를 잘못 해석
  - 다국어 처리를 위해 표준을 마련 => <u>유니코드</u> 16진수

- 그러나 바이트 순서에 대해서 표준화하지 못함

  - (유니코드도 Character Set으로 구분된다 / Universal Character Set 2, Universal Character Set 4)

  - 파일을 인식 시 파일이 UCS-2, USC-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야하는 문제 발생 (인덱스의 방향이 서로 다른 것들을 구분 할 필요성 有)
  - 유니 코드의 적당한 외부 인코딩이 필요

![](https://user-images.githubusercontent.com/52684457/62843889-51b15c00-bcf8-11e9-8d00-ddb73f985e37.PNG)



### :unicorn:유니코드 인코딩

- ##### UTF-8 (in web)

  - MIN : 8bit, MAX : 32bit(1 Byte*4)

- ##### UTF-16 (in windows, java)

  - MIN : 16bit, MAX : 32bit(2 Byte*2)

- ##### UTF-32 (in unix)

  - MIN : 32bit, MAX : 32bit(4 Byte*1)

  

### :snake:파이썬 인코딩

- 2.x 버전 - ASCII => #-*- coding: utf-8 -\*-
- 3.x 버전 - 유니코드 UTF-8 => 생략가능
- 다른 인코딩 방식으로 처리 시 첫 줄에 작성하는 위 항목에 원하는 인코딩 방식을 지정해주면 됨



##### :ant:Python에서의 문자열 처리

- char 타입 없음
- 텍스트 데이터의 취급방법이 통일되어 있음

```python
arr = 'ABCDEFG'

# 인덱싱을 하나씩 읽을 수 있다.
for i in range(len(arr)):
    print(arr[i], end=' ')

# 리스트로 하나씩 쪼개서 넣기
mylist = list(arr)
print(mylist)
```

- 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용 가능
- 문자열 클래스에서 제공되는 메소드
  - replace(), split(), isalpha(), find()
- 문자열은 튜플과 같이 요소값을 변경 할 수 없음(immutable)



![](https://user-images.githubusercontent.com/52684457/62844399-11ec7380-bcfc-11e9-910b-a90b66a7a26e.PNG)



문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있음
- 자기 문자열을 이용할 경우는  swap을 위한 임시 변수가 필요하며 반복 수행을 문자열 길이의 반만을 수행해야 함

```python
arr = 'abcdefg'
print(arr[::-1])

arr = list(arr)
n = len(arr)
for i in range(n//2):
    # arr[i] <-> arr[n-1-i]
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
print(arr)
print(''.join(arr))
```

![](https://user-images.githubusercontent.com/52684457/62845744-84158600-bd05-11e9-9579-40e1507b08c8.png)

- 앞뒤로 같은 문자열이 읽히는 문자 - **회문**

  - *ex) 기러기, level . . .*

  ```python
  # 1.
  import sys
  sys.stdin = open("1989.txt", "r")
  
  tc = int(input())
  for k in range(1, tc + 1):
      arr = input()
      m = len(arr)
  
      for i in range(m//2):
          if arr[i] == arr[m-1-i]:
              result = '1'
          else:
              result = '0'
      # print(result)
      print('#{} {}'.format(k, result))
      
  # 2.
  T = int(input())
      for m in range(1, T+1):
          arr = list(map(str, input()))
          new_arr = [i for i in arr]
          for i in range(len(arr)//2):
              new_arr[len(arr)-1-i], new_arr[i] = arr[i], arr[len(arr)-1-i]
          if new_arr == arr:
              print('#{} 1'.format(m))
          else:
              print('#{} 0'.format(m))
  ```

  

```python
# 문자열 정렬 => 사전순 정렬 (길이와는 상관 x)
'aaa' == 'aab'  # False
'aaa' > 'aab'  # False
'aaa' < 'aab'  # True

# 문자열 수를 int로 바꾸는 방법
arr = '12345'
val = 0
for i in arr:
    val = val * 10 + int(i)
    
print(val)

# int(arr)도 가능
```

### :round_pushpin: 패턴 매칭

- 패턴 매칭에 사용되는 알고리즘들
  - 고지식한 패턴 검색 알고리즘
  - 카프-라빈 알고리즘
  - KMP 알고리즘
  - 보이어-무어 알고리즘

#### :black_flag: 고지식한 알고리즘(Brute Force)

![](https://user-images.githubusercontent.com/52684457/62847824-533c4d80-bd13-11e9-9666-f585cddee828.png)

```python
p = 'leehaein'
t = 'sfwehiuhdskjleehaeindsfheuk'

n, m = len(t), len(p)   # n: 텍스트의 길이, m: 패턴의 길이

# 텍스트에서 패턴이 있을 수 있는 모든 시작위치
for i in range(n - m + 1):
    j = 0
    while j < m:
        if t[i + j] != p[j]:
            break
        j += 1
    if j == m:
        print(t[i:i + m])
# ---------------------------------------
n, m = len(t), len(p) 

i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j + 1
        j = -1
        
    i, j = i + 1, j + 1
    if j == m:
        print(t[i - j:])
        break
```



#### :black_flag: KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로. 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화 함
  - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
- **시간복잡도** : O(M+N)

> *예제)*
>
> 'abcd', 길이=4
>
> | 접두어 |  길이  | 접미어 |
> | ------ | :----: | -----: |
> | a      | 길이=1 |      d |
> | ab     | 길이=2 |     cd |
> | abc    | 길이=3 |    bcd |
> | abcd   | 길이=4 |   abcd |

![](https://user-images.githubusercontent.com/52684457/62848507-fb9fe100-bd16-11e9-9417-8a5c1ba3a02f.png)

![](https://user-images.githubusercontent.com/52684457/62848374-571d9f00-bd16-11e9-95cb-8cd97e7567cb.PNG)

![](https://user-images.githubusercontent.com/52684457/62848517-065a7600-bd17-11e9-8c30-e7867d90e695.png)

#### :black_flag: 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 보이어-무어 알고리즘은 패턴에 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼이 된다.

![](https://user-images.githubusercontent.com/52684457/62848683-9b5d6f00-bd17-11e9-96bb-4b14abf0f702.png)

![image](https://user-images.githubusercontent.com/52684457/62848705-b29c5c80-bd17-11e9-8aaa-ba68c140158d.png)

![](https://user-images.githubusercontent.com/52684457/62848786-fd1dd900-bd17-11e9-8b04-22ebe9165dbd.png)



![](https://user-images.githubusercontent.com/52684457/62848842-2d657780-bd18-11e9-93fd-547d11d1f364.png)



------



```python
# 재귀 함수 - 자기 자신을 호출하는 함수
# 재귀 호출 ---> 재귀적 정의(점화식) 구현하기에서 많이 쓰임
# 그래프의 깊이 우선 탐색, 백 트래킹
# for, while 사용하지 않고 반복적 작업을 할 수 있다.

def printHello():

    print('Hello!!!')
    printHello()
# 무한루프에 빠지게 된다.

def printHello():
    if i < 3: # 조건을 넣어서 돌아가게끔 한다.
        print('Hello!!!')
        printHello()
        
def printHello():
    if i == 3:
        print(----------)
    else:
        print('Hello!!!')
        printHello()
        
#---------------------------
printHello()

# 위와 비슷한 패턴
for i in range(3):
    print('Hello!!!')
#---------------------------
        
def printHello():
    if i == 3:
        print(----------)
    
    else:
        print('Hello!!!')
        printHello(i + 1) # 0~3까지 갔다가 3, 2, 1, 0으로 되돌아온다.

def printHello(i, n):
    if i == n:
        print(----------)
        return 
    
    else:
        print('Hello!!!')
        printHello(i + 1, n)
        
def printHello(i, n):
    if i == n:
        print(----------)
        return 
    
    else:
        print(i, '> Hello!!!')
        printHello(i + 1, n)
        
        

#---------------------------
cnt = 0
def printHello(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
    printHello(i + 1, n)
    printHello(i + 1, n)
    #printHello(0, 3)
    #print(cnt)
    #도출값 8
    
    #왜 8이 나올까?
```



