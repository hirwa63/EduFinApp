from django.contrib import admin
from django.urls import path
from core.views import testing_view, health_check 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing', testing_view, name='testing'),
    path('health', health_check, name='health'),    
]