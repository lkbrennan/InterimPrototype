from django.contrib import admin

from .models import Student, Teacher, Parent, Class,Quiz,Question,Results, School,teachesAt,\
        teachesClass,attendsClass,StudentAnswer, methodology

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(attendsClass)
admin.site.register(Class)
admin.site.register(teachesClass)
admin.site.register(Teacher)
admin.site.register(teachesAt)
admin.site.register(School)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(methodology)
admin.site.register(Results)

