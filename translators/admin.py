from django.contrib import admin

from .models import Genre, WordType, Novel, Chapter

admin.site.register(Genre)
admin.site.register(WordType)
admin.site.register(Novel)
admin.site.register(Chapter)
# Register your models here.
