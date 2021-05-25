from django.urls import path
from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogDeleteView,
    BlogCreateView,
    AddCommentView,
)

urlpatterns = [
    path('blog/<int:pk>/comment/', 
     AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/edit/',
         BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/',
         BlogDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/',
         BlogDeleteView.as_view(), name='post_delete'),
    path('new/', 
        BlogCreateView.as_view(), name='post_new'),
    path('', 
        BlogListView.as_view(), name='post_list'),
]
