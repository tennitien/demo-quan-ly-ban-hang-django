from django.db import models
from customer.models import KhachHang
from employee.models import NhanVien


class HoaDon(models.Model):
    SOHD = models.CharField(unique=True, max_length=10)
    NGHD = models.DateField(null=True)

    MAKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)

    MANV = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    TRIGIA = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.SOHD
