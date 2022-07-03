from django.contrib import admin
from django.urls import path

from djangonautic import view
from . import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', view.about),
    path('',view.homepage),
]
