from django.contrib import admin
from .models import Task,Summary,User

# Register your models here.

class TaskList(admin.ModelAdmin):
    list_display = ('Title','Description','Status','Author','Created_Date','Due_Date')
    list_filter = ('Title','Author')
    search_fields = ('Title','Author')
    ordering = ['Status']


class SummaryList(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'Status')
    list_filter = ('Title','Author')
    search_fields = ('Title', 'Author')
    ordering = ['Status']

class UserList(admin.ModelAdmin):
    list_display = ("User_name", "First_name", "Last_name", "Email")
    list_filter = ("First_name", "Last_name")
    search_field = ("First_name", "Last_name")
    ordering = ['User_name']

admin.site.register(Task, TaskList)
admin.site.register(Summary, SummaryList)
admin.site.register(User, UserList)


