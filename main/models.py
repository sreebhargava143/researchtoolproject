from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Story(models.Model):
    story_name = models.CharField( max_length=250, null=True)
    description = models.TextField(blank=False)
    author = models.ForeignKey(User, verbose_name="author name", db_index=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('story_detail',
                        args=[self.publish.year,
                        self.publish.month,
                        self.publish.day,
                        self.slug])

    def __str__(self):
        return '%s' % self.story_name

class StoryCard(models.Model):
    story = models.ForeignKey("Story", verbose_name="story name", on_delete=models.CASCADE)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    # card_data = RichTextUploadingField("Write your story", blank=False)
    card_data = models.TextField("Write your story", blank=False)
    updated = models.DateTimeField(db_index=True, auto_now=True)
    # bookmark = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.card_data
