

# :card_file_box:  Algorithm

`Python` 은 인터프리터가 내장되어있어 간편한 코딩을 도와주지만 실행이 느림

### 추상 자료형 (Abstract Data Type)

> - List(배열)
>
> - Stack
>
> - Queue
>
> - Tree
>
> - Graph . . .
>
> => 특정 언어나 특정 환경 특정 운영체제에 종속되어 있는것이 아닌 추상적인 개념. 
>
> 이 5가지를 배울 것.



> #### 문제 풀때 라이브러리 사용하지 않는다.
>
> List 사용할 때 max(), min(), indexof(), sort()...사용하지 말 것
>
> 내장함수 최대한 자제할 것



#### 코딩할 때 쓰는 언어적 표현 (중요!)

- for, while(반복), if-else(분기)
- 수식(연산자)



## :closed_lock_with_key:배열(Array) 1

:bookmark: (명) **알고리즘** : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다.
                         주로 컴퓨터용어로 쓰이며, **컴퓨터가 어떤 일을 수행하기 위한 단계적 방법.**

간단하게 다시 말하면 **어떠한 문제를 해결하기 위한 절차**라고 볼 수 있다.

![](https://user-images.githubusercontent.com/52684457/62018320-307b4680-b1f5-11e9-8606-cadfa75e0dd8.JPG)

##### APS 과정의 목표중의 하나는 보다 좋은 알고리즘을 이해하고 활용하는 것이다.

> #### 무엇이 좋은 알고리즘인가?
>
> - 정확성 : 얼마나 정확하게 동작
> - **작업량** : 얼마나 적은 연산으로 원하는 값
> - **메모리** : 얼마나 적은 메모리를 사용
> - 단순성 : 얼마나 단순
> - 최적성 : 더 이상 개선할 여지없이 최적화되었는가.



> #### 알고리즘의 성능은 무엇으로 측적하는가
>
> **주어진 문제를 해결하기 위해 여러 개의 다양한 알고리즘이 가능**
> **=>** 어떤 알고리즘을 사용해야 하는가?
>
> **알고지름의 성능 분석 필요**
>
> - 많은 문제에서 성능 분석의 기준으로 알고리즘의 작업량을 비교한다.

*(ex)*

![](https://user-images.githubusercontent.com/52684457/62018599-489f9580-b1f6-11e9-9cd6-22a1bf7041c4.png)

처리를 해야할 자료의 갯수가 커지거나 문제의 크기가 커짐에 따라 작업, 계산 양이 많아질 수 밖에 없다.

=> 자료 처리에 대한 시간 - 시간 복잡도



------



알고리즘의 작업량을 표현할 때 시간복잡도로 표현한다.

#### 시간 복잡도(Time Complexity)

- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산

![](https://user-images.githubusercontent.com/52684457/62018722-da0f0780-b1f6-11e9-82e8-f7a82d96696b.png)

시간도가 높다 => 걸리는 시간이 길다. / 알고리즘2는 명령문으로만 보면 실상 1번의 계산만 하는 꼴.

> 단순 비교를 하기에는 하드웨어 소프트웨어 운영체제의 환경에따라 측정은 바뀐다. (변수가 많아서 단순비교가 어려움.) 알고리즘의 실행시간을 표현하기 위해서 논리적인 계산을 하는 것.



**가장 차수가 높은 항**을보고 시간 증가율을 알 수 있다. 
**=>** for문이 2~3 중첩해서 돌아가면 2차항 3차항으로 증가하게 된다. 그중에 차수가 가장 높은 것이 중요.



#### 시간 복잡도 ≒ 빅-오(O) 표기법

- **빅-오 표기법(Big-Oh Notation)**
- 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 계수(Coefficient)는 생략하여 표시

예를 들어

![](https://user-images.githubusercontent.com/52684457/62019540-51926600-b1fa-11e9-9e4c-4dc42ee3ba0a.png)

n개의 데이터를 입력 받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에 출력하는 알고리즘의 시간복잡도는 어떻게 되나?

-O(n)\

###### 위의 O(1)은 n의 수가 어떻든간에 일정하다는 뜻을 가지고 있다.





>- 빅 오 - O 최악의 경우 O() - 키 값이 없을 때. n번만큼 해야함
>- 오메가 - Ω 최선의 경우 omega() - 초반에 키값을 바로 찾았을 때. 
>- 씨타 - θ cita()
>
>*()안에 최고차항을 넣고 비교*
>
>빅 오와 씨타는 같다고 생각해도 됨. (*사용 빈도수 : 빅오가 가장 多* )



![](https://user-images.githubusercontent.com/52684457/62022085-7dffaf80-b205-11e9-91cf-e5bf0bcee933.png)



![](https://user-images.githubusercontent.com/52684457/62022668-4cd4ae80-b208-11e9-9e64-95201fe22179.png)





## :bookmark_tabs: 배열이란 무엇인가 (list)

- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- 아래의 예는 6개 변수를 사용해야 하는 경우, 이를 배열로 바꾸어 사용하는 것.

![](https://user-images.githubusercontent.com/52684457/62022697-7392e500-b208-11e9-9ee9-b02311ca7b84.png)



**배열의 필요성**

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.
- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

**=>** **배열을 조작**한다는 것은 결국 **필수적으로 반복문**이 들어가는 것.





![](https://user-images.githubusercontent.com/52684457/62023547-5b24c980-b20c-11e9-9890-fd99765479ee.png)

이미 사용되고 있는 것은 다른 프로그램이 건들지못한다. 이것을 관리하는 것이 운영체제.





## :book: 대표적인 정렬 방식의 종류

- 버블 정렬 (Bubble Sort)
- 카운팅 정렬 (Counting Sort)
- 선택 정렬 (Select Sort)
- 퀵 정렬 (Quick Sort)
- 삽입 정렬 (Insert Sort)
- 병합 정렬 (Merge Sort)



#### :blue_book: 버블 정렬(Bubble Sort)

**인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식**



> ###### 정렬 과정 
>
> - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
>
> - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
>
> - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블정렬이라고 한다.
>
>   
>
> - **시간 복잡도** 
>   - O(n^2)

###### 

![](https://user-images.githubusercontent.com/52684457/62023548-5b24c980-b20c-11e9-848c-f88f2550265f.png)

![](https://user-images.githubusercontent.com/52684457/62023559-637d0480-b20c-11e9-9e11-1f666ba01b44.png)

![](https://user-images.githubusercontent.com/52684457/62023574-71328a00-b20c-11e9-8d65-b48d55d728ca.png)

![](https://user-images.githubusercontent.com/52684457/62023581-78599800-b20c-11e9-9de1-5ce3aff8c599.png)

<u>네 번째 패스에서 정렬이 끝</u>나는 것을 알 수있다.



------



 아래는 앞서 살펴 본 배열을 활용한 **버블정렬을 코드로 구현**한 것

![](https://user-images.githubusercontent.com/52684457/62024137-cec7d600-b20e-11e9-93fe-81ffaba49456.png)

```python
arr = 
n = len(arr)
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i + 1]
        
     
for i in range(n - 2):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i +1], arr[i + 1]
    .
    .
    .
```

위의 코드를 이용하면 아래의 코드로 축약 할 수 있다.

```python
def BublleSort(a): # 정렬할 list
    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```



------



#### :blue_book: 선택 정렬(Select Sort)

```python
arr = [55, 7, 78, 12, 42]
""" 선택정렬(Select Sort) 순서
55를 가장 먼저보고 여태 본 수 중에서 가장 작은값으로 설정 됨
-> 다음 수(7)를 보고 더 작은 수로 적용. 나머지는 제외
-> 그 이후 똑같이 더 큰 수는 제외하고 적은 수를 남기며 적용

현재 범위에서 제일 작은 값을 찾으면 앞의 값과 자리를 교환하는 것.
"""
# 1
MIN = arr[0] # 가장 첫 번째로 본 수
for i in range(1, len(arr)):
    if arr[i] < MIN: 
        MIN = arr[i] # 작은 값은 알아내었으나 위치(index)를 알아야 함. => 인덱스 저장 필요
        

# 2
MIN = 0 # 0번 위치에 제일 작은 값을 가져 오기
for i in range(1, len(arr)):
    if arr[i] < arr[MIN]: 
        MIN = i
arr[0], arr[MIN] = arr[MIN], arr[0] # 서로 위치를 바꿔준다.
print(arr)



# 3
MIN = 1
# 시작한 위치만 바뀔 뿐, 1번째 인덱스에 2번째 인덱스의 숫자를 가져옴. (더 작은 경우 가져온다.)
for i in range(MIN + 1, len(arr)):
    if arr[i] < arr[MIN]: 
        MIN = i
arr[i], arr[MIN] = arr[MIN], arr[i]
        
        
        
# 4 최종 형태
for j in range(len(arr) - 1):
    MIN = j # 처음의 제일 작은 값을 j로 지정
    
    for i in range(j + 1, len(arr)):
        if arr[i] < arr[MIN]: 
            MIN = i
            
    arr[j], arr[MIN] = arr[MIN], arr[j]
```





#### :blue_book: 카운팅 정렬(Counting Sort)

- 항목들의 **순서를 결정하기 위해** 집합에 **각 항목**이 몇 개씩 있는지 세는 작업을 하여, **선형 시간에 정렬하는 효율적**인 알고리즘 / 순차적이어서 효율적이나 아무 상황에서 쓸 수 있지 않다. (**제한적**)
- 제한사항
  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
- 시간 복잡도
  - O(n+k) : n은 리스트 길이, k는 정수의 최대값



![](https://user-images.githubusercontent.com/52684457/62025475-397b1080-b213-11e9-8f55-59018578b651.png)

1단계에서 0개수 / 1개수 / 2개수 / 3개수 / 4개수 => 1, 3, 1, 1, 2

![](https://user-images.githubusercontent.com/52684457/62025486-426be200-b213-11e9-9fad-0b782ac1ed7e.png)

count의

인덱스 0과 1을 더하면 4

인덱스 1과 2를 더하면 5 

인덱스 2와 3을 더하면 6 . . .

1, 4, 5, 6, 8 이 나온다. => 인덱스 값

![](![8](https://user-images.githubusercontent.com/52684457/62026740-d1c6c480-b216-11e9-83b4-10411f67e8e4.png)

n-1 부터 n-1만큼 역순으로 카운트를 감소시키며 반복하면. . .

![](https://user-images.githubusercontent.com/52684457/62026782-ea36df00-b216-11e9-9fbc-80125be2e30d.png)

카운트가 각 자신의 갯수만큼 소모 된 것을 알 수 있다.

```python
data = [0, 4, 1, 3, 1, 2, 4, 1]

# 1 count 하기
counts = [0] * 5 # 최대값 = 4 / 인덱스 0부터 4까지 (최대 숫자가 리스트안에 4이기 때문.)
for val in data:
    counts[val] += 1
    
print(counts) # [1, 3, 1, 1, 2]

# 2 바로 정렬
sorted = []
for i in range(len(counts)): # 카운트로 하나씩 읽어 오는 것
    for j in range(counts[i]):
        sorted.append(i)
        
print(sorted) # [0, 1, 1, 1, 2, 3, 3, 4]


# 3
for val in data:
    counts[val] += 1
    
for i in range(1, len(counts)):
    counts[i] = counts(i-1) + counts[i]
    
```

![](https://user-images.githubusercontent.com/52684457/62025960-962afb00-b214-11e9-8a59-1aefee011cbd.png)

첫 번째 for문은 n번 돌고 두번째 for문은 k번 마지막 for문도 n번



###### 아래 연습문제 #3에서의 베이비진에서 count를 풀어 쓴 식이 있음.



------



#### :green_book: <연습 문제 # 1> : 낙차 구하기

![](https://user-images.githubusercontent.com/52684457/62027023-9aa4e300-b217-11e9-92e5-da81cf5cd291.png)

```python
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# a만 계산하면 된다. 결국 제일 끝에있는 a가 낙폭이 가장 크거나 같기 때문. (낙폭이 큰 것을 위주로 계산 하면 됨.) 자기 밑의 상자가 몇 개 깔려있냐가 중요한데 높이(7)가 같거나 큰게 몇 개가 있는지 찾으면 됨.
```



#### :green_book: <연습 문제 # 2> : baby - gin game

![](https://user-images.githubusercontent.com/52684457/62028156-8f06eb80-b21a-11e9-82f7-54feb1fb2edc.png)

![](https://user-images.githubusercontent.com/52684457/62028168-962df980-b21a-11e9-8288-2b5364b3d935.png)



**모든 경우의 수**를 순차적으로 탐색해야 하기 때문에 **완전 검색**이 **필요**하다.

하나의 경우의 수라도 조건에 적합 할 수 있기 때문. (다 따져보고 계산 해봐야 한다.)

[결정 문제]





> ###### tip)
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/62028131-80203900-b21a-11e9-9cd1-c1e5b5cbc385.png)
>
> <u>결정 문제, 최적화 문제</u> => 경로를 다 조사 해봐야 (모든 경우의 수를 다 조합해 봐야) 함 - 완전 검색





![](https://user-images.githubusercontent.com/52684457/62029164-ead27400-b21c-11e9-92de-3741edcc3b8d.png)



```python
data = 'ABC' # 3자리의 수 경우의수 => 3! 

n = len(data)
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(data[i], data[j], data[k])
            # 중복 경우의 수가 나옴 =>3! 이아닌  3 x 3 x 3
           
# 그렇다면?
n = len(data)
for i in range(n):
    for j in range(n):
        if i == j: continue
            for k in range(n):
                if i == k or j == k: continue
                    print(data[i], data[j], data[k])
                    # for문을 여러번 사용하는 대신 재귀 호출 부르는 방법도 있음.
```



![](https://user-images.githubusercontent.com/52684457/62093154-24ee5500-b2b3-11e9-8d12-2d97256d86f5.png)

```python
'''
위의 
for i in range(6):
    c[num % 10] += 1
    num //=10
에서 range(6)이 붙은 이유는 자릿수가 6자릿 수인것을 이미 알기 때문.
'''

num = 123456

arr = []
# %, /

# 몇 자리인지 길이를 모를 때 num > 0
while num > 0:
    arr.append(num % 10)
    num //=  10 # 10을 나눈 몫을 저장

print(arr)
```





#### :green_book: <연습 문제 # 3> : 건물 조망권 확보하기 위한 세대 구하기

[https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8otLKmRQDFAUD&contestProbId=AV134DPqAA8CFAYh&probBoxId=AWw8otLKmRUDFAUD+&type=PROBLEM&problemBoxTitle=01.List%287%EC%9B%9429%EC%9D%BC%29&problemBoxCnt=++1+](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8otLKmRQDFAUD&contestProbId=AV134DPqAA8CFAYh&probBoxId=AWw8otLKmRUDFAUD+&type=PROBLEM&problemBoxTitle=01.List(7월29일)&problemBoxCnt=++1+)

```python
for n in range(10):
    N = int(input())
    num = list(map(int, input.split())) # input된 숫자를 공백()기준으로 나눠서 list
    
    result = 0
    for i in range(2, N-2): # (2, N-2) => 양 옆의 2칸은 사용하지 못함.
        MAX = max(num[i - 2], num[i - 1], num[i + 1], num[i + 2])
        if MAX < num[i]: # 만약 두번째로 채택할 빌딩이 가장 큰 빌딩보다 작다면...
            result += num[i] - MAX
            # 가장 높은 빌딩과 두번째로 높은 빌딩의 차이를 구해 전망권이 확보되는 곳을 구함
            
    print('#{} {}'.format(n+1,result))
```



#### :green_book: <연습 문제 # 4> : 덤프 최소 차 구하기

[https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8otLKmRQDFAUD&contestProbId=AV139KOaABgCFAYh&probBoxId=AWxAewhK4FQDFAUD&type=PROBLEM&problemBoxTitle=01.List%287%EC%9B%9430%EC%9D%BC%29&problemBoxCnt=1](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8otLKmRQDFAUD&contestProbId=AV139KOaABgCFAYh&probBoxId=AWxAewhK4FQDFAUD&type=PROBLEM&problemBoxTitle=01.List(7월30일)&problemBoxCnt=1)

가장 낮은 상자는 0에서부터 세었을 때 0이아닌 가장 작은수,
가장 높은 상자는 10에서 부터 내려갔을 때 0 이아닌 가장 큰 수로 계산

```python
for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    cnt = [0] * 101 # 빈도수 저장하는 List
    for val in arr:
        cnt[val] += 1
        
        minIdx, maxIdx = 0, 100
        i = 0
        while i < dump:
            while cnt[minIdx] == 0:
                minIdx += 1
            while cnt[maxIdx] == 0:
                maxIdx -= 1
                
            cnt[minIdx] -= 1
            cnt[minIdx + 1] += 1
            cnt[maxIdx] -= 1
            cnt[maxIdx - 1] += 1
            i += 1

if cnt[minIdx] == 0: minIdx += 1
if cnt[maxIdx] == 0: maxIdx -= 1
```



#### :green_book: <연습 문제 # 5> : 구간합

https://swexpertacademy.com/

learn - course - programming - intermediate - List1

![](https://user-images.githubusercontent.com/52684457/62432048-40040d80-b768-11e9-81b6-7dfccb0342ad.png)

```python
T = int(input())
for k in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))

for i in range(M):
    MAX += n_list[i]
    MIN += n_list[i]
    MAX = MIN = SUM

for i in range(1, N-M+1):  # i는 구간의 시작위치
    crt = 0
    for j in range(i, i+M):
        crt += n_list[j]
        
    if MAX < crt:
        MAX = crt
    if MIN > crt:
        MIN = crt

    print( '#{} {}'.format(k+1, MAX-MIN))
```

##### 해결방법2)

![](https://user-images.githubusercontent.com/52684457/62432049-40040d80-b768-11e9-82b0-d22c131082d0.png)

슬라이딩 윈도우(Sliding Window): 배열의 연속적인 구간(sub-array, 윈도우)을 왼쪽에서 오른쪽으로 움직이면서 문제를 해결하는 방법

```python
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    Sum = 0
    for i in range(M):
        Sum += arr[i]
        
    Min = Max = Sum
    for i in range(N - M + 1):
        Sum += (arr[i+M] = arr[i])
        Min = min(Min, Sum)
        Max = max(Max, Sum)
        
    print("#%d %d" % (test_case, Max = Min))
```



#### :green_book: <연습 문제 # 6> : 전기 버스

https://swexpertacademy.com/

learn - course - programming - intermediate - List1

```python
T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) +[N]
    
    ans = bus = 0
    
    for i in range(1, M + 2):
        if arr[i] - arr[i - 1] > K:
            ans = 0
            break
        if arr[i] > bus + K:
            bus = arr[i - 1]
            ans += 1
```





------

####  :blue_book:완전 검색(Exaustive Search)

- **완전 검색 방법**은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 **나열해보고 확인**하는 기법
- Brute-force 혹은 generate-and-test 기법이라고도 불림
  -  Brute-force는 야수의 힘 - 컴퓨터의 계산 성능이 굉장히 좋은 것(빠름)을 말함
- **모든 경우의 수를 테스트한 후**, 최종 해법을 도출
- 일반적으로 **경우의 수가 상대적으로 작을 때** 유용
- 모든 경우의 수를 생성하고 테스트하기 때문에 **수행 속도는 느리지만**, 해답을 찾아내지 못할 확률이 작다. (=> 즉 찾아낼 확률 높음)
- 자격 검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.



##### 최적화 문제의 기본 해결 방법 (=완전 검색)

- 최대 혹은 최소가 되는 경우를 찾는 문제

- 모든 가능한 경우를 조사한다.

- 모든 후보해를 조사한다.

- 모든 가능한 경우들이 조합과 관련이 깊다.

  - 순열, 부분집합, 조합 (n!, 2^n)

  

##### 완전 검색을 좀 더 효율적으로 하는 방법 (아래의 방법 둘 전부 완전 검색 중 하나.)

1. 백트래킹 (가지치기) - 선택을 되돌릴 수 있는 것, 이전 상태로 돌아와서 다른 선택을 함.
2. 동적 계획법(memoization)



![](https://user-images.githubusercontent.com/52684457/62035045-08f2a100-b22a-11e9-8dae-dc556b3b5790.png)



#### :closed_book:탐욕(Greedy) 알고리즘

- 탐욕 알고리즘은 **최적해를 구하는 데 사용**되는 **근시안적**인 방법
  (근시안적 : 앞일이나 사물 전체를 파악하지 못하고 눈앞의 부분적인 현상에 사로잡힌)
- **여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식**으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 X
- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.
- **완전 검색을 하지 않고** 원하는 답을 찾기 빠르다. (하지만 대부분 사용하기가 **어렵다**.)
- 백트래킹과는 다르게 한가지 선택을 고수하며 따라간다.



##### 동작 과정

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지 확인
   곧, 문제의 제약 조건을 위반하지 않는지를 검사
3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인
   아직 전체 문제의 해가 완성되지 않았다면 1.의 해 선택부터 다시 시작



#### :closed_book:분할 정복(Divide and Conquer)

- 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복 (Conquer)하는 방법
- 분할정복법은 문제의 사례를 2개 이상의 더 작은 사례로 나눈다. 이 작은 사례는 주로 원래 문제에서 따온다. 나눈 작은 사례의 해답을 바로 얻을 수 있으면 해를 구하고 아니면  더 작은 사례로 나눈다.
- **해를 구할 수 있을 만큼 충분히 더 작은 사례로 나누어 해결하는 방법**
- 하향식(top-down) 접근 방법으로 최상위 사례의 해답은 아래로 내려가면서 작은 사례에 대한 해답을 구함으로써 구한다.



  **장점**: 문제를 나눔으로써 어려운 문제를 해결할 수 있다는 엄청나게 중요한 장점이 있다. 그리고 이 방식이 그대로 사용되는 효율적인 알고리즘들도 여럿 있으며, 문제를 나누어 해결한다는 특징상 병렬적으로 문제를 해결하는 데 큰 강점이 있다. 

**단점**: 함수를 재귀적으로 호출한다는 점에서 함수 호출로 인한 오버헤드가 발생하며, 스택에 다양한 데이터를 보관하고 있어야 하므로 `스택 오버플로우`가 발생하거나 과도한 메모리 사용을 하게 되는 단점  



## :closed_lock_with_key:배열(Array) 2

#### :bookmark_tabs: 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함



> ###### 2차 배열 탐색 목록 
>
> - 행우선 탐색
> - 열우선 탐색
> - 지그재그 탐색
> - 대각 탐색
> - 대각선, 테두리 탐색
> - 사각 영역 탐색
> - 기준점으로 탐색
>
> http://problems.kr/01array/2d_search.html



#### :bookmark_tabs: 배열 순회

![](https://user-images.githubusercontent.com/52684457/62434812-e35b1f80-b774-11e9-99fb-16fd45ef8ceb.png)

- n X m 배열의 n*m개의  모든 원소를 빠짐없이 조사하는 방법

![](https://user-images.githubusercontent.com/52684457/62433079-f8808000-b76d-11e9-8010-098d076d3114.png)

`Array[j][i]`로 쓰면 열 우선순회가 되기 때문에 순서를 잘 써야 함.

![](https://user-images.githubusercontent.com/52684457/62433224-82c8e400-b76e-11e9-90a8-a22b1ea681ab.png)

```python
N = 10 #10회 지그재그 순회

for i in range(N):   # i = 행
    if i % 2 == 0:
        for j in range(N) # j = 열
        pass
    else:
        for j in range(N-1, -1, -1):
            pass
```



![](https://user-images.githubusercontent.com/52684457/62433428-5a8db500-b76f-11e9-827e-1b707a9ebfb2.png)



#### :bookmark_tabs: 델타를 이용한 2차 배열 탐색

- 2차 배열의 한 좌표에서 4 방향의 인접 배열 요소를 탐색하는 방법
- 간결하며 구현이 쉽다.

![](https://user-images.githubusercontent.com/52684457/62434223-bad22600-b772-11e9-976f-1f5006963360.png)

```python
N = 10 # N x M
dx = [-1, +1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, +1]

for x in range(N): # 모든 행에 대해서
    for y in range(N): # 모든 열에 대해서
        # [x][y]
        # 4 방향의 인접 위치 좌표를 생성
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            #경계 체크
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
```



##### 대각 탐색

![](https://user-images.githubusercontent.com/52684457/62435403-025ab100-b777-11e9-8a2e-442b6167daad.png)



![](https://user-images.githubusercontent.com/52684457/62450561-8593fb00-b7a7-11e9-846f-59f228f2cac9.png)



- 사선의 수 = N + M - 1, 즉, 사선의 시작 좌표가 **N + M - 1** 개 존재한다.

```python
# 대각 탐색
arr = [[ 1,  2,  4,  7, 11],
      [ 3,  5,  8, 12, 15],
      [ 6,  9, 13, 16, 18],
      [10, 14, 17, 19, 20]]



N, M = len(arr), len(arr[0])
# dx, dy 각각 리스트로 저장
for diag in range(0, N + M - 1):

    x = 0 if diag < M else (diag - M + 1)
    y = diag if diag < M else M - 1

    while x < N and y >= 0:
        print('%2d' % arr[x][y], end='')
        x += 1
        y -= 1
    print()
```



#### :closed_book:부분집합 생성하기

![](https://user-images.githubusercontent.com/52684457/62436484-bc075100-b77a-11e9-80f9-d641036f77c4.png)

![](https://user-images.githubusercontent.com/52684457/62436587-156f8000-b77b-11e9-8737-662a0bc2bb63.png)

```python
arr = 'ABC'
bits = [0] * 3

def print_set(bits):
    print(bits, end=' ')
    for i in range(len(bits)):
        if bits[i]:
            print(arr[i], end=' ')
    print()

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            # print(bits)
            print_set(bits)
```

```python
# 도출 값
[0, 0, 0]
[0, 0, 1] C
[0, 1, 0] B
[0, 1, 1] B C
[1, 0, 0] A
[1, 0, 1] A C
[1, 1, 0] A B
[1, 1, 1] A B C
```



#### :closed_book:비트 연산자

| 비트 연산자 | 비트 단위로 AND 연산을 한다.                 |
| ----------- | -------------------------------------------- |
| &           | 비트 단위로 AND 연산을 한다.                 |
| \|          | 비트 단위로 OR 연산을 한다.                  |
| <<          | 피연산자의 비트 열을 왼쪽으로 이동시킨다.    |
| \>>         | 피연산자의 비트 열을 오른쪽으로 이동 시킨다. |

- << 

  - 1 << n : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.

- & 

  - i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 리턴한다.

  

  ![](https://user-images.githubusercontent.com/52684457/62438755-e7426e00-b783-11e9-91ef-f708d5282ebc.png)

```python
n = 10

if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 위의 코드를 써도 되지만 아래의 방법도 가능하다.  

    
# 최하위의 1이 비트값이 0 인지 1인지 판단하는 것. (n의 0제곱이 0인지 1인지.)
# 2의 제곱은 전부 짝수 인 것을 알 수 있다.
if n & 1:
    print('홀수')
else:
    print('짝수')
```



##### n진수

```python
# n진수
num = 10
print(bin(num))
num2 = 0b1010 # 2진수
num16 = 0xa # 16진수
print(num, num2, num16) # 다 같은 10

# &, |
a = 0b1010
b = 0b1011
c = a & b
d = a | b
print(bin(c)) # 도출값 : b11010 / 하나라도 0(False)면 0(False)
print(bin(d)) # 도출값 : b11011 / 하나라도 1(True)면 1(True)
```

![](https://user-images.githubusercontent.com/52684457/62439731-e9a6c700-b787-11e9-89ef-4d7bf2ee71c4.png)

> **위의** 그림은 **<<**을 나타낸 것
>
> `<<`  - *2     
>
> - *(ex) a = 10 을 (a<<1 => 20) (a<<2 => 40) (a<<3 => 80)*
>   *1<<10 은 2의 10제곱      =>     2<<10 2의 11제곱*   
>
> `>>`  - / 2



![](https://user-images.githubusercontent.com/52684457/62440604-d7c72300-b78b-11e9-85d3-4175d23b1e9d.png)

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n : 원소의 개수
for i in range(1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n+1): # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
    print()
print()
```

```python
# 도출 값
3,
6,
3, 6,
7,
3, 7,
6, 7,
3, 6, 7,
1,
3, 1,
6, 1,
3, 6, 1,
7, 1,
3, 7, 1,
6, 7, 1,
3, 6, 7, 1,
5,
3, 5,
6, 5,
3, 6, 5,
7, 5,
3, 7, 5,
6, 7, 5,
3, 6, 7, 5,
1, 5,
3, 1, 5,
6, 1, 5,
3, 6, 1, 5,
7, 1, 5,
3, 7, 1, 5,
6, 7, 1, 5,
3, 6, 7, 1, 5,
4,
3, 4,
6, 4,
3, 6, 4,
7, 4,
3, 7, 4,
6, 7, 4,
3, 6, 7, 4,
1, 4,
3, 1, 4,
6, 1, 4,
3, 6, 1, 4,
7, 1, 4,
3, 7, 1, 4,
6, 7, 1, 4,
3, 6, 7, 1, 4,
5, 4,
3, 5, 4,
6, 5, 4,
3, 6, 5, 4,
7, 5, 4,
3, 7, 5, 4,
6, 7, 5, 4,
3, 6, 7, 5, 4,
1, 5, 4,
3, 1, 5, 4,
6, 1, 5, 4,
3, 6, 1, 5, 4,
7, 1, 5, 4,
3, 7, 1, 5, 4,
6, 7, 1, 5, 4,
3, 6, 7, 1, 5, 4,
```







![](https://user-images.githubusercontent.com/52684457/62441788-7786b000-b790-11e9-830e-04760464b570.png)

인덱스의 위치가 바뀌는 것을 이용하여 접근한 방식

| 10진수 | 2진수  | n = 10 |
| ------ | ------ | ------ |
| 10     | 1010   | n      |
| 20     | 10100  | n << 1 |
| 40     | 101000 | n << 2 |



```python
arr = [3, 6, 7, 1, 5, 4] # 리스트의 개수가 6 => 2의 6제곱
N = len(arr) # N : 원소의 개수
subset = 10 # 부분 집합

for j in range(N):
    if subset & (1 << j):
        print(arr[j], end=' ') # j는 1, 3 이 나온다. 인덱스 1, 3은 6, 1

for subset in range(1 << N): # 1<<N : 부분 집합의 개수
    print(subset, end='> ')
    for j in range(N): # 원소의 수만큼 비트를 비교함
        if subset & (1 << j): 
            print(arr[j], end=', ')
    print()

# << >> 개념 그리고 10진수를 2진수로 표현했을 때의 인덱스 값으로 문제를 풀이
```

```python
# 도출 값
6 1

0>
1> 3,
2> 6,
3> 3, 6,
4> 7,
5> 3, 7,
6> 6, 7,
7> 3, 6, 7,
8> 1,
9> 3, 1,
10> 6, 1,
11> 3, 6, 1,
12> 7, 1,
13> 3, 7, 1,
14> 6, 7, 1,
15> 3, 6, 7, 1,
16> 5,
17> 3, 5,
18> 6, 5,
19> 3, 6, 5,
20> 7, 5,
21> 3, 7, 5,
22> 6, 7, 5,
23> 3, 6, 7, 5,
24> 1, 5,
25> 3, 1, 5,
26> 6, 1, 5,
27> 3, 6, 1, 5,
28> 7, 1, 5,
29> 3, 7, 1, 5,
30> 6, 7, 1, 5,
31> 3, 6, 7, 1, 5,
32> 4,
33> 3, 4,
34> 6, 4,
35> 3, 6, 4,
36> 7, 4,
37> 3, 7, 4,
38> 6, 7, 4,
39> 3, 6, 7, 4,
40> 1, 4,
41> 3, 1, 4,
42> 6, 1, 4,
43> 3, 6, 1, 4,
44> 7, 1, 4,
45> 3, 7, 1, 4,
46> 6, 7, 1, 4,
47> 3, 6, 7, 1, 4,
48> 5, 4,
49> 3, 5, 4,
50> 6, 5, 4,
51> 3, 6, 5, 4,
52> 7, 5, 4,
53> 3, 7, 5, 4,
54> 6, 7, 5, 4,
55> 3, 6, 7, 5, 4,
56> 1, 5, 4,
57> 3, 1, 5, 4,
58> 6, 1, 5, 4,
59> 3, 6, 1, 5, 4,
60> 7, 1, 5, 4,
61> 3, 7, 1, 5, 4,
62> 6, 7, 1, 5, 4,
63> 3, 6, 7, 1, 5, 4,
```

```python
# 합이 0이되는 부분집합 구하기
arr = [3, 6, -1, 7, -3, 1, -5, -1, 5, 4] # 2의 n제곱만큼 돎.
N = len(arr) # 10

for i in range(1, 1 << N): # i는 부분집합을 표현, 공집합은 필요없다는 가정하에 1,
    Sum = 0
    for j in range(N):
        if i & (1 << j): # arr[j]를 포함하는지 / 비트표현에서 j번째 인덱스에 포함하는것인지 아닌지
            Sum += arr[j]
    if Sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=', ')
        print()
```

```python
# 도출 값
3, -3,
-1, 1,
3, -1, -3, 1,
6, -1, -5,
3, 6, -1, -3, -5,
7, -3, 1, -5,
1, -1,
3, -3, 1, -1,
6, -5, -1,
-1, 7, -5, -1,
3, 6, -3, -5, -1,
3, -1, 7, -3, -5, -1,
6, -1, 1, -5, -1,
3, 6, -1, -3, 1, -5, -1,
-5, 5,
3, -3, -5, 5,
-1, 1, -5, 5,
3, -1, -3, 1, -5, 5,
-1, -3, -1, 5,
1, -5, -1, 5,
3, -3, 1, -5, -1, 5,
-1, -3, 4,
1, -5, 4,
3, -3, 1, -5, 4,
-3, -1, 4,
-1, -3, 1, -1, 4,
3, -1, -5, -1, 4,
6, -1, -3, -5, -1, 4,
-1, -3, -5, 5, 4,
-3, -5, -1, 5, 4,
-1, -3, 1, -5, -1, 5, 4,
```





------



### :book:검색(Search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것 
  - 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색(Sequential search)
  - 이진 검색(binary search)
  - 해쉬(hash)



#### :blue_book:순차 검색(Sequential Search)

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
- 2가지 경우
  - 정렬되어 있지 않은 경우
  - 정렬되어 있는 경우



##### :triangular_flag_on_post:정렬되어 있지 않은 경우

- 검색 과정
  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
  - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
  - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

![](https://user-images.githubusercontent.com/52684457/62442149-e3b5e380-b791-11e9-8b94-3f387a17900e.png)

![](https://user-images.githubusercontent.com/52684457/62442155-ea445b00-b791-11e9-99ba-4c26381741bc.png)

![](https://user-images.githubusercontent.com/52684457/62442166-f203ff80-b791-11e9-9477-a1351322a6b8.png)





##### :triangular_flag_on_post:정렬되어 있는 경우

- 검색 과정
  - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자.
  - 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.

![](https://user-images.githubusercontent.com/52684457/62442172-faf4d100-b791-11e9-9fef-0a234aa48898.png)

![](https://user-images.githubusercontent.com/52684457/62442183-06e09300-b792-11e9-93d2-a2e741a51102.png)

완전 검색할 필요없이 검색을 종료 할 수 있다.

![](https://user-images.githubusercontent.com/52684457/62442186-0c3ddd80-b792-11e9-9ee4-a4b0d32499cf.png)



###### :star:이진 탐색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- **이진 검색을 하기 위해**서는 **자료가 정렬된 상태**여야 한다.

- 검색과정
  - 자료의 중앙에 있는 원소를 고른다.
  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  - 찾고자하는 값을 찾을 때 까지 위의 1~3의 과정을 반복한다.

![](https://user-images.githubusercontent.com/52684457/62443939-2b8b3980-b797-11e9-83dd-d329ca3bb44e.png)

![](https://user-images.githubusercontent.com/52684457/62443941-2b8b3980-b797-11e9-921f-661b794f9f35.png)

```python
arr = [] # 값이 들어잇는 리스트라고 가정
key = 123
start, end = 0, len(arr) - 1

def binarySearch(arr, key):
    start, end = 0, len - 1

    while start <= end:
        mid = (start + end) >> 1 # /2가 됨 , //2를 해줘도 된다.
        if arr[mid] == key: # 중간 값에서 이미 찾았다면 (검색 성공!)
            break
        if arr[mid] > key:
        # 중간의 값과 키값을 비교를 했더니 키값이 더 크다면 => 왼쪽에서 찾아야 함
            end = mid - 1
        else:
            start = mid + 1 # 시작할 위치를 중간 다음으로 

        return -1
```



```python
# 재귀 함수 이용
def binarySearch(arr, start, end, key):
    if start > end : return False
    mid = (start + end) >> 1
    if arr[mid] == key:
        return True
    if arr[mid] > key: 
        return binarySearch(arr, start, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, end, key)
```



------



#### :bookmark:인덱스

- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다.
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.
- 배열을 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의 성능 저하 문제를 해결하기 의해 배열 인덱스를 사용하라 수 있다.

![](https://user-images.githubusercontent.com/52684457/62444614-f4b62300-b798-11e9-88e5-41f858c32dc5.png)





##### 셀렉션 알고리즘(Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.

  - 최소값, 최대값 혹은 중간 값을 찾는 알고리즘을 의미하기도 한다.

- 선택과정

  - 셀렉션은 아래와 같은 과정을 통해 이루어진다.

    1. 정렬 알고리즘을 이용하여 자료 정렬하기
    2. 원하는 순서에 있는 원소 가져오기

    

> 1번부터 N번째 까지 작은 원소들을 찾아 배열의 앞쪽으로 이동, 배열의 N번째를 반환
>
> N이 비교적 작을 때 유용, O(Nn)의 수행시간을 필요로 한다.

```python
arr = [64, 25, 10, 22, 11]
N = len(arr)
# 최소값의 위치를 찾는다.
minIdx = 0
for j in range(minIdx + 1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[0], arr[minIdx] = arr[minIdx], arr[0]
# 10은 이제 자기 위치를 찾았다. => [10, 25, 64, 22, 11]
# [1, n-1] 최소값을 찾는다.

minIdx = 1
for j in range(minIdx + 1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[1], arr[minIdx] = arr[minIdx], arr[1]
# 11도 자기 위치를 찾았다. => [10, 11, 64, 22, 25]

# [2, n-1]
# [n-2, n-1] . . . n-1번 반복하면 된다.
```

```python
# 식을 정리하면,
for i in range(N - 1):
    minIdx = i
    for j in range(i + 1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)
```



#### :blue_book:선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
  - 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것
- 정렬과정
  - 주어진 리스트 중에서 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
- 시간 복잡도
  - O(n^2)

![](https://user-images.githubusercontent.com/52684457/62445082-5fb42980-b79a-11e9-94e4-89b8a7f6c785.png)

![](https://user-images.githubusercontent.com/52684457/62445094-680c6480-b79a-11e9-8833-46b96aaded52.png)

![](https://user-images.githubusercontent.com/52684457/62445102-6c388200-b79a-11e9-9156-2b50c973ea84.png)

![](https://user-images.githubusercontent.com/52684457/62445112-6fcc0900-b79a-11e9-9e84-4cc96bba23e5.png)

![](https://user-images.githubusercontent.com/52684457/62445123-75c1ea00-b79a-11e9-9c75-9bac90752003.png)

![](https://user-images.githubusercontent.com/52684457/62445129-7b1f3480-b79a-11e9-8da6-5cc3bf0ecc89.png)

![](https://user-images.githubusercontent.com/52684457/62445143-86726000-b79a-11e9-986d-cb495d5cd5dd.png)







