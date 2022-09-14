from django.urls import path, include
from . import views


urlpatterns= [
    path('auth/', include('djoser.urls')),
    path("create/", include('djoser.urls.jwt')),
    path("login/", views.login_view, name= 'login'),
    path("logout/", views.logout_view, name= 'logout')
]