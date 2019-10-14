# :card_file_box: APS :  Divide and Conquer _ Back Tracking



## :heavy_check_mark: 분할 정복 기법

- 유래
  - 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹잉 사용한 전략
  - 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔.
  - 둘로 나뉜 연합군을 한 부분씩 격파
- 설계 전략
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

![image](https://user-images.githubusercontent.com/52684457/65398044-cabfcb00-ddef-11e9-86bd-f9df2c11273f.png)

![image](https://user-images.githubusercontent.com/52684457/65398050-d27f6f80-ddef-11e9-90c0-f3722784ba2a.png)

![image](https://user-images.githubusercontent.com/52684457/65398054-dc08d780-ddef-11e9-87d9-8b0f6cccd658.png)







### :heavy_exclamation_mark: 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - top-down 방식
- **시간 복잡도** : O(n log n)

![image](https://user-images.githubusercontent.com/52684457/65398851-7ec35500-ddf4-11e9-8d5b-8231244c5d35.png)

![image](https://user-images.githubusercontent.com/52684457/65398265-2dfe2d00-ddf1-11e9-9574-d9c2d745a51c.png)





![image](https://user-images.githubusercontent.com/52684457/65398358-9baa5900-ddf1-11e9-8a58-ce3d07ede72e.png)

```python
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def mergeSort(lo, hi):     # 매개변수 ==> 문제의 크기
    print(lo, hi)
    if lo == hi: return
    # 분할
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)     # 왼쪽
    mergeSort(mid + 1, hi) #오른쪽
    # 왼쪽과 오른쪽을 병합

mergeSort(0, len(arr) - 1)
```



![image](https://user-images.githubusercontent.com/52684457/65398857-897dea00-ddf4-11e9-85b1-fe7367aba382.png)

![image](https://user-images.githubusercontent.com/52684457/65398839-6a7f5800-ddf4-11e9-8cbe-2d3d30e80264.png)

```python
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def mergeSort(lo, hi):     # 매개변수 ==> 문제의 크기
    print(lo, hi)
    if lo == hi: return
    # 분할
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)     # 왼쪽
    mergeSort(mid + 1, hi) #오른쪽
    i, j, k = lo, mid+1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k, = i+1, k+1
        else:
            tmp[k] = arr[j]
            j, k, = j+1, k+1

    while i <= mid:
        tmp[k] = arr[i]
        i, k = i+1, k+1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j+1, k+1

    for i in range(lo, hi+1):
        arr[i] = tmp[i]

print(arr)
mergeSort(0, len(arr) - 1)
print(arr)

# 출력 값
[69, 10, 30, 2, 16, 8, 31, 22]
0 7
0 3
0 1
0 0
1 1
2 3
2 2
3 3
4 7
4 5
4 4
5 5
6 7
6 6
7 7
[2, 8, 10, 16, 22, 30, 31, 69]
```



###  :heavy_exclamation_mark:퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
  - 병합 정렬과 동일?
- **차이점 1** : 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
- **차이점 2** : 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

![image](https://user-images.githubusercontent.com/52684457/65398926-f4c7bc00-ddf4-11e9-82bd-d5cac3e1427b.png)

- 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 몰아 넣기 **=>** 완벽히 정렬된 상태는 아님
  **=>** 동일한 일을 반복 **=>** 정렬 완료

![image](https://user-images.githubusercontent.com/52684457/65398963-188b0200-ddf5-11e9-988e-0e1715e01fec.png)

```python
1)
while A[i] <= p: i++
while A[j] > p: j--

2)
while A[i] < p: i++
while A[j] >= p: j--
    
# 둘 중 하나의 while문만 =를 붙여준다.
# 되도록이면 1) 처럼 윗줄에 = 를 붙여주는 것이 코드가 깔끔하다.
```





- 파티션이 중요

![image](https://user-images.githubusercontent.com/52684457/65398981-348ea380-ddf5-11e9-992b-592f7151e601.png)![image](https://user-images.githubusercontent.com/52684457/65398985-3a848480-ddf5-11e9-92e4-b7df417f1205.png)![image](https://user-images.githubusercontent.com/52684457/65398994-43755600-ddf5-11e9-9285-b66d7b74f492.png)![image](https://user-images.githubusercontent.com/52684457/65398999-4b34fa80-ddf5-11e9-93de-01571163e338.png)![image](https://user-images.githubusercontent.com/52684457/65399003-525c0880-ddf5-11e9-9b85-b63e615fd17f.png)![image](https://user-images.githubusercontent.com/52684457/65399010-58ea8000-ddf5-11e9-919e-f8fc97bbc945.png)![image](https://user-images.githubusercontent.com/52684457/65399025-715a9a80-ddf5-11e9-98dd-2f5fada1cad7.png)

```python
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):
    if lo >= hi: return
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]: i += 1
        while pivot < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j], = arr[j], arr[lo]

    quickSort(lo, j - 1)
    quickSort(j + 1, hi)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)

# 출력 값
[69, 10, 30, 2, 16, 8, 31, 22]
[2, 8, 10, 16, 22, 30, 31, 69]
```

![image](https://user-images.githubusercontent.com/52684457/65399031-7881a880-ddf5-11e9-97c8-10bfccbfe231.png)

![image](https://user-images.githubusercontent.com/52684457/65399054-93541d00-ddf5-11e9-9ffa-56870b767952.png)

```python
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]
    
    quickSort(lo, j - 1)
    quickSort(j + 1, hi)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)
```



### :heavy_exclamation_mark: 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
- 검색과정
  1. 자료의 중앙에 있는 원소를 고른다.
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  4. 찾고자 하는 값을 찾을 때까지 1~3 과정을 반복한다.

![image](https://user-images.githubusercontent.com/52684457/65402452-69a4f100-de09-11e9-95e0-8a7a1c75f9ae.png)![image](https://user-images.githubusercontent.com/52684457/65402459-79243a00-de09-11e9-947f-1ba15b37538a.png)![image](https://user-images.githubusercontent.com/52684457/65402466-804b4800-de09-11e9-90e3-02dd5851564c.png)![image](https://user-images.githubusercontent.com/52684457/65402473-88a38300-de09-11e9-9d8c-2c58a0c2bf37.png)

- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어(Multi_Core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.
  - 생물 정보 공학(Bioinformatics)에서 특정 유전자를 효율적으로 찾는데 접미어 배열(suffix array)와 함께 사용된다. 접미어 배열은 문자열에서 학습합니다.
- 최근접 점의 쌍(Closet Pair)문제는 2차원 평면상의 n개의 점이 입력으로 주어질 때, 거리가 가장 가까운 한 쌍의 점을 찾는 문제이다.
  - 컴퓨터 그래픽스, 컴퓨터 비전, 지리 정보 시스템, 항공 트래픽 제어, 마케팅(신규 가맹점 위치 선정 등)등의 분야





##  :heavy_check_mark: 백트래킹

#### :green_apple: 문제 제시 : N-Queen

![image](https://user-images.githubusercontent.com/52684457/65402788-80e4de00-de0b-11e9-92b8-d22f128e85bd.png)

![image](https://user-images.githubusercontent.com/52684457/65402801-99ed8f00-de0b-11e9-81cb-35f1ebdea750.png)

```python
N = 8
cnt = 0
visit = [0] * N
cols = [0] * N     # 퀸의 열값을 저장
# 행 값은 고정되어있기 때문에 정해줄 필요가 없다.
def Possible(k, c):      # k번 퀸의 열 1가 답이 되는 선택인지 조사
    for i in range(k):   # 0 ~ k-1 번 퀸과 대각선에 있는지 조사
        if k - i == abs(c - cols[i]):
            return False
    return True
def nQueen(k):
    if k == N:
        global  cnt
        cnt += 1
    else:
        for i in range(N):
            if visit[i] or not Possible(k, i): continue
            visit[i] = 1
            cols[k] = i
            nQueen(k + 1)
            visit[i] = 0

nQueen(0)
print(cnt)
```

![image](https://user-images.githubusercontent.com/52684457/65404430-6c0c4880-de13-11e9-8890-f76a5082e0fc.png)



### :back: 백트래킹(Backrtacking) 개념

![image](https://user-images.githubusercontent.com/52684457/65402366-d370cb00-de08-11e9-9b48-a7d438fbd48f.png)

![image](https://user-images.githubusercontent.com/52684457/65402376-e4214100-de08-11e9-8bbf-ebeb35c1d360.png)

![image](https://user-images.githubusercontent.com/52684457/65402557-167f6e00-de0a-11e9-95d7-e1f2d6f0979a.png)****

![image](https://user-images.githubusercontent.com/52684457/65402559-2008d600-de0a-11e9-8729-6d974d794013.png)



- 루트 노드에서 리프(leaf) 노드까지의 경로는 해답후보(candidate solution)가 되는데, 깊이 우선 검색을 하여 그 해답후보 중에서 해답을 찾을 수 있다.
- 그러나 이 방법을 사용하면 해답이 될 가능성이 전혀 없는 노드의 후손 노드(descendant)들도 모두 검색해야 하므로 비효율적이다.

![image](https://user-images.githubusercontent.com/52684457/65402635-af15ee00-de0a-11e9-99bc-8d22035a5e67.png)

- 모든 후보를 검사 ? : **NO!**
- 백트래킹 기법
  - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 겨 ㄹ정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
  - **가지치기(pruning)** : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

- 백트래킹을 이용한 알고리즘은 다음과 같은절차로 진행된다.
  1. 상태 공간 트리의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

![image](https://user-images.githubusercontent.com/52684457/65402740-34999e00-de0b-11e9-968f-c131b96ee3dd.png)![image](https://user-images.githubusercontent.com/52684457/65402749-411df680-de0b-11e9-92f2-278c8d6780cb.png)![image](https://user-images.githubusercontent.com/52684457/65402758-4e3ae580-de0b-11e9-9e9c-c0265336a2db.png)

![image](https://user-images.githubusercontent.com/52684457/65402849-dd47fd80-de0b-11e9-881d-2eb83ecdae37.png)

- 상태공간트리를 구축하여 문제를 해결

  ![image](https://user-images.githubusercontent.com/52684457/65403154-99ee8e80-de0d-11e9-9dc1-459ddeadacb4.png)

  ```python
  # 순열 생성
  arr = 'ABC'
  N = len(arr)
  order = [0] * N         # 순서를 저장
  def perm(a, k, n):
      if k == n:
          # process_solution()
          print(a)
      else:
          visit = [False] * n  # make_candidate
          for i in range(k):
              visit[a[i]] = True
          for i in range(n):
              if visit[i]: continue
              a[k] = i
              perm(a, k + 1, n)
  
  
  
  perm(order, 0, N)
  
  # 출력 값
  [0, 1, 2]
  [0, 2, 1]
  [1, 0, 2]
  [1, 2, 0]
  [2, 0, 1]
  [2, 1, 0]
  ```

  ![image](https://user-images.githubusercontent.com/52684457/65403184-bc80a780-de0d-11e9-8b39-2da46734e786.png)



![image](https://user-images.githubusercontent.com/52684457/65403279-d326fe80-de0d-11e9-88f9-09fb624e381b.png)

```python
arr = 'ABC'
N = len(arr)
order = [0] * N
visit = [False] * N     # 추가
def perm(a, k, n, visit):
    if k == n:
        print(a)
    else:
        for i in range(n):
            # if visit[i]: continue
            if visit & (1 << i): continue # 추가
            # visit[i] = True
            a[k] = i
            # perm(a, k + 1, n)
            # visit[i] = False
            perm(a, k + 1, n, visit | (1 << i)) # 추가



perm(order, 0, N, 0)
```









































