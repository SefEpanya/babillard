from asyncio import tasks
from pyexpat import model
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Task

# Create your views here.


def list(request):
   return render(request, template_name='index.html')  