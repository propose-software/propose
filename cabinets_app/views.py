from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Account, Material, Labor,
    Specification, Hardware, Project, Room
)
from .forms import (
    ProjectForm, AccountForm, CabinetForm, SpecForm,
    MaterialForm, HardwareForm, RoomForm
)


@login_required
def account(req):
    context = {
        'accounts': Account.objects.all()
    }
    return render(req, './account_list.html', context)


@login_required
def project_list(req, account_id=None):
    context = {
        'projects': Project.objects.filter(account__id=account_id)
    }
    return render(req, './project/project_list.html', context)


@login_required
def project_create(req, account_id=None):
    account = Account.objects.get(pk=account_id)
    if req.method == 'POST':
        form = ProjectForm(req.POST)
        if form.is_valid():
            form.instance.account = account
            new_project = form.save()
            return redirect('/project/' + str(new_project.id))
        else:
            return render(req, './project/project_create.html', {'form': form})
    else:
        form = ProjectForm()
        context = {
            'form': form,
            'account': account,
        }
        return render(req, './project/project_create.html', context)


@login_required
def project_detail(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    account = Account.objects.get(pk=project.account.id)
    specs = Specification.objects.filter(project=project)
    context = {
        'project': project,
        'account': account,
        'specs': specs,
    }
    return render(req, './project/project_detail.html', context)


@login_required
def project_update(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = ProjectForm(req.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('/project/' + str(project.id))
        else:
            return render(req, './project/project_update.html', {'form': form})
    else:
        form = ProjectForm(instance=project)
        context = {
            'form': form,
            'project': project
        }
        return render(req, './project/project_update.html', context)


@login_required
def project_delete(req, proj_id=None):
    if req.method == 'POST':
        project = Project.objects.get(pk=proj_id)
        account_id = project.account.id
        project.delete()
        return redirect('/account/' + str(account_id))
    else:
        context = {
            'project': Project.objects.get(pk=proj_id)
        }
        return render(req, './project/project_delete.html', context)


@login_required
def account_create(req):
    if req.method == 'POST':
        form = AccountForm(req.POST)
        if form.is_valid():
            new_account = form.save()
            return redirect('/account/detail/' + str(new_account.id))
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
            return redirect('/account/detail/' + str(account.id))
        else:
            return render(req, './account/account_update.html', {'form': form})
            # Where do we want to go if it gets updated?
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
        return redirect('/')
    else:
        context = {
            'account': Account.objects.get(pk=account_id)
        }
        return render(req, './account/account_delete.html', context)


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
            return redirect('/material/' + str(new_material.id))
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
            material = form.save()
            return redirect('/material/' + str(material.id))
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
        return redirect('/material/all')
    else:
        context = {
            'material': Material.objects.get(pk=material_id)
        }
        return render(req, './material/material_delete.html', context)


@login_required
def spec_create(req, proj_id=None):
    if req.method == 'POST':
        form = SpecForm(req.POST)
        if form.is_valid():
            new_spec = form.save()
            return redirect('/spec/' + str(new_spec.id))
        else:
            return render(req, './specifications/spec_create.html', {'form': form})
    else:
        form = SpecForm()
        return render(req, './specifications/spec_create.html', {'form': form})


@login_required
def spec_detail(req, proj_id=None, spec_id=None):
    context = {
        'spec': Specification.objects.get(pk=spec_id),
        'project': Project.objects.get(pk=proj_id)
    }
    return render(req, './specifications/spec_detail.html', context)


@login_required
def spec_update(req, proj_id=None, spec_id=None):
    spec = Specification.objects.get(pk=spec_id)
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = SpecForm(req.POST, instance=spec)
        if form.is_valid():
            account = form.save()
            return redirect('/spec/' + str(spec.id))
        else:
            context = {
                'form': form,
                'spec': spec,
                'project': project
            }
            return render(req, './specifications/spec_update.html', {'form': form})
    else:
        form = SpecForm(instance=spec)
        context = {
            'form': form,
            'spec': spec,
            'project': project
        }
        return render(req, './specifications/spec_update.html', context)


@login_required
def spec_delete(req, proj_id=None, spec_id=None):
    if req.method == 'POST':
        spec = Specification.objects.get(pk=spec_id)
        spec.delete()
        return redirect('/')
    else:
        context = {
            'spec': Specification.objects.get(pk=spec_id)
        }
        return render(req, './specifications/spec_delete.html', context)


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
            return redirect('/hardware/' + str(new_hardware.id))
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
            return redirect('/hardware/' + str(hardware.id))
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
        return redirect('/hardware/all')
    else:
        context = {
            'hardware': Hardware.objects.get(pk=hardware_id)
        }
        return render(req, './hardware/hardware_delete.html', context)


@login_required
def room_create(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.instance.project = project
            form.save()
            return redirect('/project/' + str(proj_id))
        else:
            return render(req, './room/room_create.html', {'form': form})
    else:
        form = RoomForm()
        context = {
            'form': form,
            'project': project
        }
        return render(req, './room/room_create.html', context)


@login_required
def room_update(req, room_id=None, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.instance.project = project
            room = form.save()
            return redirect('/project/' + str(proj_id))
        else:
            return render(req, './room/room_update.html', {'form': form})
    else:
        form = RoomForm(instance=room)
        context = {
            'form': form,
            'room': room
        }
        return render(req, './room/room_update.html', context)


@login_required
def room_delete(req, room_id=None, proj_id=None):
    if req.method == 'POST':
        room = Room.objects.get(pk=room_id)
        room.delete()
        return redirect('/project/' + str(proj_id))
    else:
        context = {
            'room': Room.objects.get(pk=room_id)
        }
        return render(req, './room/room_delete.html', context)
