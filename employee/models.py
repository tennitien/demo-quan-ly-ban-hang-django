from django.db import models


class NhanVien(models.Model):
    MANV = models.CharField(unique=True, max_length=10)
    HOTEN = models.CharField(default='', max_length=100)
    NGVL = models.DateField(null=True)
    SODT = models.CharField(default='', max_length=20)
    CHUCVU = models.CharField(default='', max_length=20)


    def __str__(self) -> str:
        return (f'{self.MANV}: {self.HOTEN}')
