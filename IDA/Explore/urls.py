from django.urls import path
from . import views

app_name = 'Explore'

urlpatterns = [
    path('chat/', views.chat, name="chat"),
	path('chat/downloadtemplate/', views.downloadtemplate),
	path('chat/downloadsample/', views.downloadsample),
    path('viewSampleData/', views.viewSampleData),
    path('TriggerNewChat/', views.TriggerNewChat),
	path('getSampleDescription/',views.getSampleDescription),
    path('validate_file/', views.validate_file),
	path('upload_file/', views.upload_file),
	path('viewMore/', views.viewMore),
]
