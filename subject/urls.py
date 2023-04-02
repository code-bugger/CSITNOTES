from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('<int:value>',views.subject),
    path('explore/<int:hero>',views.explore)
]

