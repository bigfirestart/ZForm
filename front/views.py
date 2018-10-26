from django.shortcuts import render
from main.models import Question, Answer
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse


# Create your views here.
def questionView(request , question_id):
    question = Question.objects.get(id = question_id)
    answers  = Answer.objects.filter(thisQuestionId = question_id)
    return render(request, 'question.html',{'answers': answers , "question": question})
def index(request):
    return render(request, 'indexNew.html')
def sendTestEmail(request):
    send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['bigfirestart@gmail.com'])
    return HttpResponse("sended")
