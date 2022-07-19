from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Novel, Chapter
from .forms import NovelForm
from .parsing_stuff.parser import parse

from django.views.generic.list import ListView
from django.views import View

def insert_chapters(book_name, chapter_names, chapter_contents):
    novel = get_object_or_404(Novel, title=book_name)
    data = zip(chapter_names, chapter_contents)
    for name, content in data:
        print(name)
        chapter = Chapter(name=name, novel=novel, content=content)
        chapter.save()
    return


def index(request):
    return render(request, "translators/index.html")
class NovelListView(ListView):
    template_name = "translators/novel_list.html"
    context_object_name = "novels"
    model = Novel

class NovelFormView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "translators/novel_form.html"
    success_url = reverse_lazy('translators:novel_list')
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
        novel.save()
        form.save_m2m()
    
        book_name = novel.raws.name
        chapter_names, chapter_content = parse(book_name)
        chapter_names = [chapter_name.strip() for chapter_name in chapter_names]
        insert_chapters(novel.title, chapter_names, chapter_content)
        return redirect(self.success_url)

def stream_file(request, pk):
    novel = get_object_or_404(Novel, id=pk)
    response = HttpResponse()
    response['Content-Type'] = novel.content_type
    response['Content-Length'] = len(novel.picture)
    response.write(novel.picture)
    return response




