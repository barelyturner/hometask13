from django.urls import re_path
from school import views

urlpatterns = [
    re_path(r"^schools$", views.SchoolListView.as_view()),
    re_path(r"^schools/([\w|\W]+)$", views.SchoolDetailView.as_view()),
]
