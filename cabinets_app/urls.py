from .views import (
    account, project_list,
    project_create, project_detail, project_update, project_delete,
    cabinet_create, cabinet_detail, cabinet_update, cabinet_delete,
    cabinet_detail_view, spec_detail_view, account_create, account_detail, account_update, account_delete
)
from django.urls import path

urlpatterns = [
    path('', account, name='account'),
    path('account/<int:',
         account_create, name='account_create'),
    path('account/',
         account_detail, name='account_detail'),
    path('account/',
         account_update, name='account_update'),
    path('account/',
         account_delete, name='account_delete'),

    path('account/<int:account_id>', project_list, name='project_list'),

    path('project/',
         project_create, name='project_create'),
    path('project/<int:proj_id>',
         project_detail, name='project_detail'),
    path('project/<int:proj_id>/update',
         project_update, name='project_update'),
    path('project/<int:proj_id>/delete',
         project_delete, name='project_delete'),

    path('project/<int:proj_id>/cabinet',
         cabinet_create, name='cabinet_create'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>',
         cabinet_detail, name='cabinet_detail'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>/update',
         cabinet_update, name='cabinet_update'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>/delete',
         cabinet_delete, name='cabinet_delete'),


    path('2/cabinet/2', cabinet_detail_view, name='cabinet_detail_view'),
    path('3/specification/3', spec_detail_view, name='spec_detail_view')
]
