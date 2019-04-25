#!/usr/bin/env python
# coding=UTF-8
'''
@Author: JayLee
@Github: https://github.com/yoursjay
@LastEditors: Jay
@Date: 2019-04-17 14:41:06
@LastEditTime: 2019-04-24 14:49:00
'''
from django.shortcuts import render,get_object_or_404
from gallery.models import Gallery
from django.core.paginator import Paginator


def home(request):
    gallerys = Gallery.objects.all()
    paginator = Paginator(gallerys,9)
    page = request.GET.get('page',1)
    contents = paginator.page(page)
    return render(request,'home.html',{'gallerys':contents})


def pic_detial(request,gallery_pk):
    content = get_object_or_404(Gallery, pk=gallery_pk)
    return render(request,'pic_detial.html', {'gallery':content})

