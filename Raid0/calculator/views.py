from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext


def index(request):
    return render(request,'index.html',)

def test(request):
    return render(request,'test.html'),







