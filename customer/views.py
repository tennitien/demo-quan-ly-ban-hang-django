from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import KhachHang
from .forms import AddCustomerForm
# Create your views here.


# @login_required(login_url=)
def home(request):
    objs = KhachHang.objects.all()
    return render(request, 'customer/home.html', {'objs': objs})


def add(request, ):
    form = AddCustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('customer:home')
    return render(request, 'customer/add.html', {'form': form})


def update(request, pk):
    current_customer = KhachHang.objects.get(id=pk)
    form = AddCustomerForm(request.POST or None, instance=current_customer)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('customer:home')
    return render(request, 'customer/update.html', {'form': form})


def delete(request, pk):
    customer_del = KhachHang.objects.get(id=pk)
    customer_del.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('customer:home')
