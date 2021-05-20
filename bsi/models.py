from django.db import models

# Create your models here.
from register.models import Signup


# class Tag(models.Model):
#     name =models.CharField(max_length=300,null=True)

#     def __str__(self):
#         return self.name

class Item(models.Model):  # Model class from models module is inherited in class Question.

    item_name = models.CharField(max_length=100, null=False)
    student = models.ForeignKey(Signup, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(null=False, blank=False, auto_now=True)
    item_description = models.CharField(max_length=2000, null=False)
    item_price = models.IntegerField(null=False)
    item_pic1 = models.ImageField(verbose_name='pic1', null=True, blank=True)
    STATUS = (
        ('sold', 'sold'),
        ('available', 'available'),
    )
    status = models.CharField(max_length=10, verbose_name='status', null=False, choices=STATUS, default='available')

    def __str__(self):
        return self.item_name
