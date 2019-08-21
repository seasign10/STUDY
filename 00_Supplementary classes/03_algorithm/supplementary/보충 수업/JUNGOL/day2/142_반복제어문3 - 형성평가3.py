num = int(input())

for i in range(1, num+1):
    print('*'*i)

minor = -1
for j in range(1, num): # 최종 i 값이 num+1 이 되므로 그 값을 -1씩 해주면서 줄여준다.
    print('*'*(i + minor))
    minor -= 1
