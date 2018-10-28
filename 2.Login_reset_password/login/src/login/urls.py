
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

	#reset password
	path('password_reset/', auth_views.password_reset, name='password_reset'),

    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),

   # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',auth_views.password_reset_confirm, name='password_reset_confirm'),
    
    path('reset/<uidb64>/<token>/',auth_views.password_reset_confirm, name='password_reset_confirm'),
    

    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
]     
# url('^', include('django.contrib.auth.urls')), #this is all together password reset
#path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),