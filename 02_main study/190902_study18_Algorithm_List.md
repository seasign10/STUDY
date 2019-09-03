

# :card_file_box: Algorithm : List

- ##### **리스트**

  - 순서를 가진 데이터의 집합을 가리키는 추상자료형(abstract data type)
  - 동일한 데이터를 가지고 있어도 상관없다.

  - 구현방법에 따라 크게 두 가지로 나뉜다.
    1. **순차 리스트** : 배열을 기반으로 구현된 리스트
    2. **연결 리스트** : 메모리의 동적할당을 기반으로 구현된 리스트



- 리스트의 사용을 위해 필요한 주요 함수는 다음과 같음

|    함수명    |                      기능                      |
| :----------: | :--------------------------------------------: |
| addtoFirst() |      리스트의 앞쪽에 원소를 추가하는 연산      |
| addtoLast()  |      리스트의 뒤쪽에 원소를 추가하는 연산      |
|    add()     |   리스트의 특정 위치에 원소를 추가하는 연산    |
|   delete()   | 리스트의 특정 위치에 있는 원소를 삭제하는 연산 |
|    get()     | 리스트의 특정 위치에 있는 원소를 리턴하는 연산 |



- ###### 순차 리스트

![](https://user-images.githubusercontent.com/52684457/64085397-7172f780-cd6d-11e9-99df-de4f30b9b842.png)
![](https://user-images.githubusercontent.com/52684457/64085400-789a0580-cd6d-11e9-81ef-4bb22834956a.png)

- 순차 리스트의 문제점
  - 단순 배열을 이용해 순차리스트를 구현해 사용하는 경우, 자료의 삽입/삭제 연산 과정에서 연속적인 메모리 배열을 위해 원소들을 이동시키는 작업이 필요
  - 원소의 개수가 많고 삽입/삭제 연산이 빈번하게 일어날수록 작업에 소요되는 시간이 크게 증가
  - 배열의 크기가 정해져 있는 경우, 실제로 사용될 메모리보다 크게 할당하여 메모리의 낭비를 초래할 수도 있고, 반대로 할당된 메모리보다 많은 자료를 사용하여 새롭게 배열을 만들어 작업을 해야 하는 경우가 발생할 수도 있다.



- ###### 연결 리스트(Linked List)

  - 특성
    - 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.
    - 링크를 통해 원소에 접근하므로, 순차 리스트에처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다.
    - 자료구조의 크기를 동적으로 조정할 수 있어, 메모리의 효율적인 사용이 가능
      - 쓸 일이 없으면 반납, 사용할 일이 있으면 할당











- ##### 연결 리스트의 기본 구조

![](https://user-images.githubusercontent.com/52684457/64085622-e692fc80-cd6e-11e9-8c32-2f0c3e55a6d7.png)













#### :closed_lock_with_key: 단순 연결 리스트(Singly Linked List)



![](https://user-images.githubusercontent.com/52684457/64085633-f27ebe80-cd6e-11e9-876d-525c680b01f7.png)















- ##### 단순 연결리스트의 삽입/삭제 연산

![](https://user-images.githubusercontent.com/52684457/64085638-fa3e6300-cd6e-11e9-892e-44fdc483aaa4.png)

![](https://user-images.githubusercontent.com/52684457/64085644-02969e00-cd6f-11e9-94a7-da494bdd2fa3.png)

![](https://user-images.githubusercontent.com/52684457/64085800-bbf57380-cd6f-11e9-9231-79d7c2155de9.png)

![](https://user-images.githubusercontent.com/52684457/64085802-c152be00-cd6f-11e9-8f7f-89b24d5c57ab.png)

![](https://user-images.githubusercontent.com/52684457/64085807-c7489f00-cd6f-11e9-8b76-5ba790da2b4a.png)

![](https://user-images.githubusercontent.com/52684457/64085816-d2033400-cd6f-11e9-9d02-6afe25e4f9d6.png)

![](https://user-images.githubusercontent.com/52684457/64085827-dcbdc900-cd6f-11e9-95ab-ad4072121f3c.png)



```python
class Node: # 객체를 초기화하는 특별한 함수 / 생성자
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data): # 첫 노드에 데이터 삽입
        global  Head
        Head = Node(data, Head) # 새로운 노드 생성

data = [1, 2, 3, 4]
Head = None

for i in range(len(data)):
    addtoFirst(data[i])

while Head.link != None:
    print(Head.data, end='=>')
    Head = Head.link
print(Head.data)
```

- 가장 처음 Head는 None값을 가진다.

  - 1이 들어왔을 때, => 1, None

  - 2가 들어왔을 때, => 2, 1

  - 3이 들어왔을 때, => 3, 2

    . . . 

  - 이전의 Head값이 들어오는 것을 알 수 있다.

-  `def addFirst(data):`  : Head가 Node를 가르키도록

- `while Head.link != None:` : Head의 link를 None이 될 때 까지 따라간다.

![](https://user-images.githubusercontent.com/52684457/64086531-daf60480-cd73-11e9-8ade-6057106a9095.png)

python tutor => http://pythontutor.com/visualize.html#mode=edit

![](https://user-images.githubusercontent.com/52684457/64086222-e1837c80-cd71-11e9-974e-e9d77aa24f4e.png)

![](https://user-images.githubusercontent.com/52684457/64086983-fcf08680-cd75-11e9-8adf-83bba0082661.png)



```python
def add(pre, data): # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
```

![](https://user-images.githubusercontent.com/52684457/64086595-23adbd80-cd74-11e9-8b28-f2034b8383f1.png)



```python
def addtoLast(data): # 마지막에 데이터 삽입
    global Head
    if Head == None: # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을 때 까지
            p = p.link
        p.link = Node(data, None)
```

![](https://user-images.githubusercontent.com/52684457/64086714-b9e1e380-cd74-11e9-9f54-da73769578e9.png)



```python
def delete(pre): # 다음 노드 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
        
def deleteFirst(): # 처음 노드 삭제
    global Head
    if pre == None:
        print('error')
    else:
        Head= Head.link
```

![](https://user-images.githubusercontent.com/52684457/64087240-2827a580-cd77-11e9-8451-221a98ec35a2.png)



















#### :closed_lock_with_key: 이중 연결 리스트(Doubley Linked List)

- 특성
  - 양쪽 방향으로 순회 할 수 있도록 노드를 연결한 리스트
  - 두 개의 링크 필드와 한 개의 데이터 필드로 구성

![](https://user-images.githubusercontent.com/52684457/64087334-92d8e100-cd77-11e9-9a05-f070faa69b81.png)



- ##### 이중 연결 리스트의 삽입/삭제 연산



![](https://user-images.githubusercontent.com/52684457/64087341-99675880-cd77-11e9-90f8-7e5f8a3105ae.png)

![](https://user-images.githubusercontent.com/52684457/64087351-a3895700-cd77-11e9-8892-8e4d960d3368.png)

![](https://user-images.githubusercontent.com/52684457/64087357-aab06500-cd77-11e9-9357-985b43c808cb.png)

![](https://user-images.githubusercontent.com/52684457/64087370-b308a000-cd77-11e9-8fe0-74a29ccca4af.png)

![](https://user-images.githubusercontent.com/52684457/64087493-4e9a1080-cd78-11e9-84b4-0e3cc22b4bbd.png)

![](https://user-images.githubusercontent.com/52684457/64087505-5954a580-cd78-11e9-922e-22a37c06d961.png)

![](https://user-images.githubusercontent.com/52684457/64087515-65406780-cd78-11e9-9bb3-633338ab31c0.png)

![](https://user-images.githubusercontent.com/52684457/64087525-6bcedf00-cd78-11e9-80a8-3131c528da8b.png)

![](https://user-images.githubusercontent.com/52684457/64087535-72f5ed00-cd78-11e9-99a2-0c52928a80a1.png)



- **배열의 경우**에는 원소 증가에 따른 순환 횟수가 증가하기 때문에(하나씩 체크해가면서 해당되는 것들을 카운트) 시간이 걸린다.
-  불필요한 연산이(계속해서 배열값을 확인하지 않으면 인덱스 값을 구하는것에 문제가 생김) 발생한다.



- 반면에 **리스트**는 불필요한 순회를 제거하며(체크 되는 것이 삭제 되기 때문에 남은 원소의 개수 감소)
- 연산이 단순화(이동 후 삭제라는 간단한 연산만으로 문제 해결 가능)가 된다.



#### :ledger: 삽입 정렬(Insertion Sort)

- 도서관 사서가 책을 정렬할 때, 일반적으로 활용하는 방식이 삽입 정렬이다.
- 자료 배열의 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교하여, 자신의 위치를 찾아냄으로써 정렬을 완성한다.



- ##### 정렬 과정

  - 정렬할 자료를 두 개의 부분집합 S와 U로 가정
    - 부분 집합S : 정렬된 앞 부분의 원소들
    - 부분 집합U :  아직 정렬되지 않은 나머지 원소들
  - 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 이미 정렬되어있는 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입한다.
  - 삽입 정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 한다. 부분집합 U가 공집합이 되면 삽입정렬이 완성된다.

- ##### 시간 복잡도 : O(n^2)







![](https://user-images.githubusercontent.com/52684457/64088392-29a79c80-cd7c-11e9-9b92-d350c3d7b300.png)

![](https://user-images.githubusercontent.com/52684457/64088394-2f9d7d80-cd7c-11e9-975a-4c97b751a860.png)

![](![image](https://user-images.githubusercontent.com/52684457/64088406-40e68a00-cd7c-11e9-8260-40755baa21d7.png)

![](https://user-images.githubusercontent.com/52684457/64088413-49d75b80-cd7c-11e9-9e07-90708817a5e9.png)

![](https://user-images.githubusercontent.com/52684457/64088420-50fe6980-cd7c-11e9-9b55-dac70bac97e3.png)

![](https://user-images.githubusercontent.com/52684457/64088426-5c519500-cd7c-11e9-9096-2021778a6d81.png)

![](https://user-images.githubusercontent.com/52684457/64088432-61164900-cd7c-11e9-9fc5-66b6bc62d5de.png)

![](https://user-images.githubusercontent.com/52684457/64088438-65426680-cd7c-11e9-84a5-08406e4bdefd.png)









![](https://user-images.githubusercontent.com/52684457/64088518-cd914800-cd7c-11e9-86ac-a10327e4c71f.png)

```python
def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]

a = [50, 80, 70, 20, 90]

print('정렬 전:', end='')
print(a)

insertion_sort(a)

print('정렬 후:', end='')
print(a)
```





#### :ledger: 병합 정렬​ 

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

- 분할 정복 알고리즘 활용

  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - top-down 방식

- ##### 시간 복잡도 : O(n log n)

![](https://user-images.githubusercontent.com/52684457/64090678-51503200-cd87-11e9-98a7-f2f4784d89bc.png)

![](https://user-images.githubusercontent.com/52684457/64090685-5c0ac700-cd87-11e9-9fa0-c792792b5724.png)

![](https://user-images.githubusercontent.com/52684457/64090691-65942f00-cd87-11e9-8278-7ed4f67de250.png)

![](https://user-images.githubusercontent.com/52684457/64090694-6dec6a00-cd87-11e9-85ec-b1e46a600b08.png)

```python
a = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:

        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return  result

print('정렬 전:', a)

print('정렬 후:', merge_sort(a))


```

![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567400275289.png)











![](https://user-images.githubusercontent.com/52684457/64091202-100d5180-cd8a-11e9-8f1c-3102220bdcde.png)

- 비교하는 회수가 줄어드는 것보다 교환하는 회수가 줄어드는 것이 시간복잡도가 더 빨라진다.
- 이외 쉘 정렬, 히프 정렬 등이 있다.



##### 히프 정렬, 간단하게 보기

![](https://user-images.githubusercontent.com/52684457/64094276-228d8800-cd96-11e9-8fa4-934fffbe72cd.png)





#### :card_index_dividers: 리스트를 이용한 스택

- 리스트를 이용해 스택을 구현할 수 있다.
- 스택의 원소 : 리스트의 노드
  - 스택 내의 순서는 리스트의 링크를 통해 연결됨
    - Push : 리스트의 마지막에 노드 삽입
    - Pop : 리스트의 마지막 노드 반환/삭제
- 변수 top
  - 리스트의 마지막 노드를 가리키는 변수
  - 초기 상태 : top = null

![](https://user-images.githubusercontent.com/52684457/64091461-2b2c9100-cd8b-11e9-8db0-b95dd5b0fc0f.png)





###### 똑같은 개념이지만 연결 리스트로 구현이 가능하다는 것

- 리스트를 이용한 스택의 연산

![](https://user-images.githubusercontent.com/52684457/64091466-32ec3580-cd8b-11e9-80ea-5827be0b152d.png)

![](https://user-images.githubusercontent.com/52684457/64091480-44cdd880-cd8b-11e9-88d6-e6f302dfe294.png)





##### 리스트를 이용한 스택의 구현(Python Code)

##### ![](https://user-images.githubusercontent.com/52684457/64092569-46e66600-cd90-11e9-9d23-001bf308be55.png)

```python
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def push(i): # 원소 i를 스택 top(맨 앞) 위치에 push
    global top
    top = Node(i, top) # 새로운 노드 생성

def pop(): # 스택의 top을 pop
    global top
    if top == None: # 빈 리스트이면
        print('error')
    else:
        data = top.data
        top = top.link # top이 가리키는 노드를 바꿈
        return  data

top = None
push(3)
push(4)
push(5)
push(6)
pop()

while top.link != None:
    print(top.data, end='=>')
    top = top.link
print(top.data)
```

출력 값 : `5=>4=>3`

![](https://user-images.githubusercontent.com/52684457/64091878-49938c00-cd8d-11e9-9709-0d6f2e2c1752.png)

###### pop을 하게되면 link가 바라보는 곳이 없어지게 되어, 더 이상 연결이 된 것이 없어진 노드는 존재하지만 쓸일이 없는 garbage data가 된다. 존재는 하지만 없는 것 처럼 인식이 된다.

![](https://user-images.githubusercontent.com/52684457/64092540-29190100-cd90-11e9-8907-64594f945fbd.png)

- 특정 인덱스에 노드 추가

![](https://user-images.githubusercontent.com/52684457/64152037-ad3db800-ce66-11e9-94c3-635300e19f14.png)

### :card_index_dividers: Revisit to 우선순위 큐

##### :file_folder: 배열을 이용한 우선순위 큐 구현

- 우선순위 큐의 구현
  - 배열을 이용한 우선순위 큐
  - 리스트를 이용한 우선순위 큐
- 우선순위 큐의 기본 연산
  - 삽입 : enQueue
  - 삭제 : deQueue

![](https://user-images.githubusercontent.com/52684457/64094440-b19aa000-cd96-11e9-8f73-81ad40d0c5c4.png)무조건 순서대로 넣는 것이 아니라, **우선순위에 따른**다.



##### :open_file_folder: 리스트를 이용한 우선순위 큐

- 리스트를 이용하여 우선순위
  - 연결 리스트를 이용하여 자료 저장
  - 원소를 삽입하는 과정에서 리스트 내 노드의 원소들과 비교하여 적절한 위치에 노드를 삽입하는 구조
  - 리스트의 가장 앞쪽에 최고 우선순위가 위치하게 됨
- 배열 대비 장점
  - 삽입/삭제 연산 이후 원소의 재배치가 필요 없음
  - 메모리의 효율적인 사용이 가능



















































