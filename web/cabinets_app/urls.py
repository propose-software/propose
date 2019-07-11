from .views import (
    account, account_create, account_detail, account_update, account_delete,
    material_create, material_delete, material_detail,
    material_list, material_update,
    hardware_create, hardware_delete, hardware_detail,
    hardware_list, hardware_update,
    labor_create, labor_delete, labor_detail, labor_list, labor_update
)
from .views_cab import (
    cabinet_create, drawer_form, cabinet_detail,
    cabinet_update, cabinet_delete, cabinet_list
)
from .views_proj import (
    project_list, project_create, project_detail, project_update,
    project_delete, project_home, project_pdf, project_email_pdf,
    spec_create, spec_detail, spec_delete, spec_update,
    room_create, room_update, room_delete,
)
from django.urls import path, include

from django_registration.backends.activation.views import RegistrationView
from .forms import CustomUserCreationForm

urlpatterns = [
    path('users/register/', RegistrationView.as_view(form_class=CustomUserCreationForm), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.activation.urls')),

    path('', account, name='account'),
    path('account/', account_create, name='account_create'),
    path('account/<int:account_id>', account_detail, name='account_detail'),
    path('account/<int:account_id>/update', account_update, name='account_update'),
    path('account/<int:account_id>/delete', account_delete, name='account_delete'),
    path('account/<int:account_id>/project/', project_create, name='project_create'),

    path('material/all', material_list, name='material_list'),
    path('material/', material_create, name='material_create'),
    path('material/<int:material_id>', material_detail, name='material_detail'),
    path('material/<int:material_id>/update', material_update, name='material_update'),
    path('material/<int:material_id>/delete', material_delete, name='material_delete'),

    path('hardware/all', hardware_list, name='hardware_list'),
    path('hardware/', hardware_create, name='hardware_create'),
    path('hardware/<int:hardware_id>', hardware_detail, name='hardware_detail'),
    path('hardware/<int:hardware_id>/update', hardware_update, name='hardware_update'),
    path('hardware/<int:hardware_id>/delete', hardware_delete, name='hardware_delete'),

    path('labor/all', labor_list, name='labor_list'),
    path('labor/', labor_create, name='labor_create'),
    path('labor/<int:labor_id>', labor_detail, name='labor_detail'),
    path('labor/<int:labor_id>/update', labor_update, name='labor_update'),
    path('labor/<int:labor_id>/delete', labor_delete, name='labor_delete'),

    path('project/all', project_list, name='project_list'),
    path('project/<int:proj_id>', project_home, name='project_home'),
    path('project/<int:proj_id>/detail', project_detail, name='project_detail'),
    path('project/<int:proj_id>/update', project_update, name='project_update'),
    path('project/<int:proj_id>/delete', project_delete, name='project_delete'),
    path('project/<int:proj_id>/pdf', project_pdf, name='project_pdf'),
    path('project/<int:proj_id>/email_pdf', project_email_pdf, name='project_email_pdf'),

    path('project/<int:proj_id>/room/', room_create, name='room_create'),
    path('project/<int:proj_id>/room/<int:room_id>/update', room_update, name='room_update'),
    path('project/<int:proj_id>/room/<int:room_id>/delete', room_delete, name='room_delete'),

    path('project/<int:proj_id>/spec/', spec_create, name='spec_create'),
    path('project/<int:proj_id>/spec/<int:spec_id>', spec_detail, name='spec_detail'),
    path('project/<int:proj_id>/spec/<int:spec_id>/update', spec_update, name='spec_update'),
    path('project/<int:proj_id>/spec/<int:spec_id>/delete', spec_delete, name='spec_delete'),

    path('project/<int:proj_id>/room/<int:room_id>/cabinet', cabinet_create, name='cabinet_create'),
    path('project/<int:proj_id>/cabinet/drawer_form', drawer_form, name='drawer_form'),
    path('project/<int:proj_id>/cabinet_list', cabinet_list, name='cabinet_list'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>', cabinet_detail, name='cabinet_detail'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>/update', cabinet_update, name='cabinet_update'),
    path('project/<int:proj_id>/cabinet/<int:cab_id>/delete', cabinet_delete, name='cabinet_delete'),
]
