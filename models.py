from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(models.Model):
    STATUS_CHOICES = ((1, "未激活"), (2, "激活"), (3, "拉黑"))
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    class Meta:
        db_table = "users"
