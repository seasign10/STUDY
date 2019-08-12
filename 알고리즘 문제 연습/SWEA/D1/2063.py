import sys
sys.stdin = open("2063.txt", "r")

N = int(input())
num = list(map(int, input().split()))
sor = sorted(num)

print(sor[N//2])