# :yellow_heart: Java Script

- ##### ES6 표준

- [NODEJS](https://nodejs.org/ko/download/)

  [**Windows Installer (.msi)**64-bit](https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi)

- 설치 후 bash 에서 버전 확인

  ```bash
  student@DESKTOP MINGW64 /
  $ node -v
  v12.13.0
  
  student@DESKTOP MINGW64 /
  $ npm -v
  6.12.0
  ```



## :vs: VS code 설정

![image](https://user-images.githubusercontent.com/52684457/67741101-667dd000-fa5b-11e9-8739-eeaa32a6e86c.png)

- ###### settings.json (F1 에서 검색)

```json
    "[python]": {
        "editor.tabSize": 4
        "editor.insertSpaces": true
    },
```

​	*추가*



### :large_blue_diamond: let

![image](https://user-images.githubusercontent.com/52684457/67741259-e2781800-fa5b-11e9-9f38-c713a6011671.png)

- 값을 재할당 할 수 있는 변수를 선언
- 단, 각 변수는 **한번만 선언** 할 수 있다. (할당은 여러번 가능)
  즉, **재선언** 불가

- 블록 유효 범위(block scope)

  ```js
  let x = 1
  
  if (x === 1) {
    let x = 2
  }
  ```

  - 블록{} 안에 있는 것과, 밖에 있는 함수할당은 다른 것

  ```js
  // let(변수))
  let x = 1
  
  if (x === 1) {
    let x = 2
  
    console.log(x) //2
  }
  
  console.log(x) //1
  ```

  - python 이 `python 파일명.py` 라면 java script는 `node 파일명.js` 으로 터미널에서 실행



### :large_blue_diamond: const 

- 값이 변하지 않는 상수를 선언하는 키워드

- 담긴 값이 불변임을 뜻하는 게 아니다.

- 단지 상수의 값은 **재할당 할 수 없고 재선언도 불가**능

- 블록 유효 범위(block scope)

  ```js
  //const
  
  // const 선언시 초기값을 생략하면 오류 발생
  const MY_FAV
  ```

  ```bash
  const MY_FAV
        ^^^^^^
  
  SyntaxError: Missing initializer in const declaration
  ?[90m    at Module._compile (internal/modules/cjs/loader.js:892:18)?[39m
  ?[90m    at Object.Module._extensions..js (internal/modules/cjs/loader.js:973:10)?[39m
  ?[90m    at Module.load (internal/modules/cjs/loader.js:812:32)?[39m
  ?[90m    at Function.Module._load (internal/modules/cjs/loader.js:724:14)?[39m
  ?[90m    at Function.Module.runMain (internal/modules/cjs/loader.js:1025:10)?[39m
  ?[90m    at internal/main/run_main_module.js:17:11?[39m
  ```

  - 값을 할당해보자

  ```js
  const MY_FAV = 7
  
  console.log('my favourite number is: ' + MY_FAV)
  
  // my favourite number is: 7
  ```

  - `MY_FAV = 20` 재할당 `const MY_FAV = 20` 재선언 등은 불가능

  - 하지만 불변은 아니다.

    ```js
    if (MY_FAV === 7) {
      // 블록 유효 범위로 지정된 MY_FAV 라는 변수를 만드므로 괜찮다.
      // 즉, 전역이 아닌 범위안이므로 이름 공간에서 충돌이 나지 않는다.
      const MY_FAV = 20
    
      console.log('my favourite number is: ' + MY_FAV) // 20
    }
    
    console.log(MY_FAV) // 7
    ```



### :large_blue_diamond: var (변수)

- 어디서나 **재할당 재선언 가능**

- ES6 이전의 feature 로 예기치 않은 문제를 많이 발생시키는 키워드로 절대 사용하지 않는다.

- 함수 유효 범위 (function scope)

- var로 선언된 변수의 범위는 현재 실행 문맥

  - 이 문맥이 함수 혹은 함수 외부의 전역으로도 갈 수 있다.

  ```js
  function varTest() {
    var x = 1
    if (true) {
      var x = 2
      console.log(x) // 2 상위 블록과 같은 변수
    }
    console.log(x) // 2
  }
  
  varTest()
  ```

  ```js
  function varTest() {
    let x = 1
    if (true) {
      let x = 2
      console.log(x) // 2 상위 블록과 다른 변수
    }
    console.log(x) // 1
  }
  
  varTest()
  ```

  ###### let 과 var

  ```js
  // let 과 var
  var a = 1
  let b = 2
  
  if (a === 1) {
    var a = 11
    let b = 22
  
    console.log(a) // 11
    console.log(b) // 22
  }
  
  console.log(a) // 11
  console.log(b) // 2
  ```



****



- 어디에 쓸지 결정하는 것은 프로그래머의 몫

- `PI`, `DAYS_IN_JUNE` 과 같은 경우는 상수가 적절

- `WHATHER_TEMP` 처럼 모호한 경우(각자가 생각하는 좋아하는 기온이 다르므로) 이런 경우는 변수가 적절

   

****



- 일단 모든 선언에서 가능한 상수(const)를 사용
- 먼저 상수를 생각 **=>** 값이 바뀌는 것이 더 자연스러운 상황이라면, 그 때 변수로 바꿔서 사용하는 것을 권장



****



1. **var** : 할당 및 선언 자유 / 함수 스코프
2. **let** : 할당 자유 / 선언은 한번만 / 블럭 스코프
3. **const** : 할당 및 선언 모두 한번만 / 블럭 스코프



### 식별자 (identifier)

- 변수명은 식별자 라고 불리며 특정 규칙을 따른다.
  1. 반드시 문자, 달러($), 또는 밑줄로 시작해야 한다. 이후는 숫자도 가능
  2. 대소문자를 구분하며 클래스명을 제외하고는 대문자로 시작하지 않는 것이 좋다.
  3. 예약어는 사용 불가능(class, super, const, case, function...)

```js
// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName

// 배열은 복수형 변수명을 사용
const dogs = []

// 정규 표현식은 'r' 로 시작
const rDecs = /.*/

// 함수
function getPropertyName() {
  return 1
}

// boolean 을 반환하는 변수 - 'is' 로 시작
let isAvailable = false

// 2. 파스칼 케이스 (PascalCase) - 클래스, 생성자 (=== upper-camel-case)
class User {
  constructor(options) {
    this.name = option.name
  }
}

// 3. 대문자 스네이크 케이스(SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'thisissecretkey'
```



#### :weight_lifting_man: Hoisting



> #### var 할당 과정
>
> 1. 선언 + 초기화
> 2. 할당

```js
console.log(a) // undefined
var a = 10
console.log(a) // 10

// JS 가 이해한 코드
var a // 선언과 초기화
console.log(a) // undefinde
a = 10 // 할당
console.log(a)
```

- 이 개념은 JS **변수**가 끌어 올려지거나 함수나 표현이 최상단으로 올려지는 것을 말한다.
- 끌어 올려진 변수는 `undefined` 값을 반환 한다.
- 변수와 함수를 위한 메모리 공간을 미리 확보하는 과정



> #### let 할당 과정
>
> 1. 선언
> 2. TDZ (Temporal Dead Zone, 임시적 사각지대)
> 3. 초기화
> 4. 할당
>
> 

```js
// let은 되지 않는다. ReferenceError
console.log(b)
let b = 10
console.log(b)
```

```bash
console.log(b)
            ^

ReferenceError: Cannot access 'b' before initialization
```

- 초기화 하기도 이전에 과정을 거치려 했기 때문에 오류가 난다.
  TDZ라는 공간 안에 있기 때문에 선언만 되어있고 할당은 되지 않은 상태

```js
// 마찬가지로 아래와 같은 과정을 거친다
let b // 선언 + TDZ
console.log(b) 
b = 10 // 할당 불가 (초기화가 아직 안됨)
console.log(b) 
```



****



```js
if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y ===3) {
    var x = 1
  }
  console.log(y) // 3 
}

if (x === 1) {
  console.log(y) // 3 
}

// JS 가 이해한 코드
var x
var y
if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y ===3) {
    var x = 1
  }
  console.log(y) // 3 
}

if (x === 1) {
  console.log(y) // 3 
}
```

- let, const 의 정의가 평가되기까지 초기화가 되지 않는다는 의미
  - 호이스팅이 되지않아 정의가 되지 않는다는 의미와는 다르다.



### :package: 타입과 연산자 

>  ###### 타입
>
>  1. Primitive
>  2. Reference

#### Primtive

불변하다는 특징을 띄고 있다. 

1. Numbers
   - `Infinity` : 양의 무한대와 음의 무한대로 나뉨
   - `NaN` : Not Number, 표현할 수 없는 값
     - 0/0, "문자"*10, Math.sqrt(- 9)
2. Strings
3. Boolean
   python과 다르게 소문자를 사용 (true, false)
4. Empty Value



```js
// 숫자열
const a = 13
const b = -3
const c = 3.14 //float
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000'
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a, b, c, d, e, f, g)

// 문자열
const sentence1 = 'sentence'
const sentence2 = "sentence"
const sentence3 = `sentence`

// backtick
// const word = "안녕
// 하세요"

// console.log(word)

// 줄바꿈이 되지 않는다. 단, 아래는 가능하다.
const word1 = "안녕 \n하세요"
console.log(word1)


const word2 = `안녕
하세요`
console.log(word2)


// Template Literal
// JS 에서 문자열을 입력하는 방식
const age = 10
const message = `홍길동은 ${age}
세 입니다.`
console.log(message)
```



#### Literal

*변하지 않는 값*

- 값을 프로그램 안에서 직접 지정한다는 의미
- 값을 만드는 방법
- JS는 우리가 제공한 리터럴 값을 받아 데이터를 만듦

```javascript
// room 변수를 가리키는 식별자 / 'conference_room' (따옴표 안)은 리터럴
let room = 'conference_room'

let hotelRoom = room

// 에러, comference_room 식별자는 존재하지 않는다.
hotelRoom = conference_room
```

- JS는 따옴표를 통해 리터럴과 식별자를 구분한다.

- 식별자는 숫자로 시작할 수 없으므로 숫자에는 따옴표가 필요 없다. (숫자형 리터럴)

  ```js
  const happy = 'hello'
  const hacking = 'world!!' + 'lol' + '!!!'
  console.log(happy, hacking)
  ```





#### Empty Value : `null` // `undefined`

- 동일한 역할을 하는 이 2개의 키워드가 존재하는 이유는 단순한 JS의 설계 실수
- 큰 차이를 두지말고 interchangeable 하게 사용할 수 있게 권장

> ###### `undefined`
>
> - 값이 없을 경우 JS가 자동으로 할당 해주는 값
>
>   ```js
>   let first_name // undefined (선언만 하고 할당하지 않음)
>   console.log(first_name)
>   ```

> ###### `null`
>
> - 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값
>
>   ```js
>   let last_name = null
>   console.log(last_name) // null - 의도적으로 값이 없음을 표현
>   ```

```js
// console

typeof null
"object"
typeof undefined
"undefined"
```



```js
// console

null === undefined
false
null == undefined
true
```

> `==` 동등 연산자,
>
> `===` 일치 연산자, 메모리가 같은 객체를 가르키고 있음 **=>** 권장
>
> `!ture` **=>** `False` 
>
> `!`는 반대를 의미



```js
// Number.isNaN() 함수는 값이 Not a Number인지 여부를 판별
Number.isNaN(null) // false
Number.isNaN(undefined) // false
```



> ###### 선언자를 쓰지않으면 자동으로 var가 부여된다.
>
> ex) `a = 1` **=>** `var a = 1`



##### 할당 연산자

```js
// console

let c = 0
undefined
c += 10
10
console.log(c)
VM164:1 10
undefined
c -= 3
7
c *= 10
70
c++
70
c
71
c--
71
c
70
```



##### 비교 연산자

```js
// console

c < 30
false
c >=30
true
c === 70
true

// 소문자가 더 크다
'A' < 'B'
true
'Z' < 'a'
true
```



##### 동등 연산자

```js
// console

const a = 1
undefined
const b = '1'
undefined
a == b
true
a != b
false
a == Number(b) // 자동 형변환
true
```

> 형변환
>
> ```js
> // console
> 
> 8 * null
> 0
> '5' - 1
> 4
> '5' + 1
> "51"
> 'five' * 2
> NaN
> a === b
> false
> a === Number(b)
> true
> ```



##### 논리 연산자

```js
// console

8 * null
0
'5' - 1
4
'5' + 1
"51"
'five' * 2
NaN
a === b
false
a === Number(b)
true
true && false
false
true && true
true
1 && 0
0 // 0은 flase
0 && 1
0
4 && 7
7 // 둘다 true값(1이상) 이기 때문에 7까지 읽는다.
false || true
true
false || false
false
1 || 0
1
0 || 1
1
4 || 7
4 // 둘다 true값 이기 때문에 ||(or은 하나만 true여도 true)에서는 4까지만 읽는다.
```



##### 삼향 연산자

- `boolean ? 첫번째 식 : 두번째 식`
- true 는 왼쪽 false는 오른쪽 값이 출력

```js
// console

true ? 1 : 2
1
false ? 1 : 2
2

const result = Math.PI > 4 ? 'YES' : 'NO'
undefined
result
"NO"
```



### :package: 조건과 반복문

```js
// console 

const userName = prompt('Hello! who r u??')
undefined
userName
"haein"
```



![image](https://user-images.githubusercontent.com/52684457/67818904-58c95880-faf6-11e9-9f2a-5d36cb07dbfc.png)

```js
// console

if (userName === '1q2w3e4r') { // shift + enter
	message = '<h1>This is admin page</h1>' // tap
} else if ( userName === 'ssafy' ) {
	message = '<h1>You r from ssafy</h1>'
} else {
	message = `<h1>Hello ${userName}</h1>` // ` 백틱
}
"<h1>Hello haein</h1>"
message
"<h1>Hello haein</h1>"
```



- ###### Document 조작 (돔 조작, 문서 조작)

```js
// console

document.write(message)
undefined
```

![image](https://user-images.githubusercontent.com/52684457/67819054-f9b81380-faf6-11e9-8a83-69fc3e358fc8.png)

#### 조건문

###### if / switch

```js
// console

const userName = prompt('Hello Who r u?') // 1q2w3e4r 입력
undefined
let mass
undefined
let message = ''
undefined
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>this is admin</h1>'
    }
    case 'ssafy': {
		message = '<h1>you r from ssafy</h1>'
    }
	defalt: {
		message = `<h1>hello ${userName}</h1>`
    }
}
"<h1>hello 1q2w3e4r</h1>" // 왜 첫번째 case가 출력되지 않은 것일까?
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>this is admin</h1>'
		console.log(message)
    }
    case 'ssafy': {
		message = '<h1>you r from ssafy</h1>'
		console.log(message)
    }
	defalt: {
		message = `<h1>hello ${userName}</h1>`
		console.log(message)
    }
}
VM3030:4 <h1>this is admin</h1>
VM3030:8 <h1>you r from ssafy</h1>
VM3030:12 <h1>hello 1q2w3e4r</h1>
// console.log 를 찍어보면 멈추지않고 끝까지 구문이 돌아서 마지막 구문이 출력된다.
// => switch 특징
undefined
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>this is admin</h1>'
		break // 해당 조건을 만족하면 멈추도록하는 구문을 추가
    }
    case 'ssafy': {
		message = '<h1>you r from ssafy</h1>'
		break
    }
	defalt: {
		message = `<h1>hello ${userName}</h1>`
		console.log(message)
    }
}
"<h1>this is admin</h1>"
```

```js
// if
const userName = 'ssafy'

