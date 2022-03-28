from django.urls import path 
from . import views 

app_name='posts'
urlpatterns=[
    path('',views.PostListView.as_view(),name='all'),
    path('drafts/',views.DraftListView.as_view(),name='drafts'),

    path('/<int:pk>/detail',views.PostDetail.as_view(),name='detail'),
    path('/<int:pk>/edit',views.PostUpdate.as_view(),name='edit'),
    path('/<int:pk>/remove',views.DeletePost.as_view(),name='delete'),

    path('about',views.AboutView.as_view(),name='about'),
    path('new/',views.PostCreate.as_view(),name='new'),

    path('posts/<int:pk>/comment/',views.add_comment,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),

    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),

    path('<int:pk>/publish/',views.post_publish,name='post_publish'),





]