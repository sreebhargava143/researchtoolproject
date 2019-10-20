from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    title = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    urlToImage = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    publishedAt = models.CharField(max_length=500, null=False, blank=False)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'Author:-{self.author}, Title:-{self.title} PostedAt:-{self.publishedAt}'
