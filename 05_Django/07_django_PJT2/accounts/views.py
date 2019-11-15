
# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # auth_login(request,user)
            return redirect('movies:index')


    else:
        form = UserCreationForm
    context={'form':form,}
    return render(request, 'accounts/signup.html',context)

def login(request):

    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
        
    context = {'form':form}
    return render(request, 'accounts/login.html',context)


def logout(request):

    auth_logout(request)
    return redirect('movies:index')

