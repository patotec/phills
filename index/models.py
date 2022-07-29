from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=2000)
	message = models.TextField()

	def __str__ (self):
		return self.name

class Quote(models.Model):
	fullname = models.CharField(max_length=200)
	email = models.EmailField()
	type_shipment = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	curent_location = models.CharField(max_length=200,blank=True)
	pickup = models.CharField(max_length=200)
	track_id = models.CharField(max_length=10, default='0')
	width = models.CharField(default='0',max_length=20)
	height = models.CharField(default='0',max_length=20)
	length = models.CharField(default='0',max_length=20)
	weight = models.CharField(default='0',max_length=20)
	status = models.CharField(max_length=50,default='Processing')
	date_at = models.DateTimeField(auto_now_add=False,blank=True)
	Delivered = models.BooleanField(default=False)

	def __str__ (self):
		return self.fullname

class Review(models.Model):
	name = models.CharField(max_length=200)
	image = models.FileField()
	body = models.TextField()

	def __str__ (self):
		return self.name
# Create your models here.
