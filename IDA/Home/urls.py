from django.urls import path
from . import views
from Home.views import home,login,doLogin,FirstLogin,doLogout,changepassword,doChangePassword,TermOfService,copyright,contoh_form_tanpa_file, FirstLogin, DoFirstLogin, TrialEnd
app_name= 'Home'
urlpatterns = [
	path('', home, name="home"),
	path('doLogin/', doLogin),
	# path('login/', login),
	path('login/', FirstLogin, name="login"),
	path('doLogout/', doLogout, name="logout"),
	path('changepassword/', changepassword, name="changepassword"), #fak: buat refer ke fungsi changepassword
	path('doChangePassword/', doChangePassword),
	path('copyright/', copyright, name="copyright"),
	path('TermOfService/', TermOfService),
    path('TrialEnd/', TrialEnd),
	path('contoh_form_tanpa_file/', contoh_form_tanpa_file)
]