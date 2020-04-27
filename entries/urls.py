from django.urls import path

from .views import HomeView, EntryView, CreateEntryView, AboutView #importing all the views

urlpatterns = [
    path('', HomeView.as_view(), name="blog-home"),#home page url
    path('entry/<int:pk>/',EntryView.as_view(), name = "entry-detail"),#readmore or full blog view url
    path('create_entry', CreateEntryView.as_view(success_url='/'), name = "create_entry"),# create new post url
    path('about', AboutView.as_view(), name = "about"),# about url
]