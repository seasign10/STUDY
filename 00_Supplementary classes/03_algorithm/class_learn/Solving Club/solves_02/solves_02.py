for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    cnt = [0] * 101 # 빈도수 저장하는 List
    for val in arr:
        cnt[val] += 1
        
        minIdx, maxIdx = 0, 100
        i = 0
        while i < dump:
            while cnt[minIdx] == 0:
                minIdx += 1
            while cnt[maxIdx] == 0:
                maxIdx -= 1
                
            cnt[minIdx] -= 1
            cnt[minIdx + 1] += 1
            cnt[maxIdx] -= 1
            cnt[maxIdx - 1] += 1
            i += 1

if cnt[minIdx] == 0: minIdx += 1
if cnt[maxIdx] == 0: maxIdx -= 1