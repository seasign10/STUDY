p = 'leehaein'
t = 'sfwehiuhdskjleehaeindsfheuk'

n, m = len(t), len(p)   # n: 텍스트의 길이, m: 패턴의 길이

# 텍스트에서 패턴이 있을 수 있는 모든 시작위치
for i in range(n - m + 1):
    j = 0
    while j < m:
        if t[i + j] != p[j]:
            break
        j += 1
    if j == m:
        print(t[i:i + m])

# i = j = 0
# while i < n:
#     if p[j] != t[i]:
#         i = i - j + 1
#         j = -1
        
#     i, j = i + 1, j + 1
#     if j == m:
#         print(t[i - j:])
#         break