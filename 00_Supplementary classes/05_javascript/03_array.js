const numbers = [1, 2, 3, 4,]

numbers.length // 길이
numbers[-2] // undefined => 정확한 양의 정수 index만 가능

numbers.reverse() // 순서를 거꾸로 => 원본도 변경시킴
// [4, 3, 2, 1]

numbers.push(100) // 5 (배열의 길이를 리턴)
// [4, 3, 2, 1, 100]

numbers.pop() // 100 (배열의 마지막 요소 제거 후 return)
// [4, 3, 2, 1]

numbers.shift() // 4 (배열의 첫번째 요소 제거 후 return)
// [3, 2, 1]

numbers.unshift() // 배열의 첫번째 요소로 값 추가 (길이를 return)

numbers.includes(1) // true (값이 있으면 true 없으면 false)

const numbers = [1, 2, 3, 4, 'a', 'a']

numbers.indexOf('a') // 4 => 처음 찾은 요소의 index를 반환 (중복이 있어도 처음 찾은 요소의 index만 반환)
numbers.indexOf(100) // -1 => 찾고자 하는 요소가 없으면 -1 

numbers.join() // 1, 2, 3, 4, 'a', 'a'
numbers.join('') // 1234aa
numbers.join('-') // '1-2-3-4-a-a'