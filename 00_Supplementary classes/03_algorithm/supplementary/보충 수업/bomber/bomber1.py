import sys; sys.stdin = open('bomber1_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # Max_x = 0
    # Max_y = 0
    idx_x = 0
    idx_y = 0
    Max = 0

    for i in range(N):
        x = y = 0
        for j in range(N):
            x += arr[i][j]
            y += arr[j][i]
            sums = x + y

            if sums > Max:
                Max = sums
                idx_x = i
                idx_y = j

            # if Max_x < x:
            #     Max = x
            #     idx_x = i
            #
            # if Max_y < y:
            #     Max = y
            #     idx_y = j
            #
            # Max = Max_x + Max_y

    print('#{}'.format(tc), i, j, Max)
