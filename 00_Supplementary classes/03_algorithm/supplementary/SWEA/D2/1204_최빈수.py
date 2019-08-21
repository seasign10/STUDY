import sys
sys.stdin = open("1204.txt", "r")

# 최빈수 = 가장 빈도수가 높은 값 (가장 여러번 나타나는 값)
t = int(input())

for i in range(1, t+1):
    tc = int(input())
    student = list(map(int, input().split()))
    cnt = [0] * 101
    # print(tc, student)
    for val in student:
        cnt[val] += 1

    Maxidx = 0
    for j in range(0, len(cnt)):
        if cnt[Maxidx] <= cnt[j]:
            Maxidx = j

    print('#{} {}'.format(i, Maxidx))

