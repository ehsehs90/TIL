from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def index(request):

    return render(request, 'accounts/index.html')
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)   # 장고 UserCreationForm 들고오는 코드
        if form.is_valid():
            form.save()
            # auth_login(request,user)
            return redirect('movies:index')
    else:
        form = UserCreationForm
    
    context ={'form':form,}
    return render(request, 'accounts/signup.html', context)

def login(request):
    # form = AuthenticationForm(request, request.POST)
    # auth_login(request, form.get_user())
    if request.user.is_authenticated:
        return redirect('moives:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:        
        form  = AuthenticationForm()
    context =  {'form':form,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def password(request):
    return render(request, 'movies:index')


def update(request):
    return render(request, 'movies:index')

def delete(request):
    request.user.delete()
    return redirect('movies:index')