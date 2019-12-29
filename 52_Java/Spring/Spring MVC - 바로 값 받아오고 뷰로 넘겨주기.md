**바로 값 받아오고 뷰로 넘겨주기**

데이터가 많아지면, 

@RequestParam("id") String id, @RequestParam("pwd") String pwd, ...

위와같이 너무 코드양이 많아진다.

 

이렇게 할 필요없이 스프링에서 편하게 하는 방법을 제공해준다.

 

VO 객체를 메소드의 파라미터로 넣어주면,

스프링프레임워크에서 알아서

값을 set 해주고, 뷰로 값을 넘겨준다.

 

그리고, 뷰에서는 그냥 사용만하면 된다.

 

굉장히 편리하기 때문에 이 방법을 많이 사용한다.

이러한 VO 객체를 커맨드 객체라고 한다.

 

기존에는 아래와 같이 사용했지만,

```
@Controller
public class HomeController {    
    @RequestMapping("/member/memberInfo")
    public String memberInfo(@RequestParam("id") String id, @RequestParam("pwd") String pwd, @RequestParam("name") String name,
            @RequestParam("age") int age, @RequestParam("address") String address, Model model) {
 
        MemberVO memberVO = new MemberVO();
        memberVO.setId(id);
        memberVO.setPwd(pwd);
        memberVO.setName(name);
        memberVO.setAge(age);
        memberVO.setAddress(address);
        
        model.addAttribute("memberVO", memberVO);
        
        return "/member/memberInfo";
    }
}

```

 

이렇게 할 필요없이

바로 파라미터에 VO 객체를 넣어주면 된다.

```
@Controller
public class HomeController {    
    @RequestMapping("/member/memberInfo")
    public String memberInfo(MemberVO memberVO) {
        // 아무런 내용이 없지만,
        // 스프링 프레임워크가 알아서 값을 받아와, 뷰로 값을 넘긴다.
        return "/member/memberInfo";
    }
}
```

딱 보기에도 코드의 양이 줄고,

편하게 사용할 수 있다는 것을 알 수 있다.

 

memberInfo.jsp

```
<body>
ID : ${memberVO.id}<br>
비밀번호 : ${memberVO.pwd}<br>
이름 : ${memberVO.name}<br>
나이 : ${memberVO.age}<br>
주소 : ${memberVO.address}
</body>
```



![img](https://t1.daumcdn.net/cfile/tistory/99B1A13E5AB0691C19)



 

 

**참고**

여러개의 데이터를 받을때는 VO 객체를 만들어서 사용하는 것이 편리하다.

 



![img](https://t1.daumcdn.net/cfile/tistory/9987B13D5AB069C618)



MemberVO.java

```
package com.edu.spring_mvc_ex.model;
 
public class MemberVO {
 
    private String id;
    private String pwd;
    private String name;
    private int age;
    private String address;
    
    // get set method
    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getPwd() {
        return pwd;
    }
    public void setPwd(String pwd) {
        this.pwd = pwd;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }
    
    @Override
    public String toString() {
        return "MemberVO [id=" + id + ", pwd=" + pwd + ", name=" + name + ", age=" + age + ", address=" + address + "]";
    }
    
}
```

