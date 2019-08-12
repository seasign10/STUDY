import sys
sys.stdin = open("2058.txt", "r")

N = input()
# result = 0

# for i in N:
#     result += int(i) % 10
# print(result)

res = 0
for i in N:
    res += int(i)
print(res)