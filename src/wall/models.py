from django.db import models

from django.conf import settings


class Post(models.Model):


	text = models.TextField(max_length=450)
	create_data = models.DateTimeField(auto_now_add=True)
	published = models.BooleanField(default=True)
	moderation = models.BooleanField(default=True)
	view_count = models.PositiveBigIntegerField(default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	def __str__(self):
		return f'Post by {self.user}'