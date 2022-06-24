from django.db import models


class SiteErrorLog(models.Model):
    fileName = models.CharField(max_length=255)
    httpHost = models.CharField(max_length=255)
    httpUrl = models.CharField(max_length=255)
    parameter = models.CharField(max_length=3000, null=True)
    httpReferer = models.CharField(max_length=1000, null=True)
    remoteAddr = models.CharField(max_length=255)
    localAddr = models.CharField(max_length=255)
    httpUserAgent = models.CharField(max_length=255)
    httpMethod = models.CharField(max_length=255)
    httpCookie = models.CharField(max_length=3000)
    errorNumber = models.IntegerField()
    errorCategory = models.CharField(max_length=255)
    errorDescription = models.CharField(max_length=1000)
    errorCol = models.IntegerField()
    errorLine = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.errorCategory