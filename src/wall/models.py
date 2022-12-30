from django.db import models
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

from src.comments.models import AbstractComment


class Post(models.Model):
	"""Post model"""


	text = models.TextField(max_length=450)

	created_date = models.DateTimeField(auto_now_add=True)

	published = models.BooleanField(default=True)

	moderation = models.BooleanField(default=True)
	view_count = models.PositiveBigIntegerField(default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	def __str__(self):
		return f'Post by {self.user}'

	def comments_count(self):
		return self.comments.count()

	
class Comment(AbstractComment, MPTTModel):
	"""Comment for a post"""

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

	parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

	def __str__(self):
		return f'{self.user} - {self.post}'
