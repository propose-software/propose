from django import forms
from .models import (
    Account, Material, Hardware,
    Labor, Project, Specification,
    Cabinet, Drawer
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'account',
            'name',
            'physical_address',
            'site_contact',
            'contact_phone',
            'contact_email',
            'hourly_rate'
        ]

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'billing_address',
            'billing_phone',
            'billing_email',
            'contact_name',
            'discount'
        ]