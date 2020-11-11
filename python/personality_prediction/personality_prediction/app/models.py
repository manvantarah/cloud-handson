from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(max_length=100)
	mobile = models.IntegerField(max_length=100)
	address = models.CharField(max_length=1000)