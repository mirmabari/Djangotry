from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'mir'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('post/new/', views.new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('file',views.csvf,name="csv"),
    path('dbfile',views.getfile,name="csvdb"),
    path('pdf',views.getpdf),
    path('email',views.email),
    path('register',views.register),
    path('reglist',views.regget),
]
