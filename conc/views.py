# coding: utf-8
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.

@cache_page(5)  # 单位:秒
def index(request):
    return render(request, 'conc/index.html')
