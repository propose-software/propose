from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import (
    Account, Material, Labor,
    Specification, Cabinet, Drawer,
    Hardware, Project
)
from .forms import (
    ProjectForm, AccountForm, CabinetForm
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
def project_create(req):
    if req.method == 'POST':
        form = ProjectForm(req.POST)
        if form.is_valid():
            new_project = form.save()
            return redirect('/project/' + str(new_project.id))
        else:
            return render(req, './project/project_create.html', {'form': form})
    else:
        form = ProjectForm()
        return render(req, './project/project_create.html', {'form': form})


@login_required
def project_detail(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    account = Account.objects.get(pk=project.account.id)
    context = {
        'project': project,
        'account': account
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

'''
    path('account/',
         account_create, name='account_create'),
    path('account/',
         account_detail, name='account_detail'),
    path('account/',
         account_update, name='account_update'),
    path('account/',
         account_delete, name='account_delete'),
'''

@login_required
def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_account = form.save()
            return redirect('/account/' + str(new_account.name))
        else:
            return render(request, './account/account_create.html', {'form': form})
    else:
        form = AccountForm()
        return render(request, './account/account_create.html', {'form': form})

@login_required
def account_detail():
    pass
@login_required
def account_update():
    pass
@login_required
def account_delete():
    pass


@login_required
def cabinet_list(req, proj_id=None):
    context = {
        'project': Project.objects.get(pk=proj_id),
        'cabinets': Cabinet.objects.filter(project__id=proj_id)
    }
    return render(req, './cabinet/cabinet_list.html', context)


@login_required
def cabinet_create(req, proj_id=None):
    if req.method == 'POST':
        form = CabinetForm(req.POST)
        if form.is_valid():
            max_cab_no = Cabinet.objects.filter(project__id=proj_id).aggregate(Max('cabinet_number'))
            form.instance.cabinet_number = max_cab_no['cabinet_number__max'] + 1
            new_cabinet = form.save()
            return redirect('cabinet_detail', proj_id=proj_id, cab_id=new_cabinet.id)
        else:
            return render(req, './cabinet/cabinet_create.html', {'form': form})
    else:
        context = {
            'form': CabinetForm(),
            'project': Project.objects.get(pk=proj_id)
        }
        return render(req, './cabinet/cabinet_create.html', context)


@login_required
def cabinet_detail(req, proj_id=None, cab_id=None):
    cabinet = Cabinet.objects.get(pk=cab_id)
    project = Project.objects.get(pk=proj_id)
    account = Account.objects.get(pk=project.account.id)
    context = {
        'cabinet': cabinet,
        'project': project,
        'account': account
    }
    return render(req, './cabinet/cabinet_detail.html', context)


@login_required
def cabinet_update(req, proj_id=None, cab_id=None):
    cabinet = Cabinet.objects.get(pk=cab_id)
    if req.method == 'POST':
        form = CabinetForm(req.POST, instance=cabinet)
        if form.is_valid():
            cabinet = form.save()
            return redirect('cabinet_detail', proj_id=proj_id, cab_id=cab_id)
        else:
            return render(req, './cabinet/cabinet_update.html', {'form': form})
    else:
        form = CabinetForm(instance=cabinet)
        context = {
            'form': form,
            'project': Project.objects.get(pk=proj_id),
            'cabinet': cabinet
        }
        return render(req, './cabinet/cabinet_update.html', context)


@login_required
def cabinet_delete(req, proj_id=None, cab_id=None):
    if req.method == 'POST':
        cabinet = Cabinet.objects.get(pk=cab_id)
        cabinet.delete()
        return redirect('project_detail', proj_id=proj_id)
    else:
        context = {
            'project': Project.objects.get(pk=proj_id),
            'cabinet': Cabinet.objects.get(pk=cab_id)
        }
        return render(req, './cabinet/cabinet_delete.html', context)
