from django.db import models

class Stock_Name(models.Model):
    ticker = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    open = models.FloatField(null=True, blank=True)



    def __str__(self):
        return self.ticker





