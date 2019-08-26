# :file_folder: Algorithm : Stack 2



##### :green_book: <연습 문제 : 계산기>

- 중위 표기법 : 3 + 4 * 2 : 4 * 2 연산을 먼저, 그 다음 3을 더하는 방식
- 후위 표기법 : 3 + 4 * 2 : 3 + 42* **=>** 342*+ : 컴퓨터는 중위표기법의 계산을 하기가 어렵다. 스택을 사용해서 후위 표기법을 할 수 있다.

> 중위 표기법(infix notation)
>
> - 연산자를 피연산자의 가운데 표기하는 방법
>   *ex) A + B*
>
> 후위 표기법(postfix notation)
>
> - 연산자를 피연산자 뒤에 표기하는 방법
>   *ex) AB+*

**=====>** 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용) 후 후위 표기법의 수식을 스택을 이용하여 계산



![](https://user-images.githubusercontent.com/52684457/63658181-9dc5cb80-c7e3-11e9-985f-0b3a657b353d.png)

![](https://user-images.githubusercontent.com/52684457/63658186-a4544300-c7e3-11e9-90b9-c3e17d11507e.png)

![](https://user-images.githubusercontent.com/52684457/63658263-293f5c80-c7e4-11e9-9cdf-c304fa62bd69.png)

![](https://user-images.githubusercontent.com/52684457/63658279-483dee80-c7e4-11e9-9da1-2e1dd2ab9064.png)

![](https://user-images.githubusercontent.com/52684457/63658311-a9fe5880-c7e4-11e9-9db2-b416bc5c4cd5.png)

![](https://user-images.githubusercontent.com/52684457/63658317-b5ea1a80-c7e4-11e9-8d0b-036af464cfed.png)

![](https://user-images.githubusercontent.com/52684457/63658322-bda9bf00-c7e4-11e9-9184-2e9faa0369f4.png)

![](https://user-images.githubusercontent.com/52684457/63658323-c5696380-c7e4-11e9-84e8-c3c66e95d266.png)

![](https://user-images.githubusercontent.com/52684457/63658329-cbf7db00-c7e4-11e9-9ec6-aad30981a1ee.png)

![](https://user-images.githubusercontent.com/52684457/63658335-d1edbc00-c7e4-11e9-8672-94565d06b5c4.png)

![](https://user-images.githubusercontent.com/52684457/63658338-d7e39d00-c7e4-11e9-8a5c-cb447904ad69.png)

![](https://user-images.githubusercontent.com/52684457/63658342-de721480-c7e4-11e9-9776-a9a3abfc06e3.png)

![](https://user-images.githubusercontent.com/52684457/63658346-e631b900-c7e4-11e9-90dd-66dc057a1fbd.png)

![](https://user-images.githubusercontent.com/52684457/63658352-ecc03080-c7e4-11e9-88c4-6aac2755f0f0.png)

![](https://user-images.githubusercontent.com/52684457/63658357-f47fd500-c7e4-11e9-8226-e908eed45308.png)

![](https://user-images.githubusercontent.com/52684457/63658365-fb0e4c80-c7e4-11e9-9c22-47e1a0358714.png)

![](https://user-images.githubusercontent.com/52684457/63658374-019cc400-c7e5-11e9-84e5-efd70d81eb64.png)

> ###### 4가지의 연산자(+, -, *, /)만을 적용하여 중위표기식을 후위표기식으로
>
> ```python
> t = input()
> number = []
> operator = ''
> result = ''
> 
> for i in t:
>     if i.isdigit(): # 숫자(피연산자)일 경우
>         number.append(i)
>         # print(number)
> 
>     elif i=='+' or i=='-' or i=='*' or i=='/': # 연산자일 경우
>         operator += i
>         # print(operator)
> 
> for j in number:
>     result += j
> result = result + operator
> 
> print(result)
> ```



![](https://user-images.githubusercontent.com/52684457/63659035-06b04200-c7ea-11e9-974d-9a1868240b9a.png)

![](https://user-images.githubusercontent.com/52684457/63659041-10d24080-c7ea-11e9-9b7e-ceef765c6146.png)

![](https://user-images.githubusercontent.com/52684457/63659048-16c82180-c7ea-11e9-924a-4d17c423ebf7.png)

![](https://user-images.githubusercontent.com/52684457/63659059-234c7a00-c7ea-11e9-9b45-71b44ee8bc0e.png)

![](https://user-images.githubusercontent.com/52684457/63659067-28a9c480-c7ea-11e9-995e-3674de4c9b04.png)

![](https://user-images.githubusercontent.com/52684457/63659074-2f383c00-c7ea-11e9-96e3-f6ce773f664b.png)

![](https://user-images.githubusercontent.com/52684457/63659077-34958680-c7ea-11e9-9b9f-9e94310538b9.png)



> ###### 파이썬에서 문자열로 된 수식을 eval() 내장 함수로 계산 가능
>
> - 스택을 두 번 사용해서 처리했던 연산을 파이썬에서 제공되는 **eval() 내장 함수**로 계산 가능
> - Evaluation = "값을 구함" 이라는 뜻
> - 올바른 수식을 사용하지 않으면 "syntex error"가 뜸
> - *ex) eval(3+4\*4/2)*



------



## :stop_sign: :raised_back_of_hand: 백 트래킹

- 백트래킹(Backtracking) 기법은 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법

- 백트래킹 기법은 최적화(optimization) 문제와 결정(decision)문제를 해결 가능

- **결정 문제** : 문제의 조건을 만족하는 해가 존재하는지의 여부를 **'yes' or 'no'**로 답하는 문제

  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(Subset Sum)문제 등

  

##### :balloon: backtracking과 DFS는 같은걸까?

- DFS를 사용하여 정답을 찾는 과정이 백트래킹



##### :green_book: <연습 문제 : 미로 찾기>

![](https://user-images.githubusercontent.com/52684457/63659599-357be780-c7ed-11e9-83d0-3e7e10be9935.png)

![](https://user-images.githubusercontent.com/52684457/63659648-7ecc3700-c7ed-11e9-99db-0e8a59f05b19.png)

- 이때의 탐색은 시계방향 기준으로 이동
- (1, 0) (1, 1) (1, 2) 순이다. 위의 이미지는 오타가 난 것
- 막다른 길을 마주하게되면 마지막 스택을 꺼내면서 마지막 자리의 정보를 얻을 수 있다.



![](https://user-images.githubusercontent.com/52684457/63659651-868bdb80-c7ed-11e9-8e38-0d8e45de8a88.png)

- 스택을 꺼내면서 다시 (1, 2) (1, 1)순으로 되돌아 온다.

![](https://user-images.githubusercontent.com/52684457/63659661-90adda00-c7ed-11e9-844f-91bbf2aad435.png)

- 백트래킹과 깊이우선탐색과의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Prunnig 가지치기)
  - 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음, 즉, N!(N factorial) 가지의 경우의 수를 가진문제에 대해 깊이우선 탐색을 가하면 당연히 처리 불가능한 문제
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

`깊이우선탐색` : 모든 후보를 검사

`백트래킹` : 모든 후보를 검사하지 않음



- 백트래킹, 모든 후보를 검사?
  - **NO!**
- 백트래킹 기법
  - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
  - **가지치기(pruning)** : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.
- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행
  1. 상태 공간 트리의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속 진행



##### :green_book: < 연습 문제 :  N-Queen >

- n*n 정사각형안에 n개의 Queen을 배치하는 문제
- 모든 Queen은 자신의 일직선상 및 대각선 상에 아무것도 놓이지 않아야 함

> ###### 4*4 정사각형안에 4개의 퀸 배치
>
> - 일반 백트래킹 알고리즘
>
> ```python
> def checknode(v): #node
>     if promising(v):
>         if there is a solution at v: # 유망하다면 (solution이 있다면)
>             write the solution
>         else:
>             for u in each child of v:
>                 checknode(u)
> ```
>
> ![](https://user-images.githubusercontent.com/52684457/63660225-6a3d6e00-c7f0-11e9-8ee4-a0c8a3069305.png)
>
> - 먼저 (1, 1)에 배치
> - (2, 1), (2, 2)dpsms 1열의 퀸과 간섭이 일어나므로 배치할 수 없음
>
> ![](https://user-images.githubusercontent.com/52684457/63660240-7de8d480-c7f0-11e9-983a-6f4b8e0faa75.png)
>
> - (c), (f), (g) : 이전으로 돌아감
> - (k) : 최종 결과 (4개의 퀸을 모두 배치 완료)



### :deciduous_tree: 상태 공간 트리

- 있을 수 있는 모든 형태를 트리형태로 표현을 한 것

- 해를 찾기 위해 탐색할 필요가 있는 모든 후보들을 포함하는 트리
- 트리의 모든 노드들을 방문하면 해를 찾는것이 가능



![](https://user-images.githubusercontent.com/52684457/63660718-b5f11700-c7f2-11e9-90c3-8ec04bb0e41f.png)

- 문제 수행이 불가능해지는 노드는 사전에 탐색을 중지하기 때문에 깊이우선탐색보다 노드 수가 매우 적음



### :vs: 깊이 우선 검색 vs 백트래킹

- 순수한 깊이 우선 검색 = 155 노드

- 백트래킹 = 27 노드

  (백트래킹이 깊이우선탐색 수행시간의 약 1/5 소요됨)



##### :green_book: < 연습문제 : 부분집합 구하기 (subset) >

- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset(멱집합)이라 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2**n이 나온다.
- 백트래킹 기법으로 powerset을 구해보자.
  - 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용
  - n개의 원소가 들어있는 집합의 2**n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
  - 여기서 배열의 i번째 항복은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

> set = [a, b, c, d]
>
> ∅
>
> a
>
> b
>
> c
>
> d
>
> ab
>
> ac
>
> ad
>
> bc
>
> bd
>
> cd
>
> abc
>
> abd
>
> acd
>
> bcd
>
> abcd
>
> - 2\*\*4 **=>** 경우의 수 : 16

![](https://user-images.githubusercontent.com/52684457/63661075-2f3d3980-c7f4-11e9-971b-6d8d12f19544.png)



![](https://user-images.githubusercontent.com/52684457/63661447-90194180-c7f5-11e9-9047-8add6288115a.png)

![](https://user-images.githubusercontent.com/52684457/63662260-d3c17a80-c7f8-11e9-83a9-4a3090315032.png)

```python
def process_solution(a, k):
    print("(", end="")
    for i in range(k+1):
        if a[i]:
            print(i, end="")
    print(")", end="")
```

- input의 개수에 따른 경우의 수를 구하기

- backtrack(a, k, input)

  - (k, input) k, input **=>** 행, 열 index

  - ([0000], k, input) **=>** a라는 4자리 **=>** 0은 고려하지않고 1, 2, 3만 고려 **=>** *ex) a = {1, 2, 3}*

    > backtrack([0000], k **<=**0, input **<=**3)
    >
    > 
    >
    > ###### c[1]이 계속 True (1인 경우)
    >
    > backtrack([0100], 1, 3) # index 1이 선택 or 선택하지 않음 (1 = 선택, 0 = 선택하지 않음)
    >
    > backtrack([0110], 2, 3) # index 2이 선택 or 선택하지 않음
    >
    > backtrack([0111], 3, 3) # index 3이 선택 or 선택하지 않음
    >
    > [0111] **=>** 출력 : 1, 2, 3
    >
    > 
    >
    > ###### c[1]이 False(0인 경우) => 그 다음 c[1]이 True
    >
    > backtrack([0010],1, 3)
    >
    > .
    >
    > .
    >
    > .
    >
    > 
    >
    > - 그림으로 표현하면 아래와 같다.
    >
    > ![](https://user-images.githubusercontent.com/52684457/63662154-5eee4080-c7f8-11e9-9ac6-400c3fc5ee2d.png)

![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566789447430.png)

```python
def backtrack(a, k, input):
    global MAXCANDIDATES # 함수 바깥의 변수를 사용하기 때문에 전역변수를 적용시켜준다.
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    print("(", end="")
    for i in range(k+1):
        if a[i]:
            print(i, end="")
    print(")", end="")

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
```



###### {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합은?

```python
def process_solution(a, k):
    i_list = []
    sum = 0
    for i in range(k+1):
        if a[i] == True:
            i_list.append(i)
            sum += i
    if sum == 10:
        print(i_list)
        
    # or
    sum_value = 0
    for i in range(k + 1):
        if a[i]:
            sum_value += i
            
    if sum_value == 10:
        if a[i]
            print(i, end="")
            
backtrack(a, 0, 10)
```



##### :green_book: 백트래킹을 이용하여 순열 구하기

> data = {a, b, c, d}
>
> 4P4 (4가지의 수 중에서 4개를 뽑는 것) == 4!(4factorial / 4 * 3 * 2 * 1)  *곱의 법칙*
>
> - 어떤 두 사건이 있을 때 두 사건 중 하나만 일어나도 상관 없으면 **합의 법칙** 
>   (*ex 주사위에서 2의 배수가 나올 확률은 2, 4, 6 즉, 1/6을  3번 더해주는 것* ) 
> - 두 사건이 모두 일어나야 하면 **곱의 법칙**
>   (*ex 숫자카드 카드 n장을 m자리 자연수를 만드는 경우, n \* (n-1)\*(n-2)...m만큼* )

![](https://user-images.githubusercontent.com/52684457/63666090-2145e380-c809-11e9-9066-94cf69b811af.png)

- 접근 방법은 앞의 부분집합 구하는 방법과 유사

  ```python
  def backtrack(a, k, input):
      global MAXCANDIDATES
      c = [0] * MAXCANDIDATES
  
      if k == input:
          for i in range(1, k+1):
              print(a[i], end=" ")
          print()
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k, input)
  
  def construct_candidates(a, k, input, c):
      in_perm = [False] * NMAX
  
      for i in range(1, k):
          in_perm[a[i]] = True
  
      ncandidates = 0
      for i in range(1, input+1):
          if in_perm[i] == False:
              c[ncandidates] = i
      return ncandidates
  
  MAXCANDIDATES = 100
  NMAX = 100
  a = [0] * NMAX
  backtrack(a, 0, 3)
  ```



------



## :triangular_flag_on_post: 분할 정복 알고리즘

![1566795863005](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566795863005.png)

- 주어진 문제의 입력을 다루기 쉽게 **부분으로 분할하여 문제를 해결(정복)하는 방식의 알고리즘**
- 문제를 더 이상 나눌 수 없을 때까지 나누고 이렇게 나누어진 문제들을 각각 풂으로써 전체 문제의 답을 얻는 앍리즘
- 문제의 두 단계인 1분할과 2정복으로 나눠서 해결하는 것
- 분할한 입력에 대하여 동일한 알고리즘을 적용하여 해를 계산하며 이들의 해를 취합하여 원래 문제의 해를 얻음
- 엄청나게 크고 방대한 문제를 조금씩 나눠가면서 용이하게 출 수 있는 문제단위로 나눈다음 그것들을 다시합쳐서 해결하자는 개념

![](https://user-images.githubusercontent.com/52684457/63666670-d9748b80-c80b-11e9-8ec5-b706748d4ccf.png)



![](https://user-images.githubusercontent.com/52684457/63666533-08d6c880-c80b-11e9-90e1-ce4cdde52cd1.png)

![](https://user-images.githubusercontent.com/52684457/63666542-18eea800-c80b-11e9-9344-ec8b5558afc6.png)

- 거듭제곱을 반씩 나누어서 곱해나감
  (반으로 나뉜 부분은 다시 반으로 나누어서 곱해가면서 재귀적으로 하나의 값만 남을 때까지 나눔)
- 짝수일 경우 반으로 나누어 주면 되고, 홀수일 경우에는 +1, or -1을하여 짝수로 만들어 준 후, 반으로 다시 나누어서 계산하면 된다. -1을 했을 경우에는 *n, +1을 했을 경우에는 /n을 해주면 된다.
  *ex) 2^9 **=>** (9 - 1) **=>** (8) **=>** 2^4 \* 2^4 \*2*



- 분할 정복의 대표적인 예

  - 합병 정렬

  - 퀵 정렬

  - 이진 탐색 (절반으로 나누어 반반씩 비교하는 것)

  - 거듭제곱 연산(a^b)

    *ect . . .*



### :rabbit2: 퀵 정렬

- 평균적으로 수행 속도가 매우 빠른 정렬 방법

- 정렬할 전체 데이터에 대해서 정렬을 수행하지 않고 기준키를 중심으로 왼쪽 부분 리스트와 오른쪽 부분 리스트로 분할아여 정렬

- 이때 기준이 되는 **기준키를 피벗(pivot)**이라 함

- 피벗을 기준으로 왼쪽 부분 리스트에는 피벗보다 작은 데이터들을 이동 시키고 오른쪽 부분 리스트에는 피벗보다 큰 데이터들을 이동

- 작은 값을 갖는 데이터와 큰 값을 갖는 데이터로 분리해가며 정렬하는 방법

- 프로그램에서 순환 호출을 이용하기 때문에 스택이 필요

> ###### 피벗(pivot)의 선택 방법
>
> - 전체 데이터 중 가운데 위치한 데이터
> - 첫 번째 데이터
> - 마지막 데이터
> - 별도의 수식을 사용하여 정하기도 함

> ##### :grey_question: 주어진 배열을 두 개로 분할하고, 각각을 정렬한다 **=>** 합병정렬과 동일?
>
> ###### 합병 정렬
>
> - 하나의 리스트를 두 개의 균등한 크기로 반복해서 분할한 뒤 분한된 부분 리스트를 정렬한 다음 두 리스트를 합하여 전체가 정렬된 리스트를 만드는 방법
>
> - ###### 차이점
>
>   1. 합병 정렬은 그냥 두 부분으로 나누는 반면에, 퀵정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
>   2. 각 부분 정렬이 끝난 후, 합병정렬은 "합병"이란 후처리 작업이 필요하나, 퀵정렬은 필요로 하지 않는다.

![](https://user-images.githubusercontent.com/52684457/63667627-88669680-c80f-11e9-8fde-43b22df8f530.png)

![](https://user-images.githubusercontent.com/52684457/63667645-91576800-c80f-11e9-977f-d95cec584719.png)

![](https://user-images.githubusercontent.com/52684457/63667654-987e7600-c80f-11e9-9f8e-cbdc6884018e.png)

![](https://user-images.githubusercontent.com/52684457/63667689-ae8c3680-c80f-11e9-83d4-5d02cc54795b.png)

![](https://user-images.githubusercontent.com/52684457/63667699-b8159e80-c80f-11e9-859a-0d45860904db.png)

![](https://user-images.githubusercontent.com/52684457/63667708-c06dd980-c80f-11e9-99a6-186cd378e316.png)

![](https://user-images.githubusercontent.com/52684457/63667722-cb286e80-c80f-11e9-9656-0f823afcb5da.png)

![](https://user-images.githubusercontent.com/52684457/63667733-d2e81300-c80f-11e9-8e14-1a4510d5a56b.png)



![](https://user-images.githubusercontent.com/52684457/63668501-47bc4c80-c812-11e9-828d-c525a527b811.png)

- 이 방식은 반으로 쪼개어 양옆으로 탐색하는 방식



![](https://user-images.githubusercontent.com/52684457/63668677-b8636900-c812-11e9-8814-ed5bee03334a.png)

- 양 옆에서 값을 비교하는 방식

```python
def quickSort(a, low, high):
    if low < high:
        pivot = partition(a, low, high) # 피벗 구함
        quickSort(a, low, pivot-1) # 피벗보다 작은 부분을 다시 퀵정렬
        quickSort(a, pivot+1, high) # 피벗보다 큰 부분을 다시 퀵정렬

def partition(a, pivot, high):
    L = pivot + 1
    R = high
    while True:
        while L < high and a[L] < a[pivot]:
            L += 1
        while R > pivot and a[R] > a[pivot]:
            R -= 1
        if R <= L:
            break
        a[L], a[R] = a[R], a[L]
        L += 1
        R -= 1
    a[pivot], a[R] = a[R], a[pivot]
    return R

a = [54, 88, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전', a)
quickSort(a, 0, len(a)-1)
print('정렬 후', a)
```

- 이 외에 리스트의 가장 첫 원소를 피벗으로 선택해도 된다.
  - 이럴 경우 피벗의 다음 위치로 부터 오른쪽으로 움직이면서 크기를 비교하여 피벗보다 큰 데이터를 찾는다

##### :turtle: :vs: :rabbit2: 퀵 정렬의 최악의 시간 복잡도는 O(n^2)로, 합병정렬에 비해 좋지 못하다.

- 그런데 왜 "빠른"정렬이라고 했을까?
- 퀵정렬의 평균 복잡도는 nlog 이기 때문



![](https://user-images.githubusercontent.com/52684457/63668865-53f4d980-c813-11e9-8279-129018c0aad2.png)















































