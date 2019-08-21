num = list(map(int, input().split()))
odd = 0
even = 0
for i in num:
    if i % 2:
        odd += 1
    else:
        even += 1
print('even : {}'.format(even))
print('odd : {}'.format(odd))

