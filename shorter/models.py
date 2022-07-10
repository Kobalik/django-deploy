from django.db import models
from django.contrib.auth.models import User

class Shorter_history(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=50, unique=True)