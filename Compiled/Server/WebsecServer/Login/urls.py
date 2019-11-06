from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ShowLoginPage, name="ShowLoginPage"),
    path('phone/', views.SmartphoneLogin, name="SmartphoneLogin"),
]