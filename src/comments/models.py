from django.db import models

from django.conf import settings


class AbstractComment(models.Model):
    """A comment on an posts"""


    text = models.TextField(max_length=200)

    create_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    moderation = models.BooleanField(default=True)
    view_count = models.PositiveBigIntegerField(default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'Commented by {self.user}'

    
    class Meta:
        abstract = True