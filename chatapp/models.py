import register
from django.db import models
from register.models import Signup
from datetime import datetime
# Create your models here.

# models for chat transaction

class ChatTransaction(models.Model):
    s = models.ForeignKey(Signup, on_delete=models.CASCADE)
    d = models.CharField(max_length=255)
    transaction_id = models.AutoField(primary_key=True)
    time = models.TimeField(auto_now=True,null=True)
# model for messages

class Message(models.Model):
    s = models.ForeignKey(Signup, on_delete=models.CASCADE)
    d = models.CharField(max_length=255)
    transaction_id = models.ForeignKey(ChatTransaction,on_delete=models.CASCADE)
    message_id = models.AutoField(primary_key=True)
    message = models.TextField()
    time = models.TimeField(auto_now=True, null=True)

