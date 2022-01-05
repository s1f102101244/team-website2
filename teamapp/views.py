from django.shortcuts import render
from django.http import HttpResponse
import random

fortune = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']

# Create your views here.



def index(request):

	if request.method == 'GET':
		return render(request, 'teamapp/index.html')
	elif request.method == 'POST':
		title = request.POST['title']
		text = request.POST['text']
		return HttpResponse('運勢 : {}, コメント : {}'.format(title, text))

