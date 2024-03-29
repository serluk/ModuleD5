from django.urls import path
from .views import NewsList, NewsDetail, PostCreateView, PostDeleteView, UpdatePostView, PostSearch

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name="post_detail"),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', UpdatePostView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='search'),
]
