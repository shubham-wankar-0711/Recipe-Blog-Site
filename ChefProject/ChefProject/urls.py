"""ChefProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from testApp import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path('blog/', views.post_list_view),
    path('tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view,name = 'tag_view'),
    path(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>\[-\w]+)/$', views.post_detail_view,name='post_detail'),
    url(r'^(?P<id>\d+)/share', views.mail_send_view),
    path('breakfast/', views.breakfast_view),
    path('lunch/', views.lunch_view),
    path('dinner/', views.dinner_view),
    path('dessert/', views.dessert_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('add/', views.add_view),
    path('search/', views.search_view,name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
