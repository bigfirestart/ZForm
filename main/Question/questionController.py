from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Question
from main.utils.utils import *
from django.contrib.auth.models import User
from main.Answer.answerController import getAnswersFromQuestionId


def questionRequestSwitcher(request , question_id):
    #try:
        if(request.method == 'GET'):
            question = Question.objects.get(id =question_id)
            answers = getAnswersFromQuestionId(question_id)
            qustionWithAnswerList= question.toList()
            answersList = {}
            iter =1
            for answer in answers:
                    answersList["Answer " + str(iter)]= answer.toList()
                    iter+=1

            qustionWithAnswerList["Answers:"]  =answersList
            questionJson = JSONFactory(qustionWithAnswerList)
            return HttpResponse(questionJson, status= 200)
        elif (request.method == 'PUT'):
            return HttpResponse(status= 200)
        elif (request.method == 'DELETE'):
            deleteFormById(form_id)
            return HttpResponse(status= 200)
        else:
            return HttpResponse(status= 404)
    #except Exception as ex:
    #    return  HttpResponse(ex, status= 500)
def createNewQuestion(author_id):
    question = Question(author_id = author_id)
    question.save()
    return question
