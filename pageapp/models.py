from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    docs = models.TextField(max_length=500)
    publish_date = models.DateTimeField()