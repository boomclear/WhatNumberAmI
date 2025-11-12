from django.shortcuts import render

# from django.http import HttpRequest
from .forms import UploadImageForm
from .models import UserImage
from django.shortcuts import get_object_or_404, render, redirect

TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates")'


def index(request):
    form = UploadImageForm
    if request.method == "GET":
        return render(request, "index.html", {"form": form})


def userUpload(request):
    if request.method == "POST":
        userForm = UploadImageForm(request.POST)
        if userForm.is_valid():
            userSubmission = userForm.save()
            return redirect("userResultPage", pk=userSubmission.pk)
        else:
            return render(request, "error.html", {"request": request})


def userResultPage(request, pk):
    userSubmission = get_object_or_404(UserImage, pk=pk)
    return render(request, "userResultPage.html", {"result": userSubmission})
