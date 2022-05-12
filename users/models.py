from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from .utils import GenderChoice


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, password: str, **extra) -> None:
        self._validate(email=email, password=password)
        user = self.model(email=self.normalize_email(email),
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    password: str) -> None:
        self._create(email, password)

    def create_superuser(self,
                         email: str,
                         password: str) -> None:
        self._create(email, password, is_staff=True, is_superuser=True, is_active=True)


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='Почта')
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя и фамилия')
    avatar = models.ImageField(null=True, blank=True,)
    phone = models.CharField(max_length=15)
    birth_day = models.DateField(null=True, blank=True, verbose_name='День рождения')
    gender = models.CharField(max_length=20, default='other',
                              choices=GenderChoice.choice(), verbose_name='Пол')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обнавлено')

    is_active = models.BooleanField(default=False, verbose_name='Активный')
    is_banned = models.BooleanField(default=False, verbose_name='Заблокированный')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Админ')

    class Supplier(models.Model):
        name = models.CharField(max_length=45)
        sub_represent = models.CharField(max_length=100)
        phone = models.CharField(max_length=15)
        address = models.CharField(max_length=45)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    class Meta:
        app_label = 'users'
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'


    objects = UserManager()