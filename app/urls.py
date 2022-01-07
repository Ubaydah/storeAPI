from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', Register.as_view()),
    path('update_user/<str:pk>/', UpdateUser.as_view()),
    path('login/', Login.as_view()),
    path('change_password/<int:pk>/', ChangePassword.as_view()),
]