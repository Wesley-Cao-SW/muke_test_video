# -*- coding:utf-8 -*-

from django.urls import path
from .views.base import Index
from .views.video import ExVideo, VideoSub, CusVideo
from .views.auth import User, Regist, Logout
from .views.comment import CommentView

urlpatterns = [
    path('index', Index.as_view(), name='client_index'),
    path('index/exvideo', ExVideo.as_view(), name='client_exvideo'),
    path('index/videosub/<int:video_id>', VideoSub.as_view(), name='client_video_sub'),
    path('index/cusvideo', CusVideo.as_view(), name='client_cusvideo'),
    path('index/user', User.as_view(), name='client_user'),
    path('index/regist', Regist.as_view(), name='client_user_regist'),
    path('index/logout', Logout.as_view(), name='client_user_logout'),
    path('index/comment/add', CommentView.as_view(), name='client_add_comment'),
]
