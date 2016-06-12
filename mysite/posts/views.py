from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    if request.user.is_authenticated():
        context = {
        "title":"you are authenticated to use see this content"
        }
    else:
        context = {
         "title":"List"
        }
    return render(request, "index.html", context)
def post_create(request):
    context = {
     "title":"Detail"
    }
    return render(request, "index.html", context)

def post_detail(request):
    return HttpResponse("<h1>detail</h1>")



def post_updated(request):
    return HttpResponse("<h1>updated</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
