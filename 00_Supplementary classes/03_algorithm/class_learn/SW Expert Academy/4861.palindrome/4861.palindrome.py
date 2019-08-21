import sys
sys.stdin = open("4861.txt", "r")

T = int(input())

for l in range(1, T+1):
    N = int(input())
    M = int(input())
    for i in N:
        for j in M: 

# 회문 조사 방법
# 가능한 모든 경우를 조사하는 방법
arr = []
N = M = 0 # N: 행의 길이, M: 찾을 회문 길이
# tlwkrdnlcl 0 ~ N - M
for row in range(N):
    
    for start in range(N - M + 1):
        end = start + M - 1
        for i in range(M//2):
            if arr[row][start + i] != arr[row][end - i]:
                break
            else:
                # 회문을 찾음