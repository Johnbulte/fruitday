from django.db import models

# Create your models here.
class User(models.Model):
	uphone = models.CharField(max_length=20)
	upwd = models.CharField(max_length=20)
	uemail = models.EmailField()
	uname = models.CharField(max_length=20)

	def __str__(self):
		return self.uname

