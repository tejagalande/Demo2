from django.urls import include, re_path
from demoapp import views

urlpatterns = [

    re_path(r'^cars/$', views.cars_list),
]