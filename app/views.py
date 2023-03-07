from django.shortcuts import render
from django.http import HttpResponse

#create your views here.
def sample(request):
    return HttpResponse('sample craeated')
