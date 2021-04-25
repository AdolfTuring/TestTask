from rest_framework import serializers
from .models import Post, UserFollowing
from django.contrib.auth.models import User


POST_ACTION_OPTIONS = ['read', 'unread']


class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        fields = ('id', 'author', 'title', 'text', 'pubdate', 'read')
        model = Post
        

class PostCreate(serializers.Serializer):
    title=serializers.CharField()
    text=serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        return value
        
class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in POST_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets")
        return value
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = User

