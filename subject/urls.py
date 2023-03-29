from django.urls import path
from . import views
urlpatterns = [
    path('<str:value>',views.home),
    path('content/<str:value>',views.explore),
    path('chapter/<str:zero>',views.chapter)
]

