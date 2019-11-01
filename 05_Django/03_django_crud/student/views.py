from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    student = Student.objects.all()[::-1]
    context = {'student':student}
    return render(request, 'student/index.html',context)

def new(request):
    return render(request, 'student/new.html')


# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content= request.POST.get('content')


    article = Student(title=title, content=content)
    article.save()
    
    #return render(request,'articles/create.html')
    return redirect('/student/index/')


def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {'student':student}
    return render(request, 'student/detail.html', context)

def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('/student/index/')

def edit(request,student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {'student':student}
    return render(request, 'student/edit.html',context)

def update(request, student_pk):
    student=Student.objects.get(pk=student_pk)
    student.title = request.POST.get('title')
    student.content = request.POST.get('content')
    student.save()
    return redirect(f'/student/{student.pk}/')

