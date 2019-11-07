## Authentication(인증)

###### 장고에서 이미 Auth 관련 기능을 만들어 두었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, 어드민 페이지에서 로그인 기능도 사용하고 있었다.

- Authentication(인증) -> 신원확인

- 자신이 누구라고 주장하는 신원을 확인하는 것



### 1. Accounts

- 기존 앱에서 구현해도 되지만, 장고에서 일반적으로 기능 단위로 애플리케이션을 나누는 것이 일반적이므로 accounts라는 새로운 앱을 만들어보자.

- accounts 앱 생성

  ```shell
  $ python manage.py startapp accounts
  ```

- `settings.py` 앱등록(출생신고)

- URL 분리

  ```python
  #config/urls.py
  urlpatterns = [
      path('accounts/', include('accounts.urls')),
  ]
  
  
  
  #accounts/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  
  urlpatterns = [
      path('index/', views.index ,name ='index'), 
  ]
  ```

  

### 2. SignUp

- `view.py`

  ```python
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import UserCreationForm
  # Create your views here.
  
  
  # Auth CRUD : CREATE
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = UserCreationForm    
      context = {'form':form}
      return render(request, 'accounts/signup.html', context)
  
  ```

- `urls.py`

  ```python
  urlpatterns = [    
      path('signup/', views.signup, name='signup'),    
  ]
  ```

  

- `signup.html`

  ```html
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block body %}
  <h1> 회원가입 </h1>
  
  
  <form action ="" method="POST">
  {% csrf_token %}
  {% bootstrap_form form layout='inline' %}
  {% buttons submit='가입' reset='초기화' %}
  {% endbuttons %}
  </form>
  {% endblock %}
  ```

  - `{{form.as_p}}` 의 bootstrap 적용 

    ```javascript
    {% bootstrap_form form layout='inline' %}
    ```

  - `input type="submit" value="가입"` 의 bootstrap 적용

    ```javascript
    {% buttons submit='가입' reset='초기화' %}
    ```

    

- 헤헤헤

- 

### 3. Login

- `view.py`

  ```python
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  
  def login(request):
      #request에 user가 돌아다닌다
      #이미 로그인되어있는 친구가 get으로 로그인 들어오려고 하면 index로 redirect시켜버리자
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method =='POST':
          # 세션 관련된 정보를 받기 위해 request를 받는다
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context ={'form':form}
      return render(request, 'accounts/login.html', context)
  ```

  

- f

- f

### Logout

- `view.py`

  ```python
  from django.contrib.auth import logout as auth_logout
  
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```

  













