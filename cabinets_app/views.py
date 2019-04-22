from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (
    Account, Material, Labor,
    Specification, Cabinet, Drawer,
    Hardware, Project
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
