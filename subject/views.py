from django.shortcuts import render
from .models import Subject,Note,Question
# Create your views here.


def home(request):
    return render(request,'index.html')

def subject(request,value):
    model=Subject.objects.all().filter(semester=value)
    return render(request,'subject.html',{'model':model})

def explore(request,hero):
    model=Note.objects.all().filter(Subject_Name=hero)
    modela=Question.objects.all().filter(Subject_Name=hero)
    return render(request,'chapter.html',{'model':model,'modela':modela})

def searchbar(request):
    if request.method=="GET":
        val=request.GET.get('search')
        model=Note.objects.filter(Chapter__contains=val)
    return render(request,'Search.html',{'model':model})
