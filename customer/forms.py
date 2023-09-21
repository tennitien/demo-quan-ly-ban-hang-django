from django import forms
from .models import KhachHang


class AddCustomerForm(forms.ModelForm):
    MAKH = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Mã khách hàng",
    )

    HOTEN = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Họ tên"
    )

    DCHI = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Địa chỉ"
    )

    SODT = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Số điện thoại"
    )

    NGSINH = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}),
        label="Ngày sinh"
    )

    DOANHSO = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control"}),
        label="Doanh số"
    )

    NGDK = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}),
        label="Ngày đăng ký"
    )

    class Meta:
        model = KhachHang
        fields = ['MAKH', 'HOTEN', 'DCHI', 'SODT', 'NGSINH', 'DOANHSO', 'NGDK']
