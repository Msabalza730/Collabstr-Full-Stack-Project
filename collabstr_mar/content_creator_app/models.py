from django.db import models


class Creator(models.Model):
    """Model to save the creator information"""

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    rating = models.FloatField()
    platform_choices = [
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok'),
        ('User Generated Content', 'User Generated Content'),
    ]
    platform = models.CharField(max_length=30, choices=platform_choices)

    def __str__(self):
        return self.username


class Content(models.Model):
    """Model to save the content about creators"""
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
