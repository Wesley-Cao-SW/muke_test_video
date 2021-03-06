# -*- coding:utf-8 -*-

from os import name
from django.urls import path
from .views.base import Index
from .views.auth import Login, Logout, AdminManger, UpdateAdminStatus, ClientManager
from .views.video import ExternalVideo, VideoSubView, VideoStarView, StarDelet, SubDelet, VideoUpdate, VideoStatusUpdate
from .views.comments import CommentsStatus

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
    path('index/externalvideo/update/<int:video_id>', VideoUpdate.as_view(), name='dashboard_externalvideo_update'),
    path('index/externalvideo/statusupdate/<int:video_id>', VideoStatusUpdate.as_view(), name='dashboard_externalvideo_statusupdate'),
    path('index/video/comments/status/<int:comment_id>/<int:video_id>', CommentsStatus.as_view(), name='dashboard_comment_status'),
    path('index/clientuser', ClientManager.as_view(), name='dashboard_client_user'),
]
