"""ZForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path , re_path
from main.Form.formController import formRequestSwitcher, getAllUserForms
from main.Question.questionController import questionRequestSwitcher

urlpatterns = [
    path('forms/<int:form_id>',formRequestSwitcher),
    re_path(r'^forms$',getAllUserForms),
    path('questions/<int:question_id>' , questionRequestSwitcher)
]
