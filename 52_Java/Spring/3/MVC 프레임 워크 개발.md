## MVC 프레임 워크 개발

### MVC 프레임워크 구조

- Model2 : MVC 아키텍처를 적용했지만, DispatcherServlet 클래스 하나로 Controller 기능을 구현

- 하나의 서블릿으로 Controller를 구현하면 클라이언트의 모든 요청을 하나의 서블릿이 처리한다

- DispatcherServlet.java

  - ```java
    package com.springbook.view.controller;
    
    import java.io.IOException;
    import java.util.List;
    
    import javax.servlet.ServletException;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import javax.servlet.http.HttpSession;
    
    import com.springbook.biz.board.BoardVO;
    import com.springbook.biz.board.impl.BoardDAO;
    import com.springbook.biz.user.UserVO;
    import com.springbook.biz.user.impl.UserDAO;
    
    
    public class DispatcherServlet extends HttpServlet {
    	private static final long serialVersionUID = 1L;
     
    	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    		
    		process(request, response);
    	}
    
    	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    		
    		request.setCharacterEncoding("UTF-8");
    		process(request, response);
    	}
    	
    	private void process(HttpServletRequest request, HttpServletResponse response) throws IOException {
    		
    		// 1. 클라이언트의 요청 path 정보를 추출한다.
    		String uri = request.getRequestURI();
    		String path = uri.substring(uri.lastIndexOf("/"));
    		System.out.println(path);
    		// 2. 클라이언트의 요청 path에 따라 적절히 분기 처리 한다.
    		if(path.equals("/login.do")) {
    			System.out.println("로그인 처리");
    			
    			// 1.사용자 입력 정보 추출
    			String id = request.getParameter("id");
    			String password = request.getParameter("password");
    			
    			// 2. DB 연동 처리
    			UserVO vo = new UserVO();
    			vo.setId(id);
    			vo.setPassword(password);
    			
    			
    			UserDAO userDAO = new UserDAO();
    			UserVO user = userDAO.getUser(vo);
    			
    			//3. 화면 네비게이션
    			if(user != null){
    				response.sendRedirect("getBoardList.do");
    					
    			}else{
    				response.sendRedirect("login.jsp");
    				
    			}
    		}else if(path.equals("/logout.do")) {
    			System.out.println("로그아웃 처리");
    			
    			// 1. 브라우저와 연결된 세션 객체를 강제 종료한다.
    			HttpSession session = request.getSession();
    			session.invalidate();
    			// 2. 세션 종료 후, 메인 화면으로 이동한다.
    			response.sendRedirect("login.jsp");	
    			
    		}else if(path.equals("/insertBoard.do")) {
    			System.out.println("글 등록 처리");
    		
    			//1. 사용자 입력 정보 추출
    			request.setCharacterEncoding("UTF-8");
    			String title = request.getParameter("title");
    			String writer =	request.getParameter("writer");
    			String content = request.getParameter("content");
    			
    			//2. DB연동 처리
    			
    			BoardVO vo = new BoardVO();
    			vo.setTitle(title);
    			vo.setWriter(writer);
    			vo.setContent(content);
    			
    			BoardDAO boardDAO = new BoardDAO();
    			boardDAO.insertBoard(vo);
    			
    			//3. 화면 네비게이션
    			response.sendRedirect("getBoardList.do");
    
    		}else if(path.equals("/updateBoard.do")) {
    			System.out.println("글 수정 처리");
    			//1. 사용자 입력 정보 추출
    			request.setCharacterEncoding("UTF-8");
    			String title = request.getParameter("title");
    			String content = request.getParameter("content");
    			String seq = request.getParameter("seq");
    			
    			//2. DB연동 처리
    			BoardVO vo = new BoardVO();
    			vo.setTitle(title);
    			vo.setContent(content);
    			vo.setSeq(Integer.parseInt(seq));
    			
    			BoardDAO boardDAO = new BoardDAO();
    			boardDAO.updateBoard(vo);	
    			
    			//3. 화면 네비게이션
    			response.sendRedirect("getBoardList.do");
    		}else if(path.equals("/deleteBoard.do")) {
    			System.out.println("글 삭제 처리");
    			
    			//1. 사용자 입력정보 추출
    			String seq= request.getParameter("seq");
    			//2. DB연동
    			BoardVO vo = new BoardVO();
    			vo.setSeq(Integer.parseInt(seq));
    			
    			BoardDAO boardDAO = new BoardDAO();
    			boardDAO.deleteBoard(vo);
    			
    			//3. 화면 네비게이션
    			response.sendRedirect("getBoardList.do");	
    		}else if(path.equals("/getBoard.do")) {
    			System.out.println("글 상세 조회 처리");
    			
    			// 1. 검색할 게시글 번호 추출
    			String seq = request.getParameter("seq");
    			
    			
    			// 2. DB연동 처리
    			BoardVO vo = new BoardVO();
    			vo.setSeq(Integer.parseInt(seq));
    
    			
    			BoardDAO boardDAO = new BoardDAO();
    			BoardVO board = boardDAO.getBoard(vo);
    			// 3. 검색 결과를 세션에 저장하고 상세 화면으로 이동한다
    			HttpSession session = request.getSession();
    			session.setAttribute("board", board);
    			response.sendRedirect("getBoard.jsp");
    			
    		}else if(path.equals("/getBoardList.do")) {
    			System.out.println("글 목록 검색 처리");
    			
    			// 1. 사용자 입력 정보 추출(검색 기능은 나중에 구현)
    			// 2. DB연동 처리
    			BoardVO vo = new BoardVO();
    			BoardDAO boardDAO = new BoardDAO();
    			List<BoardVO> boardList = boardDAO.getBoardList(vo);
    
    			// 3. 검색 결과를 세션에 저장하고 목록 화면으로 이동한다.
    			HttpSession session = request.getSession();
    			session.setAttribute("boardList", boardList);
    			response.sendRedirect("getBoardList.jsp");
    		}		
    	}
    }
    
    ```

  - 와 ! 진짜 길다

    - 결국, Controller 를 서블릿 클래스 하나로 구현하는것은 여러 측면에 문제가 있다
    - **SpringMVC** 를 사용하자



