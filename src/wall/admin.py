from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post interface for admin"""

    list_display = ("user", "published", "create_date", "moderation", "view_count", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Comment for posts"""
    
    list_display = ("user", "post", "published", "id")
    # actions = ['unpublish', 'publish']
    mptt_level_indent = 15