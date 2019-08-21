import sys
sys.stdin = open("1986.txt", "r")

tc = int(input())

# a = '5'
# print(int(a)) # str이 int되는 것 확인함.

for i in range(1, tc+1):
    n = int(input())
    empty = ''
    for j in range(1, n+1):
        if j % 2:
            empty += ' +'
        elif j % 2==0:
            empty += ' -'
        empty += str(j)
    empty = empty.split()
    sums = 0 # empty에 값을 더해줄 것
    for l in empty:
        sums += int(l)
    print('#{} {}'.format(i, sums))