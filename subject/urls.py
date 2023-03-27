from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('see/<str:value>',views.see)
]

