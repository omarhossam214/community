from django.shortcuts import render
# Create your views here.



def index(request):
    
    return render(request,'course-detail/course-detail.html')
    