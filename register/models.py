from django.db import models

# Create your models here.
class Signup(models.Model):  # Model class from models module is inherited in class Question.

    name = models.CharField(max_length=20, verbose_name="Name")
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10,verbose_name="Gender")
    student_id = models.CharField(max_length=10, verbose_name="College Registration ID", unique=True) #college id hi dalegi
    email = models.EmailField(max_length=100, verbose_name='College Email ID')
    COURSE = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('MCA', 'MCA'),
        ('MSc', 'MSc'),
        ('MBA', 'MBA'),
        ('Ph.D', 'Ph.D'),
    )
    course = models.CharField(max_length=20, verbose_name='Course Name')
    # branch = models.CharField(max_length=50, verbose_name='branch')
    # start_year = models.DateField(verbose_name='From')
    # end_year = models.DateField(verbose_name='To')
    password = models.CharField(max_length=100, verbose_name='Password')
    dob = models.DateField(max_length=10, verbose_name='Date Of Birth')
    photo = models.ImageField(verbose_name='Photo')
    mobile_number = models.IntegerField(verbose_name='mobile number')

    def __str__(self):  # A method is declared so that in admin panel Text of Question is displayed.
        return self.student_id