from django.db import models
from django.contrib.auth.models import User


class Footimg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='footimg')

    image1 = models.ImageField(upload_to='footimg/', null=True)
    nickname1 = models.CharField(max_length=20, unique=True, null=True)
    message1 = models.CharField(max_length=100, null=True)

    image2 = models.ImageField(upload_to='footimg/', null=True)
    nickname2 = models.CharField(max_length=20, unique=True, null=True)
    message2 = models.CharField(max_length=100, null=True)

    image3 = models.ImageField(upload_to='footimg/', null=True)
    nickname3 = models.CharField(max_length=20, unique=True, null=True)
    message3 = models.CharField(max_length=100, null=True)
