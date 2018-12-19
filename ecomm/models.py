from django.db import models

class Items(models.Model):
	item = models.CharField(max_length=800)
	Description = models.CharField(max_length=800)
	ItemImage = models.CharField(max_length=800)
	
	def  __str__(self):
		return self.item


class userComments(models.Model):
	fullName = models.CharField(max_length=800)
	mobileNo = models.CharField(max_length=800)
	city = models.CharField(max_length=800)
	message = models.CharField(max_length=800)
	
	def  __str__(self):
		return self.mobileNo
