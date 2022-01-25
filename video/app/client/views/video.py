# -*- coding:utf-8 -*-

from re import TEMPLATE
from django.views import View
from django.shortcuts import redirect, reverse, get_object_or_404
from app.libs.base_mako import render_to_response
from app.model.video import Video, FromType
from app.model.comment import Comment
from app.utils.permission import client_auth

class ExVideo(View):
    TEMPLATE = 'client/video/video.html'
    
    def get(self, request):
        data = {}
        videos = Video.objects.exclude(from_to = FromType.custom.value)
        data['videos'] = videos
        return render_to_response(request, self.TEMPLATE, data)

class CusVideo(View):
    TEMPLATE = 'client/video/video.html'
    
    def get(self, request):
        data = {}
        videos = Video.objects.filter(from_to = FromType.custom.value)
        data['videos'] = videos
        return render_to_response(request, self.TEMPLATE, data)


class VideoSub(View):
    TEMPLATE = 'client/video/video_sub.html'
    
    def get(self, request, video_id):
        data = {}
        video = get_object_or_404(Video, id=video_id)
        data['video'] = video
        
        user = client_auth(request)
        data['user'] = user
        
        comments = Comment.objects.filter(video=video, status=True).order_by('-id')
        data['comments'] = comments
        
        return render_to_response(request, self.TEMPLATE, data)
