from django.contrib import admin
from .models import CustomUser

#admin.site.register(CustomUser)

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','username','email','birthday')
    search_fields = ('pk','username')

admin.site.register(CustomUser,UserAdmin)
