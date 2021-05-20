# Generated by Django 3.2.3 on 2021-05-20 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_alter_signup_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('item_description', models.CharField(max_length=2000)),
                ('item_price', models.IntegerField()),
                ('item_pic1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='pic1')),
                ('status', models.CharField(choices=[('sold', 'sold'), ('available', 'available')], default='available', max_length=10, verbose_name='status')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.signup')),
            ],
        ),
    ]
