from django.contrib import admin
from .models import *

admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(Matching)
# Registers your models here.