### SpringMVC 란?

| 클래스            | 기능                                                         |
| ----------------- | ------------------------------------------------------------ |
| DispatcherServlet | 유일한 서블릿 클래스로서 모든 클라이언트의 요청을 가장 먼저 처리하는 FrontController |
| HandlerMapping    | 클라이언트의 요청을 처리할 Controller 매핑                   |
| Controller        | 실질적인 클라이언트의 요청 처리                              |
| ViewResolver      | Controller가 리턴한 View 이름으로 실행될 JSP 경로            |



### MVC 프레임워크 구현

##### (1) Controller 인터페이스 작성

- DispatcherServlet 은 클라이언트의 요청을 가장 먼저 받아들이는 Front Controller

- 하지만 클라이언트 요청을 처리하기 위해 DispatcherServlet이 하는 일은 거의 없으며, 실질적인 요청 처리는 각 Controller 에서 담당

- 구체적인 Controller 클래스 구현

  - 모든 Controller 를 같은 타입으로 관리하기 위한 인터페이스 생성

  - 모든 Controller 의 최상위 인터페이스 필요

    > 클라이언트 요청을 받은 DispatcherServlet은 HandlerMapping을 통해 Controller 객체를 생성하고, 검색된 Controller 를 실행한다. 이때 어떤 Controller 객체가 검색되더라도, 같은 코드로 실행시키기 위해 모든 Controller의 최상위 인터페이스가 필요하다.

  - Controller.java(`Controller interface`)

  - ```java
    public interface Controller {
    	String handleRequest(HttpServletRequest request, HttpServletResponse response);
    }
    ```

##### (2) LoginController 구현

Controller 인터페이스를 구현한 LoginController 클래스를 만든다

- ```java
  public class LoginController implements Controller{
  	@Override
  	public String handleRequest(HttpServletRequest request, HttpServletResponse response) {
  		System.out.println("로그인 처리");		
  		// 1.사용자 입력 정보 추출
  		String id = request.getParameter("id");
  		String password = request.getParameter("password");		
  		// 2. DB 연동 처리
  		UserVO vo = new UserVO();
  		vo.setId(id);
  		vo.setPassword(password);		
  		UserDAO userDAO = new UserDAO();
  		UserVO user = userDAO.getUser(vo);		
  		//3. 화면 네비게이션
  		if(user != null){
  			return "getBoardList.do";				
  		}else{
  			return "login";			
  		}
  	}
  ```

  - Controller 인터페이스의 handleRequest() 메소드를 재정의 했으므로 로그인 처리 기능의 마지막은 이동할 화면을 리다이렉트하지 않고 **리턴하는 것으로 처리**한다
  - 로그인에 실패했을 때 이동할 화면 정보가 login.jsp 가 아니라 그냥 login 이다. 
    - ViewResolver 클래스
    - handleRequest() 메소드가 확장자 없는 문자열을 리턴하면, 자동으로 'jsp' 확장자가 붙는다



##### (3) HandlerMapping 클래스 작성

- HandlerMapping 은 모든 Controller 객체들을 저장하고 있다가, 클라이언트의 요청이 들어오면 요청을 처리할 특정 Controller 를 검색하는 기능을 제공한다.
- HandlerMapping 객체는 DispatcherServlet 이 사용하는 객체이다. 
- 따라서 DispatcherServlet 이 생성되고 init() 메소드가 호출될 때 **단 한 번** 생성된다

