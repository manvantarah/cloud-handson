from django.urls import path
from .import views
# from django.contrib.auth.views import Loginview, Logoutview

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logoutUser, name='logout')
]

