from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Заметки'
        ordering = ['created']


    def __str__(self):
        return self.title