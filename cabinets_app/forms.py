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


class SpecForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = [
            'project',
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
            'date_updated',
        ]


class CabinetForm(forms.ModelForm):
    class Meta:
        model = Cabinet
        fields = [
            'specification',
            'room',
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
    extra=1
)

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [
            'name',
            'cost_per',
            'unit_type',
            'markup'
        ]

