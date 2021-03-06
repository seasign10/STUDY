## :oncoming_automobile: 동기식 처리 모델 (Synchronous)

- 직렬적으로 task를 수행

- 태스크는 순차적으로 실행되며 어떤 작업이 수행중이면 다음 작업은 대기

  *ex) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 이후 태스크들은 블로킹(blocking) 된다.*

```python
from time import sleep # 잠시 시스템을 멈추게 하는 것

def sleep_3s():
    sleep(3)
    print('Wake up!')

print('Start sleeping')
sleep_3s() # 해당식이 동작되기 전까지는
print('End of program') # 동작하지 않게 된다. => 그때까지 코드의 실행을 blocking => 동기식 처리
```





## :oncoming_automobile: 비동기식 처리 모델 (Asynchronous)

- 병렬적으로 태스크를 수행

- 태스크가 종료되지 않는 상태라 하더라도 대기하지 않고 다음 태스크를 실행

  *ex) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 기다리지 않고(non-blocking) 즉시 다음 태스크를 수행*

- JS 대부분의 DOM 이벤트와 Timer 함수, Ajax 요청은 비동기식 처리 모델로 동작

```js
const nothing = () => {
  console.log('sleeping')
}

console.log('start')
setTimeout(nothing, 3000) // 단위가 밀리세컨드 => 3000 , 3초
console.log('end')
// start => end => sleeping 각자 따로 놀고있는 코드 실행 순서

function sleep_3s() {
  setTimeout(() => console.log('wake up'), 3000)
}
console.log('Start sleeping')
sleep_3s()
console.log('End of program')
// => 위와 동일, 종료될때 까지 기다리지 않고 실행 (non-blocking)
```





****



## :rocket: Blocking & Non-Blocking

- #### 이벤트 루프

- 단 한가지 **콜스택**과 **콜백큐**를 감시하는 역할만 한다.
- 만약 콜스택이 비어 있으면 이벤트 루프는 콜백큐에서 첫 번째 이벤트를 가져다가 콜스택에 밀어 넣고, 결과적으로 해당 이벤트가 실행된다.
- 이러한 반복은 이벤트 루프에서는 `tick` 이라고 한다.
- 이벤트 루프는 호스팅 환경(브라우저 or nodejs)에 내장된 메커니즘(JS 엔진에 있는게 아니다.)
- 이것은 시간의 흐름에 따라 코드의 수행을 처리하며 그때마다 JS 엔진을 작동 시킨다.



##### setTimeout(callback, msecs)

- callback 함수가 1초뒤에 실행될 것이다 라는 의미가 아니다.
- **1초 후에 콜백 큐에 추가될 것이라는 의미**
- 만약에 콜백 큐에 mycallback보다 먼저 추가된 이벤트가 있었을수도 있기 때문에 실제 1초보다 더 오랜시간이 걸릴 수도 있다.

