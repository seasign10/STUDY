import sys
sys.stdin = open("1970.txt", "r")

tc = int(input())

for i in range(1, tc+1): 

    # 중첩 for문을 사용할 필요가 없다. 거스름돈인 change라는 변수를 중복 사용함으로서 불필요한 계산을 줄인다.
    # 그리고 for문을 한번 더 사용하게 되면 if문부터 시작해서 넣어줘야할 조건이 굉장히 많아진다.
    # ex) 5만원보다 크다면... 그럼 5만원보다 작다면?, 그 와중에 만원보다 크다면... 또 만원보다 작다면? ...

    change = int(input()) # 이 곳 for문을 전부 다 돌고 다음 거스름돈이 들어올때 새로 change = int(input())이 들어오므로 for을 굳이 더 사용할 필요 x
    f_m = int(change / 50000) # 50000을 나눈 몫이 5만원이 필요한 개수, int로 묶는 대신 //을 사용해주어도 될 것 같다.
    
    change = change % 50000 # 현재 거스름돈 50000원이 필요한 상황이 없어진 돈의 나머지
    m = int(change / 10000) # 그 나머지를 다시 10000을 나눠서 나오는 몫 int(정수)값 m(만원)

    change = change % 10000
    f_ch = int(change / 5000)

    change = change % 5000
    ch = int(change / 1000)

    change = change % 1000
    f_b = int(change / 500)

    change = change % 500
    b = int(change / 100)

    change = change % 100
    f_s = int(change / 50)

    change = change % 50
    s = int(change / 10) # 위의 과정을 반복 후 마무리.
    
    print('#{}'.format(i))
    print(f_m, m, f_ch, ch, f_b, b, f_s, s) # int값 이므로 굳이 fstring, format을 쓸 필요없이 변수명 입력.

    # 풀이 소요 시간 : 약 30분

    
 