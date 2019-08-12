# 재귀 함수 - 자기 자신을 호출하는 함수
# 재귀 호출 ---> 재귀적 정의(점화식) 구현하기에서 많이 쓰임
# 그래프의 깊이 우선 탐색, 백 트래킹
# for, while 사용하지 않고 반복적 작업을 할 수 있다.

def printHello():

    print('Hello!!!')
    printHello()
# 무한루프에 빠지게 된다.

def printHello():
    if i < 3: # 조건을 넣어서 돌아가게끔 한다.
        print('Hello!!!')
        printHello()

#---------------------------
printHello()

# 위와 비슷한 패턴
for i in range(3):
    print('Hello!!!')

    -

