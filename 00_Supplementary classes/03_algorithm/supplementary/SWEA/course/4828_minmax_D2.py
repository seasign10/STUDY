import sys
sys.stdin = open("4828.txt", "r")

tc = int(input())

for i in range(1, tc+1):
    n = int(input())
    aj = list(map(int, input().split()))
    
    Max = 0
    for j in aj:
        if Max < j:
            Max = j
    Min = aj[0]
    for j in aj:
        if Min > j:
            Min = j
    
    print('#{} {}'.format(i, Max-Min))