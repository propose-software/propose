from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Account, Material, Labor,
    Specification, Cabinet, Drawer,
    Hardware, Project
)
from .forms import (
    ProjectForm, AccountForm
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
def cabinet_detail_view(request):
    return render(request, './cabinet_detail.html')


@login_required
def spec_detail_view(request):
    return render(request, './spec_detail.html')
