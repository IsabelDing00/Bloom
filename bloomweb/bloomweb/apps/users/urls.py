from django.urls import path, include
from . import views

urlpatterns = [
    # users
    path('register/', views.registerView),
    path('login/', views.LoginView),
]


