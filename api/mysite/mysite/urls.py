from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^", include("school.urls")),
]
