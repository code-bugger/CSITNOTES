from django.shortcuts import render
from .models import item

# Create your views here.
def home(request):
    model=item.objects.all()
    return render(request,'subject.html',{'model':model})