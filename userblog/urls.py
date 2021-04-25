from django.urls import path
from .views import PostViev, ListUsers, UserBlogViev, CreatePost, PostID

urlpatterns = [
    path('', PostViev.as_view()),
    path('<int:pk>', PostID.as_view()),
    path('create/', CreatePost.as_view()),
    path('users/', ListUsers.as_view()),
    path('users/<str:name>', UserBlogViev.as_view()),
    ]
