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

from django.urls import path,re_path
from testApp import views
from django.conf.urls import url,include
from rest_framework import routers
from testApp.API_Service.views import BlogPostView
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title=' Swagger API for BlogPost')

router=routers.DefaultRouter() 
router.register('Blog_Post_API',BlogPostView)


urlpatterns = [    
    path(r'', include(router.urls)),
    path('swagger-api/', schema_view),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token), 
    path('auth-jwt-verify/', verify_jwt_token),      
]