# Generated by Django 2.2.1 on 2019-05-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets_app', '0004_auto_20190527_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('name', 'account')},
        ),
        migrations.AddField(
            model_name='hardware',
            name='labor_minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]