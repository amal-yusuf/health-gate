from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('upvote/<slug:slug>', views.PostUpVote.as_view(), name='post_upvote'),
    path('downvote/<slug:slug>', views.PostDownVote.as_view(), name='post_downvote'),
    path('post/<int:slug>/comment/reply/<int:slug1>', views.CommentReply.as_view(), name='comment_reply'),
]