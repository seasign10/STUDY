num = int(input())

double = 0
li = []
for i in range(1, 100): 
    if double >= 99:
        break
    else:
        double += num
        if double > 100:
            break
        li.append(double)
        if double % 10 ==0:
            break
for j in li:
    print(j, end=' ')
