from django.db import models
from django.contrib.auth.models import User




class maktab(models.Model):
    name = models.CharField(max_length=100, default='')
    oquvchilar_soni = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.name


class xonalar(models.Model):
    xonanomi = models.CharField(max_length=221, default='')
    nechikishiligi = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.xonanomi
