n, m = map(int, input().split())

cnt =  0

if n > m :
    for i in range(1, 10):
        for j in range(n, m-1, -1):
            print('{} *{:2} = {:2}'.format(j, i, i*j), end='   ')
            cnt += 1
            if cnt == n - m + 1: # 5 - 3 = 2 ===> +1 / 6 - 2 = 4 ===> +1
                                 # 5, 4, 3 => 3        6, 5, 4, 3, 2 => 5
                print()
                cnt = 0
elif n < m:
    for i in range(1, 10):
        for j in range(n, m+1):
            print('{} *{:2} = {:2}'.format(j, i, i*j), end='   ')
            cnt += 1
            if cnt == m - n + 1:
                print()
                cnt = 0

elif n == m:
    for i in range(1, 10):
        for j in range(n, m+1):
            print('{} *{:2} = {:2}'.format(j, i, i*j))