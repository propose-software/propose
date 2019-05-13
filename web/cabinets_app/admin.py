from django.contrib import admin
from .models import (
    Account, Project, Cabinet,
    Drawer, Specification, Material,
    Labor, Hardware
)
from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register((
    User,
    Account,
    Project,
    Cabinet,
    Drawer,
    Specification,
    Material,
    Labor,
    Hardware
))
