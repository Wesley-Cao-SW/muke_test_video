# -*- coding:utf-8 -*-

import functools
from django.shortcuts import redirect, reverse
from app.models import ClientUser
from .consts import COOKIE_NAME

def dashboard_auth(func):
    
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):
        user = request.user
        
        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('dashboard_login'), request.path))
        
        return func(self, request, *args, **kwargs)
    return wrapper

# 判断是否登录
def client_auth(request):
    
    value = request.COOKIES.get(COOKIE_NAME)
    
    if not value:
        return None
    
    user = ClientUser.objects.get(id=value)
    
    if user and user.status:
        return user
    else:
        return None
