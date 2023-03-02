from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.Search_Event.as_view(), name='homepage'),
     path('concert', views.get_concert_page)
]
