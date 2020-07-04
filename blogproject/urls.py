from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

#from django.contrib.auth import views
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

#urlpatterns = [
 #  url( r'^accounts/login/$',auth_views.LoginView.as_view(template_name="blog/registration/login.html"), name="login"),
#]
urlpatterns = [
    #url(r'^accounts/login/$', views.login, name='login'),
    path('accounts/login/',LoginView.as_view(), name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),

     #url( r'^accounts/login/$',auth_views.LoginView.as_view(template_name="blog/registration/login.html"), name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blogapp.urls')),
    #url( r'^accounts/logout/$',auth_views.LogoutView.as_view(template_name="blog/registration/login.html"), name="login"),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
