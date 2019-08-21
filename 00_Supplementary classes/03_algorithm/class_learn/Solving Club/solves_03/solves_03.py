import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for i in range(100)]

    ans = 0 
    dsum1 = dsum2 = 0
    for i in range(100):
        rsum = csum = 0
        dsum1 += arr[i][i]
        dsum2 += arr[i][99 - i]
        for j in range(100):    
            rsum += arr[i][j]
            csum += arr[j][i]
        ans = max(ans, rsum, csum)
    ans = max(ans, dsum1, dsum2)

    print('#{} {}'.format(tc, ans))