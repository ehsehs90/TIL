## 어노테이션 기반 스프링MVC

스프링은 어노테이션 기반 설정을 제공함으로써 과도한 XML 설정으로 인한 문제를 해결한다 Spring MVC 도 스프링 설정 파일에 HandlerMapping, Controller, ViewResolver 같은 여러 클래스를 등록해야 하므로 어노테이션 설정을 최대한 활용하여 XML설정을 최소화 할 필요가 있다.

### 1. 어노테이션 기반 MVC 개발

##### 1.1 어노테이션 관련 설정

- 스프링 MVC 에서 어노테이션을 사용하려면 먼저 `<beans>` 루트 엘리먼트에 context 네임스페이스를 추가한다.
- 그리고 HandlerMapping, Controller, ViewResolver 클래스에 대한 `<bean>`등록을 모두 삭제하고 `<context:component-scan>` 엘리먼트로 대체한다.
  - Controller 클래스가 스캔 범위에 포함되도록 `<context:component-scan>` 엘리먼트의 base-package 속성에 Controller 클래스들이 있는 가장 상위 패키지 'com.springbook.view'를 등록한다.
  - getBoard.jsp 와 getBoardList.jsp 파일의 위치도 원래대로 src/main/webapp 폴더 밑으로 되돌린다.

##### 1.2 @Controller 사용하기

- 기존 : 스프링 컨테이너가 Controller 클래스를 생성하게 하기 위해 Controller 클래스들을 스프링 설정파일에 `<bean>` 등록 한다.
- 어노테이션 : 컨트롤러 클래스 모두를 일일이 `<bean>` 등록 하지 않고, 선언부 위에 @Controller 를 붙인다
  - 이는 스프링 설정파일에 `<context:component-scan>` 으로 스프링 컨테이너가 컨트롤러 객체들을 자동으로 생성하기 때문:computer:
  - @Component 를 상속한 @Controller 는 @Controller 가 붙은 클래스의 객체를 메모리에 생성하는 기능 제공
    - 단순히 객체를 생성하는것에 그치지 않고, DispatcherServlet 이 인식하는 Controller 객체로 만듬

##### 1.3 @RequestMapping 사용하기

> 앞에서 @Controller를 클래스 위에 추가함으로써 InsertBoardController 객체를 생성하고 Controller 로 인식하게 할 수 있지만, 클라이언트의 "/insertBoard.do" 요청에 대해서 insertBoard() 메소드가 실행되도록 할 수 없다.

- 기존 : HandlerMapping 을 이용하여 클라이언트의 요청을 매핑했었다.
- 스프링 : @RequestMapping 을 이용하여 HandlerMapping 설정을 대체한다.
  - @RequestMapping 을 insertBoard() 메소드 위에 설정한다.

##### 1.4 클라이언트 요청 처리

대부분 Controller 는 사용자의 입력 정보를 추출하여 VO(Value Object) 객체에 저장한다. 그리고 비즈니스 컴포넌트의 메소드를 호출할 때 VO 객체를 인자로 전달한다.

사용자 입력 정보는 HttpServletRequest 의 getParameter() 메소드를 사용해 추출한다.

 - 따라서 InsertBoardController 를 위와 같이 작성해도 글 등록작업은 정상으로 처리한다.
   	- 만약 사용자가 입력하는 정보가 많거나 변경되는 상황에는 그만큼 자바코드가 필요하고, 입력정보가 변경될 떄마다 Controller 클래스가 수정되어야 한다.
    - 하지만 이를 Command 객체를 이용하면 이런 문제를 해결할 수 있다. Command 객체는 Controller 메소드 매개변수로 받은 VO 객체라고 보면 된다. 
      	- InsertBoardController 클래스의 insertBoard() 메소드를 Command 객체를 이용해 구현한다.

### 2. 어노테이션으로 게시판 프로그램 구현하기

##### 2.1 글 등록 기능 구현하기

##### 2.2 글 목록 검색 구현하기

##### 2.3 글 상세 보기 구현하기

##### 2.4 글 수정 기능 구현하기

##### 2.5 글 삭제 기능 구현하기

##### 2.6 로그인 기능 구현하기

##### 2.7 로그아웃 기능 구현하기

##### 2.8 컨트롤러 통합하기

##### 2.9 요청 방식에 따른 처리

###### 2.9.1 method 속성

###### 2.9.2  JSP에서 Command  객체 사용

###### 2.9.3 @ModelAttribute 사용

##### 2.10 Servlet API 사용

##### 2.11 Controller 의 리턴 타입

##### 2.12 기타 어노테이션

###### 2.12.1 @RequestParam 사용하기

###### 2.12.2 @ModelAttribute 사용하기

###### 2.12.3 @SessionAttributes 사용하기



### 3. 프레젠테이션 레이어와 비즈니스 레이어 통합

##### 3.1 비즈니스 컴포넌트 사용

##### 3.2 비즈니스 컴포넌트 로딩

###### 3.2.1 2-Layered 아키텍쳐

###### 3.2.2 ContextLoaderListener 등록

###### 3.2.3 스프링 컨테이너의 관계



### 4. 검색 기능 추가 구현

##### 4.1 검색 정보 추출

##### 4.2 Controller 구현

##### 4.3 DAO 클래스 수정



### 5. 파일 업로드 &#127746;

##### 5.1 파일 업로드 처리

##### 5.2 예외 처리

###### 5.2.1 어노테이션 기반의 예외 처리

###### 5.2.2 XML 기반의 예외 처리





### 6. 다국어 처리

### 7. 데이터 변환

##### 7.1 JSON 으로 변환하기

###### 7.1.1 Jackson2 라이브러리 내려받기

###### 7.1.2 HTTPMessageConvertor 등록

###### 7.1.3 링크 추가 및 Controller 수정

###### 7.1.4 실행 결과 확인



##### 7.2 XML로 변환하기

###### 7.2.1 JAXB 2 설정 추가

###### 7.2.2 Controller 수정

###### 7.2.3 실행 결과 확인

