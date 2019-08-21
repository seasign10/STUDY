import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

for i in range(T):  # 테스트케이스 개수
    N = int(input())
    listA = []
    listB = []
    for j in range(N):  # 칠할 구간 개수 (색깔 개수)
        arr = list(map(int, input().split()))
        I = arr[2] - arr[0]
        J = arr[3] - arr[1]
        for x in range(I+1):
            for y in range(J+1):
                if arr[-1] == 1:
                    listA.append((arr[0]+x, arr[1]+y))
                else:
                    listB.append((arr[0]+x, arr[1]+y))
    print('#{} {}'.format(i+1, len(set(listA) & set(listB))))






# for i in tc:
#     inter = int(input())
#     n, m = 9, inter
#     for j in range(n - m + 1):
#         for l in range(n - m + 1)

#             for x in range(j, j + m):
#                 for y in range(l, l + m):
#                     print('#{} {}')

