from django.urls import path

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="Blog - Home") #needs to be completed
]