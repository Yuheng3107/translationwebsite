from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from translators.models import Novel, Genre


class NovelListView(ListView):
    template_name = 'home/novel_list.html'
    model = Novel

    def get(self, request):
        novels = Novel.objects.all()
        genre_list = []
        for novel in novels:
            genres = [genre for genre in Genre.objects.all() if genre in novel.genres.all()]
            genre_list.append(genres)
        
        data = zip(novels, genre_list)
        ctx = {'data': data}
        print(data)
        return render(request, self.template_name, ctx)


class NovelDetailView(DetailView):
    template_name = 'home/novel_detail.html'
    model = Novel
    def get(self, request, pk):
        novel = Novel.objects.get(id=pk)
        genres = [genre for genre in Genre.objects.all() if genre in novel.genres.all()]
        ctx = {'novel': novel, 'genres': genres}
        return render(request, self.template_name, ctx)
    
