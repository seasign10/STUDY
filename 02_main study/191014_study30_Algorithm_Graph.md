# :bar_chart: 그래프

- 그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현
- 그래프는 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조
  - |V| : 정점의 개수
  - |E| : 그래프에 포함된 간선의 개수
  - |V|개의 정점을 가지는 그래프는 최대 |V|(|V|-1)/2 간선이 가능
    *예) 5개의 정점이 있는 그래프의 최대 간선 수는 10(= 5\*4/2)개이다*
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이



## :old_key: 서로소 집합(Disjoint-sets)

![image](https://user-images.githubusercontent.com/52684457/66725440-00932500-ee6d-11e9-977a-db9c2ad1fece.png)

![image](https://user-images.githubusercontent.com/52684457/66725525-f32a6a80-ee6d-11e9-8a6a-b7778a5fcaa9.png)





### :family: 상호배타 집합 표현

#### :link: 연결리스트

![image](https://user-images.githubusercontent.com/52684457/66725534-0d644880-ee6e-11e9-95f5-0ef47f01676b.png)

![image](https://user-images.githubusercontent.com/52684457/66725591-82d01900-ee6e-11e9-9729-f0c232a84705.png)



#### :deciduous_tree: 트리

![image](https://user-images.githubusercontent.com/52684457/66725595-8f547180-ee6e-11e9-9fc5-c6f553106de5.png)

![image](https://user-images.githubusercontent.com/52684457/66725634-fd993400-ee6e-11e9-8707-83a48feaa977.png)

![image](https://user-images.githubusercontent.com/52684457/66725643-0b4eb980-ee6f-11e9-89a9-bc4499c350d7.png)

### 

### :family: 상호배타 집합에 대한 연산

![image](https://user-images.githubusercontent.com/52684457/66725671-51a41880-ee6f-11e9-9fd1-61b4cb4977ed.png)

![image](https://user-images.githubusercontent.com/52684457/66725677-67194280-ee6f-11e9-8cff-1a7c19e50f0a.png)

- 연산의 효율을 높이는 방법
  - Rank를 이용한 Union
    - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크Rank라는 이름으로 저장
    - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
  - Path compression
    - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.

![image](https://user-images.githubusercontent.com/52684457/66725812-240b9f00-ee70-11e9-8c88-2c6e3a2612cd.png)

![image](https://user-images.githubusercontent.com/52684457/66725824-34237e80-ee70-11e9-8c52-b22b827698ce.png)

![image](https://user-images.githubusercontent.com/52684457/66725827-3b4a8c80-ee70-11e9-8783-c53a9d9c83ec.png)

- `Make_Set()` 연산

  - Make_Set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

    ```python
    p[x] : 노드 x의 부모 저장
    rank[x] : 루트 노드가 x인 트리의 랭크 값 저장 
    
    Make_Set(x):
        p[x] <- x
        rank[x] <- 0
    ```

- `Find_Set()` 연산

  - Find_Set(x) : x를 포함하는 집합을 찾는 오퍼레이션

    ```python
    Find_Set(x):
        if x != p[x]:     # x가 루트가 아닌 경우
            p[x] <- Find_Set(p[x])
        return p[x]
    ```

- `Union` 연산

  - Union(x, y) : x와 y를 포함하는 두 집합을 통합하는 오퍼레이션

    ```python
    Union(x, y):
        Link(Find_Set(x), Find_Set(y))
        
    Link(x, y):
        if rank[x] > rank[y]:      # rank는 트리의 높이
            p[y] <- x
        else:
            p[x] <- y
            if rank[x] == rank[y]:
                rank[y]++
    ```



##### :green_book: 연습 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&&&

```python
# disjoint-set
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # p = [0] * V + 1 # 정점의 번호 1~V
    p = [x for x in range(V + 1)]

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]
    # def union(x, y):
    #     # a = find_set(x); b = find_set(y)
    #     # if a == b: return # 합칠 필요가 없기 때문에
    #     # p[b] = a
    #     p[y] = x
    ans = V # 초기 집합의 순 / 독립적으로 있기 때문에 따로 따로 씀
    for _ in range(E):
        u, v = map(int, input().split())
        a = find_set(u); b = find_set(v)
        if a == b: continue
        p[b] = a
        ans -= 1
```



# :evergreen_tree: 최소신장트리(MST)

- 그래프에서 최소 비용 문제
  1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
  2. 두 정점 사이의 최소 비용의 경로 찾기
- 신장 트리
  - n개의 정젖ㅁ으로 이루어진 무향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
- 최소신장트리 (Minimum Spanning Tree)
  - 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

![image](https://user-images.githubusercontent.com/52684457/66726992-5f5d9c00-ee77-11e9-84a2-ba25b8beb3cc.png)

- 각 간선에 주어진 가중치의 합이 최소로 최적 해를 구하는 것이 최소신장트리
- 즉 최소신장트리는 하나 (**단,** 간선의 가중치가 다 다른 값으로 가중치가 주어졌을 때)
- 같은 값을 가진 간선이 중복된 경우에는 여러개일 경우가 있다.
- *도로 건설 비용과 같은 문제에서 많이 쓰인다.*



### :seedling: MST 표현

![image](https://user-images.githubusercontent.com/52684457/66726936-0a218a80-ee77-11e9-8ae2-8e5389491166.png)

![image](https://user-images.githubusercontent.com/52684457/66726936-0a218a80-ee77-11e9-8ae2-8e5389491166.png)

### :seedling: Prime 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
  1. 임의 정점을 하나 선택해서 시작
  2. 선택한 정점과 인접하는 정점들 중의 **최소 비용의 간선**이 존재하는 정점을 선택
  3. 모든 정점이 선택될 때까지 1, 2 과정을 반복
- 서로소인 2개인 집합(2 djsjoint-sets) 정보를 유지
  - 트리의 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
  - 비트리 정점들(non-tree vertrices) - 선택 되지 않은 정점들

![image](https://user-images.githubusercontent.com/52684457/66727954-40620880-ee7d-11e9-9afd-f4e8a2a9d34b.png)

![image](https://user-images.githubusercontent.com/52684457/66727979-540d6f00-ee7d-11e9-92ec-40443602ead5.png)![image](https://user-images.githubusercontent.com/52684457/66727998-69829900-ee7d-11e9-8fe5-8e3f02c873a3.png)



### :seedling: KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
  1. 최초, 모든 간선을 가중치에 따라 **오름차순**으로 정렬
  2. 가중치가 가장 낮은 간선부터 선태갛면서 트리를 증가
     - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
  3. n-1개의 간선이 선택될 때까지 2.를 반복

![image](https://user-images.githubusercontent.com/52684457/66727217-9e402180-ee78-11e9-985d-9e80bb9f9335.png)![image](https://user-images.githubusercontent.com/52684457/66727223-a6985c80-ee78-11e9-9e98-00f410c92c53.png)

![image](https://user-images.githubusercontent.com/52684457/66727225-adbf6a80-ee78-11e9-9569-c0d3c78204fb.png)

![image](https://user-images.githubusercontent.com/52684457/66727228-b617a580-ee78-11e9-9d8c-b77119bda3ca.png)



##### :green_book: 연습

```python
# input.txt
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
```

```python
V, E = map(int, input().split())
# G = [[] for _ in range(V)] # 0 ~ V-1
Edge = []
for _ in range(E):
    # u, v, w = map(int, input().split())
    Edge.append(tuple(map(int, input().split())))
Edge.sort(key=lambda x: x[2])
p = [x for x in range(V)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
# V - 1
MST = []
cur = 0
while len(MST) < V - 1:
    u, v, w = Edge(cur)
    a = find_set(u); b = find_set(v)
    if a != b:
        p[b] = a
        MST.append((u, v, w))
        cur += 1
```



## :straight_ruler: 최단 경로

- 최단 경로 정의
  - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
  - 다익스트라(dijkstra) 알고리즘
    - 음의 가중치를 허용하지 않음
  - 벨만-포드(Bellman-Ford) 알고리즘
    - 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
  - 플로이드-워샬(Floyd-Warshall) 알고리즘



### :triangular_ruler: Dijkstra 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작정점(s)에서 끝정점(t) 까지의 최단 경로에 정점 x가 존재
  이 때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로구성
- 탐욕 기법을 사용한 알고지름으로 MST의 프림 알고리즘과 유사

![image](https://user-images.githubusercontent.com/52684457/66730780-b15dec00-ee8e-11e9-827e-21ce7c179853.png)

```text
weighted_graph.txt
8 10
1 2 2
1 3 3
2 4 3
2 5 5
3 6 1
4 7 4
5 6 1
5 7 1
6 8 6
7 8 2
```

```python
import sys; sys.stdin = open('weighted_graph.txt')

from queue import PriorityQueue

def DIJKSTRA_PRIORITYQ(s):

    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        d, u = Q.get()
        if d > D[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put((D[v], v))

    print(D[1: V + 1])
    print(P[1: V + 1])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

DIJKSTRA_PRIORITYQ(1)
```

```python
from queue import Queue

def BFS(s, G):

    D[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put(v)

    print()
# ----------------------------------------------

import sys
sys.stdin = open("weighted_graph.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0xfffff] * (V + 1)
P = [i for i in range(V + 1)]


for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


BFS(1, G)

print(D[1:])
print(P[1:])
```

![image](https://user-images.githubusercontent.com/52684457/66732014-26342480-ee95-11e9-856b-be6a660f076d.png)

![image](https://user-images.githubusercontent.com/52684457/66732020-30562300-ee95-11e9-9e56-a2bcd8593775.png)

![image](https://user-images.githubusercontent.com/52684457/66732038-4663e380-ee95-11e9-941a-f8d5a8f143ef.png)

![image](https://user-images.githubusercontent.com/52684457/66732044-4d8af180-ee95-11e9-8851-0dcb49cd0e39.png)

![image](https://user-images.githubusercontent.com/52684457/66732064-5bd90d80-ee95-11e9-8d3f-5e39ffa98494.png)

![image](https://user-images.githubusercontent.com/52684457/66732073-6398b200-ee95-11e9-9feb-5b8ee0986535.png)

![image](https://user-images.githubusercontent.com/52684457/66732099-698e9300-ee95-11e9-8ed6-78aa38ccf1a7.png)