if (userName === '1q2w3e4r') { 
	message = '<h1>This is admin page</h1>' 
} else if ( userName === 'ssafy' ) {
	message = '<h1>You r from ssafy</h1>'
} else {
	message = `<h1>Hello ${userName}</h1>` 
}

// switch
switch(userName) {
  case '1q2w3e4r': {
  message = '<h1>this is admin</h1>'
  break 
  }
  case 'ssafy': {
  message = '<h1>you r from ssafy</h1>'
  break
  }
defalt: {
  message = `<h1>hello ${userName}</h1>`
  console.log(message)
  }
}
```





###### while / for

```js
// while
let i = 0

while (i < 6) { // true인 동안만 구문이 돌 것 0 1 2 3 4 5
  console.log(i)
  i++
}

//for
for (let j = 0; j < 6; j++) {
  console.log(j)
}


const numbers = [0, 1, 2, 3, 4, 5,]

for (let number of numbers) {
  console.log(number)
}


for (const number of numbers) { // 재 할당 하지 않겠다 => const
  console.log(number)
}
// 전부 0, 1, 2, 3, 4, 5 가 출력
```



### :package: 함수

- 파이썬에도 이름없는 익명 함수가 있다 : **lambda**

```python
def ssafy1(x):
    return x + 1

lambda x: x + 1
ssafy2 = lambda x: x + 1
ssafy2(2)

