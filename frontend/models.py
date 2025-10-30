from django.db import models

image_storage = "/Users/austinwoods/CodingProjects/Python/DumpFiles"


class UserImage(models.Model):
    userImage = models.ImageField(upload_to=image_storage)
    userAnswer = models.CharField(max_length=30)
        