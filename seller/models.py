from django.db import models
from django.contrib.auth.models import User # 장고에서 자체적으로 만들어놓은 테이블

# class Category(models.Model):
#   name = models.CharField(max_length=200)

class TravelProduct(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.TextField()
  Image_url = models.URLField()