from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('public.urls')),
    path('user/', include('authuser.urls')),
    path('company/', include('company.urls')),
    path('inventory/', include('inventory.urls')),
    path('repair/', include('repair.urls')),
]
