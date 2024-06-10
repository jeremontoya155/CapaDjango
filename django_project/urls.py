from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('inicio.urls')),
    path('estaticos/',include('estaticos.urls')),
    path('admin/', admin.site.urls),
    
]
