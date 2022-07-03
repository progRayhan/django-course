from django.contrib import admin
from django.urls import path, include

from djangonautic import views
from . import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('about/', views.about),
    path('',views.homepage),
]
