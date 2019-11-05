//===============================(var)===============================

// 나중에 선언된 변수를 참조할 수 있다. (hoisting)
console.log(x) // undefined
var x = 10
console.log(x) // 10

// 내부적으로 위의 코드가 도는 과정
var x // 1. 선언이 최상단 / 선언 + 초기화(undefined) => 동시 진행
console.log(x) // 2. undefined 에러가 나지 않는다
x = 10 // 3. 여기서 할당
console.log(x) // 10



//===============================(let)===============================

console.log(y) // Cannot access 'y' before initialization => 초기화 전에 접근할 수 없다.
let y = 10
console.log(y)

// 내부적으로 위의 코드가 도는 과정
let y // 1. 선언 후 TDZ(임시적 사각지대)에 존재
console.log(y) // 2. 참조 error => 초기화 전에 참조하려 하였기 때문에 (초기화가 안된 상태)
y = 10
console.log(y)



//===================================================================

if (x !== 1) {
  console.log(y) // undefined (선언도 할당도 되지 않은 상태)
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3 
}
if (x === 1) {
  console.log(y) // 3 var의 입장에서는 함수 스코프인데 함수가 없으므로 전역 변수를 가져올 수 있다.
}