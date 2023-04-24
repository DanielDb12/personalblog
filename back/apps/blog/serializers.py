from rest_framework import serializers

from apps.category.serializer import CategorySerializer
from .models import Post



#nos permite convertir la informacion en formato Json
class PostSerializer(serializers.ModelSerializer):
   
    thumbnail=serializers.CharField(source='get_thumbnail')
    video=serializers.CharField(source='get_video')
    category = CategorySerializer()
    class Meta:
        model=Post
        fields=[
                'blog_url',
                'title',
                'slug',
                'thumbnail',
                'video',
                'description',
                'excerpt',
                'category',
                
                'published',
                'status',

                ]
