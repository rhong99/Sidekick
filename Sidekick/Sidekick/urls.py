from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Sidekick.Home.urls')),
    path('user/', include('Sidekick.User.urls')),
]
