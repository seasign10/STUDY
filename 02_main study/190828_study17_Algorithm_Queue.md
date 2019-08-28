# :card_file_box: Algorithm : Queue

- ##### 큐(Queue)의 특성

  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 큐의 뒤에는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
  - 선입출구조( FIFO : First In First Out)
    - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)

![](https://user-images.githubusercontent.com/52684457/63818973-6dfefb00-c97e-11e9-99e1-e497f7ec4ab3.png)

#### :open_file_folder: 큐의 선입출 구조

![](https://user-images.githubusercontent.com/52684457/63819001-8b33c980-c97e-11e9-9dc2-6dd9e65c6889.png)

- 큐의 기본 연산

  - 삽입 : enQueue
  - 삭제 : deQueue

  

- 큐의 사용을 위해 필요한 주요 연산은 다음과 같다.

|     연산      | 기능                                                |
| :-----------: | :-------------------------------------------------- |
| enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산         |
|   deQueue()   | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산  |
| createQueue() | 공백의 상태를 큐를 생성하는 연산                    |
|   isEmpty()   | 큐가 공백상태인지를 확인하는 연산                   |
|   isFull()    | 큐가 포화상태인지를 확인하는 연산                   |
|    Qpeek()    | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산 |



##### :heavy_plus_sign: 큐의 연산과정

1. **공백 큐 생성** : createQueue();
   ![](https://user-images.githubusercontent.com/52684457/63819196-596f3280-c97f-11e9-82ba-cc0ab116bcc2.png)
2. **원소 A 삽입** : enQueue(A);
   ![](https://user-images.githubusercontent.com/52684457/63819205-5ecc7d00-c97f-11e9-9028-6321d8d7da0c.png)
3. **원소 B 삽입** : enQueue(B);
   ![](https://user-images.githubusercontent.com/52684457/63819211-62f89a80-c97f-11e9-9c17-aa1e125d65b8.png)
4. **원소 반환/삭제** : deQueue();
   ![](https://user-images.githubusercontent.com/52684457/63819274-a0f5be80-c97f-11e9-9d45-df3cadf20183.PNG)
5. **원소 C 삽입** : enQueue(C);
   ![](https://user-images.githubusercontent.com/52684457/63819275-a18e5500-c97f-11e9-8a89-d37f10329592.PNG)
6. **원소 반환/삭제** : deQueue();
   ![](https://user-images.githubusercontent.com/52684457/63819276-a18e5500-c97f-11e9-8174-00021958f660.PNG)
7. **원소 반환/삭제** : deQueue();
   ![4](https://user-images.githubusercontent.com/52684457/63819277-a18e5500-c97f-11e9-8873-be49a89be202.PNG)



####  :red_circle: 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - **front** : 저장된 첫 번째 원소의 인덱스
  - **rear** : 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기 상태 : front = rear = 1
  - 공백 상태 : front = rear
  - 포화 상태 : rear = n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)
- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front 와 rear를 -1로 초기화

![](https://user-images.githubusercontent.com/52684457/63819427-401ab600-c980-11e9-8421-a4034c536275.png)

![](https://user-images.githubusercontent.com/52684457/63819434-4872f100-c980-11e9-8d5c-d735f32f2a1f.png)

![](https://user-images.githubusercontent.com/52684457/63819446-4f99ff00-c980-11e9-92d9-441aaa29a3df.png)

![](https://user-images.githubusercontent.com/52684457/63819456-56c10d00-c980-11e9-8136-532a5ae6e4cc.png)



- 예제

```python
# 큐를 구현하여 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
# 큐에서 세개의 데이터를 차례로 꺼내서 출력
# ====>  1, 2, 3 이 출력

import queue

q = queue.Queue()
q.put('A')
q.put('B')
q.put('C')

while not q.empty():
    print(q.get())
```



#### :red_circle: 선형 큐 이용시의 문제점



![](https://user-images.githubusercontent.com/52684457/63820515-79552500-c984-11e9-8eec-5fe56451ce3d.png)

![](https://user-images.githubusercontent.com/52684457/63820523-81ad6000-c984-11e9-88fb-418a5ed387c9.png)

#### :red_circle: 원형큐의 구조

- ###### 초기 공백 상태

  - front = rear = 0

  

- ###### index의 순환

  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
  - 이를 위해 나머지 연산자 mod를 사용

  

- ###### front 변수

  - 공백 상태와 포화 상태 구분을 쉽게하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

  

- ###### 삽입 위치 및 삭제 위치

  |        |        삽입 위치        |         삭제 위치         |
  | :----: | :---------------------: | :-----------------------: |
  | 선형큐 |     rear = rear + 1     |    front = front  + 1     |
  | 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |



- ###### 원형 큐의 연산 과정

  ![](https://user-images.githubusercontent.com/52684457/63820784-8c1c2980-c985-11e9-92a4-6a413dfe6f12.PNG)

  ![](https://user-images.githubusercontent.com/52684457/63820785-8c1c2980-c985-11e9-9ed4-650b2f4e0d48.PNG)

  ![](https://user-images.githubusercontent.com/52684457/63820786-8c1c2980-c985-11e9-9c3f-0f951c47caa5.PNG)

#### :red_circle: 원형 큐의 구현

- ###### 초기 공백 큐 생성

  - 크기 n인 1차원 배열 생성
  - front와 rear를 0으로 초기화

![](https://user-images.githubusercontent.com/52684457/63820888-f0d78400-c985-11e9-932c-63d56d006265.png)

![](https://user-images.githubusercontent.com/52684457/63820898-fb921900-c985-11e9-84e1-cd6b14aa34f8.png)

![](https://user-images.githubusercontent.com/52684457/63820906-0482ea80-c986-11e9-90ff-1ed77b341c9b.png)



- 원형 큐의 구현 예 (C코드)

![](https://user-images.githubusercontent.com/52684457/63820911-0cdb2580-c986-11e9-9a51-42d4e0bf930c.png)

```python
def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item): # 원형 큐의 삽입 연산
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

def deQueue(): # 원형 큐의 삭제 연산
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

cQ_SIZE=3
cQ=[0]*cQ_SIZE

front = rear = 0 # front와 rear를 0으로 초기화

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())
```





#### :red_circle: 연결 큐의 연산과정

![](https://user-images.githubusercontent.com/52684457/63821916-a7893380-c989-11e9-8907-9a80fffebdc2.png)

![](https://user-images.githubusercontent.com/52684457/63821932-b1129b80-c989-11e9-8477-4b18c42cedb4.png)

![](https://user-images.githubusercontent.com/52684457/63821939-b66fe600-c989-11e9-9c61-57008f1ad5ad.png)

![](https://user-images.githubusercontent.com/52684457/63821963-cbe51000-c989-11e9-99fd-619a00bccfb7.png)

#### :red_circle: 연결 큐의 구현

![](https://user-images.githubusercontent.com/52684457/63822329-fedbd380-c98a-11e9-9296-6ddc5f5ab191.PNG)

![](https://user-images.githubusercontent.com/52684457/63822331-fedbd380-c98a-11e9-909b-849c41aa6ea3.PNG)

![](https://user-images.githubusercontent.com/52684457/63822332-ff746a00-c98a-11e9-9215-0592b83b9f74.PNG)

![](https://user-images.githubusercontent.com/52684457/63822333-ff746a00-c98a-11e9-8451-84b97c70f75a.PNG)



#### :red_circle: 연결 큐의 구현 예 (PYTHON)

![](https://user-images.githubusercontent.com/52684457/63822335-ff746a00-c98a-11e9-9312-7b62b1a1d2b7.PNG)

![](https://user-images.githubusercontent.com/52684457/63822336-ff746a00-c98a-11e9-836d-324da8ea40f2.PNG)

![](https://user-images.githubusercontent.com/52684457/63822339-000d0080-c98b-11e9-91e2-ad50494a2f9d.PNG)



#### :red_circle: 우선순위 큐 (Priority Queue)

- ###### 우선순위 큐의 특성

  - 우선 순위를 가진 항목들을 저장하는 큐
  - FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

- ###### 우선순위 큐의 적용 분야

  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링

- ###### 우선순위 큐의 구현

  - 배열을 이용한 우선순위 큐
  - 리스트를 이용한 우선순위 큐

- ###### 우선순위 큐의 기본 연산

  - 삽입 : enQueue
  - 삭제 : deQueue

  ![](https://user-images.githubusercontent.com/52684457/63822981-27fd6380-c98d-11e9-961e-8600bf899fcc.png)

#### :red_circle: 배열을 이용한 우선순위 큐

- ###### 배열을 이용하여 우선순위 큐 구현

  - 배열을 이용하여 자료 저장
  - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  - 가장 앞에 최고 우선순위의 원소가 위치하게 됨

- ###### 문제점

  - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
  - 이에 소요되는 시간이나 메모리 낭비가 큼



#### :red_circle: 큐의 활용 : 버퍼

- ###### 버퍼

  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

- ###### 버퍼의 자료 구조

  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
  - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용

- ###### 키보드 버퍼

![](https://user-images.githubusercontent.com/52684457/63823121-b1ad3100-c98d-11e9-9263-9e68c9f51cd1.png)

## :red_car: BFS(Breadth First Search)​

- 그래프를 탐색하는 방법에는 크게 두 가지가 있음
  - 깊이 우선 탐색(Depth First Search, DFS)
  - 너비 우선 탐색(Breadth First Search, BFS)
- 너비 우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우서탐색을 진행히야 하므로, 선입선출 형태의 자료구조인 큐를 활용

![](https://user-images.githubusercontent.com/52684457/63823498-08ffd100-c98f-11e9-9036-feeaa11389f2.png)

![](https://user-images.githubusercontent.com/52684457/63823511-1026df00-c98f-11e9-98d5-c7c9451f5a17.png)

![](https://user-images.githubusercontent.com/52684457/63825059-38fda300-c994-11e9-88d1-d8b185396838.PNG)

![](https://user-images.githubusercontent.com/52684457/63825060-38fda300-c994-11e9-9034-7d8bca9ae4ab.PNG)

![](https://user-images.githubusercontent.com/52684457/63825061-39963980-c994-11e9-81cf-f3d4302f360b.PNG)

![](https://user-images.githubusercontent.com/52684457/63825062-39963980-c994-11e9-8025-354b7faff98d.PNG)

![](https://user-images.githubusercontent.com/52684457/63825063-39963980-c994-11e9-804c-cf847b78c991.PNG)

![](https://user-images.githubusercontent.com/52684457/63825064-39963980-c994-11e9-8a55-2a9a0040af2e.PNG)

![](https://user-images.githubusercontent.com/52684457/63825066-3a2ed000-c994-11e9-91a8-39a045a4407b.PNG)

![](https://user-images.githubusercontent.com/52684457/63825067-3a2ed000-c994-11e9-9d8b-475c026070c1.PNG)

![](https://user-images.githubusercontent.com/52684457/63825068-3a2ed000-c994-11e9-97a4-efd8eb7136c3.PNG)







































