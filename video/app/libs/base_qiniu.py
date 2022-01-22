# -*- coding:utf-8 -*-

from qiniu import Auth, put_data, put_file
from django.conf import settings

class Qiniu(object):
    
    def __init__(self, buket_name, base_url):
        self.buket_name = buket_name
        self.base_url = base_url
        self.q = Auth(settings.QINIU_AK, settings.QINIU_SK)
        
    def put(self, name, path):
        token = self.q.upload_token(self.buket_name, name)
        ret, info = put_file(token, name, path)
        
        if 'key' in ret:
            remote_url = '/'.join([self.base_url, ret['key']])
        return remote_url
    
video_qiniu = Qiniu(buket_name=settings.QINIU_VIDEO, base_url=settings.QINIU_VIDEO_URL)
