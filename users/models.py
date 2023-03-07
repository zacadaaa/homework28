from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import check_birth_date, check_email


class Location(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Местоположение'

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    STATUS = [
        (MEMBER, "Гость"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Администратор")
    ]
    
    role = models.CharField(max_length=9, choices=STATUS, default="member")
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(unique=True, validators=[check_email])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
