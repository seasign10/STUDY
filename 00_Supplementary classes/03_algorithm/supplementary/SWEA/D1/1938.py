import sys
sys.stdin = open("1938.txt", "r")

result = 0

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
