from atexit import register
from django import template
register = template.Library()

@register.simple_tag
def prefix_tag(cur_str):
    """自定义简单标签"""
    return "hello {}".format(cur_str)

@register.filter
def replace_django(value):
    """自定义过滤器"""
    return value.replace("django", "Django")