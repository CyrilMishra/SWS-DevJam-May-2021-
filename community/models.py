import register
from django.db import models
from register.models import Signup



# community
class CommunityQuestion(models.Model):
    student_id = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True)
    question_id = models.AutoField(primary_key=True,)
    question_description = models.TextField(null=True)
    publishing_date = models.DateField()
    stu_department = models.CharField(max_length=255, default='0000000',null=True)
    stu_name = models.CharField(max_length=255,null=True,default="mnnit")


# Create your models here.
# community answer
class CommunityAnswer(models.Model):
    question_id = models.ForeignKey(CommunityQuestion, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True)
    answer_id = models.AutoField(primary_key=True)
    answer_discrption = models.TextField()
    upvote = models.IntegerField(null=True, default=0)
    downvote = models.IntegerField(null=True, default=0)
    answer_assets = models.FileField(null=True)
