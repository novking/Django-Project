from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
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
    return render(request, "posts/base.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        # instant = form.save(commit= False)
        # instant.save()
        instance = form.save()
        messages.success(request, "successfully created", extra_tags="btn btn-primary")
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
        messages.success(request, "good to go", extra_tags="btn btn-success")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "what have you done?! i cannot save the file :(")
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "posts/posts_form.html", context)


def post_delete(request, pk=None):
    instance = get_object_or_404(models.Post, id=pk)
    instance.delete()
    messages.success(request, "good to go", extra_tags="btn btn-danger")
    return HttpResponseRedirect(reverse_lazy("posts:post_list"))
