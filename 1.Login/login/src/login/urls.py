
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views #new
from django.views.generic.base import TemplateView #new

urlpatterns = [
	path('admin/', admin.site.urls),

	# home page or redirect page
	path('',TemplateView.as_view(template_name='home.html'),name='home'),
	#login page url
 	path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout,{'next_page':'/'}, name='logout'),
]
