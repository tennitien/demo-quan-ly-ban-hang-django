from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SanPham
from .forms import AddProductForm
# Create your views here.


def home(request):
    objs = SanPham.objects.all()
    return render(request, 'product/home.html', {'objs': objs})


def add(request, ):
    form = AddProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('product:home')
    return render(request, 'product/add.html', {'form': form})


def update(request, pk):
    current_product = SanPham.objects.get(id=pk)
    form = AddProductForm(request.POST or None, instance=current_product)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('product:home')
    return render(request, 'product/update.html', {'form': form})


def delete(request, pk):
    product_del = SanPham.objects.get(id=pk)
    product_del.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('product:home')
