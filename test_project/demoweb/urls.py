from django.urls import include, re_path
from demoweb import views

urlpatterns = [
    re_path(r'^info$', views.information),
    re_path(r'^tag',views.setTag)
]