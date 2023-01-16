from django.shortcuts import render
from . models import Blog

def blog(request):
    context = {}
    query = Blog.objects.all()
    context['query'] = query
    return render(request, 'blog.html', context)