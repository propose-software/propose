from django.core.mail import EmailMessage
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse, FileResponse
from io import BytesIO
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Account, Material, Labor,
    Specification, Hardware, Project, Room, Cabinet
)
from .forms import (
    ProjectForm, EmailProjectForm, AccountForm, CabinetForm, SpecForm,
    MaterialForm, HardwareForm, RoomForm
)


# ----- PROJECTS ----- #

@login_required
def project_list(req, account_id=None):
    context = {
        'projects': Project.objects.all()
    }
    return render(req, './project/project_list.html', context)


@login_required
def project_home(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    rooms = Room.objects.filter(project=project)
    cabinets = Cabinet.objects.filter(project=project)
    context = {
        'project': project,
        'rooms': rooms,
        'cabinets': cabinets,
    }
    return render(req, './project/project_home.html', context)


@login_required
def project_create(req, account_id=None):
    account = Account.objects.get(pk=account_id)
    if req.method == 'POST':
        form = ProjectForm(req.POST)
        if form.is_valid():
            form.instance.account = account
            new_project = form.save()
            return redirect('project_detail', proj_id=new_project.id)
        else:
            context = {
                'form': form,
                'account': account
            }
            return render(req, './project/project_create.html', context)
    else:
        context = {
            'form': ProjectForm(),
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
            return redirect('project_detail', proj_id=project.id)
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
        project.delete()
        return redirect('account_detail', account_id=project.account.id)
    else:
        context = {
            'project': Project.objects.get(pk=proj_id)
        }
        return render(req, './project/project_delete.html', context)


@login_required
def project_pdf(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    account = Account.objects.get(pk=project.account_id)
    rooms = Room.objects.filter(project=project)
    cabinets = Cabinet.objects.filter(project=project)
    context = {
        'account': account,
        'project': project,
        'rooms': rooms,
        'cabinets': cabinets,
        'request': req
    }
    template = get_template('./project/project_pdf.html')
    html = template.render(context)
    stream = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), stream)
    # return HttpResponse(stream.getvalue(), content_type='application/pdf') # open in browser
    response = HttpResponse(stream.getvalue(), content_type='application/pdf')
    filename = f'{project.name} Project Invoice.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@login_required
def project_email_pdf(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = EmailProjectForm(req.POST)
        if form.is_valid():
            project = Project.objects.get(pk=proj_id)
            account = Account.objects.get(pk=project.account_id)
            rooms = Room.objects.filter(project=project)
            cabinets = Cabinet.objects.filter(project=project)
            context = {
                'account': account,
                'project': project,
                'rooms': rooms,
                'cabinets': cabinets,
                'request': req
            }
            template = get_template('./project/project_pdf.html')
            html = template.render(context)
            stream = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), stream)
            email = EmailMessage(
                subject=f'{project.name} Invoice',
                body=req.POST.get('message'),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[req.POST.get('recipient')]
            )
            email.attach(f'{project.name} Invoice.pdf', stream.getvalue())
            email.send()
            return redirect('project_detail', proj_id=proj_id)
        else:
            context = {
                'form': form,
                'project': project
            }
            return render(req, './project/project_email_pdf.html', context)
    else:
        form_data = {
            'recipient': project.contact_email
        }
        context = {
            'form': EmailProjectForm(form_data),
            'project': project
        }
        return render(req, './project/project_email_pdf.html', context)


# ----- SPECIFICATIONS ----- #

@login_required
def spec_create(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = SpecForm(req.POST)
        if form.is_valid():
            form.instance.project = project
            form.save()
            return redirect('project_detail', proj_id=proj_id)
        else:
            context = {
                'form': form,
                'project': project
            }
            return render(req, './specifications/spec_create.html', context)
    else:
        context = {
            'form': SpecForm(),
            'project': project
        }
        return render(req, './specifications/spec_create.html', context)


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
            form.save()
            return redirect('project_detail', proj_id=proj_id)
        else:
            context = {
                'form': form,
                'spec': spec,
                'project': project
            }
            return render(req, './specifications/spec_update.html', context)
    else:
        context = {
            'form': SpecForm(instance=spec),
            'spec': spec,
            'project': project
        }
        return render(req, './specifications/spec_update.html', context)


@login_required
def spec_delete(req, proj_id=None, spec_id=None):
    if req.method == 'POST':
        spec = Specification.objects.get(pk=spec_id)
        project = Project.objects.get(pk=proj_id)
        spec.delete()
        return redirect('/')
    else:
        context = {
            'spec': Specification.objects.get(pk=spec_id),
            'project': Project.objects.get(pk=proj_id)
        }
        return render(req, './specifications/spec_delete.html', context)


# ----- ROOMS ----- #

@login_required
def room_create(req, proj_id=None):
    project = Project.objects.get(pk=proj_id)
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.instance.project = project
            form.save()
            return redirect('project_detail', proj_id=proj_id)
        else:
            context = {
                'form': form,
                'project': project
            }
            return render(req, './room/room_create.html', context)
    else:
        context = {
            'form': RoomForm(),
            'project': project
        }
        return render(req, './room/room_create.html', context)


@login_required
def room_update(req, proj_id=None, room_id=None):
    project = Project.objects.get(pk=proj_id)
    room = Room.objects.get(pk=room_id)
    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.instance.project = project
            room = form.save()
            return redirect('project_detail', proj_id=proj_id)
        else:
            context = {
                'form': form,
                'room': room,
                'project': project
            }
            return render(req, './room/room_update.html', {'form': form})
    else:
        form = RoomForm(instance=room)
        context = {
            'form': form,
            'room': room,
            'project': project
        }
        return render(req, './room/room_update.html', context)


@login_required
def room_delete(req, proj_id=None, room_id=None):
    if req.method == 'POST':
        room = Room.objects.get(pk=room_id)
        room.delete()
        return redirect('project_detail', proj_id=proj_id)
    else:
        context = {
            'room': Room.objects.get(pk=room_id),
            'project': Project.objects.get(pk=proj_id)
        }
        return render(req, './room/room_delete.html', context)
