
from django.db import models
from django.contrib.auth.models import User


class Earning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earning = models.IntegerField(default=0)

