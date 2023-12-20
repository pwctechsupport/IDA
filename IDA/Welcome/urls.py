from django.urls import path
from . import views
from Welcome.views import welcomeLogin
app_name= 'Welcome'
urlpatterns = [
	path('', views.WelcomeFirstLogin, name="welcome"),
    path('welcomeLogin/', welcomeLogin)
]