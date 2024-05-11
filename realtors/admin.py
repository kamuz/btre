from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_time')
    list_display_links = ('id', 'name')
    list_per_page = 2
    search_fields = ('name',)

admin.site.register(Realtor, RealtorAdmin)