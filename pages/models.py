from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

# For Slugify
from django.utils.text import slugify
import string
import random

# To generate differnt slug
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=500)
    minimum_bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    end_time = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_posted',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            # can be added duplicate product with same name
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Products, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:product_detail', args=[self.id, self.slug])


class Bid(models.Model):
    bid_item =models.ForeignKey(Products,on_delete=models.CASCADE,related_name='bid_item')
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering =('-bid_price',)

    def __str__(self):
        return str(self.created_by)
   