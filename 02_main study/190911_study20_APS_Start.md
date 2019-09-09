# :card_file_box: APS : Start 

> ###### 1. Start
>
> - 비트 연산, 진수, 실수
>
> ###### 2. 완전탐색, 탐욕
>
> - 순열, 조합 생성
>
> ###### 3. 분할정복, 백트래킹
>
> - 순열, 조합 생성, N-Queen, 동전 거스름돈
> - 퀵정렬, 병합정렬
>
> ###### 4. 그래프
>
> - DFS, BFS
> - 최단경로(다익스트라), 최소 신장 트리(Prim, Kruskal)
> - Disjoint-Set(자료구조)
>
> ###### 5. 문자열
>
> - 패턴 매칭, 접미어 트리, 접미어 배열
>
> ###### 6. 동적 계획법
>
> ###### 7. 동적 계획법, NP-Complete
>
> ###### 8. 근사해, 수학(경우의 수 확률, 정수론)



> ###### 이해하기
>
> 1. SW 문제 해결 역량이란?
> 2. 역량 강화하는 방법
> 3. 효율적인 알고리즘의 필요성
> 4. 알고리즘 성능 측정 방법 중 하나인 시간복잡도
> 5. 프로그램을 작성하기 위한 기본 중 표준 입출력 방법
> 6. 비트 수준의 연산과 알고리즘
> 7. 컴퓨터에서의 실수 표현 방법



> ###### 복잡도의 점근적 표기
>
> - 시간 (또는 공간) 복잡도는 입력 크기에 대한 함수로 표기하는데, 이 함수는 주로 ㅇ ㅕ러개의 항을 가지는 다항식
> - 이를 단순한 함수로 표현하기 위해 점근적 표기(Asymptotic Notation)를 사용
> - 입력 크기 n이 무한대로 커질 때의 복잡도를 간단히 표현하기 위해 사용하는 표기법
>   - O(Big-Oh) - 표기
>   - Ω(Big-Omega) - 표기
>   - Θ(Big-Theta) - 표기



> ###### python3 표준입출력
>
> - 입력
>   - Raw 값의 입력 : input()
>     - 받은 입력값을 문자열로 취급
>   - Evaluated된 값 입력 : eval(input())
>     - 받은 입력값을 평가된 데이터 형으로 취급
> - 출력
>   - print()
>     - 표준 출력 함수. 출력값의 마지막에 개행 문자 포함
>   - print('text', end='')
>     - 출력 시 마지막에 개행문자 제외할 시
>   - print('%d'%number)
>     - Formatting 된 출력



> ###### 파일의 내용을 표준 입력으로 읽어오는 방법
>
> - import sys
> - sys.stdin = open('A.text', 'r')
>
> ```python
> import sys
> sys.stdin = open('input.text', 'r')
> sys.stdout = open('output.text', 'w')
> 
> text = input()
> print(text)
> ```
>
> - `intput()`, `int(input())`, `list(map(int, input().split()))` 등을 사용하여 읽어오기
> - `list(map(int, input().split()))` : 한 줄 입력 받아서 공백 기준으로 나누고, 정수로 형 변환
> - `map(int, input().split())` : 한 줄이 아닌, 각각의 변수로 받을 때 사용
>   - map을 사용하면 형변환이 용이하기 때문에 사용(str => int)
>     input()값은 기본 str값을 가지고 有



#### :arrows_counterclockwise: 비트연산자의 기능

| 연산자 | 연산자의 기능                                                |
| :----: | ------------------------------------------------------------ |
|   &    | 비트단위로 AND 연산을 한다.<br />예) num & num2              |
|   \|   | 비트단위로 OR 연산을 한다.<br />예) num \| num2              |
|   ^    | 비트단위로 XOR 연산을 한다. (같으면 0 다르면 1)<br />예) num ^ num2 |
|   ~    | 단항 연산자로서 피연산자의 모든 비트를 반전시킨다.<br />예) ~num |
|   <<   | 피연산자의 비트 열을 왼쪽으로 이동<br />예) num << 2         |
|  \>>   | 피연산자의 비트 열을 오른쪽으로 이동<br />예) num >> 2       |

> ###### 1 << n
>
> - 2^n의 값을 갖는다.
> - 원소가 n개일 경우의 모든 부분집합의 수를 의미
> - Power set (모든 부분 집합)
>   - 공집합과 자기 자신을 포함한 모든 부분집합
>   - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.
>
> ###### i & (1 << j)
>
> - 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미



