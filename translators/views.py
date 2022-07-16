from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Novel
from .forms import NovelForm

from django.views.generic.list import ListView
from django.views import View

class IndexView(ListView):
    model = Novel

def index(request):
    return render(request, "translators/index.html")

class NovelFormView(View):

    template_name = "translators/novel_form.html"
    success_url = reverse_lazy('translators:index')
    def get(self, request):
        form = NovelForm()
        ctx = {"form": form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = NovelForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template_name, ctx)

        novel = form.save()
        return redirect(self.success_url)




