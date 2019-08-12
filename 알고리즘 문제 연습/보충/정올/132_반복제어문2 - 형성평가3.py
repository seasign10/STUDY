num = int(input())

add = 0
for i in range(num+1):
    if i % 5 ==0:
        add += i
print(add)