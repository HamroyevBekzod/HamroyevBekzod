from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'about',
        'price',
        'duration',
        'image',
        'phone',
    )

    list_display = ['title','about','price','duration','image','phone']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'level',
        'about',
        'phone',
    )

    list_display = ['name', 'image', 'level', 'about', 'phone']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = (
        'picture',
        'title',
        'about',
        'vidio',
    )  

    list_display = ['picture', 'title', 'about', 'vidio']

@admin.register(Level)
class LevelAdmin(admin.Model.Admin):
    fields = (
        'lider',
    )    

    list_display = ['lider']

@admin.register(Students)
class StudentsAdmin(admin.Model.Admin):
    fields = (
        'fullname',
        'email',
        'number',
        'extnumber',
        'day',
        'stu_day',
    )    

    list_display = ['fullname', 'email', 'number', 'extnmber', 'day', 'stu_day']

@admin.register(Contact)
class ContactAdmin(admin.Model.Admin):
    fields = (
        'tel_nomer',
        'email',
        'level',
        'message',
    )    

    list_display = ['tel_nomer', 'email', 'level', 'message']