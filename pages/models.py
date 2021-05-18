from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "ID:" + str(self.pk) + " " + self.title

class Auction(models.Model):
	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
	number_of_bids = models.IntegerField()
	time_starting = models.DateTimeField()
	time_ending = models.DateTimeField()
	
	def __str__(self):
		return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)