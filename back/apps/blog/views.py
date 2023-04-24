from unittest import result
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from rest_framework import permissions


from .models import Post
from .serializers import PostSerializer
from apps.category.models import CategoryApp
from .pagination import SmallSetPagination,LastSetPagination,MediumSetPagination

from django.db.models.query_utils import Q


class BlogListView(APIView):
  #  permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Post.postobjects.all().exists():

            posts = Post.postobjects.all()

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(results, many=True)

            return paginator.get_paginated_response({'posts': serializer.data})


        else:
            return Response({'error':'No posts aa found'}, status=status.HTTP_404_NOT_FOUND)




class PostDetailView(APIView):
    #permission_classes = (permissions.AllowAny,)
    def get(self, request, post_slug, format=None):
        #post = Post.objects.get()
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response({'post':serializer.data}, status=status.HTTP_200_OK)



