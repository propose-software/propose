from django.contrib import admin
from .models import (
    Account, Project, Cabinet,
    Drawer, Specification, Material,
    Labor, Hardware
)

admin.site.register((
    Account,
    Project,
    Cabinet,
    Drawer,
    Specification,
    Material,
    Labor,
    Hardware
))
