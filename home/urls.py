from django.urls import path
from .views import home, my_logout, center


urlpatterns = [
    path('', home, name="home"),
    path('center/', center, name="center"),
    path('logout/', my_logout, name="logout"),
]
