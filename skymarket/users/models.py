from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractBaseUser):

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    ROLE = [
        ("user", "Пользователь"),
        ("admin", "Админ"),
    ]
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=5, default=UserRoles.USER, choices=UserRoles.choices)
    image = models.ImageField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
