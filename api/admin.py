from django.contrib import admin
from api.models import student

# @admin.register(student)
# class Admin(admin.ModelAdmin):
#     list_display=['roll','name','city']
    
    
# admin.site.register(student) 
class sjg(admin.ModelAdmin):
    list_display = ('roll','name','city','id')

admin.site.register(student,sjg)



 
# 

# Register your models here.
