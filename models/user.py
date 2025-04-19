from tortoise import fields
from tortoise.models import Model
from enum import Enum


class User(Model):
    id = fields.BigIntField(pk=True, auto=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255, null=True)
    deleted_at = fields.DatetimeField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user"
        default_connection = "default"

