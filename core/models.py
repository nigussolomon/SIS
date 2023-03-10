from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

USER_TYPES = [
    ("Student", "STUDENT"),
    ("Instructor", "INSTRUCTOR"),
    ("Admin", "ADMIN"),
    ("Other Staff", "OTHER STAFF"),
]


class CustomAccMan(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        user_type = USER_TYPES[2][0]
        if other_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must be set to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must be set to is_superuser=True")

        return self.create_user(
            email, first_name, last_name, password, user_type, **other_fields
        )

    def create_user(
        self, email, first_name, last_name, password, user_type, **other_fields
    ):
        if not email:
            raise ValueError("Please provide a valid email address")
        if not first_name:
            raise ValueError("Please provide a valid first name")
        if not last_name:
            raise ValueError("Please provide a valid last name")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class SisUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    user_type = models.CharField(max_length=30, choices=USER_TYPES)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccMan()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
