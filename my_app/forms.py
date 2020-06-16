from django import forms
from .models import Menu


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'dishes',
            'schedule',
            'is_active',
        ]

