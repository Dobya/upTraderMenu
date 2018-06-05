from django.contrib import admin
from .models import *
# Register your models here.

class menuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "menu")
    list_filter = ("menu",)

admin.site.register(menu)
admin.site.register(menuItem, menuItemAdmin)