from django.shortcuts import render
# Create your views here.
from active.models import instructor


def index(request):

    
    return render(request,'index/index.html')
    