from django.db import models
# Create your models here.
# ForeignKey = Many-to-one
class Form(models.Model):
    name = models.CharField(max_length = 128)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    firstQuestionId = models.IntegerField(default = 0, null = False)
    isPrivate = models.BooleanField(default = False)
    def __str__(self):
        return self.name
    def toList(self):
        return {"type": "Form" , "id": self.id , "author_id" : self.author.id, "name": self.name ,  "firstQuestionId":self.firstQuestionId}
class Answer(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE )
    answerText = models.CharField(max_length = 256)
    nextQuestionId= models.IntegerField(default = 0)
    thisQuestionId = models.IntegerField(default = 0)
    def __str__(self):
        return self.answerText
    def toList(self):
            return {"type": "Answer" ,"id": self.id ,"author_id": self.author.id , "answer_text": self.answerText , "thisQuestionId":self.thisQuestionId , "nextQuestionId":self.nextQuestionId  }

class Question(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    questionText = models.CharField(max_length = 512)

    def __str__(self):
        return self.questionText
    def toList(self):
        return {"type": "Question", "id": self.id ,"author_id": self.author.id ,  "questionText":self.questionText }
