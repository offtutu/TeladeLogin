from pathlib import Path

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render


def front_index(request):
    return render(request, "index.html")


def front_style(request):
    css_path = Path(settings.FRONT_DIR) / "style.css"
    return FileResponse(css_path.open("rb"), content_type="text/css; charset=utf-8")


def unicorn_preview(request):
    return render(
        request,
        "unicorn_preview.html",
        {"has_django_unicorn": settings.HAS_DJANGO_UNICORN},
    )