list(map(ssafy1, [1, 2, 3])) # [2, 3, 4]
list(map(lambda x: x+1, [1, 2, 3])) # [2, 3, 4]
```

- **JS**

```js
// 1. 선언식 (srarement, declaration)
// 함수 선언식은 코드가 실행되기 전에 로드된다.
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7)) // 9

// 2. 표현식 (expression)
// 함수 표현식은 인터프리터가 해당 코드에 도달 했을 때 로드된다.
const sub = function(num1, num2) { // 이름이 없는 함수 => 익명함수
  return num1 - num2
}

console.log(sub(7, 2)) // 5

console.log(typeof add) // 타입 : function
console.log(typeof sub) // 타입 : function

// Arrow Function 화살표 함수
// 화살표 함수의 경우 일반 function 키워드로 정의한 함수와 100% 동일한 것이 아님
// 화살표 함수는 항상 익명
// 변수에 할당할 수 있지만, 이름 붙은 함수(생성자)로는 만들 수 없음
const ssafy1 = function(name) {
  return `hello, ${name}`
}

//리팩토링(refectoring)
// 1. function 키워드 삭제
const ssafy1 = (name) => { return `hello, ${name}` }

// 2. 매개변수의 '()' 소괄호 생략 (단, 함수 매개변수가 하나일 경우만)
const ssafy1 = name => { return `hello, ${name}` }

