from django.urls import path
from . import views as pred_view

urlpatterns = [
    path('login/', pred_view.login_view, name="login"),
    path('register/', pred_view.register_user, name="register"),
    path("logout/", pred_view.logout_view, name="logout"),
    path('index', pred_view.index, name='index'),
    path('pred', pred_view.pred, name='pred'),
    path('contact', pred_view.contact, name='contact'),
]
