a, b = map(int, input().split())

sums = 0
count = 0
if a > b:
    a, b = b, a
for i in range(a, b+1):
    if i % 3 ==0 or i % 5 ==0:
        sums += i
        count += 1  
avg = round(sums / count, 1)
print('sum : {}'.format(sums))
print('avg : {}'.format(avg))
