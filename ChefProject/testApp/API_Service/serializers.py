from rest_framework import serializers 
from testApp.models import Post,Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields=['name','email','body']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields= ['category','title','user_detail','body','status','comments']
        

class UserSerializer(serializers.ModelSerializer):
    blog_post = PostSerializer(many=True)
    class Meta:
      model = User
      fields = ['username','first_name','last_name','email','blog_post']
      
    








