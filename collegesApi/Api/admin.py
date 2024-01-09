from django.contrib import admin
from Api.models import CollegeModel,StudentModel

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name','type','college_for','state')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    
    list_display=('firstName','lastName','gender','dateOfBirth','emailId','address')
    search_fields = ('firstName',)

admin.site.register(CollegeModel,CollegeAdmin)
admin.site.register(StudentModel,StudentAdmin)