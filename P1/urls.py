from django.urls import path
from . import views

app_name = 'P1'

urlpatterns = [
    path('home',views.home,name="home")
    
    
]
