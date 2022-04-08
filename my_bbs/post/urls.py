from django.urls import path
from post import views

urlpatterns = [
    path("topic_list/", views.topic_list_view),
    path("topic_detail/<int:topic_id>/", views.topic_detail_view),
    path("topic_comment/", views.add_comment_to_topic_view),
    path("hello_world/", views.hello_world),
    path("search_topic_form/", views.search_topic_form),
    path("search_topic/", views.search_topic_form),
    path("topic_model_form/", views.topic_model_form)
]