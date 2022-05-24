from django.shortcuts import render
from portfolio import models


def main_page(request):
    projects = models.Project.objects.all
    return render(request, "main.html", {'projects': projects})

def view_project(request):
    pass