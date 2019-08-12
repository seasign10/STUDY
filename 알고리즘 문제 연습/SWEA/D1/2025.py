import sys
sys.stdin = open("2025.txt", "r")

num = int(input())

result = 0
n = 0

for i in range(1, num+1):
    result += i
print(result)