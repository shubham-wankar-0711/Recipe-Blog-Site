from rest_framework import viewsets 
from testApp.models import Post,Comment
from django.contrib.auth.models import User
from testApp.API_Service.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BlogPostView(viewsets.ModelViewSet):
  queryset=User.objects.all()
  serializer_class=UserSerializer
  authentication_classes=[JSONWebTokenAuthentication,]
  permission_classes=[IsAuthenticated,]
  # pagination_class = PageNumberPagination
  search_fields=('username',)
  ordering_fields=('username',)
  http_method_names = ['get']
    