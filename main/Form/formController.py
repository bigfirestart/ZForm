from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Form
from main.utils.utils import *
from django.contrib.auth.models import User
from main.Question.questionController import createNewQuestion



@csrf_exempt
def getAllUserForms(request):
    try:
        if(request.method == 'GET'):
            forms = Form.objects.filter(author = request.user)
            formsList= []
            for form in forms:
                formInList = form.toList()
                formsList.append(formInList)
            jsonForms = JSONFactory(formsList)
            return HttpResponse(jsonForms)
        #form Creating
        elif(request.method == 'POST'):
            return createNewForm(request)
    except Exception as ex:
            return HttpResponse(ex, status= 500)
@csrf_exempt
def formRequestSwitcher(request, form_id):
    try:
        #All Forms of user
        if(request.method == 'GET'):
            form = getFormById(form_id)
            formJson = JSONFactory(form.toList())
            return HttpResponse(formJson, status= 200)
        elif (request.method == 'PUT'):
            return HttpResponse(status= 200)
        elif (request.method == 'DELETE'):
            deleteFormById(form_id)
            return HttpResponse(status= 200)
        else:
            return HttpResponse(status= 404)
    except Exception as ex:
            return HttpResponse(ex, status= 500)



#CRUD
def getFormById(form_id):
    form = Form.objects.get(id = form_id)
    return form
    #Form.objects.filter(id == requestFormId)
def deleteFormById(form_id):
    form = Form.objects.get(id = form_id)
    form.delete()
def createNewForm(request):
    #TODO write parse for request json
    #requestJSON = str(request.readline()).split("{")[1].split("}")[0]
    print(request.POST['username'])
    question = createNewQuestion(1)
    form = Form(name = "test" , firstQuestionId = question.id , author_id = 1)
    form.save()
    return HttpResponse(JSONFactory(form.toList()), status = 201)
