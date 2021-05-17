
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def coins(request):
    roll1 = request.POST.get('rollno1')
    roll2 = request.POST.get('rollno2')
    roll3 = request.POST.get('rollno3')
    coin1 = request.POST.get('coin1')
    coin2 = request.POST.get('coin2')
    coin3 = request.POST.get('coin3')
    params = {'rollno1':roll1, 'coins1':coin1, 'rollno2':roll2,'coins2':coin2,'rollno3':roll3,'coins3':coin3}
    return render(request, 'coins.html', params)
