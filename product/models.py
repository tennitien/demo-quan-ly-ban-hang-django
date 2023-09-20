from django.db import models

# Create your models here.


class SanPham(models.Model):
    MASP = models.CharField(unique=True, max_length=10)
    TENSP = models.CharField(max_length=255, default='')
    DVT = models.CharField(max_length=50, default='')
    NUOCSX = models.CharField(max_length=100, default='')
    GIA = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.MASP}: {self.TENSP}'
