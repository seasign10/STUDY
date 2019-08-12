import sys
sys.stdin = open("1545.txt", "r")


N = int(input())
for i in range(1, N+1, ):
    if i == 1:
        print(N, end=' ')
    print(N - i, end=' ')