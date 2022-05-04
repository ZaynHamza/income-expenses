from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Expense(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    category = models.CharField(max_length=266)

    def __str__(self):
        return self.category

    class Meta:
        ordering: ['-date']


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