> ###### 비트 연산 예제1
>
> ```python
> def Bbit_print(i):
>     output = ''
>     for j in range(7, -1, -1):
>         output += '1' if i & (1 << j) else '0'
>     print(output)
>     
> for i in range(-5, 6):
>     print('%3d' % i, end-'')
>     Bbit_print(i)
> ```
>
> ![](https://user-images.githubusercontent.com/52684457/64498316-f66e8b80-d2ee-11e9-8fc7-bee837b07f5f.png)
>
> 



> ###### 비트 연산 예제2
>
> ```python
> def Bbit_print(i):
>     output = ''
>     for j in range(7, -1, -1):
>         output += '1' if i & (1 << j) else '0'
>     print(output, end=' ')
> a = 0x10
> x = 0x01020304
> print('%d = ' % a, end='')
> Bbit_print(a)
> print()
> print('0%X = ' % x, end='')
> for i in range(0, 4):
>     Bbit_print((x >> i*8) & 0xff)
> ```
>
> ![](https://user-images.githubusercontent.com/52684457/64498460-8ad8ee00-d2ef-11e9-9e72-c1e603b0695f.png)



>###### 엔디안 (Endianness)
>
>- 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW 아키텍처마다 다르다.
>- 주의 : 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산 할 때 올바로 이해하지 않으면 오류를 발생 시킬 수 있다.
>- 엔디안은 크게 두 가지로 나뉨
>  - 빅 엔디안(Bing-endian)
>    - 보통 큰 단위가 앞에 나옴. 네트워크
>  - 리틀 엔디안(Litthle-endian)
>    - 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터
>
>|    종류     | 0x1234의 표현 | 0x12345678의 표현 |
>| :---------: | :-----------: | :---------------: |
>|  빅 엔디안  |     12 34     |    12 34 56 78    |
>| 리틀 엔디안 |     34 12     |    78 56 34 12    |
>
>
>
>###### 비트 연산 예제3
>
>- 엔디안 확인 코드
>
>```python
>n = 0x00111111
>
>if n & 0xff:
>    print('little endian')
>else:
>    print('big endian')
>```
>
>###### 비트 연산 예제4
>
>- 엔디안 변환 코드
>
>```python
>def ce(n): # change endian
>    p = []
>    for i in range(0, 4):
>        p.append((n >> (24 - i*8)) & 0xff)
>    return p
>```
>
>```python
>def ce1(n):
>    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000)
>| (n >> 8 & 0xff00) | (n >> 24 & 0xff)
>```
>
>```python
>x = 0x01020304
>p = []
>for i in range(0, 4):
>    p.append((x >> (i*8))& 0xff)
>
>print('x = &d&d&d&d' % (p[0], p[1], p[2], [3]))
>p = ce(x)
>print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
>```



> ###### 비트 연산 예제5
>
> - 비트 연산자 ^를 두 번 연산하면 처음 값을 반환한다.
>
> ```python
> def Bbit_print(i):
>     output = ''
>     for j in range(7, -1, -1):
>         output += '1' if i & (1 << j) else '0'
>     print(output)
> a = 0x86
> key = 0xAA
> 
> print('a      ==>', end='')
> Bbit_print(a)
> 
> print('a^=key ==>', end='')
> a ^= key
> Bbit_print(a)
> 
> print('a^=key ==>', end='')
> a ^= key
> Bbit_print(a)
> ```
>
> ![](https://user-images.githubusercontent.com/52684457/64498866-7a297780-d2f1-11e9-8a36-564c7d3ff1f9.png)



> #### :repeat_one: 진수
>
> **0o** 로 시작하면 2진수   **==>** `bin`  2진법
>
> **0b** 로 시작하면 8진수   **==>** `oct`  8진법
>
> **0x** 로 시작하면 16진수 **==>** `hex `  16진법
>
> `int`로 10진수를 바꾸어주어도 되지만  `ord()`(아스키 코드)를 사용하여 바꾸어 주어도 된다.
>
> ![](https://user-images.githubusercontent.com/52684457/64498914-bc52b900-d2f1-11e9-9af8-846a9b86674c.png)
>
> ![](https://user-images.githubusercontent.com/52684457/64498963-f1f7a200-d2f1-11e9-88c5-ba3c41702fc1.png)
>
> ###### 컴퓨터에서의 음의 정수 표현 방법
>
> - 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환
>   - -6 : 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 : 부호와 절대값 표현
>   - -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 : 1의 보수 표현
> - 2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다
>   - -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 : 2의 보수 표현



> #### :repeat_one: 실수
>
> ![](https://user-images.githubusercontent.com/52684457/64499355-97f7dc00-d2f3-11e9-9645-cbe544c4cc60.png)
>
> ![](https://user-images.githubusercontent.com/52684457/64499364-a9d97f00-d2f3-11e9-974f-d6e614ecfca9.png)
>
> - 실수의 표현
>   - 컴퓨터는 실수를 표현하기 위해 부동 소수점(floaring-point) 표기법을 사용
>   - 부동 소수점 표기 방법은 소수점의 위치를 고정시켜 표현하는 방식
>     - 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밑수의 지수승으로 표현
>
> ```
> 1001.0011 => 1.0010011 x 2^3
> ```
>
> - 실수를 저장하기 위한 형식
>
>   - 단정도 실수(32비트)
>   - 배정도 실수(64비트)
>
>   ![](https://user-images.githubusercontent.com/52684457/64499473-105e9d00-d2f4-11e9-8a66-288dd1d3bbb8.png)
>
>   ![](https://user-images.githubusercontent.com/52684457/64499577-924ec600-d2f4-11e9-8f93-375c717e5238.png)
>
>   ![](https://user-images.githubusercontent.com/52684457/64499639-de016f80-d2f4-11e9-9e7d-a3a175f8f4c5.png)

























