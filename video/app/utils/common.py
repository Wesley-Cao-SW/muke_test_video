#  -*- coding:utf-8 -*-
from genericpath import exists
import os
import time
import shutil
from django.conf import settings
from app.libs.base_qiniu import video_qiniu
from app.models import VideoSub, Video
from app.tasks import video_task

def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)
    except:
        return {'code': -1, 'msg': message}
    
    return {'code': 0, 'msg': 'success'}

def remove_paths(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

def handle_video(video_file, video_id, number):
    path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp')
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([path, name])
    
    temp_path = video_file.temporary_file_path()
    # 临时保存到本地
    shutil.copyfile(temp_path, path_name)
    
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_out')
    out_name = '{}_{}'.format(int(time.time()), video_file.name.split('.')[0])
    out_path_name = '/'.join([out_path, out_name])
    
    command = 'ffmpeg -i {} -c copy {}.mp4'.format(path_name, out_path_name)
    
    video = Video.objects.get(id=video_id)
    videosub = VideoSub.objects.create(
        video = video,
        url = '',
        number = number,
    )
    
    video_task.delay(command, out_path_name, out_name, video_file.name, path_name, videosub.id)
    