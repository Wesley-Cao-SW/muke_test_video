# -*- coding:utf-8 -*-

from re import TEMPLATE
from django.views import View
from django.shortcuts import redirect, reverse

class Index(View):
    TEMPLATE = 'client/index.html'

    def get(self, request):
        
        return redirect(reverse('client_exvideo'))