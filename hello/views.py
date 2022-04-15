from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
import datetime


def index(request):
    params={
        'title':'Dakoku',
        'message':'your data:',
        'form': HelloForm()
        }
    if 'button1' in request.POST:
        now = datetime.datetime.now()
        params['message']=request.POST['name']+'さんは'+str(now)+'に出勤しました。'
        params['form']=HelloForm(request.POST)
    if 'button2' in request.POST:
        now = datetime.datetime.now()
        params['message']=request.POST['name']+'さんは'+str(now)+'に退勤しました。'
        params['form']=HelloForm(request.POST)
    return render(request,'hello/index.html',params)

