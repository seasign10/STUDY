num = int(input())

strnum = ''
n = (2*num) - 1 # 역순
mul = 1 

# num이 4라고 해보자.
# add를 바로 최종값 10이 나오도록 해보자.
add = 0 # 최종값을 낼 저장소
plus = 1 # 1, 3, 6, 10 ==> +2, +3, +4 ..
for l in range(num):
    add += plus # 초기화 할 필요가 없다. 더해진값에 더 하고 또 더하기 때문.
    plus += 1
# print(add) # 값이 제대로 나오는 것을 확인

count = 0 # num만큼의 수만큼 for문 돌리고, 오른쪽으로도 num숫자부터 엔터


num_box = [] # 빈 list에 숫자를 담아주자.
for r in range(1, add+1):
    # print(r, end=', ') # 필요한 수 10까지 나오는 것을 확인
    num_box.append(r)
# print(num_box) # int값으로 넣어줘야 10이 1,0 으로 들어가지 않음.

print_box = ''
for i in num_box:
    print_box += str(i) + ' '
    print(str(i) + ' ', end='')
    count += 1  
    if count == num:
        count = 0
        print() # 줄이 바뀔때 마다.
        print(end='  '*mul) # 2칸의 공백이 +1, +1, +1... 숫자 앞에존재
        num -= 1
        mul += 1






# for i in range(1, num+1):
    # count += 1
    # box = mul*' ' + strnum
    # print(box)
    # mul += 1
    # if count == num: 
    #     print(box)
    #     count = 0


# a = 6
# for j in range(1, a+1):
#     print(j, end=' ')



# n = (2*num) - 1
# mul = 0
# # 아래 식 응용
# star = '*'
# for i in range(num):
#     res = star*n 
#     print((mul*' ') + star*n) 
#     mul += 2 
#     n-= 2

