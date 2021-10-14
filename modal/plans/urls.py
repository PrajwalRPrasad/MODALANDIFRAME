from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    #index-home page, calling other functions using same name as defined in views
    
    
    path('', views.stream, name="stream"),
       
]
