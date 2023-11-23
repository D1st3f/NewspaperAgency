import os
from uuid import uuid4

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Redactor(AbstractUser):
    year_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


def generate_unique_filename(instance, filename):
    filename = f"{uuid4().hex}.jpg"
    return os.path.join('images/', timezone.now().strftime('%Y/%m/%d/'), filename)


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to=generate_unique_filename)
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic, related_name="newspaper")
    publishers = models.ManyToManyField(Redactor, related_name="newspaper")

    def save(self, *args, **kwargs):
        if os.path.exists(self.image.path):
            img = Image.open(self.image.path)
            if img.format == 'WEBP':
                new_path = os.path.splitext(self.image.path)[0] + '.jpg'
                img.convert('RGB').save(new_path, 'JPEG')
                self.image.name = os.path.relpath(new_path, 'media')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title