from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'portal/home.html')
	#return HttpResponse("<h1>Hello Bitch!</h1>")
def login(request):
	return render(request,'portal/login.html')