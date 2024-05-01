from django.db import models

from accounts.models import User


class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/products')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

