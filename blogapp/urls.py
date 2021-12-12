from django.contrib import admin
from django.urls import path
from .views import HomeView,DetailView,AddPostView,UpdatePostView,DeletePostView
app_name='blogapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='index'),
    path('article/<int:pk>',DetailView.as_view(),name='detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update'),
    path('article/remove/<int:pk>',DeletePostView.as_view(),name='delete')
]