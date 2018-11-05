from django.shortcuts import render
from empapp.models import employee

def home(request):
    return render(request,'home.html')

def emp(request):
    e_list=employee.objects.all()
    my_dict={'e_list':e_list}
    return render(request,'employee.html',context=my_dict)

