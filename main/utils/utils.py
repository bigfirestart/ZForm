from django.http import HttpRequest
import json

def requestToList(request):
    requestList = request.path.split("/")
    for el in requestList:
        if(el == ''):
            requestList.remove('')
    return requestList

def JSONFactory(obj):
    return (json.dumps(obj, default=lambda o: o.__dict__,  indent=4))
