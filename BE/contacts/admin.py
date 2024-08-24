from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk','username', 'birthday', 'party_room_address')
    search_fields = ('username', 'party_room_address')
