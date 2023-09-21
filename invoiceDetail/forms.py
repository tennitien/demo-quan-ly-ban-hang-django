from django import forms
from .models import CTHD
from invoice.models import HoaDon
from product.models import SanPham


class AddInvoiceDetailForm(forms.ModelForm):
    SOHD = forms.ModelChoiceField(
        queryset=HoaDon.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    MASP = forms.ModelChoiceField(
        queryset=SanPham.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    SL = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={"class": "form-control"}),
        label="Trị giá"
    )

    class Meta:
        model = CTHD
        fields = ['SOHD', 'MASP', 'SL']
