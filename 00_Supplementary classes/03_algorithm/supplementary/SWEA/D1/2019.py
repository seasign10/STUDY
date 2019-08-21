import sys
sys.stdin = open("2019.txt", "r")

N = int(input())

result = 0
for i in range(1, N+1):
    if result == 0:
        result += 1
        print(result, end=' ')
    result *= 2
    print(result, end=' ')