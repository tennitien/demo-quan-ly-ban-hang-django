from django.db import models
from invoice.models import HoaDon
from product.models import SanPham


class CTHD(models.Model):
    SOHD = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    MASP = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SL = models.IntegerField(default=0)

    def __str__(self) -> str:
        return (f'{self.SOHD}: {self.MASP}, {self.SL}')
