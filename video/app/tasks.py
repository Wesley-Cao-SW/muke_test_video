# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import time
# from celery import task
 
from celery import shared_task

from app.libs.base_qiniu import video_qiniu
from app.models import Video, VideoSub

@shared_task
def video_task(command, out_path_name, out_name, video_file_name, path_name, videosub_id):
    from app.utils.common import remove_paths
    # 转码后临时保存到本地
    os.system(command)
    
    put_path = '.'.join([out_path_name, 'mp4'])
    if not os.path.exists(put_path):
        # 删除本地临时保存的视频文件
        remove_paths([put_path, out_name])
        return False
    
    final_name = '{}_{}'.format(int(time.time()), video_file_name)
    url = video_qiniu.put(final_name, put_path)
    

    if url:
        try:
            video_sub = VideoSub.objects.get(id = videosub_id)
            video_sub.url = url
            video_sub.save()
            return True
        except:
            return False
        finally:
            remove_paths([put_path, path_name])
    return False
