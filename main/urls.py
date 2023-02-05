
from django.urls import path

from main.views import index, category_detail

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),


]
