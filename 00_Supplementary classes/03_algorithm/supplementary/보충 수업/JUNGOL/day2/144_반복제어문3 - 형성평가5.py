num = int(input())
n = (2*num) - 2 # 최대값에서 -1만 해주면 공백값을 생성 가능
one = 1 # 1부터 시작해서 +2, +2 씩 되는 것을 해주기 위한 변수
for i in range(num):
    print(' '*n + '*'*one)
    n -= 2
    one += 2 # 가운데 정렬 시에는 한칸씩 사용했던 공백이 다 몰아서 왼쪽으로 왔기 때문에
    # 두칸씩 더해준다.