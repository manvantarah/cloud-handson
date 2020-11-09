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

##	Step 3)	Create A Django Application

	$	django-admin startproject django_project

### Go to the defined path and make the changes

	$	cd django_app
	$	python3 manage.py migrate

##	Step 4)	Creating a super user for django application

	$	python3 manage.py createsuperuser

### Give the username and password 

##	Step 5)	Run the Django Application with the favourite editor

	$	sudo subl django_project/settings.py

#### Add the host IP address 

	ALLOWED_HOSTS = ['server_IP']

## Run the Django application server with below command

	$	python3 manage.py runserver server_IP:8000


## Good to Work with Django





