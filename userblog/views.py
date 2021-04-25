from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, UserFollowing
from .serializers import PostSerializer, UserSerializer, PostActionSerializer, PostCreate
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail


class PostViev(APIView):
    '''
    Main page with all post by folowed users
    '''
    def get(self, request, format=None):
        '''
        return page with posts ordered by publication data
        '''
        folowing_authors=[user.user_id.pk for user in UserFollowing.objects.filter(following_user_id=request.user)]
        feed=Post.objects.filter(author__in=folowing_authors).order_by('-pubdate')
        serializer=PostSerializer(feed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''
        Action options are: read, unread
        '''
        serializer = PostActionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data=serializer.validated_data
            post_id = data.get("id")
            action = data.get("action")
            qs = Post.objects.filter(id=post_id)
            if not qs.exists():
                return Response({}, status=404)
            obj = qs.first()
            if action == "read":
                obj.read.add(request.user)
                serializer = PostSerializer(obj)
                return Response(serializer.data, status=200)
            elif action == "unread":
                obj.read.remove(request.user)
                serializer = PostSerializer(obj)
                return Response(serializer.data, status=200)
            else: return Response(status=400)


class ListUsers(generics.ListAPIView):
    '''
    list users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostID(APIView):
    '''
    Return one post using id of post
    '''
    def get(self, request, pk, format=None):
        try:
            post=Post.objects.get(pk=pk)
            serializer=PostSerializer(post)
            return Response(serializer.data)
        except Exception: 
            return Response(status=404)

class CreatePost(APIView):
    '''
    creating posts with sending email for folowers if they have email
    '''
    def post(self, request, format=None):
        serializer=PostCreate(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data=serializer.validated_data
            author=request.user
            title=data.get('title')
            text=data.get('text')
            if Post.objects.create(author=author, title=title, text=text):
                try:
                    user=User.objects.get(username=request.user)
                    post=Post.objects.filter(author=author, title=title, text=text)
                    follower=[user.following_user_id.email for user in UserFollowing.objects.filter(user_id=request.user)]
                    send_mass_mail(f'New massage', 'Hi, you have new posts. http://127.0.0.1:8000/{post.id}', str(user.email), follower, fail_silently=True)
                    return Response(status=200)
                except Exception:
                    return Response(status=200)
            else: return Response(status=400)


class UserBlogViev(APIView):
    '''
    class for viewing personal blog other users and make folowing or unfolowing
    '''
    
    def get(self, request, name, format=None):
        name=User.objects.get(username=name)
        post=Post.objects.filter(author=name.id).order_by("-pubdate")
        serializer=PostSerializer(post, many=True)
        return Response(serializer.data)
        
    def post(self, request, name, format=None):
        action=request.data.get('action')
        if action=="follow":
            user = User.objects.get(username=name)
            follower = User.objects.get(username=request.user)
            if user==follower:
                return Response(status=400)
            c=UserFollowing.objects.filter(user_id=user, following_user_id=follower)
            if not c.exists():
                UserFollowing.objects.create(user_id=user, following_user_id=follower)
                return Response(status=201)
            else:
                return Response(status=400)
        elif action=="unfollow":
            user = User.objects.get(username=name)
            follower = User.objects.get(username=request.user)
            c=UserFollowing.objects.filter(user_id=user, following_user_id=follower)
            if not c.exists():
                return Response(status=400)
            else:
                UserFollowing.objects.get(user_id=user, following_user_id=follower).delete()
                return Response(status=200)
            