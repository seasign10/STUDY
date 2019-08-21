import sys
sys.stdin = open("2071.txt", "r")

T = int(input())

result = 1

for i in range(T):
    num = list(map(int, input().split()))
    result = 1
    for j in num:
        result += j
    print('#{} {}'.format(i+1, round(result/10)))