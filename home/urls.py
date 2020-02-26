from django.urls import path
from .views import home, my_logout, center, works


urlpatterns = [
    path('', home, name="home"),
    path('center/', center, name="center"),
    path('works/', works, name="works"),
    path('logout/', my_logout, name="logout"),
]
