import sys
sys.stdin = open("1936.txt", "r")

A, B = map(int, input().split())

r = 2
s = 1
p = 3

if A == B:
    print('비겼다!')
elif A == 1 and B == 3:
    print('A')
elif A == 2 and B == 1:
    print('A')
elif A == 3 and B == 2:
    print('A')
else:
    print('B')