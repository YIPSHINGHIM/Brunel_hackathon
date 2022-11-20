from django.urls import include, path

from . import views

urlpatterns = [
    path('test',view=views.getRoutes,name="routes"),
    path('test_post',view=views.test_post_request,name="post request"),
    path('Historical_Simulation_view',view=views.Historical_Simulation_view,name="Historical_Simulation_view"),
    path('prediction',view=views.prediction,name="prediction")
]
