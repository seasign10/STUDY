const word = `hello
world`

console.log(word)

const age = 10
const message = `hello, ${age}
bye`

console.log(message)

// undefined
// 값이 없을 경우 JS 가 자동으로 할당해주는 값

// null
// 자동으로 부여해주지 않는다. 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값

// 동등 연산자 ==, != 정확한 비교가 되지 않을 수 있기 때문에 js에서 권장하지 않는다. js 에서 어느정도의 형변환의 작업이 자동으로 이루어 질 수 있기 때문.
// 일치 연산자 ===, !==

console.log(3 * null) // 0 => null 은 0 으로 인식이 됨
console.log('6' - 1) // 5 형변환의 기준이 숫자열
console.log('6' + 1) // 61 형변환의 기준이 문자열
console.log('six' * 3) // 형변환을 해도 문자열이기 때문에 계산이 되지 않는다. (NaN : Not A Number)


// 논리 연산자
// and &&
// or ||
// not !
// !true === not true === false

// 삼향 연산자
// 값 ? true : false // true면 왼쪽 false면 오른쪽으로 실행되는 구문
// true ? 1 : 2 // ? 앞의 식이 true면 왼쪽 ? 뒤의 식이 true면 오른쪽
// 'ssafy' ? 'class' : 'awsome' // 문자열도 true로 인식이 된다 (값이 있기 때문) class가 출력된다.
// const result = 'ssafy' ? 'class' : 'awsome' // 변수로 할당도 가능하다.