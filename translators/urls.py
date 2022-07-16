from django.urls import path

from . import views

app_name = 'translators'
urlpatterns = [
    path('', views.NovelListView.as_view(), name='novel_list'),
    path('addnovel', views.NovelFormView.as_view(), name='novel_form')
]

