from django.shortcuts import render

# Create your views here.

from .models import *

def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'category-detail.html')


