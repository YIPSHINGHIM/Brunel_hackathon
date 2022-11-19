from django.urls import include, path

from . import views

urlpatterns = [
    path('test',view=views.getRoutes,name="routes")
]
