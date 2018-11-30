from django.db import models


# Create your models here.
class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    company_name = models.CharField()
