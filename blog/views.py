from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.

def blog_page(request):
    blogs = Blog.objects.get_queryset().order_by('id')
    paginator = Paginator(blogs,9)
    page = request.GET.get('page',1)
    contents = paginator.page(page)
    return render(request,'blog.html',{'contacts':contents})

def blog_detial(request,blog_pk):
    content = get_object_or_404(Blog, pk=blog_pk)
    return render(request,'detial.html', {'blog':content})

