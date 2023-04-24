from django.db import models

# Create your models here.


class CategoryApp(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    views = models.IntegerField(default=0, blank=True)

    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    thumbnail = models.ImageField(upload_to="media/categories/")

    def __str__(self):
        return self.name


    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''

 
