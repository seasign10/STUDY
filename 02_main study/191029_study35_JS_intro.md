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

- 이 개념은 JS 변수가 끌어 올려지거나 함수나 표현이 최상단으로 올려지는 것을 말한다.
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





## :electric_plug: 타입과 연산자 

>  ###### 타입
>
>  1. Primitive
>  2. Reference

### Primtive

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

```console
typeof null
"object"
typeof undefined
"undefined"
```



```console
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

















