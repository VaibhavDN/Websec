from django.urls import path, include
from . import views

urlpatterns = [
    path('user/',views.ShowLoginPageUser, name="ShowLoginPageUser"),
    path('admin/',views.ShowLoginPageAdmin, name="ShowLoginPageAdmin",),
]