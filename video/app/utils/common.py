#  -*- coding:utf-8 -*-

def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)
    except:
        return {'code': -1, 'msg': message}
    
    return {'code': 0, 'msg': 'success'}