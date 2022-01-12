# -*- coding:utf-8 -*-

from enum import Enum, unique
from django.db import models
from django.db.models.deletion import SET_NULL
from datetime import timedelta

class VideoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    episode = 'episode'
    variety = 'variety'
    other = 'other'
    
VideoType.movie.label = '电影'
VideoType.cartoon.label = '动漫'
VideoType.episode.label = '剧集'
VideoType.variety.label = '综艺'
VideoType.other.label = '其他'

class FromType(Enum):
    youku = 'youku'
    custom = 'custom'
    
FromType.youku.label = '优酷'
FromType.custom.label = '自制'

class NationalityType(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    america = 'america'
    other = 'other'
    
NationalityType.china.label = '中国'
NationalityType.japan.label = '日本'
NationalityType.korea.label = '韩国'
NationalityType.america.label = '美国'
NationalityType.other.label = '其他'

class IdentityType(Enum):
    to_star = 'to_star'
    supporting_rule = 'supporting_rule'
    director = 'director'
    
IdentityType.to_star.label = '主演'
IdentityType.supporting_rule.label = '配角'
IdentityType.director.label = '导演'

class Video(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=500, default='')
    video_type = models.CharField(max_length=50, default=VideoType.other.value)
    from_to = models.CharField(max_length=20, null=False, default=FromType.custom.value)
    nationality = models.CharField(max_length=20, default=NationalityType.other.value)
    info = models.TextField()
    status = models.BooleanField(default=True, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('name', 'video_type', 'from_to', 'nationality')
        
    def __str__(self):
        return f'name:{self.name}\nvideo_type:{self.video_type}\nfrom_to:{self.from_to}\nnationality:{self.nationality}'
    
    def utc_to_local(self, utc_time):
        time = utc_time + timedelta(hours=8)
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        return time
    
class VideoStar(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_name='video_star', blank=True, null=True)
    name = models.CharField(max_length=100, null=False)
    identity = models.CharField(max_length=50, default='')
    
    class Meta:
        unique_together = ('video', 'name', 'identity')
        
    def __str__(self):
        return f'video:{self.video}\nname:{self.name}\nidentity:{self.identity}'
    
class VideoSub(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_name='video_sub', blank=True, null=True)
    url = models.CharField(max_length=500, null=False)
    number = models.IntegerField(default=1)
    
    class Meta:
        unique_together = ('video', 'number')

    def __str__(self) -> str:
        return f'video:{self.video}\nnumber:{self.number}'
