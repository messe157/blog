from django.db import models
from django.contrib.auth.models import User #importando bilbiotcas

# Create your models here.

STATUS = (
    (0, "Rascunho"),
    (1, "Publicar"),
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BigIntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    #UPLOAD DE IMAGENS
    class Image(models.Model):
        title = models.CharField(max_length=200)
        #image = models.ImageField(upload_to='images')
        image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

        def __str__(self):
            return self.title