from django.urls import path
from . import views

urlpatterns=[
    path('login',views.user_login,name='login'),
    path('registration',views.register,name='registration'),
    path('logout',views.logout_user,name='logout_user'),
]