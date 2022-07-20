from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class SiteType(models.Model):
    siteType = models.CharField(max_length=255)

    def __str__(self):
        return self.siteType

class DeviceType(models.Model):
    deviceType = models.CharField(max_length=255)

    def __str__(self):
        return self.deviceType

class Manager(models.Model):
    manage = models.CharField(max_length=255)

    def __str__(self):
        return self.manage

class Task(models.Model):
    siteType = models.ManyToManyField(SiteType)
    deviceType = models.ManyToManyField(DeviceType)
    prioritize = models.CharField(max_length=1)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    request = models.CharField(max_length=20)
    manager = models.ManyToManyField(Manager)
    taskName = models.CharField(max_length=255)
    referenceUrl = models.CharField(max_length=255, null=True, blank=True)
    taskContent = models.CharField(max_length=3000, blank=True)
    taskState = models.CharField(max_length=1)
    taskProgress = models.IntegerField(default=0, help_text="0~100사이 값으로 입력하세요.", validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    taskStartDate = models.DateTimeField(null=True, blank=True)
    taskEndDate = models.DateTimeField(null=True, blank=True)
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
