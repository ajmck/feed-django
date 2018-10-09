from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.leaflet, name="leaflet"),   # primary link, but 'map' shadows the python function
    path('leaflet', views.leaflet, name="leaflet"),
    path('here', views.here, name="here"),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/up', views.post_vote_up, name='post_vote_up'),
    path('<int:post_id>/down', views.post_vote_down, name='post_vote_down'),
    path('<int:post_id>/reset', views.post_vote_reset, name='post_vote_reset'),
    path('c/<int:comment_id>/up', views.comment_vote_up, name='comment_vote_up'),
    path('c/<int:comment_id>/down', views.comment_vote_down, name='comment_vote_down'),
    path('c/<int:comment_id>/reset', views.comment_vote_reset, name='comment_vote_reset'),
    path('classic', views.classic, name='classic'),
    path('about', views.about, name='about'),
]
