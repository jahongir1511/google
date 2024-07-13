from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_home, name='home'),  # Bosh sahifaga otadi
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
]
