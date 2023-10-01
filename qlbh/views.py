from django.shortcuts import render
from product.models import SanPham
from customer.models import KhachHang
from invoice.models import HoaDon
from invoiceDetail.models import CTHD
from django.core import serializers



def home(request):

    products = serializers.serialize('json', SanPham.objects.all())
    customers = serializers.serialize('json', KhachHang.objects.all())
    invoices = serializers.serialize('json', HoaDon.objects.all())
    invoicedetails = serializers.serialize('json', CTHD.objects.all())
    data = {'products': products, 'customers': customers, 'invoices': invoices, 'invoicedetails': invoicedetails}

    return render(request, 'home.html', data)

