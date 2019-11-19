const tests = [90, 85, 77, 13, 58]

const sum = tests.reduce(function(total, score, ){
  return total += score
})


// 에러! -> () 생략하려면 하나의 인자가 있어야 한다. 이건 2개의 인자니까 () 붙여주자
// const sum1 = tests.reduce(total, score => total +=score )
// console.log(sum1)


const sum2 = tests.reduce((total, score) => total +=score )
console.log(sum2)
