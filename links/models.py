from turtle import update
from django.db import models
from .utils import get_link_data
# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    
    class Meta:
        ordering = ('price_difference', '-created')


    def save(self, *args, **kwargs):
        name, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price
                self.current_price = price
        else:
            self.old_price = 0
            self.price_difference = 0

        self.name = name
        self.current_price = price
        
        super().save(*args, **kwargs)
