from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PaperGen, ElectGen
import random

class GenerateKey(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    service = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Service", "class":"form-control"}), label="")
    value = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Value", "class":"form-control"}), label="")
    amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")
    unique = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = PaperGen
        exclude = ("user",)

class GenerateElect(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    service = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Service", "class":"form-control"}), label="")
    value = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Value", "class":"form-control"}), label="")
    amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")
    uniquec = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Unique", "class": "form-control"}), label="")

    class Meta:
        model = ElectGen
        exclude = ("user",)