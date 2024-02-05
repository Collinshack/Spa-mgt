from django import forms
from .models import ElectronicCardSum, ElectronicCardService, PhysicalCardService, PhysicalCardSum, Service

class PhysicalCardSumForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = PhysicalCardSum
        exclude = ("user", "status", "type", "created_at" )


class PhysicalCardServiceForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=False, widget=forms.widgets.Select(attrs={"placeholder": "Service", "class": "form-control"}), label="Select service")
    purchased_frequency = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Purchase frequency", "class":"form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = PhysicalCardService
        exclude = ("user", "status", "type", "created_at" )



class ElectronicCardSumForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")
    amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Amount", "class": "form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = ElectronicCardSum
        exclude = ("user", "status", "type", "created_at" )



class ElectronicCardServiceForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=False, widget=forms.widgets.Select(attrs={"placeholder": "Service", "class": "form-control"}), label="Select service")
    purchased_frequency = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Purchase frequency", "class": "form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = ElectronicCardService
        exclude = ("user", "type", "status", "created_at")







