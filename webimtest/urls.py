from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_redirect),
    path('fivefriends/', include('fivefriends.urls'))
]
