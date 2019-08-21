# for <====> while 변환 가능하다.
# for => 반복횟수를 알 수 있을 때
# while => 반복횟수를 정확히 알 수 없을 때 (종료조건을 잘 정해야 함)

arr = list(range(5)) # range는 iterable한 존재
# iterable 의 의미는 member를 하나씩 차례로 반환 가능한 object를 말한다. 
# iterable 의 예로는 sequence type인 list, str, tuple 이 대표적이다. 

for i in arr:
    print('Hello')
    # Hello
    # Hello
    # Hello
    # Hello
    # Hello

# i도 for 문 안에서 적용이 된다. (잘 사용하지 않는 사례)
for i in range(5):
    print(i)
    i += 10
    print('==>', i)
    # 0
    # ==> 10
    # 1
    # ==> 11
    # 2
    # ==> 12
    # 3
    # ==> 13
    # 4
    # ==> 14



# while (수식): True면 계속 돌고 False면 끝난다.
# 내부에 break 문이 없으면 무한루프에 돌게 된다.

while 1: # 상수값만 있으면 무한 루프; 항상 True 값. => while + 수식(변수 : 값이 변하는것)을 포함하고 있어야 함.
    print('hello')
    break

i = 0 # 수식에 사용되는 초기값 설정
while i < 5:
    print(i)
    # 수식에 사용된 변수의 값을 변경하는 부분이 반드시 내부에 있어야 함

for i in range(5):
    for j in range(5):
        for k in range(5):
            if k > j:
                break # 자기 자신이 쓰인 가장 가까운 for문에서 벗어나는 것. 중첩 for문을 전체적으로 벗어나진 않는다.

for i in range(5):
    print(i)
    if i == 5: # i의 값이 0, 1, 2, 3, 4까지만 돌기 때문에 이 조건문을 작동하지 않는다.
        break # break를 만나게 되면 else문은 작동되지 않는다.
else: # for 문이 다 돌고나서 종료 조건이 만족되었을 때 else가 만족이 된다.
    print('else...') 



