from django.db import models
from django.utils import timezone


class Post(models.Model):
    writer = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    hits = models.IntegerField(default=0)
    preview = models.CharField(max_length=30, default='')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
