from django.contrib import admin
from homeapp.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','query']

admin.site.register(Contact,ContactAdmin)
