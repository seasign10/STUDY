const text = {
  name: 'ssafy',
  'class number': '123456789', // key 가 여러단어 일 때는 문자열로 작성
  products: {
    ipad: '2019',
    iphone: '11 pro',
    macbook: '2019 pro',
  }
}

// test.name
// test['name']
// test.class number // 불가능
// test['class number'] 
// test.class_number // 불가능

let brands = ['Apple', 'Samsung',]

let products = {
  'phone': ['iphone', 'galaxy'],
  'labtop': ['macbook', 'series9'],
}

const shop = {
  // es6 부터는 중복되는 구문을 생략해도 된다.
  brands,
  products,
  // brands: brands,
  // products: products,
}

console.log(shop)

// JSON (JavaScript Object Notation)
// Object => String
const jsonData = JSON.stringify({ // JSON => String
  coffee: 'Latte',
  iceCream: 'Mint',
})

console.log(jsonData) // {"coffee":"Latte","iceCream":"Mint"}
console.log(typeof jsonData) // string

// String => Object
const parseData = JSON.parse(jsonData)

console.log(parseData) // { coffee: 'Latte', iceCream: 'Mint' }
console.log(typeof parseData) // object


// Object
// js의 key-value 형태의 자료 구조

// JSON
// 데이터를 표현하기위한 단순 문자열 