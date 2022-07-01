from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    taskName = models.CharField(max_length=255)

    def __str__(self):
        return self.taskName


class ScheduleComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
