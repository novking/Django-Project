from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import PostForm

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
    form = PostForm(request.POST or None)
    if form.is_valid():
        # instant = form.save(commit= False)
        # instant.save()
        instance = form.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "posts/posts_form.html", context)

def post_detail(request, pk=None):
    instance = get_object_or_404(models.Post, id=pk)
    return render(request, "posts/detail.html", {"instance":instance})




def post_updated(request, pk=None):
    instance = get_object_or_404(models.Post, id=pk)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instant = form.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "posts/posts_form.html", context)


def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
