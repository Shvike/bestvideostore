from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from json import dumps


def hello(request):
    return HttpResponse("<h1>Hellou</h1>")
# Create your views here.


def world(request):
    response = {"name":"Alex", "d":34, "arr":"12345"}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)

def accept_comment(request, id):

    Comment.objects.create(text=request.POST["commentary"], comment_video_id=id)
    print(request.POST)
    # 1
    # Comment.objects.create(text=request.GET["commentary"], comment_video_id=id)

    # 2
    # vid = Video.objects.get(id=id)
    # Comment.objects.create(text="hi text", comment_video=vid)

    # 3
    # c = Comment(text=request.GET["commentary"], comment_video_id=id)
    # c.save()

    # print(id)
    # print(request.GET["commentary"])
    return redirect("main_page")

def only_video(request, id):
    response = {"video":Video.objects.get(id=id)}
    return render(request, "only_video.html", response)

def add_like(request, id):
    v = Video.objects.get(id=id)
    v.likes += 2
    v.save()
    return redirect("main_page")

def ajax_like(request):
    id = request.GET["id"]
    v = Video.objects.get(id=id)
    v.likes += 1
    v.save()
    return HttpResponse(v.likes)

def ajax_comment(request):
    id = request.GET["id"]
    val = request.GET["val"]
    com = Comment.objects.create(text=val, comment_video_id=id)
    response = {"id":com.id, "date":com.date.__str__()}
    response = dumps(response)
    return HttpResponse(response)