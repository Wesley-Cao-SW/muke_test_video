# -*- coding:utf-8 -*-

from django.urls import path
from .views.base import Index
from .views.auth import Login, Logout, AdminManger, UpdateAdminStatus
from .views.video import ExternalVideo, VideoSubView, VideoStarView, StarDelet, SubDelet

urlpatterns = [
    path('index', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('logout', Logout.as_view(), name='dashboard_logout'),
    path('index/admin', AdminManger.as_view(), name='dashboard_admin'),
    path('index/admin/update/status', UpdateAdminStatus.as_view(), name='dashboard_admin_update_status'),
    path('index/externalvideo', ExternalVideo.as_view(), name='dashboard_externalvideo'),
    path('index/externalvideo/videosub/<int:video_id>', VideoSubView.as_view(), name='dashboard_videosub'),
    path('index/externalvideo/star', VideoStarView.as_view(), name='dashboard_star'),
    path('index/externalvideo/star/delete/<int:star_id>/<int:video_id>', StarDelet.as_view(), name='dashboard_star_delete'),
    path('index/externalvideo/sub/delete/<int:sub_id>/<int:video_id>', SubDelet.as_view(), name='dashboard_sub_delete'),
]
