from django.shortcuts import render
from django.http import HttpResponse
import random

fortune = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']

# Create your views here.

def index(request):
	return HttpResponse('Hello Django')

def index(request):
	data = {
		'fortune' : random.choices(fortune)
    }
	return render(request, 'teamapp/index.html', data)

