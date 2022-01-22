# -*- coding:utf-8 -*-

from django.http import request
from django.views import View
from app.libs.base_mako import render_to_response
from app.utils.permission import dashboard_auth

class Index(View):
    TEMPLATE = 'dashboard/index.html'
    
    @dashboard_auth
    def get(self, request):
        return render_to_response(request, self.TEMPLATE)