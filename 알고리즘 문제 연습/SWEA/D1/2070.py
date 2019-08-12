import sys
sys.stdin = open("2070.txt", "r")

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print('#{} >'.format(i))
    elif a < b:
        print('#{} <'.format(i))
    else:
        print('#{} ='.format(i))