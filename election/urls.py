"""election URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from e2074.views import profile,home,signup,wpadmin,wpzone,wpdistrict,wppoliticaldiv,post,wppost,profile
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^candidate/(?P<slug>[\w-]+)/$',profile, name='profile'),
    url(r'^$', home, name='home'),
    url(r'^wp-admin/login/$', login, name='login'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^wp-admin/logout/$', logout, {'next_page':'home'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^wp-admin/$', wpadmin, name='wpadmin'),
    url(r'^wp-admin/zone/$', wpzone, name='wpzone'),
    url(r'^wp-admin/district/$', wpdistrict, name='wpdistrict'),
    url(r'^wp-admin/politicaldiv/$', wppoliticaldiv, name='wppoliticaldiv'),
    url(r'^(?P<slug>[\w-]+)/$', post, name='post'),
    url(r'^wp-admin/post/$', wppost, name='wppost'),
    url(r'^(?P<district>[\w-]+)/(?P<politicaldiv>[\w-]+)/(?P<slug>[\w-]+)/$', profile, name='profile'),


]
