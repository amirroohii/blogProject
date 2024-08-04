from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostsView.as_view()),
    path('<int:pk>/', views.PostRetrieveView.as_view(), name='post-detail'),
    path('author-post/', views.ListPostForAuthorView.as_view()),
    path('author-post/detail/', views.author_posts_detail)
]

