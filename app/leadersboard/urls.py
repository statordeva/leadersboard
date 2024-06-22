from django.urls import path

from .views import *

urlpatterns = [
    path("", user_list, name="user_list"),
    path("<int:user_id>", user_detail, name="user_detail"),
    path("<int:user_id>/increment", user_points_increment, name="user_points_increment"),
    path("<int:user_id>/decrement", user_points_decrement, name="user_points_decrement"),
    path("summary", user_points_summary, name="user_points_summary"),
]