from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.CharField(max_length=500)
    minimum_bid_price = models.DecimalField(max_digits=10,decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering =('date_posted',)
        index_together = (('id','slug'),)
    def __str__(self):
        return "ID:" + str(self.pk) + " " + self.title
    


class Auction(models.Model):
	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
	number_of_bids = models.IntegerField()
	time_starting = models.DateTimeField()
	time_ending = models.DateTimeField()
	
	def __str__(self):
		return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)