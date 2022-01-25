# -*- coding:utf-8 -*-

from django.views import View
from django.shortcuts import reverse, redirect
from app.model.comment import Comment

class CommentsStatus(View):
    
    def get(self, request, comment_id, video_id):
        comment = Comment.objects.get(id=comment_id)
        
        comment.status = not comment.status
        comment.save()
        
        return redirect(reverse('dashboard_videosub', kwargs={'video_id': video_id}))
