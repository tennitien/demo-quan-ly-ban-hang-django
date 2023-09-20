from django import forms
from .models import SanPham

class AddProductForm(forms.ModelForm):
    MASP = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "MASP", "class": "form-control"}),
        label=""
    )

    TENSP = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "TENSP", "class": "form-control"}),
        label=""
    )

    DVT = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "DVT", "class": "form-control"}),
        label=""
    )

   
    NUOCSX = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"placeholder": "NUOCSX", "class": "form-control", "type": "date"}),
        label=""
    )

    GIA = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "GIA", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = SanPham
        fields = ['MASP', 'TENSP', 'DVT', 'NUOCSX', 'GIA']