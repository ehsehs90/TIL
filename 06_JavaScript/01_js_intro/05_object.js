const me = {
  name : '도현',    //key가 한 단어일 때
  'phone number' : '01094865440',   //key가 여러 단어일 때
  appleProjucts: {
    iphone : 'none',
    watch : 'none',
    macbook: 'none'
  }
}


me.name     //"도현"
me['name']      //"도현"
me['phone number']    //"01094865440"
me['appleProjucts']
  // {iphone: "none", watch: "none", macbook: "none"}
me.appleProjucts.iphone    //"xs"s