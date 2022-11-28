from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login", views.login, name="login"),
    path("registrarse", views.registrarse , name="registrarse"),
]