// 3. {} && return 생략 (단, 함수의 바디에 표현식이 1개일 경우만)
const ssafy1 = name => `hello, ${name}`

// Arroe function refactoring
let square = function(num) {
  return num ** 2
}
let square = (num) => { return num ** 2 }
let square = num => { return num ** 2 }
let square = num => num ** 2 

// 매개변수가 없다면 ? => () 나 _ 를 사용
let noArgs = () => 'No Args'
let noArgs = _ => 'No Args'

// object(객체) 를 return 한다면
let returnObject = () => { return {key: 'vlaue'} } // return을 명시적으로 적어준다.
console.log(returnObject) // [Function: returnObject]

// object 를 return 하는데 return을 사용하지 않을 경우 소괄호를 사용
let returnObject = () => ({key: 'vlaue'})

// object return 시 문제상황
// 1. return이 없는데 ()를 안 쓴 경우
let returnObject = () => {key: 'vlaue'}
const test = returnObject()
console.log(typeof test) // undefined (정의되지 않음)

// 기본 매개변수를 줄 때는 매개변수의 개수와 상관없이 무조건 ()를 해야한다.
const sayHello = (name='noName') => `hi ${name}`


// Anonymous Function (익명함수 / 1회용 함수)
// 1. 기명함수로 만들기 (변수/상수에 할당하기) - 생성과 동시에 함수의 인수로 할당
const cube = function (num) { return num ** 3 } // 변수 할당
const squareRoot = num => num ** 0.5

console.log(cube(2)) // 8
console.log(squareRoot(4)) // 2

// 2. 익명함수 즉시 실행
console.log((function (num) { return num ** 3 })(2)) // 8
console.log((num => num ** 0.5)(4)) // 2

// 함수 호이스팅
ssafy() // 아래에서 선언된 것을 끌어올려 호출

function ssafy() {
  console.log('hoisting!')
}

// 변수에 할당한 함수(즉, 표현식)는 호이스팅 되지 않는다.
// 이것은 변수의 유효범위 규칙을 따르기 때문
// let
ssafy2()

let ssafy2 = function () {
  console.log('hoisting!') // ReferenceError
}

// let (JS가 이해한 코드)
let ssafy2 // 1. 변수 선언

ssafy2() // 2. 함수 호출 => ssafy2는 초기화도 안되었는데 함수를 호출 (ReferenceError)

ssafy2 = function () {
  console.log('hoisting!') 
}

// var
ssafy3()

var ssafy3 = function () {
  console.log('hoisting!') // TypeError, ssafy3 is not a function (이미 변수가 되어있어서 함수가 아님 => 초기화까지는 진행된 상태)
}

// var (JS가 이해한 코드)
var ssafy3 // 1. 변수 선언(+초기화)

ssafy3() // 2. 함수 호출 => ssafy3은 변수인데 호출 (TypeError)

ssafy3 = function () {
  console.log('hoisting!')
}
```



## :floppy_disk: Data structure : Object & Array

```js
const numbers = [1, 2, 3, 4,]

console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index만 가능
console.log(numbers.length) // 4

// 원본 파괴
console.log(numbers.reverse())
console.log(numbers) //reverse는 원본을 바꿔서 뒤집어놓는다.
console.log(numbers.reverse()) // 한번 더 사용함으로서 원본으로 되돌려 놓음

// push - 값을 집어넣지만 배열의 길이를 return
console.log(numbers.push('a')) // 5
console.log(numbers) // [1, 2, 3, 4, 'a']

// pop - 배열의 가장 마지막 요소 제거 후 return
console.log(numbers.pop()) // a
console.log(numbers) // [1, 2, 3, 4]

// unshift - 배열의 가장 앞에 요소를 추가, return은 배열의 길이
console.log(numbers.unshift('a')) // a
console.log(numbers) // ['a', 1, 2, 3, 4]

// shift - 배열의 가장 앞에 요소 제거 후 return
console.log(numbers.shift()) // a
console.log(numbers) // [1, 2, 3, 4]

// boolean return
console.log(numbers.includes(1)) // true
console.log(numbers.includes(0)) // false

