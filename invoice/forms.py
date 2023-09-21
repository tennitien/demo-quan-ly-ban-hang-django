from django import forms
from .models import HoaDon
from customer.models import KhachHang
from employee.models import NhanVien


class AddInvoiceForm(forms.ModelForm):
    SOHD = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Số hóa đơn')

    NGHD = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}),
        label="Ngày hợp đồng"
    )

    MAKH = forms.ModelChoiceField(
        queryset=KhachHang.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control", "label": "Nhãn của bạn"}),
    )

    MANV = forms.ModelChoiceField(
        queryset=NhanVien.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    TRIGIA = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={"class": "form-control"}),
        label=""
    )

    class Meta:
        model = HoaDon
        fields = ['SOHD', 'NGHD', 'MAKH', 'MANV', 'TRIGIA']
