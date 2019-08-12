import sys
sys.stdin = open("2043.txt", "r")

P, K = map(int, input().split())

count = 1
num = K
for i in range(999):
    count += 1
    num += 1
    if num == P:
        print(count)
