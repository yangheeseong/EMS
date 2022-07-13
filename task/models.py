from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    siteType = models.CharField(max_length=50)
    deviceType = models.CharField(max_length=10)
    prioritize = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    request = models.CharField(max_length=20)
    manager1 = models.CharField(max_length=20)
    manager2 = models.CharField(max_length=20)
    taskName = models.CharField(max_length=255)
    referenceUrl = models.CharField(max_length=255, null=True)
    taskContent = models.CharField(max_length=3000, null=True)
    completeState = models.CharField(max_length=1)
    completeDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskName


class TaskComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
