# -*- coding:utf-8 -*-

from django.views import View
from django.http import JsonResponse
from django.shortcuts import reverse
from app.model.comment import Comment
from app.model.video import Video
from app.model.auth import ClientUser

class CommentView(View):
    
    def post(self, request):
        data = {}
        
        content = request.POST.get('content','')
        userId = request.POST.get('userId', '')
        videoId = request.POST.get('videoId', '')
        
        if not all([content, userId, videoId]):
            return JsonResponse({'code': -1, 'msg': '缺少必要字段'})
        
        video = Video.objects.get(id=videoId)
        user = ClientUser.objects.get(id=userId)
        
        comment = Comment.objects.create(content=content, video=video, user=user)

        data['comment'] = comment.data()
        
        return JsonResponse({'code': 0, 'msg': 'success', 'data': data})
