from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import (
    Account, Material, Labor,
    Specification, Hardware, Project, Room, Cabinet
)
from .forms import (
    ProjectForm, AccountForm, CabinetForm, SpecForm,
    MaterialForm, HardwareForm, RoomForm, LaborForm
)


# ----- ACCOUNTS ----- #

@login_required
def account(req):
    context = {
        'accounts': Account.objects.all()
    }
    return render(req, './account_list.html', context)


@login_required
def account_create(req):
    if req.method == 'POST':
        form = AccountForm(req.POST)
        if form.is_valid():
            new_account = form.save()
            return redirect('account_detail', account_id=new_account.id)
        else:
            return render(req, './account/account_create.html', {'form': form})
    else:
        form = AccountForm()
        return render(req, './account/account_create.html', {'form': form})


@login_required
def account_detail(req, account_id=None):
    account = Account.objects.get(pk=account_id)
    projects = Project.objects.filter(account__id=account_id)
    context = {
        'account': account,
        'projects': projects,
    }
    return render(req, './account/account_detail.html', context)


@login_required
def account_update(req, account_id=None):
    account = Account.objects.get(pk=account_id)
    if req.method == 'POST':
        form = AccountForm(req.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('account_detail', account_id=account_id)
        else:
            return render(req, './account/account_update.html', {'form': form})
    else:
        form = AccountForm(instance=account)
        context = {
            'form': form,
            'account': account
        }
        return render(req, './account/account_update.html', context)


@login_required
def account_delete(req, account_id=None):
    if req.method == 'POST':
        account = Account.objects.get(pk=account_id)
        account.delete()
        return redirect('account')
    else:
        context = {
            'account': Account.objects.get(pk=account_id)
        }
        return render(req, './account/account_delete.html', context)


# ----- MATERIALS ----- #

@login_required
def material_list(req):
    context = {
        'materials': Material.objects.all()
    }
    return render(req, './material/material_list.html', context)


@login_required
def material_create(req):
    if req.method == 'POST':
        form = MaterialForm(req.POST)
        if form.is_valid():
            new_material = form.save()
            return redirect('material_detail', material_id=new_material.id)
        else:
            return render(req, './material/material_create.html', {'form': form})
    else:
        form = MaterialForm()
        return render(req, './material/material_create.html', {'form': form})


@login_required
def material_detail(req, material_id=None):
    material = Material.objects.get(pk=material_id)
    context = {
        'material': material,
    }
    return render(req, './material/material_detail.html', context)


@login_required
def material_update(req, material_id=None):
    material = Material.objects.get(pk=material_id)
    if req.method == 'POST':
        form = MaterialForm(req.POST, instance=material)
        if form.is_valid():
            form.instance.date_updated = timezone.now()
            material = form.save()
            return redirect('material_detail', material_id=material.id)
        else:
            return render(req, './material/material_update.html', {'form': form})
    else:
        form = MaterialForm(instance=material)
        context = {
            'form': form,
            'material': material
        }
        return render(req, './material/material_update.html', context)


@login_required
def material_delete(req, material_id=None):
    if req.method == 'POST':
        material = Material.objects.get(pk=material_id)
        material.delete()
        return redirect('material_list')
    else:
        context = {
            'material': Material.objects.get(pk=material_id)
        }
        return render(req, './material/material_delete.html', context)


# ----- HARDWARE ----- #

@login_required
def hardware_list(req):
    context = {
        'hardware': Hardware.objects.all()
    }
    return render(req, './hardware/hardware_list.html', context)


@login_required
def hardware_create(req):
    if req.method == 'POST':
        form = HardwareForm(req.POST)
        if form.is_valid():
            new_hardware = form.save()
            return redirect('hardware_detail', hardware_id=new_hardware.id)
        else:
            return render(req, './hardware/hardware_create.html', {'form': form})
    else:
        form = HardwareForm()
        return render(req, './hardware/hardware_create.html', {'form': form})


@login_required
def hardware_detail(req, hardware_id=None):
    hardware = Hardware.objects.get(pk=hardware_id)
    context = {
        'hardware': hardware,
    }
    return render(req, './hardware/hardware_detail.html', context)


@login_required
def hardware_update(req, hardware_id=None):
    hardware = Hardware.objects.get(pk=hardware_id)
    if req.method == 'POST':
        form = HardwareForm(req.POST, instance=hardware)
        if form.is_valid():
            hardware = form.save()
            return redirect('hardware_detail', hardware_id=hardware_id)
        else:
            return render(req, './hardware/hardware_update.html', {'form': form})
    else:
        form = HardwareForm(instance=hardware)
        context = {
            'form': form,
            'hardware': hardware
        }
        return render(req, './hardware/hardware_update.html', context)


@login_required
def hardware_delete(req, hardware_id=None):
    if req.method == 'POST':
        hardware = Hardware.objects.get(pk=hardware_id)
        hardware.delete()
        return redirect('hardware_list')
    else:
        context = {
            'hardware': Hardware.objects.get(pk=hardware_id)
        }
        return render(req, './hardware/hardware_delete.html', context)


# ----- LABOR ----- #

@login_required
def labor_list(req):
    context = {
        'labor': Labor.objects.all()
    }
    return render(req, './labor/labor_list.html', context)


@login_required
def labor_create(req):
    if req.method == 'POST':
        form = LaborForm(req.POST)
        if form.is_valid():
            new_labor = form.save()
            return redirect('labor_detail', labor_id=new_labor.id)
        else:
            return render(req, './labor/labor_create.html', {'form': form})
    else:
        form = LaborForm()
        return render(req, './labor/labor_create.html', {'form': form})


@login_required
def labor_detail(req, labor_id=None):
    labor = Labor.objects.get(pk=labor_id)
    context = {
        'labor': labor,
    }
    return render(req, './labor/labor_detail.html', context)


@login_required
def labor_update(req, labor_id=None):
    labor = Labor.objects.get(pk=labor_id)
    if req.method == 'POST':
        form = LaborForm(req.POST, instance=labor)
        if form.is_valid():
            labor = form.save()
            return redirect('labor_detail', labor_id=labor_id)
        else:
            return render(req, './labor/labor_update.html', {'form': form})
    else:
        form = LaborForm(instance=labor)
        context = {
            'form': form,
            'labor': labor
        }
        return render(req, './labor/labor_update.html', context)


@login_required
def labor_delete(req, labor_id=None):
    if req.method == 'POST':
        labor = Labor.objects.get(pk=labor_id)
        labor.delete()
        return redirect('labor_list')
    else:
        context = {
            'labor': Labor.objects.get(pk=labor_id)
        }
        return render(req, './labor/labor_delete.html', context)
