from django.db import models

image_storage = "../../DumpFiles"


class UserImage(models.Model):
    userImage = models.ImageField(upload_to=image_storage, null=True, blank=True)
    userAnswer = models.CharField(max_length=30)
