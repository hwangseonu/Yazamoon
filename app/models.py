from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
import json


class VerifyCode(models.Model):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=5, unique=True)


class UserManager(BaseUserManager):
    def create_user(self, email, name, student_id, password):
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            student_id=student_id,
        )

        group = Group.objects.get_or_create(name=student_id[:3])
        user.groups.add(group)

        user.set_password(password)
        user.save(using=self._db)

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

        group = Group.objects.get_or_create(name=student_id[:3])
        user.groups.add(group)

        user.set_password(password)
        user.save(using=self._db)
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


class ClassModel(models.Model):
    class_id = models.IntegerField(primary_key=True)

    def set_seats(self, x):
        self.seats = json.dumps(x)

    def get_seats(self):
        return json.loads(self.seats)


class SeatModel(models.Model):
    student = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=False, primary_key=True)
    cls = models.ForeignKey(ClassModel, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=3, null=False)
    status = models.CharField(max_length=10, null=False, default="miss")

    def set_position(self, pos: tuple):
        row = pos[0]
        column = pos[1]
        self.position = f"{row},{column}"

    def get_position(self) -> tuple:
        return tuple(map(int, self.position.split(',')))
