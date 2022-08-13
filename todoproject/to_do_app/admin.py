from django.contrib import admin

# Register your models here.
from .models import  ToDo
# admin.site.register(ToDo)

@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'finishdate', 'user')
    list_display_links = ('title','status')
    search_fields = ("title",)
    list_filter = ('status','finishdate')

    class Meta:
        model = ToDo
