# coding:utf-8
from django.shortcuts import render
from models import Question,Choices
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    Ques=Question.objects.all()
    Ques1=Question.objects.all()
    return render(request,'index.html',locals())



def show(request,id):
    que=Question.objects.get(pk=id)
    choice_biao=que.choices_set
    chos=choice_biao.all()
    con={'Ques':que,'Chos':chos}
    return render(request,'show.html',con)

def showAction(request,id):
    que=Question.objects.get(pk=id)
    choice_biao=que.choices_set
    chos=choice_biao.all()
    try:
        num=request.POST.getlist('checkboxs')
    except (KeyError,Choices.DoesNotExist):
        return render(request,'show.html',{'Chos':chos,'Ques':que,'myERROR':'你没有选中选项，重选'})
    for x in num:
        target=choice_biao.get(pk=x)
        target.vote+=1
        target.save()
    que=Question.objects.get(pk=id)
    return render(request,'showresult.html',{'Que':que})


def index2(req,id):
    pass