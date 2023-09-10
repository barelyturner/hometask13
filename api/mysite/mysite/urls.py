from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path


def health_check(request):
    if request.method == "GET":
        return JsonResponse("Hi, everything is going well!", safe=False)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health", health_check),
    re_path(r"^", include("school.urls")),
 #   re_path(r"^", include("location.urls")),
]
