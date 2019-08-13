# CSV

- 셀 단위단위가 ,(콤마)로 이루어져있음. 

```python
avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    },
    {
        "name": "thor odinson",
        "gender": "male",
        "appearances": 2402,
        "years since joining": 52
    },
    {
        "name": "steven rogers",
        "gender": "male",
        "appearances": 3458,
        "years since joining": 51
    }
]
```

```python
# 1. csv.DictWriter()

import csv
with open('avenger.csv', 'w', newline='', encoding='utf-8') as f:
    # newline='', encoding='utf-8' 는 윈도우가 깨지지 않도록 쓴 것.

    # 저장할 페이퍼들의 필드 이름을 미리 정한다. (헤더를 정해야 함.)
    fieldnames = ('name', 'gender', 'appearances', 'years since joining')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()

    # 딕셔너리를 순회하며 key를 통해 한 줄씩(value를) 작성한다.
    # 리스트 안에 딕셔너리가 있는 형태기 때문에 .value()를 넣으면 안됨.
    for avenger in avengers:
        writer.writerow(avenger)
```

저장 후 실행 시키면, avengers.csv 파일이 생성된다.

![](https://user-images.githubusercontent.com/52684457/61501086-ba166180-aa08-11e9-8405-300c3141fe0f.PNG)

확장자를 설치한 후

![](https://user-images.githubusercontent.com/52684457/61501241-7708be00-aa09-11e9-92fb-48290051e9ca.png)

Open Preview를 하면 확인 가능하다.

```python
# 2. csv.DictReader()
import csv
with open('avengers.csv',newline='', encoding='utf8') as f:
    reader = csv.DictReader(f)

    # 한 줄씩 읽는다.
    for row in reader:
        print(row['name'])
        print(row['gender'])
        print(row['appearances'])
        print(row['years since joining'])
```

파일 실행 후 얻을 수 있는 값.

```python
tony stark
male
3068
52
robert bruce banner
male
2089
52
thor odinson
male
2402
52
steven rogers
male
3458
51
```

