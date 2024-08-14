from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def validate_duration(value):
    if value.total_seconds() > 120:
        raise ValidationError(_("Время выполнения не должно превышать 120 секунд."))


def validate_periodicity(value):
    if value > 7:
        raise ValidationError(
            _("Периодичность не может быть реже, чем раз в семь дней.")
        )
