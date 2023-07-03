from django.urls import path
from .views import PostListView


urlpatterns = [
    path('posts', PostListView.as_view(), name='posts_list'),
]

# path(<url адресс>, <view>, name='<внутреннее имя маршрута>')
# .as_view() добавляется только когда используются встроенный view
