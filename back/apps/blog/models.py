from django.db import models
import uuid
from django.utils import timezone

from apps.category.models import CategoryApp

# Create your models here.


def blog_directory_path(instance, filename):
    #{0}-->hace referencia que de la instancia tendra un titulo{1}queva tener un filename
    return 'blog/{0}/{1}'.format(instance.title,filename)

class Post(models.Model):
    #permite que cuando se suba un blog se puepa no o ver sin borrarlo
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    
    options = (
                ("draft","Draft"),
                ("published","Published")
                )


    blog_url = models.UUIDField(default=uuid.uuid4, unique=True)
    title= models.CharField(max_length =255)
    thumbnail= models.ImageField(upload_to=blog_directory_path,)
    slug= models.SlugField(unique=True)
    image = models.ImageField(upload_to=blog_directory_path)
    video = models.FileField(upload_to=blog_directory_path, blank=True, null=True)               
    description = models.TextField()
    excerpt = models.CharField(max_length=100)

    category = models.ForeignKey(CategoryApp,on_delete=models.PROTECT)

    published = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=10, choices=options, default="draft")
    
    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager


    class Meta:
        #se ordena por fecha
        ordering = ('-published',)

   
   #muestra los post
    def __str__(self) :
        return self.title

    #muestra los video

    def get_video(self): 
        if self.video:
            return self.video.url
        return ''


    def get_thumbnail(self): 
        if self.thumbnail:
            return self.thumbnail.url
        return ''




