from django.urls import path
from . import views
app_name='indexurl'
urlpatterns = [
    
	path('', views.myindex, name='index'),
	path('about/', views.myabout, name='about'),
	path('services/', views.myservices, name='services'),
	path('contact/', views.mycontact, name='contact'),
	path('track/', views.mytrack, name='track'),
	path('quote/', views.myquote, name='quote'),
	path('dash/', views.dash, name='dash'),

]