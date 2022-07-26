from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('singup', views.singup_views, name='singup'),
    path('login', views.login_views, name='login'),
    path('logout', views.logout_views, name='logout'),
]
