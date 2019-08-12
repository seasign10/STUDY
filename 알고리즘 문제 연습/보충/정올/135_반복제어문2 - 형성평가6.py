a, b = map(int, input().split())

sums = 0
mul = 0
count = 0
for i in range(a, b+1):
    if i % 3 ==0 or i % 5 ==0:
        sums += i
        mul += i 
        count += 1  
    avg = mul / count
print('sum : {}'.format(sums))
print('avg : {:.1f}'.format(avg))
