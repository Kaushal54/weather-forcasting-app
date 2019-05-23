from django.urls import path,include
from weatherapp import views
urlpatterns = [
    path('index/',views.index,name="index"),
]
