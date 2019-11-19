// for loop 활용

var students =[
  {name:'서혁진', type='male'},
  {name:'남찬우', type='male'},
  {name:'공선아', type='female'},
  {name:'이도현', type='female'},
]

var strongStudents = []
for (var i =0; i<students.length; i++){
  if(students[i].type =='female'){
    strongStudents.push(students[i])
  }
}

console.log(strongStudents)
console.log(students)
console.log(students[1].name)

// filter Helper 활용