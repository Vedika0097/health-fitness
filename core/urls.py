# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include

try:
    from rest_framework.authtoken.views import obtain_auth_token
except:
    pass

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("login/jwt/", view=obtain_auth_token),
]


# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append(path("", include("django_dyn_api.urls")))
    urlpatterns.append(path("login/jwt/", view=obtain_auth_token))
except:
    pass
