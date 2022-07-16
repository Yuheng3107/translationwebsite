from django.shortcuts import render
from django.http import HttpResponse
from .models import Novel

from django.views.generic.list import ListView

class IndexView(ListView):
    model = Novel

def index(request):
    return TemplateResponse(request, "translators/index.html")


class NovelFormView()

