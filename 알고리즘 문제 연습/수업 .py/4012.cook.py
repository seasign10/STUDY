arr = [10, 20, 30, 40]
N = 4

# 이진검색을 하기위해 두 그룹으로 분할
for set in range(1<< 4):
    A, B = [], []
    for i in range(N):
        if set & (1<<i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)
    # 결과값 중에서 최소가 되는 값 저장

    # print(A, B) 출력 값
    # [10, 20] [30, 40]
    # [10, 30] [20, 40]
    # [20, 30] [10, 40]
    # [10, 40] [20, 30]
    # [20, 40] [10, 30]
    # [30, 40] [10, 20]