from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CTHD
from .forms import AddInvoiceDetailForm
# Create your views here.

# app_name='invoiceDetail'


def home(request):
    objs = CTHD.objects.all()
    return render(request, 'invoiceDetail/home.html', {'objs': objs})


def add(request, ):
    form = AddInvoiceDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Chi tiết hóa đơn đã được thêm mới")
        return redirect('invoiceDetail:home')
    return render(request, 'invoiceDetail/add.html', {'form': form})


def update(request, pk):
    current_invoiceDetail = CTHD.objects.get(id=pk)
    form = AddInvoiceDetailForm(
        request.POST or None, instance=current_invoiceDetail)
    if form.is_valid():
        form.save()
        messages.success(request, "Chi tiết hóa đơn đã được cập nhật!")
        return redirect('invoiceDetail:home')
    return render(request, 'invoiceDetail/update.html', {'form': form})


def delete(request, pk):
    invoiceDetail_del = CTHD.objects.get(id=pk)
    invoiceDetail_del.delete()
    messages.success(request, "Đã xóa thành công")
    return redirect('invoiceDetail:home')
