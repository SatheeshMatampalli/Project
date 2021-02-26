from django.db import models

# Create your models here.
class Contact(models.Model):
	Name=models.CharField(max_length=100)
	Subject=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	phone_no=models.IntegerField()
	comments=models.TextField(max_length=2000)

	def __str__(self):
		return self.Name