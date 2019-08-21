num = int(input())

for i in range(1, num+1):
    for j in range(1, num+1):
        print('({}, {})'.format(i, j), end=' ')
    print()
