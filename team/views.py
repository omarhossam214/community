from django.shortcuts import render,get_object_or_404
from .models import Staff,Certifcation
# Create your views here.


def index(request):
    staff = Staff.objects.all()

    return render(request,'team/team.html',{'staff':staff})






def teamdetails(request, pk):
    
    staff = get_object_or_404(Staff, pk=pk)
    imgs = Certifcation.objects.filter(award_id=pk)
   

    return render(request,'mentor-detail/mentor-detail.html',{'staff':staff,'imgs':imgs})

   