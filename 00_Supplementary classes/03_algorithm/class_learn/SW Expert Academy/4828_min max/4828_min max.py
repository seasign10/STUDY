import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for i in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    
    MIN = ai[0]
    MAX = ai[0]

    for j in ai:
        if j > MAX:
            MAX = j
        if j < MIN:
            MIN = j
    diff = MAX - MIN

    print('#{} {}'.format(i+1, diff))
