from django.urls import path 
from . import views

urlpatterns = [
	path('', views.test3, name='coverpage'),
	path('login', views.test, name='login'),
	path('registration', views.test1, name='registration'),
	path('adminlogin', views.test2, name='adminlogin')
]