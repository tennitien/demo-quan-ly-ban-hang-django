from django import forms
from .models import KhachHang


class AddCustomerForm(forms.ModelForm):
    MAKH = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "MAKH", "class": "form-control"}),
        label=""
    )

    HOTEN = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "HOTEN", "class": "form-control"}),
        label=""
    )

    DCHI = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "DCHI", "class": "form-control"}),
        label=""
    )

    SODT = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "SODT", "class": "form-control"}),
        label=""
    )

    NGSINH = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"placeholder": "NGSINH", "class": "form-control", "type": "date"}),
        label=""
    )

    DOANHSO = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "DOANHSO", "class": "form-control"}),
        label=""
    )

    NGDK = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"placeholder": "NGDK", "class": "form-control", "type": "date"}),
        label=""
    )

    class Meta:
        model = KhachHang
        fields = ['MAKH', 'HOTEN', 'DCHI', 'SODT', 'NGSINH', 'DOANHSO', 'NGDK']
