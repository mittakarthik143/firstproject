from django.shortcuts import render
from studentapp.models import student

def home(request):
    return render(request,'index.html')

def studentInfo(request):
    s_list=student.objects.all()
    my_dict={'s_list':s_list}
    return render(request,'studentinfo.html',context=my_dict)