- 참고 사이트 : [loupe](http://latentflip.com/loupe/?code=ZnVuY3Rpb24gcHJpbnRIZWxsbygpIHsNCiAgICBjb25zb2xlLmxvZygnSGVsbG8gZnJvbSBiYXonKTsNCn0NCg0KZnVuY3Rpb24gYmF6KCkgew0KICAgIHNldFRpbWVvdXQocHJpbnRIZWxsbywgMzAwMCk7DQp9DQoNCmZ1bmN0aW9uIGJhcigpIHsNCiAgICBiYXooKTsNCn0NCg0KZnVuY3Rpb24gZm9vKCkgew0KICAgIGJhcigpOw0KfQ0KDQpmb28oKTs%3D!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D)

```js
const nothing = () => {
  console.log('sleeping')
}

console.log('start')
setTimeout(nothing, 3000) // 단위가 밀리세컨드 => 3000 , 3초
console.log('end')
// start => end => sleeping 각자 따로 놀고있는 코드 실행 순서

function sleep_3s() {
  setTimeout(() => console.log('wake up'), 3000)
}
console.log('Start sleeping')
sleep_3s()
console.log('End of program')
// => 위와 동일, 종료될때 까지 기다리지 않고 실행 (non-blocking)

function first() {
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

first()
setTimeout(third, 1000)
second()


console.log('Hi')

setTimeout(function ssafy() {
  console.log('ssafy')
}, 100) // 마지막에 출력

console.log('bye')
```

- 밀리세컨드는 stack에 있는 시간일 뿐, 결국에는 callback구동이 끝나야 console에 들어가기 때문에 가장 늦게 나올 수 밖에 없다.



### callback function

```js
// 배열로 이루어진 숫자들을 모두 더하는 함수
const numberAddEach = numbers => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberSubEach = numbers => {
  let sub = 0
  for (const number of numbers) {
    sub += number
  }
  return sub
}

// 배열로 이루어진 숫자들을 모두 곱하는 함수
const numberMulEach = numbers => {
  let mul = 0
  for (const number of numbers) {
    mul += number
  }
  return mul
}

// 세 함수의 공통점 : 숫자로 이루어진 배열의 요소들을 각각 [???] 한다.
// [???]를 claaback 함수에서 처리하는 일로 바꿀 수 있다.

// base template 역할
const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

// 더하기
const addEach = (number, acc = 0) => {
  return acc + number
}

// 빼기
const subEach = (number, acc = 0) => {
  return acc - number
}

// 곱하기
const mulEach = (number, acc = 1) => {
  return acc * number
}

const NUMBERS = [1, 2, 3, 4, 5,]
console.log(numbersEach(NUMBERS, addEach))
console.log(numbersEach(NUMBERS, subEach))
console.log(numbersEach(NUMBERS, mulEach))

// 하지만 addEach, subEach, mulEach 를 다시 재사용 하지 않을 것 같다면
// numbersEach 이후의 제어를 함수 정의 없이 매번 자유롭게 하려면 어떻게 ?
console.log(numbersEach(NUMBERS, (number, acc=0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc * number))
```



### Axios

- `axiosXHR` 을 요청으로 보내고 응답 받은 결과를 Promise 객체로 반환해주는 라이브러리
- axios 는 현재 JS에서 가장 HOTㅘㄴ 라이브러리 중 하나이며 프론트 엔드 프레임 워크(react, vue)에서 데이터를 주고 받을 때 필수적으로 사용되고 있음(프론트엔프 프레임 워크 **<=>** api 서버 )

- [axios](https://github.com/axios/axios) : `npm install axios`

  ```js
  const axios = require('axios')
  
  // axios.get('http://jsonplaceholder.typicode.com/posts')
  //   .then(function(response) {
  //     console.log(response)
  //   })
  //   .catch(function(err) {
  //     console.log(err)
  //   })
  
  
  // refectoring
  axios.get('http://jsonplaceholder.typicode.com/posts')
    .then(response => {
      console.log(response)
    })
    .catch(err => {
      console.log(err)
    })
  ```



###### [getDogImage](https://dog.ceo/dog-api/)

`.then(response => console.log(response))`

![image](https://user-images.githubusercontent.com/52684457/67927677-90222d00-fbfc-11e9-94a8-278409f8d88e.png)

Object **=>** data **=>** message



`.then(response => console.log(response.data.message))`

![image](https://user-images.githubusercontent.com/52684457/67927711-9f08df80-fbfc-11e9-82b9-2dfcb480c1a6.png)



###### [getCatImage](https://thecatapi.com/)

`.then(response => console.log(response))`

Object **=>** data **=>** 0 **=>** url



`.then(response => console.log(response.data[0].url))`

data안의 `0`값 안에 `{...url:http...}` 이 있으므로, 리스트로 접근해서 url을 가져온다.



###### 결과물

```js
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    img {
      width: 300px;
      height: 300px;
    }
  </style>
</head>

<body>
  <button id="dog">멈머</button>
  <button id="cat">냐냐</button>

  <div class="animals"></div>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const getDogImage = function() {
      axios.get('https://dog.ceo/api/breeds/image/random')
        .then(response => {
          const imgUrl = response.data.message
          // img tag 만들기
          const imgTag = document.createElement('img')
          // imgTag 의 src에 imgUrl 넣기
          imgTag.src = imgUrl
          // .animals 라는 div 의 자식요소로 imgTag 를 붙이자.
          document.querySelector('.animals').append(imgTag)
        })
        .catch(error => console.log(error))
    }

    const getCatImage = function() {
      axios.get('https://api.thecatapi.com/v1/images/search')
        .then(response => { 
          const imgUrl = response.data[0].url
          const imgTag = document.createElement('img')
          imgTag.src = imgUrl
          document.querySelector('.animals').append(imgTag)
        })
        .catch(error => console.log(error))
    }

    // 사진이 나오는 버튼 만들기
    const dogButton = document.querySelector('#dog')
    dogButton.addEventListener('click', getDogImage)

    const catButton = document.querySelector('#cat')
    catButton.addEventListener('click', getCatImage)
  </script>
</body>

</html>
```

![image](https://user-images.githubusercontent.com/52684457/67929614-0f196480-fc01-11e9-9746-2303b58e8510.png)

- 비동기 이기 때문에, 누른 순서가아닌, 먼저 처리가 된 사진이 나온다.
- callback 은 화살표 함수를 쓰지 않는 것에 유의 할 것





