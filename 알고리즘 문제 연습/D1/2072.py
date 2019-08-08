import sys
sys.stdin = open("2072.txt", "r")

t = int(input())

result = 0
for i in range(t):
    num = list(map(int, input().split()))
    for j in num:
        if j % 2:
            result += j
            
    print('#{} {}'.format(i+1, result))
    result = 0