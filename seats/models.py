import json

from django.db import models
from user.models import UserModel


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
