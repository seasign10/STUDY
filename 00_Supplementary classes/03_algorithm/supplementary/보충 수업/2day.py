arr = [7, 4, 8, 1, 3, 5, 2, 8, 6]
# 최대, 최소 찾기

# 1. 라이브러리 이용
print(max(arr), min(arr))

# 2. 최대 최소의 위치를 알아야 할 때
print(arr.index(8)) # 중복되는 숫자가 있을 경우 가장 앞의 수가 출력
# 하지만 가장 마지막의 숫자를 구해야하는 경우도 있음.


# 3. for문을 이용해서 직접 찾기

# 3-1. 최소 찾기
Min = arr[0]
for i in range(1, len(arr)): # len(arr) => 0, 1, 2, 3, 4, 5, 6, 7, 8
    if Min > arr[i]: # index 0부터 값을 가져와 arr을 하나씩 비교
        Min = arr[i] # arr[i]가 더 작다면 Min에 저장
print(Min)

# 3-2. 최대 찾기
Min = arr[0]
for i in range(1, len(arr)):
    if Min < arr[i]:
        Min = arr[i]

# 4. 최소값 위치 찾기
MinIdx = 0 # 0번 위치를 최소값의 위치로 저장, 가장 첫번째 요소를 넣어 다음 요소와 비교
for i in range(1, len(arr)):
    if arr[MinIdx] > arr[i]: # 0번째 arr과 1번째 arr 비교
        # if arr[MinIdx] >= arr[i]: => '='을 넣어주면 가장 마지막의 숫자를 가져오고,
        # 넣지 않으면 가장 첫 번째로 나온 값을 가져온다.
        MinIdx = i # 더 작은녀석의 인덱스로 바꿔주자.
print(MinIdx, arr[MinIdx]) # 인덱스번호, 가장 최솟값


arr2 = [0, 4, 1, 3, 1, 2, 4, 1]
# 값의 등장 횟수 계산 (counting)
# 자료값을 리스트(배열)의 인덱스로 사용한다.
# 자료값들이 양의 정수여야 한다. (인덱스는 양의 정수여야 사용가능) / [:-n:-m]와 같은 경우 제외
# 자료값들의 범위(최대값)를 알아야 한다. (양의 정수여서 보통 0부터 시작. 시작은 정해져있기 때문에 최대값을 알아야 한다.)

# arr = []
# print(arr[0]) #=> 빈 리스트는 아무것도 읽지 못해서 오류가 남.

cnt = [0] * 5 # 위의 arr2는 5만 필요 (0, 1, 2, 3, 4) 총 사용된 갯수 5 / 하지만 정확히 셀 수 없을 때에는 범위를 크게 만든다.
for val in arr2:
    cnt[val] = cnt[val] + 1

for i in range(len(cnt)):
    print(i, cnt[i])