// indexOf
console.log(numbers.push('a', 'a')) // 6
console.log(numbers) // [1, 2, 3, 4, 'a', 'a']
console.log(numbers.indexOf('a')) // 4 => 중복이 존재한다면 처음 찾은 요소의 index를 return
console.log(numbers.indexOf('b')) // -1 => 찾고자 하는 요소가 없으면 -1 return

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return
console.log(numbers.join()) // '1,2,3,4,a,a'  => 아무것도 넣지 않으면 ,를 기준으로 가져옴
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'
console.log(numbers) // [1, 2, 3, 4, 'a', 'a'] => 원본은 변화하지 않음

```



#### :yellow_heart: JOSN(JS Object Notation, JS 객체 표기법)

- KEY-VALUE 형태의 자료구조를 JS 객체와 유사한 모습으로 표현하는 표기법
- 모습만 비슷할 뿐이고 실제로 Object 처럼 사용하려면 다른 언어들 처럼 JS에서도 Parsing(구문 분석)작업이 필요

> `Object` - JS 의 key - vlaue 페어의 자료 구조
> `JSON` - 데이터를 표현하기 위한 **단순한 문자열**
>
> **=>** parsing 작업 필요

```js
const me = {
  name: 'ssafy', // key가 한 단어 일 때
  'phone number': '01012345678', // key가 여러단어 일 때
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // key가 여러 단어인 경우 반드시 []로 접근

console.log(me.appleProducts) // { ipad: '2018pro', iphone: '7', macbook: '2019pro' }
console.log(me.appleProducts.ipad)

// Object Literal (객체 표현법) 
// ES5
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}
console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// EX6+
// object 의 Key 와 Value 가 같다면, 마치 배열처럼 한번만 작성 가능
let bookShop2 = {
  books,
  comics,
  magazines,
}
console.log(bookShop2)

// JSON
const jsonData = JSON.stringify({ // JSON => String
  coffe: 'Americano',
  iceCream: 'Mint Choco', // 트레일링 콤마는 JSON에서 쓸수 없다는 것을 유의 객체에서만 가능
})
console.log(jsonData)
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData) // object (객체)
```



#### :page_facing_up: Array Helper Method

> ###### Helper 
>
> 자주 사용하는 로직을 재활용 할 수 있게 만든 일종의 Library
>
> 

##### `forEach`

```js
// Array Helper Method
// 1. forEach(callback())
// 함수의 인자로 들어간 함수 즉, 콜백 함수 - 인자로 다른 함수에 전달 된 함수
// 주어진 callback 을 배열에 있는 각 요소에 대해 오름차순으로 한번씩 실행
// 아무것도 return 하지 않는다. 

// ES5
var colors = ['red', 'blue', 'green']

for (var i = 0; i < colors.length; i++) {
  console.log(colors[i])
}

// ES6
const COLORS = [ 'red', 'blue', 'green']

COLORS.forEach(function (color) {
  console.log(color)
})

COLORS.forEach( color => console.log(color))

const result = COLORS.forEach( color => console.log(color))
console.log(result) // undefined => return 값이 없음
```



##### `map`

```js
// Array Helper Method

// 2. .map(callback())
// 배열 내의 모든 요소에 대하여 각각 주어진 함수(callback)를 호출한 결과를 모아 새로운 배열 return
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때 사용

// for
var numbers = [1, 2, 3,]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i] * 2)
}

console.log(doubleNumbers) // [2, 4, 6]
console.log(numbers) // [1, 2, 3] => 원본 유지

// map
const NUMBERS = [1, 2, 3]

const DOUBLE_NUMBERS = NUMBERS.map(function(number) {
  return number * 2
})
console.log(DOUBLE_NUMBERS) // [2, 4, 6]
console.log(NUMBERS) // [1, 2, 3] => 원본 유지

// refectoring
const DOUBLE_NUMBERS = NUMBERS.map( number => number * 2)


// 2-1 연습
const newNumbers = [4, 9, 16,]
const roots = newNumbers.map(Math.sqrt) // sqrt - 제곱근 return

console.log(roots) // [2, 3, 4]


// 2-2 map 을 사용 -> images 배열 안의 object 들의 height 들만 저장되어 있는 heights 배열을 만드시오.
const images = [
  { height: '34px', width: '39px' },
  { height: '12px', width: '11px' },
  { height: '292px', width: '56px' },
]

const heights = images.map(function (image) {
  return image.height
})
console.log(heights) // [ '34px', '12px', '292px' ]


// 2-3  map을 사용하여 trips 배열의 값들을 계산 후 속도 값을 저장하는 배열 speeds를 만드시오
const trips = [
  { distance: 35, time: 10 },
  { distance: 90, time: 10 },
  { distance: 60, time: 25 },
]

const speeds = trips.map(function(trip) {
  return trip.distance / trip.time
})

console.log(speeds) // [ 3.5, 9, 2.4 ]


// 2-4
const brands = ['Marvel', 'DC',]
const movies = ['Iornman', 'Batman',]

const comics = brands.map(function(x, i) {
  return { name: x, hero: movies[i] }
})

console.log(comics)

// [
  //   { name: 'Marvel', hero: 'Ironman'},
  //   { name: 'DC', hero: 'Batman'},
// ]

// refectoring
const comics = brands.map( (x, i) => ({ name: x, hero: movies[i] }))
```



##### `filter`

```js
// Array Helper Method

// 3. .filter(callback())
// 주어진 함수의 테스트를 통과한 모든 요소를 모아 새로운 배열로 반환
// 즉, 주어진 콜백 함수로 원하는 요소만 filtering 할 수 있다.
// map 과 마찬가지로 원본은 유지

// for
var products = [
  { name: 'cucumber', type: 'vegetable'},
  { name: 'banana', type: 'fruit'},
  { name: 'carrot', type: 'vegetable'},
  { name: 'apple', type: 'fruit'},
]

var fruitProducts = [] // for 문으로 만들려면 빈 배열(Array))이 필요

