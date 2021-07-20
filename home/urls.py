from django.urls import path

from . import views

urlpatterns = [
    path('addPost/', views.AddPostView.as_view(), name='addPost'),
    path('jennPage/', views.JennPageView.as_view(), name='jennPage'),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='deletePost'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.ReadArticle.as_view(), name='read_article'),

]
