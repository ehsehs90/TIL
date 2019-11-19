// while loop
// while 키워드 뒤에 나오는 조건이 true인 경우 반복


// let i =0
// while(i<6){
//   console.log(i)
//   i++
// }


// for loop
// JavaScript 가장 기본적인 반복문. for문에서 사용할 변수 하나 정의하고, 그 변수가 특정 조건에 false값이 될때까지
//계속 연산 -반복

// for (let j =0; j<6; j++){
//   console.log(j)
// }

const numbers = [1,2,3,4,5]
for (let number of numbers){
  console.log(number)
}

for (let number of [1,2,3,4,5]){
  console.log(number)
}


for (const number of [1,2,3,4,5]){
  console.log(number)
}