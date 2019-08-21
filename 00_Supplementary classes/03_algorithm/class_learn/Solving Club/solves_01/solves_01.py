import sys
sys.stdin = open("input.txt", "r")

for k in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_count = 0
    # print(N, arr)

    for i in range(N):
        if arr[i] == 0:
            pass
        elif arr[i] != 0:
            for j in range(arr[i]):
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    if arr[i] > arr[i-2] and arr[i] > arr[i+2]:
                        arr_count += 1
                        arr[i] -= 1
                else:
                    break
    print('#{} {}'.format(k+1, arr_count))
