from django.db import models

# Create your models here.
from ads.models import Ad
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=100, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
