import sys
sys.stdin = open("4864.txt", "r")

T = int(input())

for l in range(1, T+1):
    str_1 = str(input())
    str_2 = str(input())
    # print(str_2, str_1)
    n, m = len(str_2), len(str_1)
    cnt = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if str_2[i + j] != str_1[j]:
                break
            j += 1
            cnt += 1
        if j == m:
            print('#{} 1'.format(l))
    if str_1 not in str_2:
        print('#{} 0'.format(l))
