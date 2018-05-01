
from django.conf.urls import url
from . import views

# 局部路由
urlpatterns = [
    url("", views.msgproc),
]
