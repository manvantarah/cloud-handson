from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_room,name="add_room"),
    path('new1/',views.add_aminaries,name="add_aminaries"),
    path('new2/',views.add_food,name="add_food"),
    path('update/<int:room_no>/',views.update_room,name="update_room"),

]
