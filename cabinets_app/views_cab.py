from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django import forms
from .models import (
    Account, Cabinet, Drawer, Project
)
from .forms import CabinetForm, DrawerFormSet


@login_required
def cabinet_list(req, proj_id=None):
    context = {
        'project': Project.objects.get(pk=proj_id),
        'cabinets': Cabinet.objects.filter(project__id=proj_id)
    }
    return render(req, './cabinet/cabinet_list.html', context)


@login_required
def cabinet_create(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = CabinetForm(project, req.POST)
        drawer_form = DrawerFormSet(req.POST)
        if form.is_valid():
            max_cab_no = Cabinet.objects.filter(
                project__id=proj_id).aggregate(Max('cabinet_number'))
            form.instance.cabinet_number = max_cab_no['cabinet_number__max'] + 1
            form.instance.project = project
            cabinet = form.save()
            for d in drawer_form:
                if d.is_valid() and d['height'].value() and d['material'].value():
                    instance = d.save(commit=False)
                    instance.cabinet = cabinet
                    instance.save()
            return redirect('cabinet_detail', proj_id=proj_id, cab_id=cabinet.id)
        else:
            context = {
                'form': form,
                'project': project,
                'drawer_form': drawer_form
            }
            return render(req, './cabinet/cabinet_create.html', context)
    else:
        context = {
            'form': CabinetForm(project),
            'project': project,
            'drawer_form': DrawerFormSet(queryset=Drawer.objects.none())
        }
        return render(req, './cabinet/cabinet_create.html', context)


@login_required
def drawer_form(req, proj_id=None):
    context = {
        'form': DrawerFormSet(req.POST)
    }
    return render(req, './cabinet/drawer_form.html', context)


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


def cabinet_update(req, proj_id=None, cab_id=None):
    project = Project.objects.get(pk=proj_id)
    cabinet = Cabinet.objects.get(pk=cab_id)
    if req.method == 'POST':
        form = CabinetForm(project, req.POST, instance=cabinet)
        drawers = Drawer.objects.filter(cabinet=cabinet)
        drawer_form = DrawerFormSet(req.POST, queryset=drawers)
        if form.is_valid():
            cabinet = form.save()
            for d in drawer_form:
                if d.is_valid() and d['height'].value() and d['material'].value():
                    instance = d.save(commit=False)
                    instance.cabinet = cabinet
                    instance.save()
            return redirect('cabinet_detail', proj_id=proj_id, cab_id=cab_id)
        else:
            context = {
                'form': form,
                'project': project,
                'drawer_form': drawer_form
            }
            return render(req, './cabinet/cabinet_update.html', context)
    else:
        form = CabinetForm(project, instance=cabinet)
        drawer_form = DrawerFormSet(queryset=Drawer.objects.filter(cabinet=cabinet))
        context = {
            'form': form,
            'project': project,
            'cabinet': cabinet,
            'drawer_form': drawer_form
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
