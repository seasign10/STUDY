n = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    result += i
box = result / len(num)
print('{:.2f}'.format(box))



# # 소수점 나타내는 방법
# f = 123.456789
# print('{:.1f}'.format(f))
# print('{:.2f}'.format(f))
# print('{:.3f}'.format(f))
# print('{:.4f}'.format(f))