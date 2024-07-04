from django.contrib import admin
from .models import *

# Register your models here.
class RestroAdmin(admin.ModelAdmin):
    list_display=['firstnm','lastnm','email','what','phone','message']

@admin.register(Buff)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','image']

@admin.register(Chicken)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','image']
    
@admin.register(Veg)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','image']