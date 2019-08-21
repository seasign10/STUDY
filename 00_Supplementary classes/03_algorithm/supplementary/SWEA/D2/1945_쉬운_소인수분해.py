import sys
sys.stdin = open("1945.txt", "r")

tc = int(input())

cnt = [0] * 5
com = 0
for i in range(1, tc+1):
    cnt = [0] * 5
    num = int(input())

    while num % 2 == 0:
        cnt[0] += 1
        num = num / 2
    while num % 3 == 0:
        cnt[1] += 1
        num = num / 3
    while num % 5 == 0:
        cnt[2] += 1
        num = num / 5
    while num % 7 == 0:
        cnt[3] += 1
        num = num / 7
    while num % 11 == 0:
        cnt[4] += 1
        num = num / 11
    
    # 소인수분해, 2, 3, 5, 7, 11이 계속 나눠지는 한 계속 나눠준다. (한번만 나누고 끝이 아님)
    # for 보다는 while을 이용해주는것이 좋을 것 같은 느낌이 든다.
    print('#{}'.format(i), end=' ')
    for j in cnt:
        print(j, end=' ')
        com += 1
        if com == 5:
            print()
            com = 0

    # print('#{} {}'.format(i, cnt))

