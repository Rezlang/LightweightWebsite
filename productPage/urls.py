from django.urls import path
from productPage import views

urlpatterns = [
    path("", views.home, name="home"),
]