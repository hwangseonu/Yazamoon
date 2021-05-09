from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group


class UserManager(BaseUserManager):
    def create_user(self, email, name, student_id, password):
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            student_id=student_id,
        )

        user.set_password(password)
        user.save(using=self._db)

        group, _ = Group.objects.get_or_create(name=student_id[:3])
        user.groups.add(group)
        user.save()

        return user

    def create_superuser(self, email, name, student_id, password):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            student_id=student_id,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)

        group, _ = Group.objects.get_or_create(name=student_id[:3])
        user.groups.add(group)
        user.save()

        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=5, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'student_id']


class VerifyCode(models.Model):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=5, unique=True)
