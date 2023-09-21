from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HoaDon
from .forms import AddInvoiceForm
# Create your views here.


def home(request):
    objs = HoaDon.objects.all()
    return render(request, 'invoice/home.html', {'objs': objs})


def add(request, ):
    form = AddInvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Đã thêm một hóa đơn mới")
        return redirect('invoice:home')
    return render(request, 'invoice/add.html', {'form': form})


def update(request, pk):
    current_invoice = HoaDon.objects.get(id=pk)
    form = AddInvoiceForm(request.POST or None, instance=current_invoice)
    if form.is_valid():
        form.save()
        messages.success(request, "Hóa đơn đã được cập nhật lại")
        return redirect('invoice:home')
    return render(request, 'invoice/update.html', {'form': form})


def delete(request, pk):
    invoice_del = HoaDon.objects.get(id=pk)
    invoice_del.delete()
    messages.success(request, "Hóa đơn đã xóa thành công.")
    return redirect('invoice:home')
