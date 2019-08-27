# a = ['d', 'a', 'e', 's', 'd', 5, 5, 'd', 3, 'g', 's']
b = []

def isEmpty():
    return len(b) == 0

for i in range(4):
    b.append(i)
    print('들어오는 숫자 =>', i, '리스트 =>', b)

while not isEmpty(): # 빈 리스트가 될때까지 계속 실행
    print('빠지는 숫자=>', b.pop(), '리스트=>', b)
