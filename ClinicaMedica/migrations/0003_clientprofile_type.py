# Generated by Django 2.2.4 on 2019-09-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicaMedica', '0002_typeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='type',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
