from django.contrib import admin
from studentapp.models import student

class studentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dob','marks','email','phone','address']

admin.site.register(student,studentAdmin)

