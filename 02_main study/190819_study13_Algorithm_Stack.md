# :card_file_box:  Algorithm : Stack

###  :card_index_dividers: 스택(stack)의 특성 

- **물건을 쌓아 올리듯 자료를 쌓아 올린 형태**의 자료구조

- 스택에 저장된 자료는 선형 구조를 갖는다.

  - **선형구조: 자료간의 관계가 1대1의 관계를 갖는다.**
  - 비선형구조: 자료 간의 관계가 1대 N의 관계를 갖는다.*(ex: 트리 - 그래프)*

- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

- <u>**마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출***</u>(LIFO, Last-in-First-Out : 가장 마지막에 넣은 자료가 가장 먼저 나옴)

  - 예를 들어 스택에 1, 2, 3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3, 2, 1 순으로 꺼낼 수 있다.

  - 중간 데이터를 삭제/수정이 불가능
  
    

### :card_index_dividers: 스택(stack)의 구현

- ###### 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

  - 자료구조: 자료를 선형으로 저장할 **저장소**
    - C언어에서는 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라 부르기도 한다.
    - 스택에서 마지막 삽입된 원소의 위치를 **top**이라 부른다.
  - **연산**
    - **삽입**:  저장소에 자료를 저장한다. 보통 **push**라고 부른다.
    - **삭제**: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 **pop**이라고 부른다.
    - <u>스택이 공백인지 아닌지를 확인하는 연산. isEmpty</u>
    - <u>스택의 top에 있는 item(원소)을 반환하는 연산. peek</u>

  

  ![](https://user-images.githubusercontent.com/52684457/63233588-fb9a6680-c26b-11e9-98c7-a4ad6638f668.png)

```python
# C - style
S = [0] * 3 # 저장소
top = -1 # 마지막에 저장된 자료의 인덱스
def push(item):
    global top
    # full상태를 체크
    if top == 2: return
    top += 1
    S[top] = item

def pop():
    global top
    # empty 상태체크
    if top == -1: return
    ret = S[top]
    top -= 1
    return ret

for i in range(3):
    push(i)

print(pop()); print(pop()); print(pop()); print(pop());


#Pythonic
S = [] # 저장소

def push(item):
    # full상태를 체크
    S.append(item)

def pop():
    # empty 상태체크 더이상 꺼낼게 없다면 그대로 return 있다면 -1 해서 pop()으로 꺼내기
    # pop()은 뒷자리 숫자를 없애면서 없앤 수를 호출하기 때문에 값을 꺼낼 수 있다.
    if len(S) == 0:
        print('empty')
        return
    return S.pop()

def isEmpty():
    return len(S) == 0

for i in range(3):
    push(i)

while not isEmpty():
    print(pop())
    
import time
start = time.time()
print(start, time.time)
# time을 이용하면 계산 시간을 출력 가능하다.

from collections import deque
S = deque
N = 1000000
for i in range(N):
    S.append(i)
while S:
    S.popleft() # 왼쪽에서 부터 빼는 함수
# deque를 사용하면 훨씬 더 빠른 계산 속도를 얻을 수 있다.
```



#### :cactus: 스택의 응용1 : 괄호 검사

- 괄호의 종류: 대괄호[ ], 중괄호{}, 소괄호()
- 조건
  1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
  2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  3. 괄호 사이에는 포함 관계만 존재
- 잘못된 괄호 사용의 예
  - *(a(b)*
  - *a(b)c)*
  - *a{b(c[d]e}f)*

![](https://user-images.githubusercontent.com/52684457/63235080-1c19ef00-c273-11e9-8b63-712d4710cc71.png)

- 괄호를 조사하는 알고리즘 개요
  - **문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입하고, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사**한다.
  - 이 때, 스택이 비어있으면 조건 1 또는 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배된다.
  - 마지막 괄호까지 조사한 후에도 스택에 괄호가 남아 있으면 조건 1에 위배된다.



#### :cactus: 스택의 응용2 : function call

- ##### Funcion call

  - 프로그램에서의 함수 호출과 복귀에 따른 수행 순허를 관리

    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리

    - **함수 호출이 발생하면 호출한** 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
      -지역변수, 매개변수 **개념은 똑같다.**
      존재하는 순간에 메모리를 사용하고 끝날때까지 존재하고 사라진다

      -**전역 변수**는 끝나도 계속 지속되기 때문에 여러가지로 접근이 가능

      -**매개변수**: 함수 호출하면서 넘겨주는 변수

      -**지역변수**: 함수 내부에서 선언한 변수

    - 함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어있던 복귀주소를 확인하고 복귀

    - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

![](https://user-images.githubusercontent.com/52684457/63237078-6e5f0e00-c27b-11e9-8612-d5a43f07b2bf.png)



![](https://user-images.githubusercontent.com/52684457/63237094-7ae36680-c27b-11e9-9fa3-692b19124128.png)

#### :cactus:재귀호출 : 팩토리얼

```python
# 팩토리얼 구하는 문제
# 1! = 1
# 2! = 1! * 2
# 3! = 2! * 3
# . . .
# n! = (n-1)! * n

# 문제의 크기는 자연수로 표현

def factorial(n): # 매개변수 n - 문제(크기)를 나타내는 값
                         # 반환 값 - n! 의 값(문제의 해)
    if n == 0 or n == 1:  # 기저 사례 (범위가 좁아서 쉽게 해를 구할 수 있다고 추측)
        # 재귀호출 하지 않고 종료
    else:
        # 재귀 호출
        return factorial(n - 1) * n

print(factorial(4))
```

![](https://user-images.githubusercontent.com/52684457/63240261-d583bf00-c289-11e9-8c64-5ae6072371c0.png)

![](https://user-images.githubusercontent.com/52684457/63240245-c866d000-c289-11e9-954a-9e735b960c5c.png)



#### :cactus:재귀호출 : 피보나치

- 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열을 피보나치라한다.
  - 0, 1, 2, 3, 5, 13...
- 피보나치 수열의 i번 째 값을 계산하는 함수 F를 정의하면 다음과 같다.
  - F0 = 0, F1 = 1
  - `F(i) = F(i-1) + F(i-2) for i >= 2`
- 위의 정의로부터 피보나치 수열의 i 번째 항을 반환하는 함수 재귀함수로 구현할 수 있다.

![](https://user-images.githubusercontent.com/52684457/63240690-bb4ae080-c28b-11e9-8d7f-dc9130e077be.png)

```python
def fibonacci(n): # n번째 피보나치 수를 반환
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

- 엄청난 중복 호출이 존재 **=>** 시간이 많이 걸림

![](https://user-images.githubusercontent.com/52684457/63240681-b554ff80-c28b-11e9-87a2-d6cf5617f151.png)

#### :cherry_blossom: Memoization​

![](https://user-images.githubusercontent.com/52684457/63240841-5ba10500-c28c-11e9-95cb-9af26ec06854.png)



- 앞의 예에서 피보나치 수를 구하는 알고리즘에서 fibonacci(n)의 값으 계산하자마자 저장하면(memoize), 실행시간을 O(n)으로 줄일 수 있다.
- **<u>Memoization</u>** 방법을 적용한 알고리즘은 다음과 같다.

![](https://user-images.githubusercontent.com/52684457/63241910-678ec600-c290-11e9-91f6-bbb49bf122f9.png)

```python
memo = [-1] * 100

def fibonacci(n): # n번째 피보나치 수를 반환
    if n == 1 or n == 0:
        return 0
    # 이미 답을 구했는지 확인
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

print(fibonacci(7))
```



#### :cherry_blossom: DP(Dynamic Programming) 

- 동적 계획(Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 **<u>최적화 문제를 해결하는 알고리즘</u>**
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

![](https://user-images.githubusercontent.com/52684457/63242069-03b8cd00-c291-11e9-8c7c-f69a830c58e4.png)

![](https://user-images.githubusercontent.com/52684457/63242073-0d423500-c291-11e9-8619-f60e5cc7a33b.png)

![](https://user-images.githubusercontent.com/52684457/63242283-d7ea1700-c291-11e9-8f19-e063508d99d6.png)

```python
# 피보나치 수 DP 적용 알고리즘
memo = [-1] * 100
def fibonacci(n): # n번째 피보나치 수를 반환
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1): # i ===> 문제를 나타내는 값
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

print(fibonacci(7))
```



##### :cherry_blossom: DP의 구현 방식

> - rescursive 방식 : fib1()
> - iterative 방식 : fib2()
>
> 
>
> - memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적
> - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문



------

### :bar_chart: 그래프 

- 실 세계 문제를 그래프로 추상화해서 해결하는 방법을 학습
  - 그래프 탐색 기법인 BFS와 DFS에 대해 학습
  - 그래프 알고리즘에 활용되는 상호배타 집합(Disijoint-Sets)의 자료구조에 대해 학습
  - 최소 신장 트리(Minimum Spanning Tree)를 이해하고 탐욕 기법을 이용해서 그래프에서 최소 신장 트리를 찾는 알고리즘을 학습
  - 그래프의 두 정점 사이의 최단 경로(Shortest Path)를 찾는 방법을 학습

###### 문제제시

![](https://user-images.githubusercontent.com/52684457/63242678-24822200-c293-11e9-886f-420a06c85f9c.png)

- **<u>그래프</u>**는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현

- **그래프는 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조**

  - |V|: 정점의 개수, |E|: 그래프에 포함된 간선의 개수

  - |V|개의 정점을 가지는 그래프는 최대 `|V|(|V|-1)/2` 간선이 가능

    ex) 5개 정점이 있는 그래프의 최대 간선 수는 10(=5*4/2) 개

- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N : N 관계를 가지는 원소들을 표현하기에 용이



#### :chart_with_downwards_trend: 그래프 유형 :chart_with_upwards_trend: 

- 무향 그래프(Undirected Graph) **=>** 동등한 관계 *(ex.친구 관계)*

- 유향 그래프(Directed Graph) **=>** 의존관계 선행관계 동등하지 않은 관계 *(ex.일방적인 감정 관계)*
- 가중치 그래프(Weighted Graph)
- 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)
- ![](https://user-images.githubusercontent.com/52684457/63243139-9e66db00-c294-11e9-8a89-00730844912f.png)



#### :chart_with_downwards_trend: 인접 정점 :chart_with_upwards_trend: 

![](https://user-images.githubusercontent.com/52684457/63243155-a7f04300-c294-11e9-9cb7-8187b9a8f9ec.png)



#### :chart_with_downwards_trend: 그래프 경로 :chart_with_upwards_trend: 

![](https://user-images.githubusercontent.com/52684457/63243164-b0e11480-c294-11e9-9cdc-da34bc80745e.png)

#### :chart_with_downwards_trend: 그래프 표현 :chart_with_upwards_trend: 

- **<u>간선의 정보를 저장하는 방식</u>**, 메모리나 성능을 고려해서 결정
- **인접 행렬**(Adjacent matrix)
  - |V| * |V| 크기의 2차원 배열을 이용해서 간선 정보를 저장
  - 배열의 배열(포인터 배열)

- **인접 리스트**(Adjacent List)
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- **간선의 배열**
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장



###### :point_right: 인접 행렬

![](https://user-images.githubusercontent.com/52684457/63244292-f18e5d00-c297-11e9-8d98-9a3a9b2fe6f1.png)

![](https://user-images.githubusercontent.com/52684457/63244580-c48e7a00-c298-11e9-843e-9c341725ec8e.png)

- 전체적으로 값을 다 확인 하기 때문에 비효율 적이다. 



###### :point_right: ​인접 리스트

![](https://user-images.githubusercontent.com/52684457/63244590-cbb58800-c298-11e9-93fa-3c9ba0373d0d.png)

![](https://user-images.githubusercontent.com/52684457/63244606-d5d78680-c298-11e9-9885-1cc57618dce2.png)

------

```txt
04_Stack1/DFS_input.txt
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
```

```python
import sys; sys.stdin = open('04_Stack1/DFS_input.txt', 'r')

V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)] # 정점 번호 1 ~ V

for _ in range(E):
    u, v = map(int, input().split())
    G[u].appen(v)
    G[v].append(u)
    
for i in range(1, V + 1):
    print(i, '->', G[i])
```

##### :cherry_blossom: DFS(깊이우선탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
- 두 가지 방법
  - 깊이 우선 탐색(Depth First Search, DFS)
  - **너비 우선 탐색(Breadth First Search, BFS)**
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

##### :cherry_blossom: DFS 알고리즘

1. **시작 정점 v를 결정하여 방문**
2. 정점 v에 인접한 정점 중에서
   1) 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복
   2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복
3. 스택이 공백이 될 때까지 2.를 반복

![](https://user-images.githubusercontent.com/52684457/63246137-f1dd2700-c29c-11e9-978f-d440f0988ec3.PNG)

![](https://user-images.githubusercontent.com/52684457/63246138-f1dd2700-c29c-11e9-93af-42872b413e12.PNG)

![](https://user-images.githubusercontent.com/52684457/63246139-f1dd2700-c29c-11e9-98b1-417413db28c5.PNG)![](https://user-images.githubusercontent.com/52684457/63246140-f1dd2700-c29c-11e9-899c-3c210e12a92f.PNG)

![](https://user-images.githubusercontent.com/52684457/63246141-f275bd80-c29c-11e9-97f8-dfed806594f1.PNG)

![](https://user-images.githubusercontent.com/52684457/63246142-f275bd80-c29c-11e9-81ca-76800cb766e6.PNG)

![](https://user-images.githubusercontent.com/52684457/63246143-f275bd80-c29c-11e9-9e43-2330f2aed4b6.PNG)

![](https://user-images.githubusercontent.com/52684457/63246144-f275bd80-c29c-11e9-9bef-0bc70dd9d53b.PNG)

![](https://user-images.githubusercontent.com/52684457/63246145-f30e5400-c29c-11e9-93a4-209b13bf8bd5.PNG)

![](https://user-images.githubusercontent.com/52684457/63246146-f30e5400-c29c-11e9-9f68-886c758428ca.PNG)

![](https://user-images.githubusercontent.com/52684457/63246147-f30e5400-c29c-11e9-9326-ee747490a163.PNG)

![](https://user-images.githubusercontent.com/52684457/63246148-f3a6ea80-c29c-11e9-9447-6e760523e594.PNG)

![](https://user-images.githubusercontent.com/52684457/63246149-f3a6ea80-c29c-11e9-84a4-3cbf986365a7.PNG)

![](https://user-images.githubusercontent.com/52684457/63246150-f3a6ea80-c29c-11e9-9cdd-7653c26df350.PNG)



> ###### 연습 문제
>
> ![](https://user-images.githubusercontent.com/52684457/63246130-ea1d8280-c29c-11e9-830e-6b06aeff0ee0.png)
>
> ```python
> def DFS(v): # 시작점
>     S = []
>     visit = [False] * (V + 1)
>     visit[v] = True # 시작점을 방문
>     print(v, end=" ")
>     S.append(v)     # 시작점을 스택에 push
>     while S:        # 빈 스택이 아닐 동안 v의 방문하지 않은 인접정점을 찾는다. ==> w
>         for w in G[v]:
>             if not visit[w]:
>                 visit[w] = True # w를 방문하고
>                 print(w, end=" ")
>                 S.append(v)     # v를 스택에 push
>                 v = w           # w를 현재 방문하는 정점으로 설정
>                 break
>         else:
>             v = S.pop()
> ```
>
> ```python
> def DFS(v): # v: 현재 방문하는 정점
>     visit[v] = True; print(v, end=" ")
>     for w in G[v]:
>         if not visit[w]:
>             DFS(w)
> ```





























