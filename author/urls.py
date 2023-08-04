from django.urls import path
from . import views

urlpatterns = [
    path('authors/<int:id>/articles', views.author, name='author'),
    path('magazines/<int:id>/articles', views.magazine, name='magazine'),
]
