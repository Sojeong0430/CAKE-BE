from django.contrib import admin
from django.urls import path, include
from accounts.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('accounts/', include('accounts.urls')),
    path('cakes/', include('cakes.urls')),
    path('contacts/', include('contacts.urls')),
]
