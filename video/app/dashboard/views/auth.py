# -*- coding:utf-8 -*-

from django import views
from django.views import View
from django.shortcuts import redirect, reverse
from app.libs.base_mako import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

# 登录
class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'
    
    def get(self, request):
        data = {}
        data['error'] = ''
        
        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        
        return render_to_response(request, self.TEMPLATE, data)
    
    def post(self, request):
        data={}
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        exists = User.objects.filter(username=username).exists()
        if not exists:
            data['error'] = "不存在该用户"
            return render_to_response(request, self.TEMPLATE, data)
        
        user = authenticate(username=username, password=password)
        
        if not user:
            data['error'] = "密码错误"
            return render_to_response(request, self.TEMPLATE, data)
        
        if not user.is_superuser:
            data['error'] = "没有对应权限"
            return render_to_response(request, self.TEMPLATE, data)
        
        login(request, user)

        return redirect(reverse('dashboard_index'))
   
# 注销 
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('dashboard_login'))
 
# 管理员分页显示   
class AdminManger(View):
    TEMPLATE = 'dashboard/auth/admin.html'
    
    def get(self, request):
        data = {}
        # users = User.objects.filter(is_superuser=True)
        page = request.GET.get('page',1)
        users = User.objects.all()
        p = Paginator(users, 1)
        total_page = p.num_pages
        
        if int(page) <= 1:
            page = 1
        
        current_page_obj = p.get_page(int(page)).object_list
        
        data['users'] = current_page_obj
        data['total'] = total_page
        data['current_page'] = int(page)
        return render_to_response(request, self.TEMPLATE, data)

# 更新管理员权限
class UpdateAdminStatus(View):
    
    def post(self, request):
        data = {}
        status = request.POST.get('status')
        user_id = request.POST.get('user_id')
        
        if not status:
            data['error'] = 'status不存在'
            return redirect(reverse('dashboard_admin'), data)
        
        if not user_id:
            data['error'] = '用户已不存在'
            return redirect(reverse('dashboard_admin'), data)
            
        user = User.objects.filter(id=user_id).first()
        
        if status == 'on':
            user.is_superuser = True
            user.save()
        elif status == 'off':
            user.is_superuser = False
            user.save()
        
        return redirect(reverse('dashboard_admin'))
        
    