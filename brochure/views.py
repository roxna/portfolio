from django.shortcuts import render, redirect
# from django.http import HttpResponse
from brochure.models import *
from brochure.forms import ContactForm


# Create your views here.


def home(request):
    projects = Project.objects.order_by('?')[:3]
    blogs = Blog.objects.order_by('?'[:3])
    data = {
        "projects": projects,
        "blogs": blogs}
    return render(request, "home.html", data)


def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.post)
        if form.is_valid():
            if form.save():
                return redirect("/")
    else:
        form = ContactForm()
    data = {"form": form}
    return render(request, "contact.html", data)