from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def account_view(request):
    return render(request, 'generic/base.html')

@login_required
def project_detail_view(request):
    return render(request, './project_detail.html')

@login_required
def cabinet_detail_view(request):
    return render(request, './cabinet_detail.html')

@login_required
def spec_detail_view(request):
    return render(request, './spec_detail.html')

