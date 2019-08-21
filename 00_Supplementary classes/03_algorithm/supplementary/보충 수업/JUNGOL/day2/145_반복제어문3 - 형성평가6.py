num = int(input())

strnum = ''
empty = (2*num) - 2
for i in range(1, num+1):
    # strnum += str(i)
    # print(strnum) # 숫자가 제대로 출력되는 것을 확인
    strnum += str(i) + ' '
    print(' '*empty + strnum)
    empty -= 2
    