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



#### :pen: 고지식한 방법 (brute-force)

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





## :boxing_glove: 탐욕(Greedy) 알고리즘

- 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적인 방법
- 일반적으로, 머리 속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근
- 여러 경우 중 하나를 선택할 때 마다 그 순간에 최적이라 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택 시점에서 이룽지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하며, <u>**그것이 최적이란 보장은 없다.**</u>



- 일단 한번 선택된것은 번복*(번복하는 것의 대표적인 예/ 백트래킹)*하지 않는다. 이런 특성 때문에 대부분의 탐욕 알고리즘들은 단순, 또한 제한적인 문제들에 적용
- 최적화 문제(optimization)란 가능 해들 중에서 가장 좋은(최대 또는 최소)해를 찾는 문제



> ##### 탐욕 알고리즘의 동작 과정
>
> 1. **해 선택** : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 
>                   이를 부분해집합(Solution Set)에 추가한다.
> 2. **실행 가능성 검사** : 새로운 부분 해 집합이 실행 가능한지를 확인한다.
>                                    곧 문제의 제약 조건을 위반하지 않았는 지를 검사한다.
> 3. **해 검사** : 새로운 부분 해 집합이 문제의 해가 되는지를 확인한다.
>                    아직 전체 문제의 해가 완성되지 않았다면 1의 해 선택부터 다시 시작한다.



#### :green_book: 문제 제시 : 배낭 짐싸기(Knapsack)

- 도둑은 부자들의 값진 물건들을 훔치기 위해 보관 창고에 침입하였다.
  도둑은 훔친 물건을 배낭에 담아 올 계획이다. 배낭은 담을 수 있는 물건의 총 무게(W)가 정해져 있다. 창고에는 여러 개(n개)의 물건들이 잇고 각각의 물건에는 무게와 값이 정해져있다. 경비원들에게 발각되기 전에 배낭이 수용할 수 있는 무게를 초과하지 않으면서, 값이 최대가 되는 물건들을 담아야 한다.

> **배낭(30kg)**
>
> | 물건  | 무게 |    값    |
> | :---: | :--: | :------: |
> | 물건1 | 25KG | 10천만원 |
> | 물건2 | 10KG | 9천만원  |
> | 물건3 | 10KG | 5천만원  |
> |  ...  | ...  |   ...    |

