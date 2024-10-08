from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("create_category/", views.create_category, name="create_category"),
    path("categories/", views.categories, name="categories"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
    path("feed/", views.feed, name="feed")
]