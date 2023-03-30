from django.urls import path
from . import views
urlpatterns = [
    path('<str:value>',views.home),

    path('explore/<str:hero>',views.explore)
]

