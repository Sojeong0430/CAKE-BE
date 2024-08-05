from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'd_day', 'party_room_address')
    search_fields = ('name', 'party_room_address')
    list_filter = ('birthday', 'd_day')
