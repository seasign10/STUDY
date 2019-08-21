import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for i in range(T):
    N = int(input())
    ai = int(input())
    Zero_room = [0] * 10 # 0에서부터 9까지의 수가 사용 됨.

    for j in range(N): # N자리의 수만큼 for문 돌리기
        Zero_room[ai % 10] += 1
        # 10을 계속 나눠서 소수점에서 내려간 수를 하나씩 그 수의 그 인덱스에 Zero_room에 넣어준다.
        # +=1 은 누적하기 위함이며 이런 모양새가 된다 => 9의 숫자 도출 => [0, 0, 0, 0, 0, 0, 0, 0, 1] 9의 자리에 1이 누적된다.
        ai //=10 # 10을 나눈 몫을 저장
# print(Zero_room)
    many = 0

    for l in range(len(Zero_room)):
        if Zero_room[l] >= many: # Zero_room의 인덱스 l번째의 수가 many보다 크거나 같다면
            many = Zero_room[l] # 더 큰 숫자를 할당해준다.
            num = l 

        elif Zero_room[l] == many and l > Zero_room[l-1]:
            many = many

    result = num

    print('#{} {} {}'.format(i+1, result, many))
        
        
        
        
        
        