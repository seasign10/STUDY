import sys
sys.stdin = open("2068.txt", "r")

T = int(input())

for i in range(1, T+1):
    max_num = 0
    num = list(map(int, input().split()))
    for j in num:
        if max_num < j:
            max_num = j
    print('#{} {}'.format(i, max_num))