from django import forms
from .models import SanPham


class AddProductForm(forms.ModelForm):
    MASP = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Mã sản phẩm"
    )

    TENSP = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Tên sản phẩm"
    )

    DVT = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Đơn vị tính"
    )

    NUOCSX = forms.CharField(
        required=True,
        widget=forms.DateInput(
            attrs={"class": "form-control"}),
        label="Nước sản xuất"
    )

    GIA = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control"}),
        label="Giá sản phẩm"
    )

    class Meta:
        model = SanPham
        fields = ['MASP', 'TENSP', 'DVT', 'NUOCSX', 'GIA']
