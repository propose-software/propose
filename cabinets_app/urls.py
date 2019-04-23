from .views import (
    account, project_list,
    project_create, project_detail, project_update, project_delete,
    cabinet_detail_view, spec_detail_view, account_create, account_detail, account_update, account_delete
)
from django.urls import path

urlpatterns = [
    path('', account, name='account'),
    path('account/',
         account_create, name='account_create'),
    path('account/detail/<int:account_id>',
         account_detail, name='account_detail'),
    path('account/detail/<int:account_id>/update',
         account_update, name='account_update'),
    path('account/detail/<int:account_id>/delete',
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


    path('2/cabinet/2', cabinet_detail_view, name='cabinet_detail_view'),
    path('3/specification/3', spec_detail_view, name='spec_detail_view')
]
