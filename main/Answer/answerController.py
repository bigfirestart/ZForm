from main.models import Answer
def getAnswersFromQuestionId(question_id):
    answers = Answer.objects.filter(thisQuestionId = question_id)
    return answers
