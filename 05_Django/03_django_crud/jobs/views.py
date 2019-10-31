import requests
from django.shortcuts import render
from faker import Faker
from .models import Jobs
# Create your views here.


def create(request):
    name = request.POST.get('name')
     #db에 있는지 없는지 확인  필터걸기(2개이상은 에러생기므로)
    user = Jobs.objects.filter(name=name).first()
    # past_job = request.GET.get('past_job')

    #유저 정보가 있을때
    if user:
        #r기존 직업정보 가져오기
        past_job = user.past_job
        jobs =Jobs(name=name,past_job=past_job)
        
    #유저 정보 없을 때    
    else:
        faker = Faker()
        past_job = faker.job()
        jobs = Jobs(name=name,past_job=past_job)
        
        jobs.save()

        


        #GIPHY API
    api_key = "EJrj23vHajiPsSLk3iovWjeusslgcm95"
    api_url = "http://api.giphy.com/v1/gifs/search"

    data = requests.get(f'{api_url}?api_key={api_key}&q={past_job}&limit=1&lang=ko').json()
    try:
        img_url = data.get('data')[0].get('images').get('original').get('url')

        #에러나면?
    except IndexError:
        img_url = None


    context ={ 'jobs':jobs ,'img_url':img_url}

    return render(request, 'jobs/create.html',context)

def index(request):
    return render(request, 'jobs/index.html')