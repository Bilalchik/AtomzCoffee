from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('news-detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('send-mail/', views.SendEmailMessage.as_view(), name='send-mail')
]
