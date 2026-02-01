from django.shortcuts import render
from core.models import *

def home(request):
    partners = Partner.objects.order_by("-id")
    blogs = Blog.objects.order_by("-id")
    context = {
        'partners': partners,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)