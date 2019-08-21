import sys
sys.stdin = open("1989.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    arr = input()
    m = len(arr)

    for i in range(m//2):
        if arr[i] == arr[m-1-i]:
            result = '1'
        else:
            result = '0'
    # print(result)


    print('#{} {}'.format(k, result))

T = int(input())
    for m in range(1, T+1):
        arr = list(map(str, input()))
        new_arr = [i for i in arr]
        for i in range(len(arr)//2):
            new_arr[len(arr)-1-i], new_arr[i] = arr[i], arr[len(arr)-1-i]
        if new_arr == arr:
            print('#{} 1'.format(m))
        else:
            print('#{} 0'.format(m))