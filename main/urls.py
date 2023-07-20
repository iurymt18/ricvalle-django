from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.ver_produto, name="home"),
    
]