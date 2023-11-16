from . import views
from django.urls import path


urlpatterns = [
    path("api", views.index, name="index"),
    path("senddata", views.receiveData, name="index"),
]
