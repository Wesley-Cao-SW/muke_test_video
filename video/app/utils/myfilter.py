# -*- coding:utf-8 -*-

from django import template

register = template.Library()

@register.filter
def showtime(value):
    return value.strftime('%Y-%m-%d %H:%M:%S')