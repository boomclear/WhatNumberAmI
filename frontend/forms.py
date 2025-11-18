from django import forms
from . import models


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.UserImage
        fields = ["userImage", "userAnswer"]
