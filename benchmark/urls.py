from django.urls import path

from . import views

urlpatterns = [
    path("api/", views.api),
    path("async_api/", views.async_api),
]
