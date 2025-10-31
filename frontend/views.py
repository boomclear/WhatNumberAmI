from django.shortcuts import render
from django.http import HttpResponse
from . import forms

TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates")'


def index(request):
    if request.method == "GET":
        form = forms.UploadImage
        return render(request, "index.html", {"form": form})


def userUpload(request):
    if request.method == "POST":
        return render(request, "post.html")
