# Generated by Django 2.2 on 2019-04-25 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets_app', '0012_auto_20190424_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='cabinets_app.Project'),
        ),
    ]
