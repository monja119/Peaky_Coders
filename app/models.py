from django.db import models

gender_choice = [
    ('male', 'male'),
    ('female', 'female'),
]


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='picture/user/')
    gender = models.CharField(max_length=8, choices=gender_choice, default='male')

    tel = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)

    password = models.CharField(max_length=200)


class Email(models.Model):
    user = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=100)
    frequence = models.IntegerField()
    method = models.CharField(max_length=50)


class File(models.Model):
    file = models.FileField(upload_to='files/compressor/')