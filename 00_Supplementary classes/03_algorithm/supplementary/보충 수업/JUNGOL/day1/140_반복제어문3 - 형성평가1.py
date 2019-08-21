num = list(map(int, input().split()))

add = 0
count = 0
for i in num:
    if i != 0:
        add += i
        count += 1
    else:
        break
print(add, int(add/count))