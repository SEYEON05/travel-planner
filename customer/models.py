from django.db import models
from seller.models import *
from django.contrib.auth.models import User

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(TravelProduct, on_delete=models.DO_NOTHING)
  amount = models.IntegerField(default=0)