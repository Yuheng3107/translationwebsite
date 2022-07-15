from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    #path('/novels', views.NovelListView.as_view(), name='novel_list'),
    #path('novels/<str:novel_title>/', views.NovelDetailView.as_view(), name='novel')
]