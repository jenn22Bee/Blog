from django.urls import path

from . import views

urlpatterns = [
    path('jennPage/', views.JennPageView.as_view(), name='jennPage'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.ReadArticle.as_view(), name='read_article'),

]
