// find
// 조건에 맞는 인덱스가 아니라 요소 자체를 찾고 싶을 때 사용

const PEOPLE = [
  { id: 1, admin: false },
  { id: 2, admin: true },
  { id: 3, admin: false },
]

const admin = PEOPLE.find(function(person) {
  // find는 조건에 부합하는 가장 첫번째 요소만 가져온다.
  return person.admin === false
})

console.log(admin) // { id: 1, admin: false }





// some & every
// some : 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true 를 return / 찾지 못하면 false (or 연산과 유사)
// 빈 배열 일 때 - some - false

// every : 배열의 모 든 요소가 조건에 맞아야 true / 그렇지 않다면 false (and 연산과 유사)
// 빈 배열 일 때 - every - true

// some 하나라도
const arr = [1, 2, 3, 4, 5]
const result = arr.some(elem => elem & 2 === 0)
console.log(result) // true

// every 모든 조건
const result2 = arr.every(elem => elem % 2 === 0)
console.log(result2) // false


// typeof 를 많이 찍어볼것
// ex) null(object) undefined(undefined)
// infinity 양의 무한대 / -infinity (음의 무한대)
// 조건 반복 알아야 함, 동등연산자 일치연산자
// 함수 안의 함수에서는 arrow function 사용해야 하지만
// 이벤트리스너 함수에서 arrow function 사용하지 못함
// ajax 개념을 잘 알기
