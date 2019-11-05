from django.urls import path

from book import views

urlpatterns = [
    path('', views.HomeView.as_view()),
]