for (var i = 0; i < products.length; i++) {
  if (products[i].type === 'fruit') {
    fruitProducts.push(products[i])
  }
}

console.log(fruitProducts)
// [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]


// filter
const PRODUCTS = [
  { name: 'cucumber', type: 'vegetable'},
  { name: 'banana', type: 'fruit'},
  { name: 'carrot', type: 'vegetable'},
  { name: 'apple', type: 'fruit'},
]

const FRUIT_PRODUCTS = PRODUCTS.filter( function(product) {
  return product.type === 'fruit'
  // 해당 조건이 true를 만족할 경우에 return 
})

console.log(FRUIT_PRODUCTS)
// [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]

// refectoring
const FRUIT_PRODUCTS = PRODUCTS.filter( product => product.type === 'fruit')


// 3-1 연습
// users 배열에서 admin 레벨이 true 인 user object 들만 filteredUsers 에 저장하고 
// 배열의 두번째 유저의 이름을 출력
const users = [
  { id: 1, admin: false, name: 'justin'},  
  { id: 2, admin: false, name: 'harry' },
  { id: 3, admin: true, name: 'tak' },
  { id: 4, admin: false, name: 'jason' },
  { id: 5, admin: true, name: 'juan' },
]

const filteredUsers = users.filter( function(user) {
  return user.admin === true
})

console.log(filteredUsers[1].name)

// refectoring
const filteredUsers = users.filter( user => user.admin === true)
```



##### `reduce`

```js
// Array Helper Method

// 4. .reduce(callback())
// 배열의 각 요소에 대해 주어진 reduce 함수를 실행하고, 하나의 결과 값을 반환한다.
// reduce 는 배열 내의 숫자 총합, 평균 등 배열의 값을 하나로 줄이는 동작을 한다.
// map은 배열의 각 요소를 변형한다면, reduce는 배열자체를 변형한다.

// 총합
const ssafyTests = [90, 90, 80, 77,]
const sum = ssafyTests.reduce(function (total, x) {
  return total += x
}, 0) // return에서는 x, 0을 설정해주면 0값만 나옴 return사용시에 굳이 0을 쓰려면 중괄호 끝나는 부분에 0을 입력해주어야 함
console.log(sum)

// reduce의 첫번째 매개변수는 누적 값(전 단계의 결과, 쌓여가는 누적값) === total
// 두번째 매개변수는 현재 배열 요소, 현재 인덱스, 배열 자체 순 === x
// 초기값 === 0( 첫 total 값 )
// 초기값이 생략되면 배열의 첫번째 요소가 초기값

// // refectoring
const sum = ssafyTests.reduce( (total, x) => total += x, 0) // 화살표 함수에서는 0 생략가능 (상황에 따라 써야할 때도 있음)
console.log(sum)

// 4-1 연습
// 다음 배열 내에서 요소의 총합을 구하시오
const arr = [0, 1, 2, 3]
// const totalSum = arr.reduce( (total, x) => total += x, 0)
```



##### `find`

```js
// Array Helper Method

// 5. .find(callback())
// 주어진 콜백 함수를 만족하는 첫번째 요소의 값을 반환
// 없다면 undefined 를 반환
// 조건에 맞는 인덱스가 아니라 요소 자체를 원할 때 사용

// for
var users = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

// 원하는 object를 찾아도 users를 끝까지 돌게 된다. => 마지막 요소만 나옴
for (var i = 0; i < users.length; i++) {
  if (users[i].name === 'Tony Stark') {
    user = users[i]
    break // 원하는 조건에 도달하면 더 돌지 않는다.
  }
}
console.log(user)

// find
const USERS = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

const newUser = USERS.find(user => user.name === 'Tony Stark')
console.log(newUser)
```



##### `some` / `every`

```js
// Array Helper Method

// 6. .some(callback())
// 배열 안에 어떤 요소라도(===하나라도) 주어진 콜백함수를 통과하는 지 테스트하고, 
// 결과에 따라 boolean을 return 
// 빈 배열은 무조건 false를 return 
// 조건에 맞는 요 소를 찾으면 즉시 검색을 멈추고 true 를 return
// or 연산과 유사

//some
const arr = [1, 2, 3, 4, 5,]
const result = arr.some(elem => elem % 2 === 0)
console.log(result) // true 하나라도

// 7. .every(callback())
// 배열 안에 모든 요소가 주어진 콜백 함수를 통과하는지 테스트 후,
// 결과에 따라 boolean 을 return
// 빈 배열은 무조건 ture 를 return
// 배열의 모 든 요소가 조건에 맞아야 true / 그렇지 않으면 false
// 조건에 맞지 않는 요소를 찾으면 검색을 멈추고 false 를 return
// and 연산과 유사

// every
const result2 = arr.every(elem => elem % 2 === 0)
console.log(result2) // false 모든


// 7-1 연습
// for 
// ram이 32보다 작으면 everyComputers 가 false
// 아니면 someComputers 를 ture
var everyComputers = true
var someComputers = false

var computers = [
  { name: 'macbook', ram: 8},
  { name: 'gram', ram: 16},
  { name: 'series9', ram: 32},
]

for (var i = 0; i < computers.length; i++) {
  var computer = computers[i]
  if  (computer.ram < 32) {
    everyComputers = false
  } else {
    someComputers = true
  }
}

console.log(everyComputers) // false
console.log(someComputers) // true

// some / every
var   COMPUTERS = [
  { name: 'macbook', ram: 8},
  { name: 'gram', ram: 16},
  { name: 'series9', ram: 32},
]

// some
const newSomeComputers = COMPUTERS.some( computer => computer.ram < 32 )
console.log(newSomeComputers) // true - 하나라도 충족하기 때문에

