#-*- coding:utf-8 -*-
from django.shortcuts import render

def main_page(request):
    vue = 'index.html'
    return render(request, vue)
