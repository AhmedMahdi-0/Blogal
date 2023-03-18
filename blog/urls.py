from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.HomeTemplateView.as_view(), name='home-page'),
    path('posts', views.PostsListView.as_view(), name='all-posts'),
    path('posts/read-later', views.ReadLaterView.as_view(),name='readlater'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='post-detail')
] 

