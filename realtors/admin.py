from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_time', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    list_per_page = 2
    search_fields = ('name',)

admin.site.register(Realtor, RealtorAdmin)