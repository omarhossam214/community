from django.shortcuts import render
# Create your views here.

from .models import Teacher


def index(request):
    teachers = Teacher.objects.all()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    context = {'teachers': teachers, 'days_of_week': days_of_week}
    return render(request, 'timtable/timtable.html', context)