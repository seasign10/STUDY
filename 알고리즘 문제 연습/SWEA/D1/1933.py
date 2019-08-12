import sys
sys.stdin = open("1933.txt", "r")

N = int(input())

for x in range(1, N+1):
    if N % x ==0:
        print(x, end=' ')
