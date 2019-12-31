# POJO(Plain Old Java Object)

> 단순한 자바 객체



- https://m.blog.naver.com/writer0713/220700687650 참고

  ```
  구글링을 하면 많은 자료들이 POJO를 getter / setter를 가진 단순한 자바 오브젝트로 정의하고 있다.
  
  위의 내용들에 근거하면 POJO는 "getter / setter를 가진 단순한 자바 오브젝트"이다 가 아니라
  
  "getter / setter를 가진 단순한 자바 오브젝트"는 POJO이다. 라고 하는게 맞을것 같다.
  
  "getter / setter를 가진 단순한 자바 오브젝트"는 분명 의존성도 없고, 테스트도 용이하며 추후 수정이 편리하니 POJO로 볼 수 있을것 같다.
  ```



- Not POJO 클래스
  - Servlet 클래스 - 대표적인 Not POJO 클래스
    - 개발자 마음대로 만들 수 없으며, 반드시 Servlet에서 요구하는 규칙에 맞게 클래스를 만들어야 실행 가능하다
  - Servlet 클래스 작성 규칙
    - javax.servlet, javax.servlet.http 패키지를 import해야한다
    - public 클래스로
    - Servlet, GenericServlet, HttpServlet 중 하나를 **상속**해야 한다
    - **기본 생성자**가 있어야 한다
    - 생명주기에 해당하는 메소드를 **재정의**(Overriding)한다