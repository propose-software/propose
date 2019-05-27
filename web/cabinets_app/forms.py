from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm
from .models import (
    Account, Material, Hardware,
    Labor, Project, Specification,
    Cabinet, Drawer, Room, CustomUser
)

User = get_user_model()


class CustomUserCreationForm(RegistrationForm):
    company = forms.CharField(max_length=256)

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'company', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    company = forms.CharField(max_length=256)

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'physical_address',
            'site_contact',
            'contact_phone',
            'contact_email',
            'hourly_rate'
        ]


class SpecForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = [
            'name',
            'interior_material',
            'exterior_material',
            'construction',
            'catalog',
            'finish_level'
        ]


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'name',
            'description',
            'thickness',
            'width',
            'length',
            'sheet_cost',
            'waste_factor',
            'markup',
        ]


class CabinetForm(forms.ModelForm):
    class Meta:
        model = Cabinet
        fields = [
            'specification',
            'width',
            'height',
            'depth',
            'number_of_doors',
            'number_of_shelves',
            'finished_interior',
            'finished_left_end',
            'finished_right_end',
            'finished_top',
            'finished_bottom'
        ]

    def __init__(self, project, *args, **kwargs):
        super(CabinetForm, self).__init__(*args, **kwargs)
        self.fields['specification'].queryset = Specification.objects.filter(
            project=project)


DrawerFormSet = forms.modelformset_factory(
    Drawer,
    fields=('height', 'material'),
    extra=0,
    can_delete=True
)


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [
            'name',
            'cost_per',
            'unit_type',
            'labor_minutes',
            'markup',
            'category',
        ]


class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = [
            'item_name',
            'minutes',
            'unit_type',
            'category',
        ]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
        ]
