# -*- coding:utf-8 -*-

from django.urls import path
from .views.base import Index
from .views.auth import Login, Logout, AdminManger, UpdateAdminStatus
from .views.video import ExternalVideo

urlpatterns = [
    path('index', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('logout', Logout.as_view(), name='dashboard_logout'),
    path('index/admin', AdminManger.as_view(), name='dashboard_admin'),
    path('index/admin/update/status', UpdateAdminStatus.as_view(), name='dashboard_admin_update_status'),
    path('index/externalvideo', ExternalVideo.as_view(), name='dashboard_externalvideo'),
]
