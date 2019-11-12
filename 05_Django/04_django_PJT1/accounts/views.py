from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm


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
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/change_password.html',context)


def update(request):
    if request.method =="POST":
        pass
    else:
        form = CustomUserChangeForm(instance=request.user)
        context={'form':form}

    return render(request, 'accounts/update.html', context)

def delete(request):
    request.user.delete()
    return redirect('movies:index')