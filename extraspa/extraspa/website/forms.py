from django import forms
from .models import ElectronicCardSum, ElectronicCardService, PhysicalCardService, Service



class PhysicalCardServiceForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
    phone = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"телефон", "class":"form-control"}), label="")
    amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Сумма", "class":"form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = PhysicalCardService
        exclude = ("user", "status", "type", "created_at" )



class ElectronicCardSumForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Имя", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "телефон", "class": "form-control"}), label="")
    amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Сумма", "class": "form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = ElectronicCardSum
        exclude = ("user", "status", "type", "created_at" )



class ElectronicCardServiceForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Имя", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "телефон", "class": "form-control"}), label="")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=False, widget=forms.widgets.Select(attrs={"placeholder": "Service", "class": "form-control"}), label="Select service")
    purchased_frequency = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Сумма", "class": "form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = ElectronicCardService
        exclude = ("user", "type", "status", "created_at")







