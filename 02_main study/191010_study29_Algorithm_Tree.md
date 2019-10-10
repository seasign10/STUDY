# :card_file_box: Algorithm : :evergreen_tree:Tree:evergreen_tree:

- 트리는 싸이클이 없는 무향 연결 그래프이다.
  - 두 노드(or 정점) 사이에는 유일한 경로가 존재
  - 각 노드는 최대 하나의 부모 노드가 존재 가능
  - 각 노드는 자식 노드가 없거나 하나 이상이 존재할 수 있다.
- 비선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관계를 가지는 계층형 자료구조



## :palm_tree: 트리 정의

- 한 개 이상의 노드로 이루어진 노드를 루트(root)
- 나머지 노드들은 n(>=0)개의 분리 집합 T1, ...TN으로 분리될 수 있다.
- 이들 T1, ...TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 서브 트리(subtree)라 한다.![image](https://user-images.githubusercontent.com/52684457/66529505-b2191a00-eb3e-11e9-8e33-d772e7592285.png)

## :palm_tree: 트리 용어

- **노드(node)** : 트리의 원소이고 정점(vertex)이라고도 한다.
  - 트리 T의 노드 - A, B, C, D, E, F, G, H, I, J, K
- **간선(edge)** : 노드를 연결하는 선
  - 부모 노드와 자식 노드를 연결
- **루트 노드(root node)**  : 트리의 시작 노드
  - 트리 T의 루트노드 - A

![image](C:\Users\student\Desktop\이 폴더만 빌리겠읍니다ㅎㅎ\algorithms-master\191001_보충\66529602-fdcbc380-eb3e-11e9-9a7a-23f895c41946.png)

- **형제 노드(sibling node)** : 같은 부모 노드의 자식 노드들
  - B, C, D는 형제 노드
- **조상 노드** : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  - K의 조상 노드 : F, B, A
- **서브 트리(sub tree)** : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- **자손 노드** : 서브 트리에 있는 하위 레벨의 노드들
  - B의 자손 노드 - E, F, K

![image](https://user-images.githubusercontent.com/52684457/66529851-08d32380-eb40-11e9-94c0-1c9f3d528be9.png)

- **차수(degree)**
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
    - B의 차수 = 2, C의 차수 = 1
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
    - 트리 T의 차수 = 3
  - 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드
- **높이**
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
    - B의 높이 = 1, F의 높이 = 2
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨
    - 트리 T의 높이 = 3

![image](https://user-images.githubusercontent.com/52684457/66529957-77b07c80-eb40-11e9-941e-9ffabb4c15d9.png)



### :deciduous_tree: 이진 트리(Binary Tree)

- 모든 노드들이 최대 2개의 서브 트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드(left child node)
  - 오른쪽 자식 노드(right child node)
- 이진 트리의 예

![image](https://user-images.githubusercontent.com/52684457/66529994-b7776400-eb40-11e9-8e2f-bdfaf73faa84.png)



#### :leaves: 특성

- 레벨 i에서의 노드 최대 개수는 2<sup>i</sup>개
- 높이가 h인 이진 트리가 가진 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2<sup>h+1</sup>-1)개가 된다.

![image](https://user-images.githubusercontent.com/52684457/66530042-fe655980-eb40-11e9-8c1d-4efb17663ce2.png)

#### :leaves: 종류

- **포화 이진 트리(Full Binary Tree)**
  - 모든 레벨에 노드가 포화상태로 채워져 있는 이진 트리
  - 높이가 h일 때, 최대의 노드 개수인 (2<sup>h+1</sup>-1)의 노 드를 가진 이진 트리
    - 높이 3일 때 2<sup>3+1</sup>-1 = 15개의 노드
  - 루트를 1번으로 하여 2<sup>h+1</sup>-1 까지 정해진 위치에 대한 노드 번호를 가짐

![image](https://user-images.githubusercontent.com/52684457/66530110-5603c500-eb41-11e9-917e-af6fbe95a362.png)



- **완전 이진 트리(Complete Binary Tree)**
  - 높이가 h이고 노드 수가 n개일 때 (단, 2<sup>h</sup> <= n <= 2<sup>h+1</sup>-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
  - 예) 노드가 10개인 완전 이진 트리

![image](https://user-images.githubusercontent.com/52684457/66530162-9b27f700-eb41-11e9-81da-d11b76ff200f.png)



- **편향 이진 트리(Skewed Binary Tree)**
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리

![image](https://user-images.githubusercontent.com/52684457/66530201-c27ec400-eb41-11e9-9d6c-e262cc2d2805.png)

#### :leaves: 순회(traversal)

-  순회란 트리의 각 노드를 중복되지 않게 전부 방문(visit) 하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
- 따라서 특별한 방법이 필요

- **순회 :** 트리의 토드들을 체계적으로 방문하는 것
- 3가지의 기본적인 순회방법
  - **전위 순회(preorder traversal) : VLR**
    - 자손 노드보다 현재 노드를 먼저 방문
  - **중위 순회(inorder traversal) : LVR**
    - 왼쪽 자손 노드, 현재 노드, 오른쪽 자손 노드 순으로 방문
  - **후위 순회(postorder traversal) : LRV**
    - 현재 노드보다 자손 노드를 먼저 방문

![image](https://user-images.githubusercontent.com/52684457/66530381-8304a780-eb42-11e9-848c-9431b9c9e9f8.png)

![image](https://user-images.githubusercontent.com/52684457/66530406-a596c080-eb42-11e9-84b9-84e18b268826.png)

![image](https://user-images.githubusercontent.com/52684457/66530414-ae879200-eb42-11e9-9d3f-7f76ca3f2339.png)

![image](https://user-images.githubusercontent.com/52684457/66530606-6ae15800-eb43-11e9-9d87-f3fb052fa4d0.png)

![image](https://user-images.githubusercontent.com/52684457/66530620-759bed00-eb43-11e9-9799-85667be7c0a3.png)

![image](https://user-images.githubusercontent.com/52684457/66531283-2efbc200-eb46-11e9-8361-7cf6788933e1.png)

![image](https://user-images.githubusercontent.com/52684457/66531291-3622d000-eb46-11e9-99a1-0bdcbd9d6e81.png)

#### :leaves: 트리의 표현

![image](https://user-images.githubusercontent.com/52684457/66531399-9c0f5780-eb46-11e9-8d61-5adebea80d88.png)

![image](https://user-images.githubusercontent.com/52684457/66531417-ae899100-eb46-11e9-9d59-cf01631de287.png)

![image](https://user-images.githubusercontent.com/52684457/66532041-eb568780-eb48-11e9-81de-a7fa63e5704b.png)

![image](https://user-images.githubusercontent.com/52684457/66532452-6bc9b800-eb4a-11e9-8d92-cf1e360833c4.png)

- 배열을 이용한 이진 트리의 표현의 **단점**
  - 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입, 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적



##### :wilted_flower: 연결 리스트



![image](https://user-images.githubusercontent.com/52684457/66532724-6325b180-eb4b-11e9-91f4-8815cdbf3d55.png)

![image](https://user-images.githubusercontent.com/52684457/66532745-7cc6f900-eb4b-11e9-91ff-d29d57264ef0.png)

****

##### :green_book: 연습 문제

![image](https://user-images.githubusercontent.com/52684457/66533065-9583de80-eb4c-11e9-97ff-2befb76b1504.png)

- **간선의 수 : 13** *(위의 이미지는 오타)*

- **전위 :** 1 → 2 → 4 → 7 → 12 → 3 → 5 → 8 → 9 → 6 → 10 → 11 → 13

- **중위 :** 12 → 7 → 4 → 2 → 1 → 8 → 5 → 9 → 3 → 10 → 6 → 13 → 11

- **후위 :** 12 → 7 → 4 → 2 → 8 → 9 → 5 → 10 → 13 → 11 → 6 → 3 → 1



```python
# N = 13
# arr = 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder(n): # 전위 순회
    if n != 0:
        print(n, end=" ")
        preorder(child[n][0])
        preorder(child[n][1])

def inorder(n): # 중위 순회
    if n != 0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])

def postorder(n): # 후위 순위
    if n != 0:
        postorder(child[n][0])
        postorder(child[n][1])
        print(n, end=" ")

N = int(input())
arr = list(map(int, input().split()))
child = [[0]*2 for i in range(N+1)]

for i in range(N-1):
    if child[arr[i*2]][0] == 0: # 부모 노드 i*2에 자식 노드가 없는 경우]
        child[arr[i*2]][0] = arr[i*2+1]
    else: # 이미 자식이 한 개 있는 경우
        child[arr[i*2]][1] = arr[i*2+1]

print('전위 순회 결과: ', end=" ")
preorder(1)
print()

print('중위 순회 결과: ', end=" ")
inorder(1)
print()

print('후위 순회 결과: ', end=" ")
postorder(1)
print()
```

****

#### :leaves: 연산

- 이진 탐색 트리의 연산

![ ](https://user-images.githubusercontent.com/52684457/66533076-9fa5dd00-eb4c-11e9-9eed-90762d95200d.png)

![image](https://user-images.githubusercontent.com/52684457/66536713-dd106780-eb58-11e9-9906-4553e5b26b3b.png)

![image](https://user-images.githubusercontent.com/52684457/66536931-ac7cfd80-eb59-11e9-8795-1f4d7df15f58.png)

![image](https://user-images.githubusercontent.com/52684457/66537038-07165980-eb5a-11e9-865c-8bc940982636.png)

#### :leaves:  삭제​

![image](https://user-images.githubusercontent.com/52684457/66540155-d63c2180-eb65-11e9-84bd-10bdfc94c3b9.png)



![image](https://user-images.githubusercontent.com/52684457/66540206-0daace00-eb66-11e9-9938-d2e4e4d07f9d.png)



**삭제하려는 노드가 단말 노드일 경우[차수 = 0]**

- 단말 노드는 자식 노드를 갖지않으므로 단말노드를 삭제하고 부모노드를 찾아서 링크 필드를 NULL로 설정하여 연결을 끊어줌



![image](https://user-images.githubusercontent.com/52684457/66540217-14d1dc00-eb66-11e9-8a08-538f665a22b3.png)

**삭제하려는 노드가 하나의 자식 노드[차수=1]**

- 삭제되는 노드가 왼쪽이나 오른쪽 서브트리 중 하나만 갖는 경우 그 노드는 삭제하고 서브 트리를 부모 노드를 향하도록 함



![image](https://user-images.githubusercontent.com/52684457/66540228-1ac7bd00-eb66-11e9-8522-53eb7859efdd.png)

**삭제하려는 노드가 두개의 서브트리를 가진 경우[차수=2]**

- 노드를 삭제하면 자식 노드들은 트리에서 연결이 끊어지게 됨
- 노드가 삭제된 후에도 이진 탐색 트리가 유지되어야 하므로 트리를 재구성 해야함
- 자손 노드 중에 삭제한 노드의 자리에 들어올 노드를 선택해야 함
- 이때 삭제 노드와 가장 비슷한 값을 가진 노드를 삭제 노드위치로 가져와야 함 
- 삭제 노드와 가장 비슷한 값을 가진 노드는 왼쪽 서브 트리에서 가장 큰 키 값을 가진 노드이거나 오른쪽 서브트리에서 가장 작은 키 값을 가진 노드



#### :leaves: 성능

- 탐색(searching), 삽입(insertion), 삭제(deletion) 시간은 트리의 높이만큼 시간이 걸린다.
  - O(h), h : BTS의 깊이(height) 

![image](https://user-images.githubusercontent.com/52684457/66540955-8e6ac980-eb68-11e9-9263-457dfdfd5a60.png)

- 평균의 경우

  - 이진 트리가 균형적으로 생성되어 있는 경우
  - O(log n)

- 최악의 경우

  - 한쪽으로 치우친 편향 이진 트리의 경우
  - O(n)
  - 순차탐색과 시간복잡도가 같음

  

## :deciduous_tree: 힙(heap)

![1570684633464](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570684633464.png)

![image](https://user-images.githubusercontent.com/52684457/66541038-d8ec4600-eb68-11e9-871b-6fbb6d512c35.png)

- 최대 힙 삭제 연산을 순차적으로 하면 내림차순,
- 최소 힙 삭제 연산을 순차적으로 하면 오름차순으로 정렬이 가능



![image](https://user-images.githubusercontent.com/52684457/66541062-f3262400-eb68-11e9-8c20-fcd7f2c26955.png)

- **트리 1 :** 왼쪽순으로 달려야 하는데 1이 오른쪽 순으로 달림
- **트리 2 :** 8을 봤을 때 최소 힙도 최대 힙도 아님



![image](https://user-images.githubusercontent.com/52684457/66541194-662f9a80-eb69-11e9-92da-3d3218214a12.png)

![image](https://user-images.githubusercontent.com/52684457/66541308-d3433000-eb69-11e9-8f61-de5d564e16bd.png)



![image](https://user-images.githubusercontent.com/52684457/66541214-78a9d400-eb69-11e9-8741-60d1f9ae4abf.png)



#### :leaves: 삭제

- 힙에서는 루트 노드의 원소만을 삭제 할 수 있다.
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
  - 우선순위 큐와 비교

![image](https://user-images.githubusercontent.com/52684457/66541470-59f80d00-eb6a-11e9-96eb-d4f94591879d.png)

- 차순 관계에 상관없이 첫번째로 완전 이진 트리를 생성 후, 값을 비교하며 맞는 자리에 값을 교환한다.



#### :leaves: 활용

![image](https://user-images.githubusercontent.com/52684457/66541487-69775600-eb6a-11e9-83ed-d60be9f39a54.png)

![image](https://user-images.githubusercontent.com/52684457/66541573-ac392e00-eb6a-11e9-829f-d2e581d8a038.png)



