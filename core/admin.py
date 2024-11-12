from django.contrib import admin

from .models import *

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
   list_display =[ 'id','username','email','password']
