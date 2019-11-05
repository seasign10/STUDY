// let
// 선언은 한번만 가능
// 재할당은 가능
let x = 1
// let x = 2 // already been declared
x = 3
console.log(x) // 3


// const
// 선언시 초기 값을 생략하면 에러 발생
// const SAMPLE

// 재선언 재할당 불가

const SAMPLE = 7
// const SAMPLE = 10

// 둘다 불가능
// var SAMPLE = 20
// let SAMPLE = 20

// block scope 안에 있는 상수와, 바깥 전역 변수에 있는 상수는 다르다.
// 다른 스코프 유효범위 안에있기 때문에 새로운 변수 할당과 선언이 가능
if (SAMPLE === 7) {
  const SAMPLE = 20

  console.log(SAMPLE)
}

// scope
function varFuc() {
  var x = 10
  if (true) {
    var x = 20 // let, const는 block scope / var는 함수 scope이기 때문에 
    console.log(x) // 20
  }
  console.log(x) // 20
}

varFuc()


// ==========================
function letFuc() {
  let x = 10
  if (true) {
    let x = 20 // let, const는 block scope / var는 함수 scope이기 때문에 
    console.log(x) // 20
  }
  console.log(x) // 10
}

letFuc()


// ==========================
var y = 30

function get() { // 인자 받고있는 것이 없다. 함수에 인자가 있으면 함수내의 지역 범위를 참조하게됨
  return y // 인자가 없을 경우 참조하는 것은 전역 객체 (hoisting)
}

var result = get(20)

console.log(result) // 인자가 없을 때 : 30 / 인자가 있을 때 : 20


function set(value) {
  var z = value // 10 => 낚시
}

set(10)
var result = get(20) // 위의 get이 인자가 없기 때문에 30

console.log(result) // 30