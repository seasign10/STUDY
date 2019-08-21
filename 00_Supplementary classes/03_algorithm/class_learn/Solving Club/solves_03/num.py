for tc in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for i in range(100)]

    ans = 0 # 최대값 저장
    # 행들의 합
    for i in range(100):
        S = 0
        S += arr[i][99 - i]
        S += arr[i][i]
        for j in range(100):    
            S += arr[i][j]
        ans = max(ans, S)
    # 열들의 합
    for i in range(100):
        S = 0
        for j in range(100):    
            S += arr[j][i]
        ans = max(ans, S)
    print('#{} {}'.format(tc, ans))