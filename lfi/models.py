from django.db import models


from django.db import models


# Create your models here.
from register.models import Signup

# class Tag(models.Model):
#     name =models.CharField(max_length=300,null=True)

#     def __str__(self):
#         return self.name

class LostItem(models.Model):  # Model class from models module is inherited in class Question.

    TYPE = (
        ('metal','metal'),
        ('plastic','plastic'),
        ('wooden','wooden'),
        ('leather','leather'),
        ('cloth','cloth'),
        ('mix','mix'),
        ('chemicals','chemicals'),
        )

    COLOR = (
        ('mix','mix'),
        ('transparent','transparent'),
        ('translucent','translucent'),
        ('grey','grey'),
        ('purple','purple'),
        ('gold','gold'),
        ('silver','silver'),
        ('white','white'),
        ('pink','pink'),
        ('orange','orange'),
        ('brown','brown'),
        ('black','black'),
        ('green','green'),
        ('yellow','yellow'),
        ('blue','blue'),
        ('red','red'),
        )

    SHAPE = (
        ('other','other'),
        ('circle','circle'),
        ('kite','kite'),
        ('shape-changer','shape-changer'),
        ('cube','cube'),
        ('cuboid','cuboid'),
        ('sphere','sphere'),
        ('cylindrical','cylindrical'),
        ('cone','cone'),
        ('pyramid','pyramid'),
        ('square','square'),
        ('rectangle','rectangle'),
        ('triangle','triangle'),
        )
    C_TYPE = (
        ('branded','branded'),
        ('local','local')
        )
    item_name = models.CharField(max_length=100,null=False)
    student = models.ForeignKey(Signup, null=True , on_delete=models.SET_NULL)
    date_created = models.DateField(null=False, blank = False, auto_now = True)
    item_description = models.CharField(max_length=2000,null=False)
    item_type = models.CharField(max_length=2000,null=False,choices=TYPE,default='mix')
    lost_place = models.CharField(max_length=100,null=True,blank=True)
    lost_time = models.TimeField(auto_now=False)
    lost_date = models.DateField(null=False, blank = False, auto_now = True)
    item_price = models.IntegerField(null=False)
    item_color = models.CharField(max_length=20,choices=COLOR,default='mix')
    shape = models.CharField(max_length=20,choices=SHAPE,default='other')
    author_name = models.CharField(max_length=20,null = True,blank=True)
    company_type = models.CharField(max_length=20,null=True,blank=True,choices=C_TYPE,default='local')
    item_pic1 = models.ImageField(verbose_name='pic1',null=True,blank=True)
    def __str__(self):
        return self.item_name




class FoundItem(models.Model):  # Model class from models module is inherited in class Question.

    TYPE = (
        ('metal','metal'),
        ('plastic','plastic'),
        ('wooden','wooden'),
        ('leather','leather'),
        ('cloth','cloth'),
        ('mix','mix'),
        ('chemicals','chemicals'),
        )

    COLOR = (
        ('mix','mix'),
        ('transparent','transparent'),
        ('translucent','translucent'),
        ('grey','grey'),
        ('purple','purple'),
        ('gold','gold'),
        ('silver','silver'),
        ('white','white'),
        ('pink','pink'),
        ('orange','orange'),
        ('brown','brown'),
        ('black','black'),
        ('green','green'),
        ('yellow','yellow'),
        ('blue','blue'),
        ('red','red'),
        )

    SHAPE = (
        ('other','other'),
        ('circle','circle'),
        ('kite','kite'),
        ('shape-changer','shape-changer'),
        ('cube','cube'),
        ('cuboid','cuboid'),
        ('sphere','sphere'),
        ('cylindrical','cylindrical'),
        ('cone','cone'),
        ('pyramid','pyramid'),
        ('square','square'),
        ('rectangle','rectangle'),
        ('triangle','triangle'),
        )
    C_TYPE = (
        ('branded','branded'),
        ('local','local')
        )
    item_name = models.CharField(max_length=100,null=False)
    student = models.ForeignKey(Signup, null=True , on_delete=models.SET_NULL)
    date_created = models.DateField(null=False, blank = False, auto_now = True)
    item_description = models.CharField(max_length=2000,null=False)
    item_type = models.CharField(max_length=2000,null=False,choices=TYPE,default='mix')
    lost_place = models.CharField(max_length=100,null=True,blank=True)
    lost_time = models.TimeField(auto_now=False)
    lost_date = models.DateField(null=False, blank = False, auto_now = True)
    item_price = models.IntegerField(null=False)
    item_color = models.CharField(max_length=20,choices=COLOR,default='mix')
    shape = models.CharField(max_length=20,choices=SHAPE,default='other')
    author_name = models.CharField(max_length=20,null = True,blank=True)
    company_type = models.CharField(max_length=20,null=True,blank=True,choices=C_TYPE,default='local')
    item_pic1 = models.ImageField(verbose_name='pic1',null=True,blank=True)
    STATUS = (
        ('available','available'),
        ('delivered','delivered'),
        )
    status = models.CharField(max_length=20,choices=STATUS,default='available')
    def __str__(self):
        return self.item_name


class Matching(models.Model):
    lost_item = models.ForeignKey(LostItem,null=True , on_delete=models.SET_NULL)
    found_item = models.ForeignKey(FoundItem,null=True , on_delete=models.SET_NULL)
    match_percent = models.IntegerField(null=False,default=0)

    def __str__(self):
        return self.lost_item
# Create your models here.
