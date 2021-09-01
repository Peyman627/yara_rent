from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/', include('rent.urls')),
    path('users/', include('users.urls')),
]
