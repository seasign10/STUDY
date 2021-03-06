# :roller_coaster: 동적 프로그래밍(DP)​

- 경우의 수가 굉장히 많아지는 경우 시간초과가 생긴다
  **=>** 컷팅(가지치기)이 <u>가능하다면</u> 가지를 친다 (백트래킹)



###### DP ?

- 큰 문제의 해답에 작은 문제의 해답이 포함되어 있고 이를 재귀 호출 알고리즘으로 구현하면 지나친 중복이 발생하는 경우 이 재귀적 중복을 해결하는 방법
- 어떤 문제가 여러 단계의 반복되는 부분 문제로 이루어질 때, 각 단계에 있는 부분 문제의 답을 기반으로 전체 문제의 답을 구하는 방법
- 작은 문제들의 해를 먼저 구하여 저장하고 더 큰 문제의 해를 구할 때 작은 문제의 해를 반복 계산하지 않고 저장된 결과를 사용하는 방법



#### :balloon: 동적 프로그래밍(DP)는 다음과 같이 언급 할 수 있다.

> #### DP = ? 
>
> - 완전검색을 하는데 좀 스마트 하게 하는 방법
>
> - `Recurcive` + `Memoizaition`
>
> - 점화식을 찾으면 된다.



#### :balloon: 재귀 호출 알고리즘

##### :ok_hand: 재귀적 해법이 바람직한 예

- 퀵 정렬, 병합정렬 등의 정렬 알고리즘

  ```
  병합정렬은 절반으로 나누었을시 양쪽이 전혀 다른 데이터를 가지고 있기 때문에 끝 단에 가다보면 중복이 생기는 경우가 많아진다.
  ```

  - 부분 적인 정답을 이용해서 해 구하기

- 계승(Factorial) 구하기

- 그래프의 너비 우선 탐색 등



##### :warning: 재귀적 해법이 치명적인 예

- 피보나치 수 구하기

  ```python
  fibo(n)
  
  if n < 2 : return n # 1과 0을 리턴
  else : return fibo(n - 1) + fibo(n - 2)
  ```

  ```python
  def fibo(n):
      if n < 2:
          return n
      else:
      	return fibo(n - 1) + fibo(n - 2)
  
  N = int(input())
  print('피보나치 결과:', fibo(N))
  ```

  ```python
  def fibo(n):
      global cnt
      cnt += 1
      if n < 2:
          return n
      else:
      	return fibo(n - 1) + fibo(n - 2)
  
  cnt = 0
  N = int(input())
  print('피보나치 결과:', fibo(N))
  print('호출 횟수:', fibo(N))
  ```

  - 수가 커질수록 호출 횟수가 기하급수적으로 증가한다.
    `input()` : 20 **=>** 피보나치 결과 : 6765
                                  호출 횟수 : 21891
  - 중복 호출이 생기기 때문



## :memo: Memoization

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술, 도억 계획법의 핵심이 되는 기술



> - 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장(메모이제이션)하면 실행시간을 0(n) 으로 줄일 수 있다.
>
>   ```python
>   '''memo를 위한 배열을 할당, 모두 -1로 초기화
>   memo[0]을 0으로 memo[1]은 1로 초기화'''
>   
>   def fibo(n): # DP를 이용한 피보나치(메모제이션)
>       if n >= 2 and memo[n] == -1:
>           memo[n] = fibo(n-1) + fibo(n-2)
>       return memo[n]
>   
>   N = int(input())
>   memo = [-1] * (N + 1)
>   memo[0] = 0
>   memo[1] = 1
>   
>   print('피보나치 결과:', fibo(N))
>   # print(memo)
>   ```
>
>   ```python
>   def fibo(n): # DP를 이용한 피보나치(반복)
>       memo[0] = 0
>       memo[1] = 1
>       for i in range(2, n+1):
>           memo[i]=memo[i-1]+memo[i-2]
>       return memo[n]
>   
>   N = int(input())
>   memo = [-1] * (N + 1)
>   print('피보나치 결과:', fibo(N))
>   ```
>
>   - 호출 횟수가 줄어든 것을 확인 할 수 있다.
>     `input()` : 20 **=>** 피보나치 결과 : 6765
>                                   호출 횟수 : 39





# :keyboard: 컴퓨팅 사고력

