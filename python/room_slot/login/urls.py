from django.urls import path,include
from . import views
urlpatterns=[
    path('login',views.user_login,name='user_login'),
    path('login1',views.manager_login,name='manager_login'),
    path('signup',views.user_signup,name='user_signup'),
    path('signup1',views.manager_signup,name='manager_signup'),
    path('dashboard/',include('customer.urls')),
    path('dashboard1/',include('room_manager.urls')),
    path('add-room/',include('room_manager.urls')),
    path('add-aminaries/',include('room_manager.urls')),
    path('add-food/',include('room_manager.urls')),
    path('pay/',include('room_manager.urls'))
]