- HandlerMapping.java

  ```java
  public class HandlerMapping {
  	private Map<String, Controller> mappings;	
  	public HandlerMapping() {
  		mappings= new HashMap<String, Controller>();
  		mappings.put("/login.do", new LoginController());
  	}	
  	public Controller getController(String path) {
  		return mappings.get(path);
  	}
  }
  ```

  - HandlerMapping 은 Map 타입의 컬렉션을 멤버변수로 가지고 있으면서 게시판 프로그램에 필요한 모든 Controller 객체들을 등록하고 관리한다.
  - getController() 메소드는 매개변수로 받은 path에 해당하는 Controller 객체를 HashMap 컬렉션으로부터 검색하여 리턴한다.   
  - 따라서 HashMap 에 등록된 정보를 보면 Controller 객체가 어떤 ".do"에 매핑되어 있는지 알 수 있다.

##### (4)ViewResolver 클래스 작성

- ```java
  public class ViewResolver {
  	public String prefix;
  	public String suffix;	
  	
  	public void setPrefix(String prefix) {
  		this.prefix = prefix;
  	}
  	public void setSuffix(String suffix) {
  		this.suffix = suffix;
  	}	
  	public String getView(String viewName) {		
  		return prefix + viewName + suffix;
  	}	
  }
  ```

- ViewResolver 클래스는 Controller 가 리턴한 View 이름에 접두사와 접미사를 결합해 최종으로 실행될 View 경로와 파일명을 완성한다.
- ViewResolver도 HandlerMapping과 마찬가지로 DispatcherServlet의 init() 메소드가 호출될 때 생성된다



##### (5) DispatcherServlet 수정

- ```java
  public class DispatcherServlet extends HttpServlet {
  	private static final long serialVersionUID = 1L;
  	private HandlerMapping handlerMapping;
  	private ViewResolver viewResolver;
  	
  	public void init() throws ServletException {
  		handlerMapping = new HandlerMapping();
  		viewResolver = new ViewResolver();
  		viewResolver.setPrefix("./");
  		viewResolver.setSuffix(".jsp");
  	}
  	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  		process(request, response);
  	}
  
  	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		
  		request.setCharacterEncoding("UTF-8");
  		process(request, response);
  	}
  	
  	private void process(HttpServletRequest request, HttpServletResponse response) throws IOException {	
  		
  		// 1. 클라이언트의 요청 path 정보를 추출한다.
  		String uri = request.getRequestURI();
  		String path = uri.substring(uri.lastIndexOf("/"));
  		System.out.println(path);
  		
  		// 2. HandlerMapping을 통해 path 에 해당하는 Controller를 검색한다.
  		Controller ctrl = handlerMapping.getController(path);
  		
  		// 3. 검색된 Controller 를 실행한다
  		String viewName = ctrl.handleRequest(request, response);
  		
  		// 4. ViewResolver 를 통해 viewName에 해당하는 화면을 검색한다.
  		String view = null;
  		if(!viewName.contains(".do")) {
  			view = viewResolver.getView(viewName);			
  		}else {
  			view = viewName;
  		}
  		//5. 검색된 화면으로 이동한다.
  		response.sendRedirect(view);
  	}
  }
  ```

  - 수정된 DispatcherServlet 클래스에는 init() 메소드가 재정의 되어 있다.
  - 서블릿의 init() 메소드는 서블릿 객체가 생성된 후에 멤버변수를 초기화하기 위해 자동으로 실행된다.
    - 따라서 init() 메소드에서 DispatcherServlet 이 사용할 HandlerMapping 과 ViewResolver 객체를 초기화 한다. 
    - 그러면 DispatcherServlet 은 이렇게 생성된 HandlerMapping 과 ViewResolver를 이용하여 사용자의 요청을 처리한다.
  - process() 메소드 수정
    1. 먼저 클라이언트의 요청 path 에 해당하는 Controller 를 검색하기 위해 HandlerMapping 객체의 getController() 메소드를 호출한다.
    2. 그리고 검색된 Controller 의 handlerRequest()메소드를 호출하여 요청에 해당하는 로직을 처리하고 이동할 화면 정보가 리턴된다
    3. 마지막으로 Controller 가 리턴한 View 이름을 이용해 실행될 View를 찾아 해당화면으로 이동한다

##### [로그인 기능 처리 순서 정리]

1. 클라이언트가 로그인 버튼을 클릭하여 "/login.do"요청을 전송하면 DispatcherServlet이 요청받는다
2. DispatcherServlet은 HandlerMapping 객체를 통해 로그인 요청을 처리할 LoginController를 검색한다
3. 검색된 LoginController 의 handleRequest() 메소드를 호출하면 로그인 로직이 처리된다
4. 로그인 처리 후 이동할 화면 정보가 리턴되면
5. DispatcherServlet은 ViewResolver를 통해 접두사와 접미사가 붙은 JSP파일의 이름과 경로를 리턴받는다
6. 최종적으로 JSP 를 실행하고 실행결과가 브라우저에 응답된다.

