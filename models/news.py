from tortoise import fields
from tortoise.models import Model
from enum import Enum


class News(Model):
    id = fields.BigIntField(pk=True, auto=True)
    title = fields.TextField(null=True)
    desc = fields.TextField(null=True)
    url = fields.TextField(null=True)
    published_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "news"
        default_connection = "default"

