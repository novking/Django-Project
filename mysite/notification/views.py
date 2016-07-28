from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from models import Notification

def show_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    return render_to_response('notification.html',{'notification':n})

def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()

    return HttpResponseRedirect('/accounts/loggedin')

    
