

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



------



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



#### :green_book: <연습 문제 # 1>

![](https://user-images.githubusercontent.com/52684457/62027023-9aa4e300-b217-11e9-92e5-da81cf5cd291.png)

```python
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# a만 계산하면 된다. 결국 제일 끝에있는 a가 낙폭이 가장 크거나 같기 때문. (낙폭이 큰 것을 위주로 계산 하면 됨.) 자기 밑의 상자가 몇 개 깔려있냐가 중요한데 높이(7)가 같거나 큰게 몇 개가 있는지 찾으면 됨.
```



#### :green_book: <연습 문제 # 2>

baby - gin game

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





#### :green_book: <연습 문제 # 3>

건물 조망권 확보하기 위한 세대 구하기

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



