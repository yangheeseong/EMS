from django.db import models
from django.contrib.auth.models import User

class Memo(models.Model):
    memoName = models.CharField(max_length=100)
    memo = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    uploadImages = models.ImageField(upload_to='memo/images/%Y/%m/%d/', blank=True)
    uploadFile = models.FileField(upload_to='memo/files/%Y/%m/%d/', blank=True)
    modifyDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memoName
