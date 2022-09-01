from django.db import models
from django.contrib.auth.models import User

class Amount(models.Model):
	Amount = models.FloatField(null=True, blank=True)
	
# Create your models here.
