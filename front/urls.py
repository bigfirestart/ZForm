from django.contrib import admin
from django.urls import path , include ,re_path
from front.views import questionView,index ,sendTestEmail
urlpatterns = [
    path('', index),
    path('questions/<int:question_id>', questionView , name = 'question'),
    path('stm',sendTestEmail, name = "sendTestEmail")
]
