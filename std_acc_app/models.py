from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    U_TYPES = (('l', 'LandLord'), ('s', 'Student'))
    u_type = models.CharField(max_length=1, choices=U_TYPES)


class Advertisement(models.Model):
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    weekly_rent = models.FloatField(default=0)
    available_from = models.CharField(max_length=20)
    bond_amount = models.FloatField()
    img = models.ImageField(upload_to='static/pictures')
    add_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.address}'
