# 사각 영역을 표시할때에는 각 대각선 좌표로 표현하거나,
# 길이를 구해서 표현한다.

T = int(input()) # 테스트 케이스
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 모든 자료의 합
    row_sum = col_sum = 0
    ans = 10000000000 # Min을 구하기 위함
    for i in range(N):     # 0 ~ N - 1
        row_sum = col_sum = 0 # 새로운 행에 들어갈 때 마다 초기화
        for j in range(N): # 0 ~ N - 1 / N * N

            row_sum += arr[i][j]   # 행 우선 순회
            col_sum += arr[j][i]   # 열 우선 순회
        # print(row_sum, col_sum)
            ans = min(row_sum, col_sum)
    print('MIN ==>', ans)

    S = 0
    for i in range(N): # 좌상단 => 우하단
        S += arr[i][i]

    for i in range(N): # 우상단 => 좌하단
        S += arr[i][N-1-i]
    print('S==>', S)

#---------------------------- 사각형 구하기 ------------------------------

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 M x M 영역의 좌상단 좌표를 만든다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 좌상단 i, j 가로세로 길이 = M 사각형을 행우선 탐색
            for r in range(i, i + M):       # i ~ i + M - 1까지
                for c in range(j, j + M):   # j ~ j + M - 1까지
    