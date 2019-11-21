
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/',views.detail, name="detail"),
    path('', views.allblogs, name='allblogs'),
]