![](https://user-images.githubusercontent.com/52684457/65004727-5c36c500-d938-11e9-9fb0-4e783cc50644.png)

- Knapsack 문제 유형
  - **0-1 Knapsack**
    - 배낭에 물건을 통째로 담아야 하는 문제
    - 물건을 쪼갤 수 없는 경우
  - **Fractional Knapsack**
    - 물건을 부분적으로 담는 것이 허용되는 문제
    - 물건을 쪼갤 수 있는 경우

![image](https://user-images.githubusercontent.com/52684457/65004832-bafc3e80-d938-11e9-8ac5-9b3e262bdd5a.png)

![image](https://user-images.githubusercontent.com/52684457/65004845-c8b1c400-d938-11e9-8132-d8b4b049530b.png)

![image](https://user-images.githubusercontent.com/52684457/65004857-d8c9a380-d938-11e9-9a5c-6d7c6df85b62.png)

![image](https://user-images.githubusercontent.com/52684457/65004870-e41ccf00-d938-11e9-8fb0-46a66ecc2465.png)



#### :green_book: 문제 제시 : 회의실 배정하기

- 김대리는 소프트웨어 개발팀들의 회의실 사용 신청을 처리하는 업무를 한다. 이번 주 금요일에 사용가능한 회의실은 하나만 존재하고 다수의 회의가 신청된 상태이다.

- 회의는 시작 시간과 종료 시간이 있으며, 회의 시간이 겹치는 회의들은 동시에 열릴 수 없다.

- 가능한 많은 회의가 열리기 위해서는 회의들을 어떻게 배정해야 할까?

- 입력 예

  - 회의 개수

  - (시작시간, 종료 시간)

    ```
    10
    1 4  1 6  6 10  5 7  3 8  5 9  3 5  8 11  2 13  12 14
    ```

    

> ##### 활동 선택(Activity-selection problem) 문제
>
> ![image](https://user-images.githubusercontent.com/52684457/65005003-58f00900-d939-11e9-85ec-750dd393e72a.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005026-7624d780-d939-11e9-979e-7fdac99c8c43.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005047-85a42080-d939-11e9-82a0-68f69795fdc6.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005066-93f23c80-d939-11e9-83aa-6348b103c31c.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005089-ae2c1a80-d939-11e9-86dc-d976da0a177f.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005110-bbe1a000-d939-11e9-8b42-80bb9c0f3e2a.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005133-cdc34300-d939-11e9-8772-926ccce88bf5.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005160-e2074000-d939-11e9-8f01-f14bc6d5b03f.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65005183-f3e8e300-d939-11e9-84cb-5f70932a8d07.png)

**탐욕 알고리즘의 필수 요소**

- 탐욕적 선택 속성(greedy choice property)
  - 탐욕적 선택은 최적해로 갈수 있음을 보여라
    **=>** 즉, 탐욕적 선택은 항상 안전하다.
- 최적 부분 구조(optimal substructure property)
  - 최적화 문제를 정형화하라
    **=>** 하나의 선택을 하면 풀어야 할 하나의 하위 문제가 남는다. 
- <u>**[원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해]**</u> 임을 증명하라



- 탐욕 기법과 동적 계획법의 비교

  |                          탐욕 기법                           |                       동적 계획법                       |
  | :----------------------------------------------------------: | :-----------------------------------------------------: |
  | 매 단계에서, 가장 좋게 보이는 것을 빠르게 선택한다.<br />**=>** 지역 최적 선택(local oprimal choice) | 매 단계의 선택은 해결한 하위 문제의 해를 기반으로 한다. |
  |    하위 문제를 풀기 전에 (탐욕적) 선택이 먼저 이루어진다.    |               하위 문제가 우선 해결된다.                |
  |                        Top-down 방식                         |                     Bottom-up 방식                      |
  |                 일반적으로, 바르고 간결하다.                 |                 좀더 느리고, 복잡하다.                  |



- 대표적인 탐욕 기법의 알고리즘들

  |      알고리즘       |                             목적                             |                             설명                             |  유형  |
  | :-----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----: |
  |        Prim         |       N 개의 노드에 대한 최소 신장 트리(MST)를 찾는다.       |             서브드리를 확장하면서 MST를 찾는다.              | 그래프 |
  |       Kruskal       |                         Prim과 동일                          |     싸이클이 없는 서브 그래프를 확장하면서 MST를 찾는다.     | 그래프 |
  |      Dijkstra       |    주어진 정점에서 다른 정점들에 대한 최단 경로를 찾는다.    | 주어진 정점에서 가장 가까운 정점을 찾고, 그 다음을 정점을 반복해서 찾는다. | 그래프 |
  | Huffman tree & code | 문서의 압축을 위해 문자들의 빈도수에 따라 코드값을 부여한다. | 출현 빈도가 낮은 문자부터 선택해서 이진 트리를 완성하고 코드값을 부여한다. | 문자열 |



> **탐욕 기법을 통한 Baby-gin 문제 해결**
>
> - 완전검색 아닌 방법으로 풀어보자.
>   - 6개의 숫자는 6자리의 정수 값으로 입력된다.
>   - counts 배열의 각 원소를 체크하여 run과 triplet 및 baby-gin 여부를 판단한다.
>
> ![image](https://user-images.githubusercontent.com/52684457/65007340-c5223b00-d940-11e9-8c6b-afe2cfa978a5.png)
>
> ![image](https://user-images.githubusercontent.com/52684457/65007357-d408ed80-d940-11e9-9105-f05733ff24cb.png)



#### :page_with_curl: 탐욕적 선택 속성

**종료 시간이 가장 빠른 활동 am을 선택하는 것은 항상 안전하다.**

- 전체 활동들의 집합 Si,j에서 양립 가능한 최대 크기의 부분 집합인 Ai,j가 있다.
- ak는  Ai,j에 속한 종료 시간이 가장 빠른 활동
- 만약, ak = am 이면 최대 크기 부분 집합에 포함
- 만약, ak != am 이면 Ai,j 에서 ak를 제거하고 am을 추가한다. 이 때, am은 ak보다 종료시간이 빠르기 때문에 Ai,j에 들어있는 다른 활동들과 겹치지 X
- 따라서, 종료 시간이 가장 빠른 활동을 선택하는 것은 항상 안전하다.


