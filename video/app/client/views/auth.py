# -*- coding:utf-8 -*-

from genericpath import exists
from re import TEMPLATE
from urllib import response
from django.views import View
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from app.libs.base_mako import render_to_response
from app.utils.permission import client_auth
from app.utils.consts import COOKIE_NAME
from app.model.auth import ClientUser

class User(View):
    TEMPLATE = 'client/auth/user.html'
    
    def get(self, request):
        data = {}
        user = client_auth(request)
        data['user'] = user
        
        return render_to_response(request, self.TEMPLATE, data)
    
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        
        if not all([username, password]):
            error = '缺少必要信息'
            return JsonResponse({'code': -1, 'msg': error})
        
        user = ClientUser.get_user(username, password)
        
        if not user:
            error = '用户名或者密码错误'
            return JsonResponse({'code': -1, 'msg':error})
        
        response = render_to_response(request, self.TEMPLATE)
        response.set_cookie(COOKIE_NAME, str(user.id))
        return response

class Regist(View):
    
    def post(self, request):
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        
        if not all([username, password]):
            error = '缺少必要信息'
            return JsonResponse({'code': -1, 'msg': error})
        
        exists = ClientUser.objects.filter(username=username).exists()
        
        if exists:
            error = '该用户已存在'
            return JsonResponse({'code': -1, 'msg': error})
        
        ClientUser.add(username=username, password=password)
        return JsonResponse({'code': 0, 'msg': '注册成功'})

class Logout(View):
    TEMPLATE = 'client/auth/user.html'
    
    def get(self, request):
        response = render_to_response(request, self.TEMPLATE)
        response.set_cookie(COOKIE_NAME, '')
        return response
