from . import views
from django.urls import path
from blog import views as v

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('upload/', views.image_upload_view)
    path('photo/create/', v.photo_create, name='photo_create'),
]