![image](https://user-images.githubusercontent.com/52684457/66279912-062dbf80-e8ef-11e9-875d-bdd027273044.png)

![1570412416948](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570412416948.png)

![image](https://user-images.githubusercontent.com/52684457/66281080-a508ea80-e8f4-11e9-88cc-c32a2a77879b.png)



###### :one: (직접 증명) n이 홀수이면 n**2 + n은 짝수임을 증명할 때

> - 짝수 : 2k (2의 배수)
>
> - 홀수 : 2k + 1
>
> - n = 2k + 1
>   (2k + 1)^2 + 2k + 1
>   =  4k^2 + 4k + 1 + 2k + 1
>
>   =  4k^2 + 6k + 2
>
>   = 2(2k^2 + 3k + 1)
>
>   ∴ 2로 묶어지므로 (2의 배수 이므로) 짝수이다.



###### :two: (직접 증명) m이 짝수이고  n이 홀수이면 2m + 3n은 홀수임을 증명

> - m : 2k
>
> - n : 2l + 1
>
> - 2 * 2k + 3(2l + 1)
>   = 4k + 6l + 3
>   = 2(2k + 3l + 1) + 1
>
>   (2k + 3l + 1) 을 P라고 치환할 때
>   ∴  2P(짝수) + 1 **=>** 홀수



###### :three: (간접 증명 : 대우를 증명) 자연수 n에 대해, n^2 + 5가 홀수이면 n은 짝수임을 증명

> - n^2 + 5가 홀수이면 n은 짝수
>   **=>** 명제 : p → q
>   **=>** ~q → ~p
>
> (힌트 : 명제 대신, n이 홀수(2k + 1)이면, n^2 + 5는 짝수임을 증명)
>
> - n = 2k + 1
>
> - n^2 + 5 = (2k + 1)^2 + 5
>
>   = 4k^2 + 4k + 6
>
>   = 2(2k^2 + 2k +3)
>   ∴  자연수 m에 대해 n^2 + 5가 홀수이면 n은 짝수임이 성립



###### :four: (간접 증명 : 대우를 증명) n^2이 짝수이면 n은 짝수임을 증명

> - n = 2k + 1
>
> - (2k+1)^2
>   = 4k^2 + 4k + 1
>   = 2(2k^2 + 2k) + 1
>
>   ∴ 홀수 **=>** (p → q ) = (~p → ~q ) 
>   **=>** 제곱이 짝수면 짝수



###### :five: (경우를 나누어 증명) 자연수 n에 대해 n^2 + 5n + 3은 항상 홀수임을 증명

> ( 힌트 : n이 짝수인 경우와 홀수인 경우를 따로 증명 )
>
> - 홀수 : n = 2k + 2
>
> - (2k + 1)^2 + 5(2k + 1) + 3
>   = 4k^2 + 4k + 1 + 10k + 8
>   = 4k^2 + 14k + 9
>   = 2(2k^2 + 7k + 4) + 1
>
>   ∴  홀수
>
> - 짝수 : n = 2k
>
> - n^2 + 5n + 3
>
>   = 4k^2 + 10k + 3
>   = 2(2k^2 + 5k + 1) + 1
>
>   ∴  홀수
>
> <u>홀수일 때, 짝수일 때 전부 홀수 임을 알 수 있다.</u>



###### :six: 어떤 자연수를 제곱하여도 그 결과를 3으로 나눈 나머지는 2가 아님을 증명

> **=>** n : 3k, 3k + 1, 3k + 2 이 3가지 경우로 나누어 생각해보면 된다. 
>
> - 3k^2, (3k + 1)^2, (3k + 2)^2 
>
>   **=>** 나머지가 순서대로 0, 1, 1이 남는 것을 알 수 있다. 
>
>   **=>** 그러므로 어떤 수를 제곱하여도 나머지는 2가 되지 않음을 성립



###### :seven: (모순 증명법 : 귀류법)​ 유리수와 무리수의 합은 무리수임을 증명

> (힌트 : 어떤 유리수와 어떤 무리수의 합이 유리수가 된다고 가정하고 모순을 이끌어 낼 수 있는가?)
>
> - 유리수 + 무리수 = 무리수
>
> - 유리수 + 무리수 = 유리수 **=>** :star: **모순**
>
>   ∴ a + b = c        유 + 무 = 유
>       b = c - a **(X)**   무 = 유 - 유



###### :eight: 루트2는 무리수임을 증명

> (힌트 : 유리수가 된다는 것은 기약분수로 표현이 된다는 것) 
>
> - 루트 2가 유리수라는 반대 가정을 두고 생각해보자.
>
>   **=>** 루트2 = b/a (a, b는 서로소인 정수)
>
> - 루트2a = b
>   2a^2 = b^2
>
>   b^ = 2a^2
>
>   ∴  b^2이 2의 배수이므로 b또한 2의 배수. a, b는 서로소라는 조건에 모순되므로 루트2는 무리수가 된다.



###### :nine: log<sub>2</sub> 5는 무리수임을 증명

> - log<sub>2</sub> 5 = b/a (a, b는 서로소인 정수) 유리수라고 가정
>
> - 2<sup>b/a</sup> = 5 이고, 양변을 a제곱하게 되면 2^b = 5^a
>
>   ∴ 하지만 해당 수식을 만족하는 자연수 a, b는 존재하지 않으므로 유리수라는 가정에 모순



###### :one::zero: (수학적 귀납법) 1 + 2 + 3 + … + n = n(n+1)/2 임을 증명

> 1. n = 1      (True)
>
>    ```python
>    1 = (1*2)/2 = 1 #True
>    ```
>
> 2. n = k      (가정*(假定)* : True)
>
>    ```python
>    1+2+3+...+k = k(k+1)/2
>    ```
>
> 3. n = k+1 (?) :star:
>
>    ```python
>    1+2+3...+k+(k+1) = (k+1)*(k+2)/2
>    ```
>
>    - 3번을 참이라는 것을 증명하면 참인 것을 증명 가능
>
>      ```python
>      # 좌변
>      k(k+1)/2 + (k+1)
>      = (k^2 + k + 2k + 2)/2
>      = (k^2 + 2k + 2)/2
>      
>      # 우변
>      (k^2 + 2k + k + 2)/2
>      = (k^2 + 2k + 2)/2
>      
>      # 좌변 우변 동일
>      ```



###### :one::one: 1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> + ... + n<sup>2</sup> = (n(n+1)(2n+1))/6 임을 증명

> 1. n = 1
>
>    ```python
>    1 = (1*2*3)/6 = 1 # True
>    ```
>
> 2. n = k
>
>    ```python
>    (k(k+1) * (2k+1))/6 # True라고 가정
>    ```
>
> 3. n = k+1
>
>    ```python
>    ((k+1) * (k+2) * (2(k+1)+1))/6
>    = (k(k+1) * (2k+1))/6 + (k+1)^2
>    = (2k^3 + 3k^2 + k + 6k^ + 12k +6)/6
>    = (2k^3 + 9k^2 + 13k + 6)/6 # 좌변
>    ```



###### :one::two: 2 이상의 모든 자연수 n에 대해 n<sup>3</sup> - n 은 6으로 나누어 떨어짐을 증명

> - n = 1
>   1 - 1 = 0 (참)
>
> - n = k
>   k^3 - k = 6m (참이라 가정)
>
> - n = k+1
>   (k+1)^3 - (k+1)
>   = k^3 + 3k^2 + 3k + 1 - k - 1
>
>   = k(k^2 + 3k + 2)
>
>   = k(k+1)(k+2)





![img](https://user-images.githubusercontent.com/52684457/64935105-fc81e080-d889-11e9-8bac-3b4cdee7ec9a.png)

- nCr = r! * (n!/(n-r)!)

|                                                              |           |                                                              |
| :----------------------------------------------------------: | :-------: | ------------------------------------------------------------ |
| ![image](https://user-images.githubusercontent.com/52684457/66360751-22952f00-e9b7-11e9-8842-be832a7b8f04.png) |   함수    | 수학에서, 함수 또는 사상은 첫 번째 집합의 임의의 한 원소를 두 번째 집합의 오직 한 원소에 대응시키는 이항 관계이다. |
| ![image](https://user-images.githubusercontent.com/52684457/66360695-f9749e80-e9b6-11e9-84af-3a214178760f.png) | 단사 함수 | 수학에서, 단사 함수 또는 일대일 함수는 정의역의 서로 다른 원소를 공역의 서로 다른 원소로 대응시키는 함수이다. 공역의 각 원소는 정의역의 원소 중 최대 한 원소의 상이다 |
| ![image](https://user-images.githubusercontent.com/52684457/66360738-16a96d00-e9b7-11e9-9496-f9c598bef4cc.png) | 전사 함수 | 수학에서, 전사 함수 또는 위로의 함수는 공역과 치역이 같은 함수이다. |
| ![image](https://user-images.githubusercontent.com/52684457/66360760-27f27980-e9b7-11e9-9830-1b01ed4c5038.png) |  역함수   | 수학에서, 역함수는 변수와 함숫값을 서로 뒤바꾸어 얻는 함수이다. 즉, 역함수의 대응 규칙에서, 원래의 출력값은 원래의 입력값에 대응한다. |























