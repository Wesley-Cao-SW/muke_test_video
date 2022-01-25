# -*- coding:utf-8 -*-

from django.db import models
from .auth import ClientUser
from .video import Video


class Comment(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=True, db_index=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_name='comment_video', blank=True, null=True)
    user = models.ForeignKey(ClientUser, on_delete=models.SET_NULL, related_name='comment_user', blank=True, null=True)
    
    def __str__(self):
        return self.content
    
    def data(self):
        return {
            'id': self.id,
            'content': self.content,
            'videoId': self.video.id,
            'userId': self.user.id,
            'username': self.user.username,
        }
