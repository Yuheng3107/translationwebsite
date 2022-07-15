from django.contrib import admin

from .models import Genre, WordType, Novel

admin.site.register(Genre)
admin.site.register(WordType)
admin.site.register(Novel)
# Register your models here.
