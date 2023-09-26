from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NhanVien
from .forms import AddEmployeeForm
# Create your views here.


# @login_required(login_url=)
def home(request):
    objs = NhanVien.objects.all()
    return render(request, 'employee/home.html', {'objs': objs})


def add(request, ):
    form = AddEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('employee:home')
    return render(request, 'employee/add.html', {'form': form})


def update(request, pk):
    current_employee = NhanVien.objects.get(id=pk)
    form = AddEmployeeForm(request.POST or None, instance=current_employee)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('employee:home')
    return render(request, 'employee/update.html', {'form': form})


def delete(request, pk):
    employee_del = NhanVien.objects.get(id=pk)
    employee_del.delete()
    messages.success(request, "Xóa nhân viên thành công")
    return redirect('employee:home')
