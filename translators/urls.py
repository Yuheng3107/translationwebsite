from django.urls import path

from . import views

app_name = 'translators'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addnovel', views.NovelFormView.as_view(), name='novel_form')
]

