from django.shortcuts import render
from django.views.generic.list import ListView

from translators.models import Novel


class HomePageView(ListView):
    template_name = 'home/index.html'
    model = Novel
        

# Create your views here.
