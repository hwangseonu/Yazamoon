from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    student_id = models.CharField(max_length=5)
