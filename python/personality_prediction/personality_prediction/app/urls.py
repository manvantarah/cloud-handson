from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
	path('index/',views.index, name = 'index'),
	path('candidate/',views.candidate,name='candidate'),
	#path('login/',views.login,name='login'),
	#path('recruiter/',views.recruiter,name='recruiter'),
	path('test/',views.test,name='test'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)