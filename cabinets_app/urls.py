from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .views import (
    account, project_list,
    project_create, project_detail, project_update, project_delete,
    cabinet_detail_view, spec_detail_view
)
from django.urls import path

urlpatterns = [
    path('', account, name='account'),
    path('account/<int:account_id>', project_list, name='project_list'),
    path('project/', project_create, name='project_create'),
    path('project/<int:proj_id>', project_detail, name='project_detail'),
    path('project/<int:proj_id>/update', project_update, name='project_update'),
    path('project/<int:proj_id>/delete', project_delete, name='project_delete'),
    path('2/cabinet/2', cabinet_detail_view, name='cabinet_detail_view'),
    path('3/specification/3', spec_detail_view, name='spec_detail_view')
]
