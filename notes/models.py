from django.db import models

class Course(models.Model) :
    course = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('MCA', 'MCA'),
        ('MSc', 'MSc'),
        ('MBA', 'MBA'),
        ('Ph.D', 'Ph.D'),
    )
    name = models.CharField(max_length=50,null=False,choices=course)

    def __str__(self):
        return self.name


class Document(models.Model):
    course = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('MCA', 'MCA'),
        ('MSc', 'MSc'),
        ('MBA', 'MBA'),
        ('Ph.D', 'Ph.D'),
    )
    course_name = models.CharField(max_length=50, null=False, choices=course)
    subject = models.CharField(max_length=100,null=False)
    title = models.CharField(max_length=100,null=False)
    file = models.FileField(upload_to='documents/',null=False)

    def __str__(self):
        return self.subject

