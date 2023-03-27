from django.shortcuts import render
from .models import item

# Create your views here.
def home(request):
    model=item.objects.all()
    return render(request,'subject.html',{'model':model})

def see(request,value):
    model=item.objects.all().filter(Semester=value)
    return render(request,'subject.html',{'model':model})