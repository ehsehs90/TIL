// 숫자가 담긴 배열의 요소에 각각 2를 곱하여 새로운 배열 만들기

// ES5
var numbers = [1,2,3]
var doublenumbers = []


for (var i=0;i<numbers.length;i++) {
  doublenumbers.push(numbers[i]*2)
}
console.log(doublenumbers)
console.log(numbers)  //원본 유지


// ES6+

// const DOUBLE_NUMBERS = []
// NUMBERS.map(function(number){return number*2})
// return 이 없으면 undefined (까먹지말자)

// const DOUBLE_NUMBERS = NUMBERS.map(function(number){return number*2 })
// console.log(DOUBLE_NUMBERS)


//화살표 함수 사용하여 한 줄로 줄이기
const NUMBERS = [1,2,3]
const DOUBLE_NUMBERS = NUMBERS.map( number => number*2 )
console.log(DOUBLE_NUMBERS)
console.log(NUMBERS)

// map 헬퍼를 사용해서 images 배열 안의 객체들의 height들만 저장되어있는 heights 배열을 만들어 보자
const images = [
  {height : '34px', width:'59px'},
  {height : '42px', width:'27px'},
  {height : '23px', width:'84px'},
]

const heights = images.map( function(image) {return image.height} )

console.log(heights)
console.log(images)


//map 헬퍼를 사용해서 "distance/time" = 속도" 를 저장하는 새로운 배열 speeds를 만드세요


const trips = [
  {distance:34, time:10},
  {distance:90, time:10},
  {distance:120, time:10},
]

const speeds = trips.map(function (trip) {return trip.distance / trip.time})
console.log(speeds)