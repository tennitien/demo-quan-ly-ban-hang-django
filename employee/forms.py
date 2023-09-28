from django import forms
from .models import NhanVien


class AddEmployeeForm(forms.ModelForm):
    MANV = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Mã nhân viên",
    )

    HOTEN = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Họ tên"
    )

    NGVL = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}),
        label="Ngày vào làm"
    )

    SODT = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Số điện thoại"
    )

    CHUCVU = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        label="Chức vụ"
    )

    class Meta:
        model = NhanVien
        fields = ['MANV', 'HOTEN', 'NGVL', 'SODT', 'CHUCVU',]
