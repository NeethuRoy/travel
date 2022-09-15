from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import travel_des, travel_mate


def index(request):
    obj=travel_des.objects.all()
    obj1=travel_mate.objects.all()
    return render(request, "index.html",{'result':obj,'output':obj1})