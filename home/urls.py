from django.urls import path

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.NovelListView.as_view(), name='novel_list'),
    path('novels/<int:pk>/', views.NovelDetailView.as_view(), name='novel_detail')
]