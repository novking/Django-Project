from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def post_list(request):
    object_list = models.Post.objects.all()
    if request.user.is_authenticated():
        context = {
        "object_list": object_list,
        "title":"you are authenticated to use see this content"
        }
    else:
        context = {
         "title":"List"
        }
    return render(request, "posts/index.html", context)
def post_create(request):
    instance = get_object_or_404(models.Post, id=100)
    context = {
     "title":"Detail"
    }
    return render(request, "index.html", context)

def post_detail(request, pk=None):
    instance = get_object_or_404(models.Post, id=pk)
    return render(request, "posts/detail.html", {"instance":instance})



def post_updated(request):
    return HttpResponse("<h1>updated</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