// every
const newEveryComputers = COMPUTERS.every( computer => computer.ram < 32 )
console.log(newEveryComputers) // flase - 모두 충족하지않아서
```



## :thumbsup: callback

- 인수로 다른 함수에 전달 된 함수

- 명시적으로 호출하는 방식이 아니라 **특정 이벤트가 발생했을 때** 시스템에 의해 호출되는 함수

  - 다른 함수의 실행이 끝나고 난 뒤에 실행되는 함수

    ```js
    """
     이따가 너 실행 끝나면 그때 나 좀 호출해줘.
    """
    ```

    

- 함수 호출권한을 내가 아닌 시스템이 가진다.

- JS 함수는 일급 객체

  1. 변수에 담을 수 있다.
  2. 인자로 전달할 수 있다.
  3. 반환 값으로 전달할 수 있다. (*ex.return => n+1*)



##### 비동기식 처리 모델

- 호출될 함수 (콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면 콜백함수를 호출 하는 것.

```js
// console

setTimeout(function () {
    console.log('3초 후 출력됩니다.')
}, 3000)
6
VM219:2 3초 후 출력됩니다.
setTimeout ( () => console.log('3초'), 3000)
7
VM369:1 3초
```



##### 이벤트 리스너

- EventTarget.addEventListener(type, listener)

1. 무엇을 (버튼을) - `EventTarget`
2. 언제 (클릭했을 때) - `type`
3. 어떻게 (콘솔에 로그를) - `listener`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <button id="this-button">Click Me!</button>
  <div id="my"></div>
  
  <script>
  // 1. 무엇을
  const button = document.querySelector('#this-button')

  // 2. 언제     /    어떻게(콜백함수)
  button.addEventListener('click', function(event) {
    console.log(event)
    const area = document.querySelector('#my')
    area.innerHTML ='<h1>뿅!</h1>'
  })
  </script>
</body>
</html>
```



> ######  BOM (browser object model) 
>
> window.confirm()
>
> window.print()
>
> window.open()
>
> etc...



###### JS 코드를 body의 최하단에 위치하는 이유

1. JS를 읽는 시간 때문에 BODY 안에 있는 HTML 요소들이 브라우저에 그려지는게 지연 될 수 있기 때문
2.  JS 에서 특정 HTML 요소들을 읽고 이벤트를 등록해야 할 때, JS 코드가 먼저 해석되면 해당 요소가 없다고 인식되어 이벤트 등록이 되지 않을 수 있기 때문 

