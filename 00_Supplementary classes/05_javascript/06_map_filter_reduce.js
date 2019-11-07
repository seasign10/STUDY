// map 과 filter는 원본을 변경하지 않는다.
var numbers = [1, 2, 3]
var tripleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  tripleNumbers.push(numbers[i] * 3)
}

console.log(numbers) // [ 1, 2, 3 ]
console.log(tripleNumbers) // [ 3, 6, 9 ]




const NUMBERS = [1, 2, 3]
// const TRIPLE_NUMBERS = NUMBERS.map(function (number) {
//   return number * 3
// })
const TRIPLE_NUMBERS = NUMBERS.map(number => number * 3)

console.log(NUMBERS)
console.log(TRIPLE_NUMBERS) // return이 없으면 undefined를 반환




const newNumbers = [9, 16, 25] // 제곱근을 구해보자
const root = newNumbers.map(Math.sqrt)
console.log(newNumbers)
console.log(root)




const BRANDS = ['Marvel', 'DC']
const MOVIES = ['SpyderMan', 'Batman']

// const comics = BRANDS.map(function (x, i) {
//   return {
//     name: x,
//     hero: MOVIES[i]
//   }
// })
const comics = BRANDS.map((x, i) => ({
  name: x,
  hero: MOVIES[i]
}))

console.log(comics)

// 출력
// [{
//   name: 'Marvel',
//   hero: 'SpiderMan'
// }, {
//   name: 'DC',
//   hero: 'Batman'
// }]

const USERS = [
  { admin: false, name: 'harry' },
  { admin: true, name: 'may' },
  { admin: false, name: 'micle' },
  { admin: true, name: 'june' },
]

const filterUsers = USERS.filter(function(user) {
  return user.admin === true
})

console.log(filterUsers)


// reduce => 누적값이 있는 것을 잘 생각 해볼 것
// map 은 배열의 각 요소를 변형하지만 reduce 는 배열 자체를 변형

const NUMBERs = [100, 82, 70, 34]

// const result = NUMBERs.reduce(function(total, number) {
//   return total += number
// }, 0)
const result = NUMBERs.reduce( (total, number) => total + number) / NUMBERs.length
console.log(result)