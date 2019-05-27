# Generated by Django 2.2.1 on 2019-05-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='category',
            field=models.CharField(choices=[('Design', 'Design'), ('Engineering', 'Engineering'), ('Production', 'Production'), ('Finishing', 'Finishing'), ('Installation', 'Installation'), ('Misc.', 'Misc.')], default='Production', max_length=128),
        ),
    ]