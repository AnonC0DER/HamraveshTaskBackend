# Generated by Django 4.1.3 on 2022-11-15 20:02

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_container_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='last_run',
            field=django_jalali.db.models.jDateTimeField(default=None),
        ),
    ]
