from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title