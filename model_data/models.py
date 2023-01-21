from django.db import models
# from django.db.models import Model

# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    rating = models.IntegerField()
    def __str__(self):
      return f"{self.article_name} {self.url} {self.rating}"


