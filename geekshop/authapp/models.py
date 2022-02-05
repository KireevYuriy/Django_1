from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now


def default_key_expired_date():
    return timezone.now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, verbose_name="Город", blank=True)
    phone_number = models.CharField(max_length=14, verbose_name="Номер телефона", blank=True)
    avatar = models.ImageField(upload_to="users_avatars", blank=True)

    activation_key = models.CharField(verbose_name="Ключ активации", max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(verbose_name='Конец времени активации', default=default_key_expired_date)

    def is_activation_key_expired(self):
        return self.activation_key_expires < timezone.now()
