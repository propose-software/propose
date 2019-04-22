from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .views import account_view, project_detail_view, cabinet_detail_view, spec_detail_view
from django.urls import path

urlpatterns = [
    path('account', account_view, name='account_view'),
    path('1', project_detail_view, name='project_detail_view' ),
    path('2/cabinet/2', cabinet_detail_view, name='cabinet_detail_view' ),
    path('3/specification/3', spec_detail_view, name='spec_detail_view' )
]
