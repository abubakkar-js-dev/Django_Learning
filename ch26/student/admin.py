from django.contrib import admin
from student.models import Profile,Result

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','roll','email','city']

admin.site.register(Profile,ProfileAdmin);


# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('stu_id_id','email','marks')

# admin.site.register(Result,ResultAdmin);

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('stu_id_id','email','marks')

