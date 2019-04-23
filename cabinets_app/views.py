from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Account, Material, Labor,
    Specification, Cabinet, Drawer,
    Hardware, Project
)
from .forms import (
    ProjectForm
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
            return redirect('project/' + str(new_project.id))
        else:
            return render(req, './project/project_create.html', {'form': form})
    else:
        form = ProjectForm()
        return render(req, './project/project_create.html', {'form': form})


@login_required
def project_detail(req):
    context = {
        'project': Project.objects.get(id=proj_id)
    }
    return render(req, './project/project_detail.html')


@login_required
def cabinet_detail_view(request):
    return render(request, './cabinet_detail.html')


@login_required
def spec_detail_view(request):
    return render(request, './spec_detail.html')
