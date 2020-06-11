from django.shortcuts import render
from django.http import HttpResponse
from .models import Video


def hello(request):
    return HttpResponse("<h1>Hellou</h1>")
# Create your views here.


def world(request):
    response = {"name":"Alex", "d":34, "arr":"12345"}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)