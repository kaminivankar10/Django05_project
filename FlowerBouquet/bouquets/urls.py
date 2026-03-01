from django.urls import path
from bouquets import views

urlpatterns = [
    path("", views.home, name="home")
]