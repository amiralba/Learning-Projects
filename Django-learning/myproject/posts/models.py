from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title