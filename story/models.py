from django.db import models
from main.models import Story
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Storyline(models.Model):
    story_id = models.OneToOneField(Story, on_delete=models.CASCADE, primary_key=True)
    order = JSONField()
    