from django.urls import path
# from .views import PostListView, PostDetailView, PostCreateView
from .views import *


urlpatterns = [
    path('posts', PostListView.as_view(), name='posts_list'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_create', PostCreateView.as_view(), name='post_create'),
    path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('post_update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
]


# path(<url адресс>, <view>, name='<внутреннее имя маршрута>')
# .as_view() добавляется только когда используются встроенный view
