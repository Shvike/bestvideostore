from django.urls import re_path
from . import views


urlpatterns = [
    re_path('123/', views.hello),
    re_path('456/', views.world, name="main_page"),
    re_path("comment/(?P<id>[-\d]+)/", views.accept_comment, name="add_comment"),
    re_path("only_video/(?P<id>[-\d]+)/", views.only_video, name="one_video"),
    re_path("add_like/(?P<id>[-\d]+)/", views.add_like),
    re_path("ajax/add_like/", views.ajax_like),
    re_path("add_ajax_comment/", views.ajax_comment),
]