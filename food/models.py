from django.db import models

# Create your models here.


class item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name + ' ' + self.item_desc
