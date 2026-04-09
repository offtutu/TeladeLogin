from django.contrib import admin
from django.urls import include, path

from webapp.views import front_index, front_style, unicorn_preview

urlpatterns = [
    path("admin/", admin.site.urls),
    path("unicorn-preview/", unicorn_preview, name="unicorn_preview"),
    path("style.css", front_style, name="front_style"),
    path("", front_index, name="front_index"),
]

try:
    import django_unicorn  # noqa: F401
except ImportError:
    pass
else:
    urlpatterns.insert(1, path("unicorn/", include("django_unicorn.urls")))
