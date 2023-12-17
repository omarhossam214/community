from django.shortcuts import render
import os
# Create your views here.



def title(request):
    title = os.path.basename(request.path)

    return {'title':title}