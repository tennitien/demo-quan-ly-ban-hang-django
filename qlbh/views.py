from django.shortcuts import render
from product.models import SanPham
from customer.models import KhachHang
from invoice.models import HoaDon
from invoiceDetail.models import CTHD


def home(request):

    products = list(SanPham.objects.all())
    customers = list(KhachHang.objects.all())
    invoices = list(HoaDon.objects.all())
    invoicedetails = list(CTHD.objects.all())
    data = {'products': products, 'customers': customers, 'invoices': invoices, 'invoicedetails': invoicedetails}

    return render(request, 'home.html', data)

