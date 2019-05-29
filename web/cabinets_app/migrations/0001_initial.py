# Generated by Django 2.2.1 on 2019-05-29 04:31

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('billing_address', models.CharField(max_length=1024)),
                ('billing_phone', models.CharField(max_length=32)),
                ('billing_email', models.EmailField(max_length=256)),
                ('contact_name', models.CharField(max_length=128)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet_number', models.IntegerField()),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=6)),
                ('number_of_doors', models.IntegerField()),
                ('number_of_shelves', models.IntegerField()),
                ('finished_interior', models.BooleanField(default=False)),
                ('finished_left_end', models.BooleanField(default=False)),
                ('finished_right_end', models.BooleanField(default=False)),
                ('finished_top', models.BooleanField(default=False)),
                ('finished_bottom', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('cabinet_number',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('billing_address', models.CharField(max_length=1024)),
                ('billing_phone', models.CharField(max_length=32)),
                ('billing_email', models.EmailField(max_length=256)),
                ('contact_name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('Hinges', 'Hinges'), ('Drawer Guides', 'Drawer Guides'), ('Knobs/Pulls', 'Knobs/Pulls'), ('Accessories', 'Accessories'), ('Misc.', 'Misc.')], default='Misc.', max_length=128)),
                ('cost_per', models.DecimalField(decimal_places=2, max_digits=6)),
                ('labor_minutes', models.IntegerField()),
                ('unit_type', models.CharField(choices=[('Each', 'Each'), ('Pair', 'Pair'), ('Set', 'Set')], max_length=16)),
                ('markup', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'ordering': ('category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('Design', 'Design'), ('Engineering', 'Engineering'), ('Production', 'Production'), ('Finishing', 'Finishing'), ('Installation', 'Installation'), ('Misc.', 'Misc.')], default='Production', max_length=128)),
                ('minutes', models.IntegerField()),
                ('unit_type', models.CharField(choices=[('Each', 'Each'), ('Pair', 'Pair'), ('Set', 'Set'), ('Sq Ft', 'Sq Ft')], max_length=16)),
            ],
            options={
                'ordering': ('category', 'item_name'),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('category', models.CharField(choices=[('Interior Material', 'Interior Material'), ('Exterior Material', 'Exterior Material'), ('Drawer Material', 'Drawer Material')], default='Exterior Material', max_length=128)),
                ('mat_type', models.CharField(choices=[('Sheet', 'Sheet'), ('Board', 'Board'), ('Moulding', 'Moulding')], default='Sheet', max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=4)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sheet_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('waste_factor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('markup', models.DecimalField(decimal_places=2, max_digits=3)),
                ('date_updated', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('physical_address', models.CharField(max_length=1024)),
                ('site_contact', models.CharField(max_length=128)),
                ('contact_phone', models.CharField(max_length=32)),
                ('contact_email', models.EmailField(max_length=256)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='cabinets_app.Account')),
            ],
            options={
                'ordering': ('name', 'account'),
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('construction', models.CharField(choices=[('Frameless', 'Frameless'), ('Faceframe Overlay', 'Faceframe Overlay'), ('Faceframe Inset', 'Faceframe Inset')], default='Frameless', max_length=32)),
                ('catalog', models.CharField(choices=[('Laminate', 'Laminate'), ('Wood Slab', 'Wood Slab'), ('Wood 5-Piece', 'Wood 5-Piece'), ('Thermofoil', 'Thermofoil')], default='Laminate', max_length=32)),
                ('finish_level', models.CharField(choices=[('Unfinished', 'Unfinished'), ('Sand & Prep Only', 'Sand & Prep Only'), ('Clear', 'Clear'), ('Stain', 'Stain'), ('Stain & Glaze', 'Stain & Glaze'), ('Stain & Distress', 'Stain & Distress'), ('Stain, Glaze & Distress', 'Stain, Glaze & Distress'), ('Paint', 'Paint'), ('Paint & Glaze', 'Paint & Glaze'), ('Paint & Distress', 'Paint & Distress'), ('Paint, Glaze & Distress', 'Paint, Glaze & Distress')], default='Unfinished', max_length=125)),
                ('exterior_material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exterior_specifications', to='cabinets_app.Material')),
                ('interior_material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interior_specifications', to='cabinets_app.Material')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='cabinets_app.Project')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='cabinets_app.Project')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Drawer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawers', to='cabinets_app.Cabinet')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawer_material', to='cabinets_app.Material')),
            ],
            options={
                'ordering': ('height',),
            },
        ),
        migrations.AddField(
            model_name='cabinet',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinets', to='cabinets_app.Project'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinets', to='cabinets_app.Room'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='specification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cabinets', to='cabinets_app.Specification'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='cabinets_app.Company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
