from django.urls import path
from .views import index, manager_dashboard,user_dashboard

urlpatterns = [
    path('', index, name='index'), 
    path('admin_manage/', manager_dashboard, name='admin_manage'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'), 
]
