const numbers = [1,2,3,4,5]



//원본파괴
numbers.reverse()
numbers
numbers.reverse()
numbers


//push - 배열길이 return

numbers.push('a')
numbers

//pop = 배열 가장 마지막 요소 제거 후 return
numbers.pop()           //'a'
numbers                 //[1,2,3,4,5]

//unshitf = 배열 가장 앞에 요소 추가
numbers.unshift('a')      // 6 (배열의 새로운 length)
numbers                   // ['a',1,2,3,4,5]

//shift - 배열의 가장 첫번째 요소 제거 후 return
numbers.shift()             //'a'
numbers                     //[1,2,3,4,5]
