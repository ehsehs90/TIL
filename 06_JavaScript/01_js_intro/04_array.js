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



// extensions -> rainbow brackets & indent rainbow

numbers.push('a','a')       
numbers                     //[1,2,3,4,5,'a','b']
numbers.unshift('a')        //['1',1,2,3,4,5,'a','b']


// 중복된 요소가 존재하는 경우 처음 찾은 요소의 index return!
numbers.indexOf('a')    // 0
numbers.indexOf('b')    // 8
numbers.indexOf('c')    // 찾는 요소가 없으면 -1

/*
  join
  배열의 요소를 join 함수 인자를 기준으로 묶어서 문자열로 return !
*/
numbers.join()          // "a,1,2,3,4,5,a,b" ( r기본값은 ',')
numbers.join('-')       // "a-1-2-3-4-5-a-b"
numbers.join('')        // "a12345ab"
