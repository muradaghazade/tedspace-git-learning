from django.shortcuts import render
from core.models import *
from core.forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        
    partners = Partner.objects.order_by("-id")
    blogs = Blog.objects.order_by("-id")
    form = ContactForm()
    context = {
        'partners': partners,
        'blogs': blogs,
        'form': form
    }
    return render(request, 'index.html', context)