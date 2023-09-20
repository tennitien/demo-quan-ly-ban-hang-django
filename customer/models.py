from django.db import models
from django.utils import timezone


class KhachHang(models.Model):
    MAKH = models.CharField(unique=True, max_length=10)
    HOTEN = models.CharField(default='', max_length=100)
    DCHI = models.CharField(default='', max_length=200)
    SODT = models.CharField(default='', max_length=200)
    NGSINH = models.DateField(null=True)
    DOANHSO = models.IntegerField(default=0)
    NGDK = models.DateField(default=timezone.now)
#     # billId

    def __str__(self) -> str:
        return (f'{self.MAKH}: {self.HOTEN}')
