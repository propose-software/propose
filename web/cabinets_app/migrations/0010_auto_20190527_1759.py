# Generated by Django 2.2.1 on 2019-05-28 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets_app', '0009_auto_20190527_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='cabinets_app.Company'),
        ),
    ]
