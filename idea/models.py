from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title