from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	IdeaName=models.CharField(max_length=100)
	Description=models.CharField(max_length=200)
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
	   return self.IdeaName
	  
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
# Create your models here.
