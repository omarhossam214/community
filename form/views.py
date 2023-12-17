from django.shortcuts import render,get_object_or_404
from courses.models import Course

# Create your views here.


def index(request):
    
    courses = Course.objects.all()

    return render(request,'form/form.html')

