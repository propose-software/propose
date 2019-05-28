from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    Account, Project, Cabinet,
    Drawer, Specification, Material,
    Labor, Hardware, CustomUser
)

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

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
