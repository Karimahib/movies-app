from django.urls import path
from . import views

urlpatterns = [
    path("", views.video_list, name="video_list"),
    path("new/", views.video_create, name="video_create"),
    path("<str:movie_id>/", views.video_detail, name="video_detail"),
    path("<str:movie_id>/edit/", views.video_update, name="video_update"),
    path("<str:movie_id>/delete/", views.video_delete, name="video_delete"),
]
