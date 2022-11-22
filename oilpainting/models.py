from django.db import models
from users.models import User

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    # 이미지가 media파일에 몰리는 경우를 대비해 media 폴더에 년/월로 나뉘어 업로드 되게 만들어 준다.
    image = models.ImageField(blank=True, upload_to='%Y/%m/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # 좋아요
    likes = models.ManyToManyField(User, related_name="like_articles")

    def __str__(self):
        return str(self.title)