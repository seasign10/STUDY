import sys
sys.stdin = open("1983.txt", "r")

t = int(input())

for i in range(1, t+1):
    num, student = map(int, input().split()) # num: 학생 수, student: 학점 확인을 원하는 학생의 번호 ~번째 학생
    stu_lists = []
    num_lists = []

    for j in range(num):
        mid, fin, hom = map(int, input().split())
        result = (mid*0.35) + (fin*0.45) + (hom*0.2) # 총점 = 중간고사 35% + 기말고사 45% + 과제 20%
        num_lists.append(j+1) # 학생 값을 지정해줄 리스트 => zip 을 사용해서 학생 점수와 묶어줄 것
        # stu_lists.append(round(result,3)) # 출력값 읽기 편하도록 잠시 반올림.
        stu_lists.append(result) # 학생의 총점
        # stu_dict = {num_list: stu_list for num_list, stu_list in zip(num_lists, stu_lists)}
        # value 값 기준으로 정렬 하려면 lambda함수를 써야하므로, 키: 값 위치를 총점: 학생 번호로 딕셔너리를 생성
        stu_dict = {stu_list: num_list for stu_list, num_list in zip(stu_lists, num_lists)}
        # print(stu_dict)
        point_sort = sorted(stu_dict.items(), reverse=True) # 각 케이스마다 튜플로 정렬해서 저장.
        # print(point_sort) # 튜플이 되는 것을 확인 할 수 있다.
    # print(point_sort[0][0]) 인덱스로 접근이 가능한것을 확인. 인덱스로 접근해보자. 

    # 전체는 num, 학생 순위(등수)는 정렬한 것에서 인덱스를 사용.

    for l in range(len(point_sort)):
        if point_sort[l][1] == student:
            rank = l # 학생 순위, 원래 + 1을 해야 인덱스 0에서 1부터 시작한다. / 근데 문제는 +1을 하지 않아야 답이나온다 왜지?
    # print(rank)

    # 학점 계산 num/10
    # 백분위 = 학생 순위/전체
    # 즉, 백분위 = (point_sort[각자 순위]/전체 학생 수) * 100
    per = (rank/num) * 100

    if 10 > per:
        print('#{} A+'.format(i))
    elif 20 > per:
        print('#{} A0'.format(i))
    elif 30 > per:
        print('#{} A-'.format(i))
    elif 40 > per:
        print('#{} B+'.format(i))
    elif 50 > per:
        print('#{} B0'.format(i))
    elif 60 > per:
        print('#{} B-'.format(i))
    elif 70 > per:
        print('#{} C+'.format(i))
    elif 80 > per:
        print('#{} C0'.format(i))
    elif 90 > per:
        print('#{} C-'.format(i))
    else:
        print('#{} D0'.format(i))
    
# 풀이 소요 시간 : 약 3~4 시간