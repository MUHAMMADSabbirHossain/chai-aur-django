from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/update/', views.tweet_update, name='tweet_update'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
]
