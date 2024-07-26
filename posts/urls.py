from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsView.as_view()),
    path('<int:pk>/', views.PostRetrieveView.as_view()),

]
