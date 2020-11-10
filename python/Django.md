# Installing Django on Ubuntu Machine

## Step 1) Installing Python and Pip

	$	sudo apt-get update
	$	sudo apt-get install python3 

### Check Python version

	$	python3 --v

###	Install pip by the command

	$	sudo apt-get install python3-pip

### Check pip3 version

	$	pip3 -V

##	Step 2)	Installing Django

	$	pip3 install Django

###  Verify the Django version

	$	django-admin –version

##	Step 3)	Create a Django Project

	$	django-admin startproject django_project

### Go to the defined path and make the changes

	$	cd django_project
	$	python3 manage.py migrate

##	Step 4)	Creating a super user for django application

	$	python3 manage.py createsuperuser

### Give the username and password 

##	Step 5)	Run the Django Application with the favourite editor

	$	sudo subl django_app/settings.py

#### Add the host IP address 

	ALLOWED_HOSTS = ['server_IP']

## Run the Django application server with below command

	$	python3 manage.py runserver server_IP:8000


## Django Welcome file has to be seen !!

## Step 6)	Create a Django app

	$	sudo python3 manage.py startapp "app_name"

## Step 7) After succesfull creation of Django app go to go to the create a file views.py in the "Django app" folder

	$ cd djangoapp

	$ sudo subl views.py

### Insert the code in the file

#### 7)A

	from django.shortcuts import render
	from django.http import HttpResponse
	# Create your views here.
	def test(request):
		return HttpResponse('<h1>Welcome to Django Website</h1>')

### 7)B

#### OR If any files to be called, use any one code

	from django.shortcuts import render
	from django.http import HttpResponse
	# Create your views here.
	def test(request):
		return render(request,'APP_NAME/FILE_NAME')

### Save and exit from file

## Step 8) Create urls.py file in the same "Django app" folder

	$	sudo subl urls.py

### Insert the code in the urls.py file

	from django.urls import path 
	from . import views 	# . the file views in the same directory
	urlpatterns = [
    path('', views.test, name='home-page')	# "views.test is filename.function name"
	]

### Save and exit from file

## Step 8)	Exit from directory go to another directory django_project which is created in Step 3)

	$ cd ..

	$ cd django_project

### Edit urls.py in it

	from django.contrib import admin
	from django.urls import path, include # add include
	urlpatterns = [
    	path('admin/', admin.site.urls), 
    	path('',include('App_Name.urls')) # add this path with "appname"
	]

### Save and exit the file

### If you have used 7)A the stop here and execute Step 9), if not jump to Step 10)

## Step 9)

	$ cd ..

	$ sudo python3 manage.py runserver

### copy the https link in CLI and paste it in browser URL and the message "Welcome to Django Website" should be dispalyed

## Step 10) Create a folder name templates in 'App_Name' and add folder django under templates as django uses naming conventions

	$	sudo mkdir templates

	$	cd templates

	$	sudo mkdir 'App_Name'

	$	cd 'App_Name'


#### 					Here you can have diffeent files and folder to be executed!!

##	Step 11) Go to 'App_Name' and copy the class name of apps.py and open settings.py in Django_Project

	$	cd ..

	$	cd ..

	$	cd 'App_Name'

	$	sudo subl apps.py

	from django.apps import AppConfig
	class DjangoappConfig(AppConfig): # Copy DjangoappConfig, your file may have different class name
    	name = 'djangoapp'
	
#### Exit from file

	$ cd ..

	$ cd django_project

	$ cd settings.py

	INSTALLED_APPS = [
    'djangoapp.apps."Paste it here"', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	]

#### Hit save and exit from file

## Step 12)

	$ cd ..

	$ sudo python3 manage.py runserver

### copy the https link in CLI and paste it in browser URL and the message "The content in the file should e displayed" should be there!!

#### Good to Work with Django












