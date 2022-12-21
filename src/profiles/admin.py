from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import UserSonet

from django.utils.translation import gettext, gettext_lazy as _


class UserSonetAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone", "first_login", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Info"), {"fields": ("phone", "avatar", "gender")})
    )


admin.site.register(UserSonet, UserSonetAdmin)