![image](https://user-images.githubusercontent.com/52684457/67909124-76172900-fbc1-11e9-8ccf-60c9ba8ad10c.png)

상위 **parent**  하위 **child**

- `querySelector`  위에서 선택자로 요소를 찾으며 가장 먼저 찾아지는 요소를 반환 (단수)
- `querySelectorAll`  위에서 부터 선택자로 요소를 찾으며 일치하는 요소들을 모두 반환 (복수)
  - *querySe....(.classname)*

```js
// console

const bg = document.querySelector('.bg')
undefined
bg.querySelector('#dino')
<img id=​"dino" width=​"100px" height=​"100px" src=​"https:​/​/​is4-ssl.mzstatic.com/​image/​thumb/​Purple118/​v4/​88/​e5/​36/​88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/​AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/​246x0w.jpg" alt=​"google-dino">​
const dino = bg.querySelector('#dino')
undefined
dino.src
"https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
dino.id
"dino"
dino.src = '' // 이미지가 사라짐 (주소가 없어졌기 때문)
""

///////////////////////

dino
<img id=​"dino" width=​"100px" height=​"100px" src=​"https:​/​/​is4-ssl.mzstatic.com/​image/​thumb/​Purple118/​v4/​88/​e5/​36/​88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/​AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/​246x0w.jpg" alt=​"google-dino">​
dino.style.width = '50px'
"50px"

///////////////////////

dino.remove() // 이미지 지우기
undefined

///////////////////////

const bg = document.querySelector('.bg')
undefined
bg
<div class=​"bg">​…​</div>​
bg.firstElementChild.remove() // 대상의 자식요소로도 지울 수 있다.
undefined

//=> bg.lastElementChild.remove() 마지막 자식요소 삭제

const bg = document.querySelector('.bg') // 부모 선택
undefined
const dino = document.querySelector('#dino') // 자식 선택
undefined
bg.removeChild(dino) // 부모의 입장에서 원하는 자식의 요소 바로 삭제

///////////////////////

const bg = document.querySelector('.bg')
undefined
const dino = document.querySelector('#dino')
undefined
const newDino = document.createElement('img')
undefined
newDino
<img>​
newDino.src = 'https://images.homedepot-static.com/productImages/832b5bfb-c0c2-4250-855b-a4cac169ac02/svn/design-toscano-garden-statues-qm2728000-64_1000.jpg'
"https://images.homedepot-static.com/productImages/832b5bfb-c0c2-4250-855b-a4cac169ac02/svn/design-toscano-garden-statues-qm2728000-64_1000.jpg"
newDino
<img src=​"https:​/​/​images.homedepot-static.com/​productImages/​832b5bfb-c0c2-4250-855b-a4cac169ac02/​svn/​design-toscano-garden-statues-qm2728000-64_1000.jpg">​
newDino.alt = 'dino'
"dino"
newDino.id = 'dino'
"dino"
newDino.style.width = '100px'
"100px"
newDino.style.height = '100px'
"100px"
newDino
<img src=​"https:​/​/​images.homedepot-static.com/​productImages/​832b5bfb-c0c2-4250-855b-a4cac169ac02/​svn/​design-toscano-garden-statues-qm2728000-64_1000.jpg" alt=​"dino" id=​"dino" style=​"width:​ 100px;​ height:​ 100px;​">​

bg.append(newDino) // 설정한 newDino를 doc에 집어넣기
undefined

///////////////////////
```

![image](https://user-images.githubusercontent.com/52684457/67909958-68af6e00-fbc4-11e9-8af9-eeffdd7e5d39.png)



```js
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <title>Document</title>
  <style>
    .bg {
      background-color: #f7f7f7;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
  </style>
</head>

<body>
  <div class="bg">
    <img id="dino" width="100px" height="100px"
      src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
      alt="google-dino" />
  </div>

  <script>
    const dino = document.querySelector('#dino')
    dino.addEventListener('click', function() {
      console.log('아야!')
    })
  </script>
</body>

</html>
```

- dino를 클릭하면 console에 아야! 가 뜬다.



> ######  [Event](https://developer.mozilla.org/ko/docs/Web/Events) - 키보드 이벤트를 사용해보자.
>
> - keydown
>
>   콘솔 창에서 위아래 좌우를 누르면 나오는 코드를 상세보기하여 코드를 잘 따라 치자
>   ![image](https://user-images.githubusercontent.com/52684457/67910964-0f493e00-fbc8-11e9-84eb-a6ac6c322f88.png)
>
>   `console.log('left')`
>
>   `console.log(dino.style)` **=>** `dino.style.marginRight = '20px'`
>
>   예를들어 오른쪽에 margin 값을 주면 왼쪽으로 가는 것 처럼 보인다.
>
>   ![image](https://user-images.githubusercontent.com/52684457/67911078-81218780-fbc8-11e9-8204-ba452b3a07f2.png)
>
>   ![image](https://user-images.githubusercontent.com/52684457/67911090-8d0d4980-fbc8-11e9-96e1-52bd321b872e.png)
>
>   하지만 한번만 움직이고 고정이된다. 계속 움직이게 하려면 ?
>
>   ```js
>   <!DOCTYPE html>
>   <html lang="en">
>   
>   <head>
>     <meta charset="UTF-8" />
>     <title>Document</title>
>     <style>
>       .bg {
>         background-color: #f7f7f7;
>         display: flex;
>         justify-content: center;
>         align-items: center;
>         min-height: 100vh;
>       }
>     </style>
>   </head>
>   
>   <body>
>     <div class="bg">
>       <img id="dino" width="100px" height="100px"
>         src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
>         alt="google-dino" />
>     </div>
>   
>     <script>
>       const dino = document.querySelector('#dino')
>       let x = 0 // x 좌우 값
>       let y = 0 // y 상하 값
>   
>       document.addEventListener('keydown', function(e) {
>         // console.log(e)
>         if (e.key === ' ') {
>           console.log('spacebar')
>         } else if (e.code === 'ArrowLeft') {
>           console.log('left')
>           x -= 20
>           dino.style.marginLeft = `${x}px`
>           // console.log(dino.style)
>         } else if (e.code === 'ArrowUp') {
>           console.log('up')
>           y -= 20
>           dino.style.marginTop = `${y}px`
>         } else if (e.keyCode === 39) {
>           console.log('right')
>           x += 20
>           dino.style.marginLeft = `${x}px` 
>           // marginLeft를 기준으로 값이 +- 주어져야 움직임이 확실하다.
>           // marginRight값을 주면 서로 각 값이 들어가서 방향이 이상해진다.
>         } else if (e.code === 'ArrowDown') {
>           console.log('down')
>           y += 20
>           dino.style.marginTop = `${y}px`
>           // marginLeft와 동일하게 marginTop값 으로만 상하를 조절
>         } else {
>           console.log('잘못된 키')
>         }
>       })
>       
>     </script>
>   </body>
>   
>   </html>
>   ```
>
>   
>
>   ###### [Event](https://developer.mozilla.org/ko/docs/Web/Events) - 마우스 오버를 사용해보자 (추가)
>
>   ```js
>       dino.style.position = 'absolute'
>       dino.addEventListener('mouseover', function () {
>         // (현재 윈도우 너비 * 난수) - (현재 위도우 너비)
>         // Math.random() 0~1 사이의 난수
>         const newWidth = window.innerWidth * Math.random() - window.innerWidth
>         const newHeight = window.innerHeight * Math.random() - window.innerHeight
>   
>         dino.style.marginLeft = newWidth + 'px'
>         dino.style.marginTop = newHeight + 'px'
>       })
>   ```



#### :shopping: shoppin list

![image](https://user-images.githubusercontent.com/52684457/67914028-4d4b5f80-fbd2-11e9-9efb-c2b5d447cbf7.png)

```js
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>My Shopping List</h1>
  Enter a new item: <input type="text" id="item-input">
  <button id="add-button">Add Item</button>
  
  <ul id="shopping-list">


  </ul>

  <script>
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')

    button.addEventListener('click', function() {
      const itemName = input.value
      input.value = '' // 물건을 담고 초기화를 시켜주어야 기존의 value값이 사라지고 그 다음 값을 받을 수 있음
      
      // item 변수에 li 태그 객체를 담기
      const item = document.createElement('li')
      // item에 itemNmae을 담는다.
      item.innerText = itemName
      // ul 태그(shoppingList)의 마지막에 item(li 태그)을 자식요소로 추가
      shoppingList.append(item)

      // 1. Delete 버튼 태그 추가
      const deleteButton = document.createElement('button')

      // 2. deleteButton 변수에 텍스트 추가
      deleteButton.innerText = 'Delete'

      // 3. 각각의 item(li 태그)에 deleteButton 을 마지막 요소로 추가
      item.append(deleteButton)

      // 4. deleteButton 을 누르면 item을 삭제
      deleteButton.addEventListener('click', function() {
        item.remove()
      })
    })
  </script>
  
</body>
</html>
```

