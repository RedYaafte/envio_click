from django.db import models

class XmlScore(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    xml = models.FileField(upload_to='uploads/')
    score = models.IntegerField(null=True, blank=True)