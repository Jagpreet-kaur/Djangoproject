# dashboard/models.py
from django.db import models

class DashboardItem(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
