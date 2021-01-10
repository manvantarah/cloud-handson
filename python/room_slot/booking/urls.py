from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('gbook-now/<str:id>',views.gbook_now,name='gbook-now'),
    path('fbook-now/<str:id>',views.fbook_now,name='fbook-now'),
    path('cancel-room/<str:id>',views.cancel_room,name='cancel-room'),
    path('delete-room/<str:id>',views.delete_room,name='delete-room'),
    path('confirm-now-booking',views.book_confirm,name="book_confirm"),
    path('gconfirm-now-booking',views.gbook_confirm,name="gbook_confirm"),
    path('fconfirm-now-booking',views.fbook_confirm,name="fbook_confirm")
]