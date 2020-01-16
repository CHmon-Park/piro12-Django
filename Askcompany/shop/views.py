from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def archives_year(request, year):

    return HttpResponse('{}년도에 대한 내용'.format(year))