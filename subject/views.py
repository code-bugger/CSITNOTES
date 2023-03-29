from django.shortcuts import render
from .models import item

# Create your views here.
def home(request,value):
    model=item.objects.all().filter(Semester=value)
    return render(request,'subject.html',{'model':model})

def explore(request,hero):
    model=item.objects.all().filter(id=hero)
    return render(request,'contents.html',{'modela':model})

def chapter(request,zero):
    modela=item.objects.all().filter(Sem_Subject=zero)
    return render(request,'chapter.html',{'modela':modela})