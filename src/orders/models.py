from django.db import models
from django.core.exceptions import ValidationError


def validate_user_id(value):
    if value != 1:
        raise ValidationError("user_id doesn't equals 1")


class Order(models.Model):
    user_id = models.PositiveIntegerField(validators=[validate_user_id])
    order_info = models.CharField(max_length=100)
