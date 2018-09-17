from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('sign', views.sign, name='sign'),
    ]
