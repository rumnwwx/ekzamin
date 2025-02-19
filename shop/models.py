from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=100, verbose_name="Почта", unique=True)
    username = models.CharField(max_length=20, verbose_name="Имя пользователя", unique=True)
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    patronym = models.CharField(max_length=20, verbose_name="Отчество")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.name} {self.surname}"

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.FileField(upload_to='product_photo/', blank=True, null=True)

    def __str__(self):
        return self.name

