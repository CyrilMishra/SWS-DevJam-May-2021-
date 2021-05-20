
from django.contrib import admin
from .models import CommunityAnswer, CommunityQuestion
# Register your models here.
admin.site.register(CommunityQuestion)
admin.site.register(CommunityAnswer)

