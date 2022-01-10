from typing import Any

from django.http import HttpResponse
from django.shortcuts import render


def index(request: Any) -> HttpResponse:
    return render(request, 'content/index.html')


def not_found(request: Any, exception: Any) -> HttpResponse:
    return render(request, '404.html')
