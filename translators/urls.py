from django.urls import path

from . import views

app_name = 'translators'
urlpatterns = [
    path('', views.NovelListView.as_view(), name='novel_list'),
    path('addnovel', views.NovelFormView.as_view(), name='novel_form'),
    path('novel_picture/<int:pk>', views.stream_file, name='novel_picture'),
    path('chapter/<int:novel_pk>/<int:chapter_pk>', views.TranslateView.as_view(), name='chapter_view'),
]

