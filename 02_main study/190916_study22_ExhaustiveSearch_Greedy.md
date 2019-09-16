# :card_file_box: APS :  ExhaustiveSearch_Greedy

- 재귀적 알고리즘 특성 이해와 이를 구현하기위한 재귀 호출에 대해 학습
- 완전 검색의 개념을 이해, 이를 통한 문제 해결방법에 대해 모색
- 조합적 문제(Combinatorial Problems)에 대한 완전 검색 방법에 대해 이해
  - 순열, 조합, 부분집합을 생성하는 알고리즘을 학습
- 탐욕 알고리즘 기법의 개념과 주요 특성을 이해



### :recycle: 반복(Iteration)과 재귀(Recursion)

- 반복과 재귀는 유사한 작업을 수행할 수 있다.
- 반복은 수행하는 작업이 완료될 때까지 계속 반복
  - 루프(for, while 구조)
    - **for** : 반복의 회수가 정확할 때 *(ex.100회 동안 ~~을 하겠다)*
    - **while** : 반복의 조건이 정확할 때 *(ex.100이 될때까지  ~~을 하겠다)* 
      원하는 값이나 상태가 될 때 사용 (몇 번을 반복해야할지 때마다 다름)
- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
  - 하나의 큰 문제를 해결할 수 있는 (해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합
  - 재귀 함수로 구현



![](https://user-images.githubusercontent.com/52684457/64930641-b3239800-d86d-11e9-8224-14ce692cf1b9.png)

![](https://user-images.githubusercontent.com/52684457/64930717-4eb50880-d86e-11e9-82d9-25a1549dcf6c.png)

![](https://user-images.githubusercontent.com/52684457/64930758-9a67b200-d86e-11e9-9188-cfacf2d8d7af.png)

![](https://user-images.githubusercontent.com/52684457/64930819-18c45400-d86f-11e9-9ab0-86f997381a2b.png)

![](https://user-images.githubusercontent.com/52684457/64930825-2083f880-d86f-11e9-8a64-093a1fdb9582.png)

![](https://user-images.githubusercontent.com/52684457/64930887-896b7080-d86f-11e9-8cda-28291254bae0.png)

![](https://user-images.githubusercontent.com/52684457/64930895-98522300-d86f-11e9-9555-1c5c323d1ef6.png)

- 해결할 문제를 고려해서 반복이나 재귀의 방법을 선택
- 재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스럽다.
  - 추상 자료형(List, tree 등)의 알고리즘은 재귀적 구현이 간단하고 자연스러운 경우가 많다.
- 일반벅으로, 재귀적 알고리즘은 반복(Iterative) 알고리즘보다 더 많은 메모리와 연산을 필요로 한다.
- <u>입력 값 n이 커질수록 재귀 알로기즘은 반복에 비해 비효율적일 수 있다.</u>

![](https://user-images.githubusercontent.com/52684457/64930992-4cec4480-d870-11e9-8660-ab8676003000.png)

![](https://user-images.githubusercontent.com/52684457/64931173-b3be2d80-d871-11e9-9f73-e6aa17ef2623.png)

```python
arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 0]
# def getMin(문제크기):         # 최소값 구하기
#     if 가장 작은 문제:
#
#     else:getMin(더작은 문제)  # 매개변수 => 문제의 크기, 반환 값 = 문제의 해
#
# print(getMin(원문제의 크기))

def getMin(s, e):    # 최소값 구하기
    if s == e:       # 기저 사례
        return arr[s]

    else:
        ret = getMin(s, e - 1)
        return min(ret, arr[e])

print(getMin(0, len(arr) - 1))

# 재귀 호출
# 1. 동적계획법(DP) / 분할정복 ==> 재귀적 정의 구현할 때
#                              - 부분문제간의 관계(큰 문제와 작은 문제간 관계)
# 2. 탐색
#    - 그래프 깊이 우선 탐색(DFS), 트리 순회
#    - 백트래킹 --> 상태공간 트리, 그래프 탐색
```



##### 고지식한 방법 (brute-force)

![](https://user-images.githubusercontent.com/52684457/64931894-76a86a00-d876-11e9-969c-ded7b0780e12.png)

![](https://user-images.githubusercontent.com/52684457/64931924-9344a200-d876-11e9-965a-855ad9e33c49.png)

- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다.
  - 완전검색은 입력의 크기를 작게 해서 간편하고 빠르게 답을 구하는 프로그램을 작성
- 이를 기반으로 그리디 기법이나 동적 계획법을 이용해서 효율적인 알고리즘을 찾을 수 있다.
- 검정 등에서 주어진 문제를 풀 때, <u>우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직</u>

![](https://user-images.githubusercontent.com/52684457/64932048-4dd4a480-d877-11e9-8d8d-346daa963e99.png)



------



#### :green_book: 문제 제시 : 여행사 BIG sale!

![](https://user-images.githubusercontent.com/52684457/64932824-9b074500-d87c-11e9-8676-947be4c51b67.png)

![](https://user-images.githubusercontent.com/52684457/64932808-7dd27680-d87c-11e9-9937-8d8d93b72ba5.png)

- 순열을 이용

------

## :1234: 순열(Permutation)

![](https://user-images.githubusercontent.com/52684457/64932858-cc801080-d87c-11e9-8cd3-def9dbb45bc2.png)

- 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있다.
  - 예) TSP
- N 개의 요소들에 대해서 n! 개의 순열들이 존재
  - 12! = 479,001,600
  - n > 12인 경우, 시간 복잡도 폭발적으로 증가

![](https://user-images.githubusercontent.com/52684457/64934578-b0816c80-d886-11e9-8556-73ed5205406b.png)

![](https://user-images.githubusercontent.com/52684457/64934581-bd05c500-d886-11e9-9b73-de1f577221e4.png)



```python
arr = 'ABC'
N = len(arr)
for i in range(N):          # 첫번째 위치
    for j in range(N):      # 두번째 위치
        if j == i: continue                 # 중복 순열 제외 1
        for k in range(N):  # 세번째 위치 
            if k == i or k == j:continue    # 중복 순열 제외 2
            print(arr[i], arr[j], arr[k])
            
# 출력 값
A B C
A C B
B A C
B C A
C A B
C B A
```

```python
# 중복 조합
arr = 'ABCDE'
N = len(arr)
for i in range(N):          # 첫번째 위치
    for j in range(N):      # 두번째 위치
        for k in range(N):  # 세번째 위치
            print(arr[i], arr[j], arr[k])
            
# 출력 값
A A A
A A B
A A C
A A D
A A E
A B A
A B B
A B C
A B D
A B E
A C A
A C B
A C C
A C D
A C E
A D A
A D B
A D C
A D D
A D E
A E A
A E B
A E C
A E D
A E E
B A A
B A B
B A C
B A D
B A E
B B A
B B B
B B C
B B D
B B E
B C A
B C B
B C C
B C D
B C E
B D A
B D B
B D C
B D D
B D E
B E A
B E B
B E C
B E D
B E E
C A A
C A B
C A C
C A D
C A E
C B A
C B B
C B C
C B D
C B E
C C A
C C B
C C C
C C D
C C E
C D A
C D B
C D C
C D D
C D E
C E A
C E B
C E C
C E D
C E E
D A A
D A B
D A C
D A D
D A E
D B A
D B B
D B C
D B D
D B E
D C A
D C B
D C C
D C D
D C E
D D A
D D B
D D C
D D D
D D E
D E A
D E B
D E C
D E D
D E E
E A A
E A B
E A C
E A D
E A E
E B A
E B B
E B C
E B D
E B E
E C A
E C B
E C C
E C D
E C E
E D A
E D B
E D C
E D D
E D E
E E A
E E B
E E C
E E D
E E E
```



![](https://user-images.githubusercontent.com/52684457/64935105-fc81e080-d889-11e9-8bac-3b4cdee7ec9a.png)

###  

## :repeat: 순열 생성 방법

 ![](https://user-images.githubusercontent.com/52684457/64934595-cdb63b00-d886-11e9-9902-96253e1e502e.png)

![](https://user-images.githubusercontent.com/52684457/64935217-ecb6cc00-d88a-11e9-8725-fcf47050b688.png)

![](https://user-images.githubusercontent.com/52684457/64935255-2ab3f000-d88b-11e9-9ffd-2f4f286e3b57.png)

![](https://user-images.githubusercontent.com/52684457/64935787-03125700-d88e-11e9-86cb-482efcc42dda.png)

```python
arr = [1, 2, 3, 4]
N = len(arr)

def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)

# 출력 값
[1, 2, 3, 4]
[1, 2, 4, 3]
[1, 3, 2, 4]
[1, 3, 4, 2]
[1, 4, 3, 2]
[1, 4, 2, 3]
[2, 1, 3, 4]
[2, 1, 4, 3]
[2, 3, 1, 4]
[2, 3, 4, 1]
[2, 4, 3, 1]
[2, 4, 1, 3]
[3, 2, 1, 4]
[3, 2, 4, 1]
[3, 1, 2, 4]
[3, 1, 4, 2]
[3, 4, 1, 2]
[3, 4, 2, 1]
[4, 2, 3, 1]
[4, 2, 1, 3]
[4, 3, 2, 1]
[4, 3, 1, 2]
[4, 1, 3, 2]
[4, 1, 2, 3]
```

 

## :baggage_claim:부분집합

- 집합에 포함된 원소들을 선택하는 것 
- 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분집합을 찾는 것
  - 예) 배낭 짐싸기(knapsack)
- N개의 원소를 포함한 집합
  - 자기 자신과 공집합 초함한 모든 부분집합(power set)의 개수는 2^n개
  - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

![](https://user-images.githubusercontent.com/52684457/64936386-a2d0e480-d890-11e9-8b4d-8cd8f98a1d78.png)

![image](https://user-images.githubusercontent.com/52684457/64936452-fe02d700-d890-11e9-9752-63879f0045b5.png)

![image](https://user-images.githubusercontent.com/52684457/64936455-0529e500-d891-11e9-9866-816eae317634.png)

![image](https://user-images.githubusercontent.com/52684457/64936475-183cb500-d891-11e9-88d9-64039f4c8621.png)



## :abcd: 조합

![image](https://user-images.githubusercontent.com/52684457/64936486-24c10d80-d891-11e9-9064-02ef1eab71e6.png)

- r = 0 이거나 n = r이면 1
- n**C**r **=** n-1**C**r-1 **+** n-1**C**r

````python
def nCr(n, r):
    if n == r or r == 0: return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

print(nCr(5, 3))
print(nCr(10, 4))

# 출력 값
10
210
````



![](https://user-images.githubusercontent.com/52684457/64936944-576c0580-d893-11e9-9dae-93e1e05fd5c1.png)



![image](https://user-images.githubusercontent.com/52684457/64936510-4d490780-d891-11e9-8137-dbc82b305d69.png)

![](https://user-images.githubusercontent.com/52684457/64937619-db26f180-d895-11e9-854a-03397ad35043.png)

- 효율적인 방법이지는 않다.

```python
# arr = 'ABCDE'
# N = len(arr)
#
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             print(arr[i], arr[j], arr[k])

arr = 'ABCDE'
N, R = len(arr), 3 # R 뽑는 회수
choose = []

def comb(k, s): # k는 1씩 증가하는 값으로 이용
    if k == R:
        print(choose)
    else:
        for i in range(s, N):
            choose.append(arr[i])
            comb(k + 1, i + 1)
            choose.pop() # 계속 추가되는것을 방지하기 위해 추가한것을 없앤다.

comb(0, 0)
```















