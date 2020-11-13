from django.shortcuts import render, redirect
from blogs.models import Blog
from dashboard.filters import BlogFilter
from dashboard.forms import BlogForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# View all blogs
def home(request):
    blogs = Blog.objects.filter(status = "Publish").order_by('-id')

    paginator = Paginator(blogs, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    return render (request, 'index.html', { 'bloglist' : blog_list })

# view single blog post
def blog(request ,slug):
    blogpage = Blog.objects.filter(slug=slug).first()
    
    return render (request, 'blogpage.html', {'blogpage': blogpage})

