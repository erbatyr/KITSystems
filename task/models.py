from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100, null=True)
    doers = models.ManyToManyField(User, related_name='doer')
    watchers = models.ManyToManyField(User, related_name='watcher')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    planned_end_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')


class StatusEditing(models.Model):
    prev_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="prev_status")
    next_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="next_status")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.


class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    reminder_text = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.
