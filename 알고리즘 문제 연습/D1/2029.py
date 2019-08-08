import sys
sys.stdin = open("2029.txt", "r")

t = int(input())

for i in range(1, t+1):
    num1, num2 = map(int, input().split())
    n1 = num1 // num2
    n2 = num1 % num2
    print('#{} {} {}'.format(i, n1, n2))

