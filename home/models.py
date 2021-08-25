from django.conf import settings
from django.db import models


class UserLang(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="userlang_user",
    )
    language = models.CharField(
        max_length=256,
    )
    level = models.BigIntegerField()
