from django.http import HttpResponse
from django.shortcuts import render
from stock.models import Apply
import datetime

def index(request):
    context = {}
    return render(request, 'mysite/index.html', context)

def buybond(request):
    context = {}
    return render(request, 'mysite/buybond.html', context)

def buystock(request):
    context = {}
    return render(request, 'mysite/buystock.html', context)

def applybroker(request):
    context = {}
    return render(request, 'mysite/applybroker.html', context)

def savebroker(request):
    brokerApply = Apply(biztype=request.POST['broker'],name=request.POST['name'],mobile=request.POST['mobile'],apply_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    brokerApply.save()
    context = {'respcode':'0000','respmsg':'报单成功，达标后加微信即可返现','back_url':'mysite/applybroker.html'}
    return render(request, 'mysite/info.html', context)

def back(request):
    back_url = request.GET['back_url']
    context = {}
    return render(request, back_url, context)

def credit(request):
    context = {}
    return render(request, 'mysite/credit.html', context)

def applycredit(request):
    context = {}
    return render(request, 'mysite/applycredit.html', context)

def savecredit(request):
    creditApply = Apply(biztype=request.POST['bank'],name=request.POST['name'],mobile=request.POST['mobile'],apply_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    creditApply.save()
    context = {'respcode':'0000','respmsg':'报单成功，达标后加微信即可返现','back_url':'mysite/applycredit.html'}
    return render(request, 'mysite/info.html', context)
