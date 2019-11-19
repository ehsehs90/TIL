// for loop 활용
var students = [
  {name:'서혁진', type:'male'},
  {name:'남찬우', type:'male'},
  {name:'공선아', type:'female'},
  {name:'이도현', type:'female'},
]

var strongStudents = []
for (var i =0; i<students.length; i++){
  if(students[i].type =='female'){
    strongStudents.push(students[i])
  }
}

console.log(strongStudents) //원본 유지
console.log(students)       // 새로운 배열
console.log(students[1].name) // 객체 내 속성 접근하기

// filter Helper 활용
// const STRONG_STUDENTS = STUDNETS.filter(function(student){return student.type=='female'})
const STRONG_STUDENTS = STUDNETS.filter(studnet=> students.type=='female')
console.log(STRONG_STUDENTS)  //새로운 배열
console.log(STUDENTS)     //원본 유지


// filter Helper 를 사용해서 numbers 배열 중 50보다 큰 값만 필터링해서 새로운배열에 저장하기
const numbers = [15,35,13,36,69,3,61,55,99,5]
const newNumbers = numbers.filter( number => number>50 )



console.log(numbers)
console.log(newNumbers)