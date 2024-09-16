from django.contrib import admin
from .models import message , cake_custom

# Register your models here.

@admin.register(cake_custom)
class CakeCustomAdmin (admin.ModelAdmin):
    list_display = ('party',)
    search_fields = ('party',)

@admin.register(message)
class MessageAdmin (admin.ModelAdmin):
    list_display = ('pk','party','sent_by')
    search_fields = ('party',)