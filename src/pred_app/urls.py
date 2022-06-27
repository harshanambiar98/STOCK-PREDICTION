from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
]
