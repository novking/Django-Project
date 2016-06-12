from django.test import TestCase

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.title
