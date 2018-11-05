from django.contrib import admin
from empapp.models import employee

class employeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadd']

admin.site.register(employee,employeeAdmin)
