from django import forms
from .models import Business, Post, Neighbourhood

class BusinessCreateForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'neighbourhood', 'email', 'desc']

class HoodCreateForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = '__all__'