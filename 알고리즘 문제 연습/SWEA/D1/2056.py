import sys
sys.stdin = open("2056.txt", "r")

T = int(input())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
no = -1

for i in range(1, T+1):
    date = list(map(int, input().split()))
    for j in date:
        year = j // 10000
        day = j % 100
        m = j % 10000
        month = m // 100
        if month in a:
            if day <= 31:
                print('#{} {:0>4}/{:0>2}/{:0>2}'.format(i, year, month, day))
            else:
                print('#{} {}'.format(i, no))
        elif month in b:
            if day <= 30:
                print('#{} {:0>4}/{:0>2}/{:0>2}'.format(i, year, month, day))
            else:
                print('#{} {}'.format(i, no))
        elif month in c:
            if day <= 28:
                print('#{} {:0>4}/{:0>2}/{:0>2}'.format(i, year, month, day))
            else:
                print('#{} {}'.format(i, no))
        else:
            print('#{} {}'.format(i, no))
        
            