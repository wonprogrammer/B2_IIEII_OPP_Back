from django.db import models
from users.models import User

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # 좋아요
    likes = models.ManyToManyField(User, related_name="like_articles")

    def __str__(self):
        return str(self.title)



class Image(models.Model):
    image_user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_image = models.ImageField(null=True)
    output_image = models.ImageField(null=True)
