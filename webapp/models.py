import uuid
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
# Create your models here.

class Quarter(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Topic(models.Model):
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Submission(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    is_sent_for_editing = models.BooleanField(default=False)
    sent_for_edit_time = models.DateTimeField(null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=255, blank=False)
    subtext = models.CharField(max_length=255, blank=False)
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", default="thumbnails/newsletter.jpg")
    body = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_sent_for_editing:
            self.sent_for_edit_time = timezone.now()
        super().save(*args, **kwargs)

class Newsletter(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255,blank=False)
    subtext = models.CharField(max_length=255,blank=False)
    volume = models.IntegerField(blank=False)
    issue = models.IntegerField(blank=False)
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", default="thumbnails/newsletter.jpg")
    body = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return "Volume "+str(self.volume)+" | Issue "+str(self.issue)