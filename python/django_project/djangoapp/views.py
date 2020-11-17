from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
	return render(request,'djangoapp/login.html')
def test1(request):
	return render(request,'djangoapp/registration.html')
def test2(request):
	return render(request,'djangoapp/adminlogin.html')
def test3(request):
	return render(request,'djangoapp/coverpage.html')

