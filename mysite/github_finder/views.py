from django.shortcuts import render, HttpResponse
import requests
import json
import random

def github(request):
    return HttpResponse('THis is a github site')

def github_test(request):
    return HttpResponse('<h3>This is enough!</h3>')

def github_profile(request):
    jsonList = []
    parsedData = []
    username = "novking"
    pic = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList.append(json.loads(req.content.decode()))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    for i in range(3):
        pic.append ( HttpResponse('http://api.adorable.io/avatar/300/@'+username+ str(int(1000*random.random()))))

    return render(request, 'github_finder/github_profile.html', {'data':parsedData, 'picture':pic})
