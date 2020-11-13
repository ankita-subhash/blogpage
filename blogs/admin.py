from django.contrib import admin
from blogs.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status', 'Date')
 
admin.site.register(Blog, PostAdmin)

# Register your models here.
